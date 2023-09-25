# -*- coding: utf-8 -*-
import json
import re
import os
import sys
import shutil
sys.path.append(os.getcwd())
from MKafka import KafkaSender


KafkaConfig = {
    "source": "yc-llm-generate",
    "hosts": ["pbs-kafka-4gdzxs-0.kafka.queue.inneryiche.com:9092", "pbs-kafka-4gdzxs-1.kafka.queue.inneryiche.com:9092", "pbs-kafka-4gdzxs-2.kafka.queue.inneryiche.com:9092"],
    "sasl_mechanism": "SCRAM-SHA-256",
    "security_protocol": "SASL_PLAINTEXT",
    "sasl_plain_username": "chengxj",
    "sasl_plain_password": "chengxjakrpyc",
    "time_out": 3,
    # "log_topic": "uat_title_generate",
    # "log_group_id": "uat_title_generate_consumer",
    "log_topic": "llm_generate",
    "log_group_id": "llm_generate_consumer",
    "auto_offset_reset": "earliest",
    "consumer_timeout_ms": 10000,
    "enable_auto_commit": True
}

# config_path = "/cur_models/text4aigc/c_models/title_generate/title_generate_triton/Journal/LoggerKafka.json"
config_path = "LoggerKafka.json"


class QualityProcessor:
    def __init__(self):
        with open(config_path, "r") as f:
            config = json.load(f)
        self.spilt_log_dir = config["spilt_log_dir"]
        self.split_prefix = config["split_prefix"]
        self.info_key = config["key"]
        self.info_data = config["data"]
        self.log_data = []
        self.pattern = re.compile(self.info_data)
        self.kafka_core = None
        try:
            self.kafka_core = KafkaSender(KafkaConfig)
        except:
            print("init kafka core error")

    def read_file(self):
        all_lines = []
        if not os.path.exists(self.spilt_log_dir):
            os.mkdir(self.spilt_log_dir)
        filenames = os.listdir(self.spilt_log_dir)
        for filename in filenames:
            if filename.startswith(self.split_prefix):
                if not filename.endswith("log"):
                    continue
                self.log_file = os.path.join(self.spilt_log_dir, filename)
                lines = open(self.log_file, "r").readlines()
                all_lines.extend(lines)
                for line in lines:
                    if line in self.log_data:
                        continue
                    if self.info_key in line:
                        matches = self.pattern.findall(line)
                        try:
                            try:
                                data_json = json.loads(matches[0])
                            except:
                                data_json = eval(matches[0])
                            if "trace_id" in data_json and "start_time" in data_json:
                                print(f"send data_json trace_id={data_json['trace_id']} start_time={data_json['start_time']}")
                            else:
                                print(
                                    f"send data_json={json.dumps(data_json)}")
                            self.kafka_core.send_log_data(data_json, ensure_ascii=False)
                        except:
                            print("error", line.strip())
        self.kafka_core.batch_flush()
        self.log_data = all_lines


if __name__ == "__main__":
    d = QualityProcessor()
    for i in range(0, 35):
        d.read_file()
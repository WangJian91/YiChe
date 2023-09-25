# -*- coding: utf-8 -*-
from kafka import KafkaProducer
from kafka import KafkaConsumer
from datetime import datetime
import json
import traceback
import numpy as np
import enum


class LogAction(enum.Enum):
    CONFIG = 1
    WRITE = 2


def default_dump(obj):
    """Convert numpy classes to JSON serializable objects."""
    if isinstance(obj, (np.integer, np.floating, np.bool_)):
        return obj.item()
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    else:
        return obj


class KafkaSender(object):
    def __init__(self, config):
        hosts = config["hosts"]
        # self.common_topic = config["common_topic"]
        self.log_topic = config["log_topic"]
        # self.alert_topic = config["alert_topic"]
        self.time_out = config["time_out"]

        if "sasl_mechanism" in config:
            self.sasl_mechanism = config["sasl_mechanism"] if "sasl_mechanism" in config else None
            self.security_protocol = config["security_protocol"] if "security_protocol" in config else 'PLAINTEXT'
            self.sasl_plain_username = config["sasl_plain_username"] if "sasl_plain_username" in config else None
            self.sasl_plain_password = config["sasl_plain_password"] if "sasl_plain_password" in config else None

            self.client = KafkaProducer(bootstrap_servers=hosts, sasl_mechanism=self.sasl_mechanism,
                                        security_protocol=self.security_protocol,
                                        sasl_plain_username=self.sasl_plain_username,
                                        sasl_plain_password=self.sasl_plain_password,
                                        api_version=(2, 0, 2))
        else:
            self.client = KafkaProducer(bootstrap_servers=hosts)

    def set_common_log_config(self, module_name, sub_name, config, is_flush=False, ensure_ascii=True):
        data = {
            "ModuleName": module_name,
            "SubName": sub_name,
            "Action": LogAction.CONFIG.value,
            "Config": config,
        }
        return self._send_data(self.common_topic, data, is_flush, ensure_ascii)

    def send_common_log_data(self, module_name, sub_name, log_type, prefix, string, is_flush=False, ensure_ascii=True):
        if type(prefix) != str:
            prefix = str(prefix)
        if type(string) != str:
            string = str(string)
        data = {
            "ModuleName": module_name,
            "SubName": sub_name,
            "Action": LogAction.WRITE.value,
            "LogType": log_type,
            "Prefix": prefix,
            "String": string,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        }
        return self._send_data(self.common_topic, data, is_flush, ensure_ascii)

    def send_log_data(self, data, is_flush=False, ensure_ascii=True):
        return self._send_data(self.log_topic, data, is_flush, ensure_ascii)

    def send_alert_data(self, module, info, is_flush=False, ensure_ascii=True):
        data = {
            "Module": module,
            "Info": info
        }
        return self._send_data(self.alert_topic, data, is_flush, ensure_ascii)

    def _send_data(self, topic, value, is_flush, ensure_ascii):
        if type(value) != dict:
            return False
        try:
            value = json.dumps(value, ensure_ascii=ensure_ascii, default=default_dump).encode()
            self.client.send(topic=topic, value=value, partition=0)
            if is_flush:
                self.client.flush()
            return True
        except Exception as e:
            print(f"set key error {e}")
            print(traceback.format_exc())
            return False

    def batch_flush(self):
        self.client.flush()


class KafkaReceiver(object):
    def __init__(self, topic, config):
        hosts = config["hosts"]
        if topic == config["log_topic"]:
            group_id = config["log_group_id"]
        elif topic == config["alert_topic"]:
            group_id = config["alert_group_id"]
        elif topic == config["common_topic"]:
            group_id = config["common_group_id"]
        else:
            return
        consumer_timeout_ms = config["consumer_timeout_ms"]
        auto_offset_reset = config["auto_offset_reset"]
        enable_auto_commit = config["enable_auto_commit"]
        self.sasl_mechanism = config["sasl_mechanism"] if "sasl_mechanism" in config else None
        self.security_protocol = config["security_protocol"] if "security_protocol" in config else 'PLAINTEXT'
        self.sasl_plain_username = config["sasl_plain_username"] if "sasl_plain_username" in config else None
        self.sasl_plain_password = config["sasl_plain_password"] if "sasl_plain_password" in config else None
        self.consumer = KafkaConsumer(topic, bootstrap_servers=hosts, group_id=group_id,
                                      enable_auto_commit=enable_auto_commit, auto_offset_reset=auto_offset_reset,
                                      consumer_timeout_ms=consumer_timeout_ms, sasl_mechanism=self.sasl_mechanism,
                                      security_protocol=self.security_protocol,
                                      sasl_plain_username=self.sasl_plain_username,
                                      sasl_plain_password=self.sasl_plain_password)

        # self.consumer = KafkaConsumer(topic, bootstrap_servers=hosts, group_id=group_id,
        #                               enable_auto_commit=enable_auto_commit, auto_offset_reset=auto_offset_reset,
        #                               consumer_timeout_ms=consumer_timeout_ms)

# kafka 初始化
# if KafkaConfig:
#     kafka_sender = KafkaSender(KafkaConfig)
# else:
#     kafka_sender = None
# -*- coding: utf-8 -*-
import sys
sys.path.append("../../")
import time



time.sleep(60)

task = {
    "TitleProcessor":  QualityProcessor()
}

ATime = 1
def run():
    for key, processor in task.items():
        processor.read_file()
    Timer(ATime, run).start()


if __name__ == "__main__":
    run()

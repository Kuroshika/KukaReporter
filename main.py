import time

from kkreporter.reporter import KukaReporter

config_path = './kkreporter/kuka_reporter_config.yaml'
kkreporter = KukaReporter(config_path=config_path, log_path=config_path)
kkreporter.ending_report()
# kkreporter.recurring_report()
# while True:
#     time.sleep(10)
#     print("main thread is running")

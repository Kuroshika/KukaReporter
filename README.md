# KukaReporter

A tool for sending logs via email at regular intervals during model training, to conveniently check the progress and status of the model training process.

> <a href="https://github.com/Kuroshika/KukaReporter/blob/master/README_ZH.md"> 中文版README</a>
## Installation
The third-party libraries required for this tool are as follows:
```shell
pip install easydict
pip install apscheduler
pip install pyyaml
```

## Usage
Place the kkreporter module in your project directory, and then import the KukaReporter class using the following import statement:
```python
from kkreporter.reporter import KukaReporter
```

```python
# The config_path is the file path of the configuration file for the KukaReporter class.
# The configuration file is located at kkreporter/kuka_reporter_config.yaml within 
# the project directory.
kkreporter = KukaReporter(config_path=[your config path], log_path=[your log path])
```
- Send log reports on a scheduled basis

```python
kkreporter.recurring_report()
```
After executing this statement, the tool will send email reports on the training progress on a scheduled basis.
- Final Training Report

Execute after training completion
```python
kkreporter.ending_report()
```




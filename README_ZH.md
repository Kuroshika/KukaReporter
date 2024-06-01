# KukaReporter

一个用于在训练模型的时候定时通过邮件发送日志的工具，方便随时查看模型训练进度与训练情况。

## Installation
本工具需要的第三方库如下
```shell
pip install easydict
pip install apscheduler
pip install pyyaml
```

## Usage
把kkreporter放在项目中，然后通过`from kkreporter.reporter import KukaReporter`导入。

```python
# config_path是KukaReporter的配置文件路径，是kkreporter文件夹下的kuka_reporter_config.yaml
kkreporter = KukaReporter(config_path=[你的配置文件路径], log_path=[你要发送的训练日志路径])
```
- 定时发送日志报告

```python
kkreporter.recurring_report()
```
执行完这句语句后，本工具会定时发送邮件报告训练进度。
- 训练结束报告

训练结束后执行
```python
kkreporter.ending_report()
```




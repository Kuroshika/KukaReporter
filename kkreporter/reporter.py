import threading
import time
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import yaml
import easydict
from apscheduler.schedulers.background import BackgroundScheduler


class KukaReporter:
    def __init__(self, config_path, log_path=None):
        with open(config_path) as f:
            information = yaml.safe_load(f)
        information = easydict.EasyDict(information)
        self.sender = information.sender
        self.receiver = information.receiver

        self.smtp_server = information.smtp_server
        self.smtp_password = information.smtp_password
        self.interval = information.reporting_interval
        if self.interval < 30:
            self.interval = 10
        self.log_path = log_path
        self.log_lines = information.log_lines

    def recurring_report(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self._report_log, 'interval', minutes=self.interval)
        scheduler.start()

    def _report_log(self, subject=None, body=None):

        if self.log_path is not None and body is None:
            try:
                with open(self.log_path, "r") as f:
                    body = f.readlines()
                if self.log_lines > 0 and self.log_lines < len(body):
                    body = body[-1 * self.log_lines:]
                body = ''.join(str(item) for item in body)
            except:
                body = "Fail to get log!"
        else:
            body = "Log file path not specified. Nothing to report!"

        if subject is None:
            subject = "[KukaReporter]Report Log File at " + str(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self._report(subject=subject, body=body)

    def ending_report(self):
        ending_subject = "[KukaReporter]Mission Complete at " + str(
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self._report_log(subject=ending_subject)

    def _report(self, subject, body):
        msg = MIMEText(str(body))
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = self.receiver
        try:
            # 发送邮件
            with smtplib.SMTP(self.smtp_server) as smtp:
                smtp.starttls()
                smtp.login(self.sender, self.smtp_password)
                smtp.send_message(msg)
        except:
            pass

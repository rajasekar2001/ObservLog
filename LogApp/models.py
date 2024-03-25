from django.db import models

class LogRecord(models.Model):
    body = models.CharField(max_length=255)
    flags = models.IntegerField(default=0)
    observed_time_unix_nano = models.BigIntegerField(default=0)
    severity_number = models.IntegerField(default=0)
    severity_text = models.CharField(max_length=50, default='')
    span_id = models.CharField(max_length=255, blank=True)
    time_unix_nano = models.BigIntegerField(default=0)
    trace_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"LogRecord - {self.body}"

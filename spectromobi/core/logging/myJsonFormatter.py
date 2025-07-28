import datetime as dt
import json
import logging
from typing import Optional

LOG_RECORD_BUILTIN_ATTRS = {
    "args", "asctime", "created", "exc_info", "exc_text", "filename",
    "funcName", "levelname", "levelno", "lineno", "module", "msecs",
    "message", "msg", "name", "pathname", "process", "processName",
    "relativeCreated", "stack_info", "thread", "threadName", "taskName"
}

class MyJSONFormatter(logging.Formatter):
    def __init__(self, fmt_keys: Optional[dict[str, str]] = None):
        super().__init__()
        self.fmt_keys = fmt_keys or {}

    def format(self, record: logging.LogRecord) -> str:
        log_dict = self._prepare_log_dict(record)
        return json.dumps(log_dict, default=str)

    def _prepare_log_dict(self, record: logging.LogRecord) -> dict:
        base = {
            "message": record.getMessage(),
            "timestamp": dt.datetime.fromtimestamp(record.created, tz=dt.timezone.utc).isoformat()
        }

        if record.exc_info:
            base["exc_info"] = self.formatException(record.exc_info)
        if record.stack_info:
            base["stack_info"] = self.formatStack(record.stack_info)

        log_data = {
            key: base.pop(val, getattr(record, val, None))
            for key, val in self.fmt_keys.items()
        }
        log_data.update(base)

        for k, v in record.__dict__.items():
            if k not in LOG_RECORD_BUILTIN_ATTRS:
                log_data[k] = v

        return log_data


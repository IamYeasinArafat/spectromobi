import logging
import logging.handlers
from pathlib import Path
import threading


class DynamicFileHandler(logging.Handler):
    """
    Custom handler that routes logs to per-service rotating files based on logger name.
    """

    def __init__(
            self, log_dir: str,
            maxBytes=2_097_152, backupCount=5, logFileExt=".jsonl", level=logging.NOTSET,
            *args, **kwargs):
        super().__init__(level, *args, **kwargs)
        self.log_dir = Path(log_dir).resolve()
        self.log_dir.mkdir(parents=True, exist_ok=True)

        self.maxBytes = maxBytes
        self.backupCount = backupCount
        self.logFileExt = logFileExt

        self.handlers: dict[str, logging.Handler] = {}

    def _get_handler(self, record: logging.LogRecord) -> logging.Handler:
        service_name = ".".join(record.name.split('.')[1:]) or "root"
        # for service name like sinthia.tts.serviceA, we want to create a log file like sinthia/logs/tts/serviceA/log.jsonl
        log_file_path = self.log_dir / service_name.replace('.', '/') / f"log{self.logFileExt}"
        log_file_path.parent.mkdir(parents=True, exist_ok=True)

        if service_name not in self.handlers:
            log_file = log_file_path
            handler = logging.handlers.RotatingFileHandler(
                log_file, maxBytes=self.maxBytes, backupCount=self.backupCount
            )
            if self.formatter:
                handler.setFormatter(self.formatter)
            handler.setLevel(self.level)
            self.handlers[service_name] = handler
        return self.handlers[service_name]

    def emit(self, record: logging.LogRecord):
        try:
            handler = self._get_handler(record)
            handler.emit(record)
        except Exception:
            self.handleError(record)

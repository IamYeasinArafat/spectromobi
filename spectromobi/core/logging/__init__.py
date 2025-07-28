# __init__.py
import logging
import atexit
import logging.config
import logging.handlers
from pathlib import Path
import json



def init_logging():
    if logging.getLogger().hasHandlers():
        return  # logging already configured

    config_path = Path(__file__).parent / "config.json"
    with open(config_path, "r") as f:
        config = json.load(f)
    logging.config.dictConfig(config)

    queue_handler = logging.getHandlerByName("queue_handler")
    if isinstance(queue_handler, logging.handlers.QueueHandler):
        queue_handler.listener.start() # type: ignore
        atexit.register(queue_handler.listener.stop) # type: ignore


__all__ = ["init_logging"]
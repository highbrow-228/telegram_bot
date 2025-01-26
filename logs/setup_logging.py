import logging

from logging.handlers import RotatingFileHandler


def setup_logger():
    logger = logging.getLogger("telegram_bot_logs")
    logger.setLevel(logging.INFO)

    # Check if the logger already has handlers, to avoid duplicates
    if not logger.hasHandlers():
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Set log format using built-in attributes
        log_format = "%(asctime)s [%(filename)s][%(name)s.%(funcName)s] - %(message)s"
        formatter = logging.Formatter(log_format, datefmt="%d.%m.%Y %H:%M:%S")

        # Set the formatter for the console handler
        console_handler.setFormatter(formatter)

        file_handler = RotatingFileHandler(
            "logs/telegram_bot_logs.log",
            maxBytes = 8_000,
            backupCount = 2
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
import logging


def get_logger(name: str, logfile: str = "log.txt") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # ファイルハンドラの作成
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG)
    file_handler_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s"
    )
    file_handler.setFormatter(file_handler_formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler_formatter = logging.Formatter(
        "%(asctime)s.%(msecs)-3d - %(levelname)s - %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(console_handler_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

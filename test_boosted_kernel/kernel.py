from metakernel import MetaKernel
import logging
import os
from datetime import datetime


def add_custom_logger_handler(logger: logging.Logger):
    """
    Add a custom handlers to the metakernel logger; located
    in ./logs/*.log
    """

    # Get current datetime in format YYYY-MM-DD_HH-MM-SS
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = os.path.join(f"logs/{timestamp}.log")

    fh = logging.FileHandler(log_filename, encoding="utf-8")
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    log_level = "DEBUG"
    logger.setLevel(log_level)


class TestKernel(MetaKernel):
    implementation = "test"
    implementation_version = "1.0"
    language = "no-op"
    help_suffix = "?"
    language_version = "0.1"
    language_info = {
        "name": "plop",
        "mimetype": "text/plain",
        "file_extension": ".plop",
    }
    banner = "Test Boosted Magics"
    app_name = "test"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        add_custom_logger_handler(self.log)

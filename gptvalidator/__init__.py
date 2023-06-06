import logging
import logging.config
from pathlib import Path

from yaml import safe_load


def setup_logging() -> None:
    # https://docs.python.org/3/howto/logging.html#configuring-logging
    logging_configuration_file = Path(__file__).parent / "logging.yml"
    logging_configuration = safe_load(stream=logging_configuration_file.read_text())
    logging.config.dictConfig(logging_configuration)


setup_logging()


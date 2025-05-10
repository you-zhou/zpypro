import logging
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


def main():
    logger.debug("Debug message from main")
    logger.info("Hello from zpypro!")
    logger.warning("This is a warning")
    try:
        1 / 0
    except Exception as e:
        logger.error(f"Error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    main()

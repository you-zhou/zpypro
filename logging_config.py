import os
import logging
import logging.config
import sys

from appdirs import user_log_dir
import yaml

from constants import APP_NAME, APP_AUTHOR, LOG_FILE


def setup_logging():
    """
    Set up logging configuration from YAML file.
    Uses appdirs to determine the appropriate log directory.
    """
    # Create log directory if it doesn't exist
    log_dir = user_log_dir(APP_NAME, APP_AUTHOR)
    os.makedirs(log_dir, exist_ok=True)

    log_file_path = os.path.join(log_dir, LOG_FILE)

    # Get the directory of the config file
    config_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(config_dir, "logging_config.yaml")

    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        # Set the log file path dynamically
        config["handlers"]["file"]["filename"] = log_file_path

        # Apply the configuration
        logging.config.dictConfig(config)

        # Log the configuration paths
        logger = logging.getLogger(__name__)
        logger.info(f"Logging to file: {log_file_path}")
        logger.info(f"Loaded logging config from: {config_path}")
    else:
        # Fallback to basic configuration if YAML file is not found
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(log_file_path)],
        )
        print(f"Warning: Logging config file not found at {config_path}. Using basic configuration.")

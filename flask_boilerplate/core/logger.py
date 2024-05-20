"""
Centralized logger for the application

Description:
    - Centralized logger for the application
    - Initializes the logger with a file handler

"""

from logging import DEBUG, FileHandler, Formatter, Logger, getLogger
from pathlib import Path
from typing import Self


class AppLogger:
    """
    Centralized logger for the application

    Description:
        - This class is used to create a centralized logger for the application
    """

    _instance: Self | None = None
    logger: Logger

    def __new__(cls) -> Self:
        """
        Singleton class

        Description:
            - This method is used to create a singleton class
            - If the instance is already created, it returns the instance
            - If the instance is not created, it creates a new instance

        Args:
            - `cls (class)`: class object

        Returns:
            - `Self`: class instance

        """

        if not cls._instance:
            cls._instance = super().__new__(cls)

            # Initialize the logger
            cls._instance.logger = getLogger(__name__)
            cls._instance.logger.setLevel(DEBUG)

            # Ensure the logs directory exists
            Path("logs").mkdir(parents=True, exist_ok=True)

            # Create handlers
            handler = FileHandler("logs/app.log")
            handler.setLevel(DEBUG)

            # Create formatters and add them to handlers
            formatter = Formatter(
                "%(asctime)s - %(filename)s:%(lineno)d - "
                "%(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)

            # Add handlers to the logger
            if not cls._instance.logger.handlers:
                cls._instance.logger.addHandler(handler)

        return cls._instance  # type: ignore

    def get_logger(self) -> Logger:
        """
        Get the logger instance

        Returns:
            - `logging.Logger`: logger instance
        """

        return self.logger

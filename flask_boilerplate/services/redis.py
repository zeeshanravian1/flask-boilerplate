import json
import logging
import fakeredis

import redis as pyredis
from redis.exceptions import ConnectionError, RedisError, TimeoutError
from retry import retry

from flask_boilerplate.core.config import ENVIRONMENT, REDIS_HOST, REDIS_PORT


class Redis:
    def __init__(self):
        self._redis_connection = None
        # Avoid additional ping for normal use-cases at the cost of
        # a redundant check
        if not self._redis_connection:
            self.redis_connect()

    def redis_connect(self):
        try:
            if self._redis_connection and self._redis_connection.ping():
                return
        except RedisError as ex:
            logging.error(f"Error while pinging {ex}")
            pass

        if ENVIRONMENT == "testing":
            self._redis_connection = fakeredis.FakeStrictRedis()
        else:
            self._redis_connection = pyredis.Redis(
                REDIS_HOST, REDIS_PORT, decode_responses=True
            )
        logging.info(f"Host={REDIS_HOST}:Port{REDIS_PORT}")

    @retry((ConnectionError, TimeoutError), 2, 1)
    def get(self, key) -> set:
        """
        Get data

        Args:
            key:
        Returns:
            data string
        """
        try:
            data = self._redis_connection.get(key)
            return json.loads(data) if data else None
        except (ConnectionError, TimeoutError) as ex:
            logging.error(f"Redis error: {ex}")
            self.redis_connect()
            raise

    @retry((ConnectionError, TimeoutError), 2, 1)
    def set(self, key, data: list) -> None:
        """
        Set data

        Args:
            key:
            data: str
        Returns:
            None
        """
        try:
            self._redis_connection.set(key, json.dumps(data))
        except (ConnectionError, TimeoutError) as ex:
            logging.error(f"Redis error: {ex}")
            self.redis_connect()
            raise

    @retry((ConnectionError, TimeoutError), 2, 1)
    def delete(self, key: str) -> None:
        """
        delete data stored at redis against a key

        Args:
            key: key for redis data
        """
        try:
            self._redis_connection.delete(key)
        except (ConnectionError, TimeoutError) as ex:
            logging.error(f"Redis error: {ex}")
            self.redis_connect()
            raise


redis = Redis()

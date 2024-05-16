"""
Base Constants

Description:
    - This module contains all base constants.

"""

from datetime import datetime, timezone

CONTENT_TYPE_JSON: dict = {"Content-Type": "application/json"}

# Response Constants
ID: int = 1
CREATED_AT: datetime = datetime.now(tz=timezone.utc)
UPDATED_AT: datetime = datetime.now(tz=timezone.utc)

TOTAL_RECORDS: int = 1
TOTAL_PAGES: int = 1
PAGE: int = 1
LIMIT: int = 10
TOKEN_EXPIRY_TIME: int = 86400

# Error Messages
ERROR_MESSAGES: dict[str, str] = {
    "409": "Integrity Error",
    "500": "Internal Server Error",
}

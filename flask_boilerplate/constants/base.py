# -*- coding: utf-8 -*-
"""
Base Constants

Description:
    - This module contains all base constants.

"""

from datetime import datetime, timezone

ID: int = 1
CREATED_AT: datetime = datetime.now(tz=timezone.utc)
UPDATED_AT: datetime = datetime.now(tz=timezone.utc)

TOTAL_RECORDS: int = 1
TOTAL_PAGES: int = 1
PAGE: int = 1
LIMIT: int = 10

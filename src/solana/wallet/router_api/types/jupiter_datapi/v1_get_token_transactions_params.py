# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1GetTokenTransactionsParams"]


class V1GetTokenTransactionsParams(TypedDict, total=False):
    from_ts: Annotated[Union[str, datetime], PropertyInfo(alias="fromTs", format="iso8601")]
    """Filter transactions from this timestamp"""

    limit: int
    """Maximum number of transactions"""

    offset: str
    """Pagination offset token"""

    offset_ts: Annotated[Union[str, datetime], PropertyInfo(alias="offsetTs", format="iso8601")]
    """Offset timestamp for pagination"""

    to_ts: Annotated[Union[str, datetime], PropertyInfo(alias="toTs", format="iso8601")]
    """Filter transactions until this timestamp"""

    trader_address: Annotated[str, PropertyInfo(alias="traderAddress")]
    """Filter by trader wallet address"""

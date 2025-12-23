# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PhantomSearchSplTokensParams"]


class PhantomSearchSplTokensParams(TypedDict, total=False):
    charts: Literal["true", "false"]
    """Include spark charts data"""

    page: str
    """Page number (0-indexed)"""

    query: str
    """Search query string"""

    sniper: Literal["true", "false"]
    """Enable sniper mode"""

    sort_by: Annotated[
        Literal["volume-desc", "volume-asc", "marketcap-desc", "marketcap-asc", "liquidity-desc", "liquidity-asc"],
        PropertyInfo(alias="sortBy"),
    ]
    """Sort field and direction"""

    time_range: Annotated[Literal["5m", "1h", "8h", "24h"], PropertyInfo(alias="timeRange")]
    """Time range for statistics"""

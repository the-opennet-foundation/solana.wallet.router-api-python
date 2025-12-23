# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V2GetTokenPriceChartParams"]


class V2GetTokenPriceChartParams(TypedDict, total=False):
    base_asset: Required[Annotated[str, PropertyInfo(alias="baseAsset")]]
    """Base asset for price calculation"""

    candles: Required[int]
    """Number of candles to return"""

    from_: Required[Annotated[Union[int, Union[str, datetime]], PropertyInfo(alias="from", format="iso8601")]]
    """Start timestamp (Unix seconds or ISO date)"""

    interval: Required[
        Literal[
            "1_SECOND",
            "15_SECOND",
            "30_SECOND",
            "1_MINUTE",
            "3_MINUTE",
            "5_MINUTE",
            "15_MINUTE",
            "30_MINUTE",
            "1_HOUR",
            "2_HOUR",
            "4_HOUR",
            "8_HOUR",
            "12_HOUR",
            "1_DAY",
            "1_WEEK",
            "1_MONTH",
        ]
    ]
    """Candlestick interval"""

    to: Required[Annotated[Union[int, Union[str, datetime]], PropertyInfo(format="iso8601")]]
    """End timestamp (Unix seconds or ISO date)"""

    type: Literal["price", "mcap"]
    """Chart type"""

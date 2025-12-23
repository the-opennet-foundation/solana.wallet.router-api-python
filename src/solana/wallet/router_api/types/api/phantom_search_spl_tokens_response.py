# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PhantomSearchSplTokensResponse", "Data", "SparkChart"]


class Data(BaseModel):
    address: Optional[str] = None

    decimals: Optional[int] = None

    liquidity: Optional[float] = None

    logo_uri: Optional[str] = FieldInfo(alias="logoURI", default=None)

    mc: Optional[float] = None
    """Market cap"""

    name: Optional[str] = None

    price_usd: Optional[float] = FieldInfo(alias="priceUsd", default=None)

    supply: Optional[float] = None

    symbol: Optional[str] = None

    telegram_call_count: Union[str, float, None] = FieldInfo(alias="telegramCallCount", default=None)

    tweets24h: Optional[int] = None

    unique_tweeters24h: Optional[int] = FieldInfo(alias="uniqueTweeters24h", default=None)

    v1h_usd: Optional[float] = FieldInfo(alias="v1hUSD", default=None)

    v24h_usd: Optional[float] = FieldInfo(alias="v24hUSD", default=None)
    """24-hour volume in USD"""

    v5m_usd: Optional[float] = FieldInfo(alias="v5mUSD", default=None)

    v8h_usd: Optional[float] = FieldInfo(alias="v8hUSD", default=None)


class SparkChart(BaseModel):
    unix_time: Optional[int] = FieldInfo(alias="unixTime", default=None)

    value: Optional[float] = None


class PhantomSearchSplTokensResponse(BaseModel):
    data: Optional[List[Data]] = None

    spark_charts: Optional[Dict[str, List[SparkChart]]] = FieldInfo(alias="sparkCharts", default=None)

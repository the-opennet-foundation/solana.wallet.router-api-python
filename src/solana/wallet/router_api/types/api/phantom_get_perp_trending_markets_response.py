# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "PhantomGetPerpTrendingMarketsResponse",
    "TrendingMarket",
    "TrendingMarketToken",
    "TrendingMarketPriceChange24h",
]


class TrendingMarketToken(BaseModel):
    address: Optional[str] = None

    chain_id: Optional[str] = FieldInfo(alias="chainId", default=None)

    resource_type: Optional[str] = FieldInfo(alias="resourceType", default=None)


class TrendingMarketPriceChange24h(BaseModel):
    amount: Optional[str] = None

    percentage: Optional[str] = None


class TrendingMarket(BaseModel):
    token: Optional[TrendingMarketToken] = None

    asset_id: Optional[int] = FieldInfo(alias="assetId", default=None)

    description: Optional[str] = None

    funding_rate: Optional[str] = FieldInfo(alias="fundingRate", default=None)

    is_at_open_interest_cap: Optional[bool] = FieldInfo(alias="isAtOpenInterestCap", default=None)

    logo_uri: Optional[str] = FieldInfo(alias="logoUri", default=None)

    max_leverage: Optional[float] = FieldInfo(alias="maxLeverage", default=None)

    name: Optional[str] = None

    open_interest: Optional[str] = FieldInfo(alias="openInterest", default=None)

    price: Optional[str] = None

    price_change24h: Optional[TrendingMarketPriceChange24h] = FieldInfo(alias="priceChange24h", default=None)

    symbol: Optional[str] = None

    sz_decimals: Optional[int] = FieldInfo(alias="szDecimals", default=None)

    volume24h: Optional[str] = None


class PhantomGetPerpTrendingMarketsResponse(BaseModel):
    trending_markets: Optional[List[TrendingMarket]] = FieldInfo(alias="trendingMarkets", default=None)

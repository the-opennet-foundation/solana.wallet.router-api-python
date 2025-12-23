# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PhantomGetSimpleTokenOverviewsResponse", "Data"]


class Data(BaseModel):
    address: Optional[str] = None

    decimals: Optional[int] = None

    logo_uri: Optional[str] = FieldInfo(alias="logoURI", default=None)

    mc: Optional[float] = None

    name: Optional[str] = None

    price_change24h: Optional[float] = FieldInfo(alias="priceChange24h", default=None)

    price_usd: Optional[float] = FieldInfo(alias="priceUsd", default=None)

    supply: Optional[float] = None

    symbol: Optional[str] = None

    v24h_usd: Optional[float] = FieldInfo(alias="v24hUSD", default=None)


class PhantomGetSimpleTokenOverviewsResponse(BaseModel):
    data: Optional[List[Data]] = None

    success: Optional[bool] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PhantomExploreMemeTokensResponse", "Data"]


class Data(BaseModel):
    bonding_curve_platform: Optional[str] = FieldInfo(alias="bondingCurvePlatform", default=None)

    image: Optional[str] = None

    liquidity: Optional[float] = None

    market_cap: Optional[float] = FieldInfo(alias="marketCap", default=None)

    name: Optional[str] = None

    symbol: Optional[str] = None

    token_address: Optional[str] = FieldInfo(alias="tokenAddress", default=None)

    unique_holders: Optional[int] = FieldInfo(alias="uniqueHolders", default=None)

    volume: Optional[float] = None


class PhantomExploreMemeTokensResponse(BaseModel):
    data: Optional[Dict[str, List[Data]]] = None

    success: Optional[bool] = None

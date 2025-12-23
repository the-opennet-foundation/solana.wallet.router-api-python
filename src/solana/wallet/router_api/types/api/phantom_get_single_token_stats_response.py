# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PhantomGetSingleTokenStatsResponse", "Data"]


class Data(BaseModel):
    trade24h: Optional[int] = None

    trade5m: Optional[int] = None

    unique_wallet24h: Optional[int] = FieldInfo(alias="uniqueWallet24h", default=None)

    unique_wallet5m: Optional[int] = FieldInfo(alias="uniqueWallet5m", default=None)

    v_buy_history24h_usd: Optional[float] = FieldInfo(alias="vBuyHistory24hUSD", default=None)

    v_history24h_usd: Optional[float] = FieldInfo(alias="vHistory24hUSD", default=None)

    v_history5m_usd: Optional[float] = FieldInfo(alias="vHistory5mUSD", default=None)

    v_sell_history24h_usd: Optional[float] = FieldInfo(alias="vSellHistory24hUSD", default=None)


class PhantomGetSingleTokenStatsResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None

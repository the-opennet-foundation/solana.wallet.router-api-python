# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SwapStats"]


class SwapStats(BaseModel):
    buy_organic_volume: Optional[float] = FieldInfo(alias="buyOrganicVolume", default=None)
    """Organic buy volume in USD"""

    buy_volume: Optional[float] = FieldInfo(alias="buyVolume", default=None)
    """Total buy volume in USD"""

    holder_change: Optional[int] = FieldInfo(alias="holderChange", default=None)
    """Net holder count change"""

    liquidity_change: Optional[float] = FieldInfo(alias="liquidityChange", default=None)
    """Liquidity change percentage"""

    num_buys: Optional[int] = FieldInfo(alias="numBuys", default=None)
    """Number of buy transactions"""

    num_net_buyers: Optional[int] = FieldInfo(alias="numNetBuyers", default=None)
    """Net buyers (buys - sells)"""

    num_organic_buyers: Optional[int] = FieldInfo(alias="numOrganicBuyers", default=None)
    """Organic buyers count"""

    num_sells: Optional[int] = FieldInfo(alias="numSells", default=None)
    """Number of sell transactions"""

    num_traders: Optional[int] = FieldInfo(alias="numTraders", default=None)
    """Unique traders count"""

    price_change: Optional[float] = FieldInfo(alias="priceChange", default=None)
    """Price change percentage"""

    sell_organic_volume: Optional[float] = FieldInfo(alias="sellOrganicVolume", default=None)
    """Organic sell volume in USD"""

    sell_volume: Optional[float] = FieldInfo(alias="sellVolume", default=None)
    """Total sell volume in USD"""

    volume_change: Optional[float] = FieldInfo(alias="volumeChange", default=None)
    """Volume change percentage"""

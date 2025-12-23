# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1GetTokenTransactionsResponse", "Tx"]


class Tx(BaseModel):
    amount: Optional[float] = None
    """Token amount"""

    asset: Optional[str] = None
    """Token mint address"""

    is_mev: Optional[bool] = FieldInfo(alias="isMev", default=None)
    """Whether this is an MEV transaction"""

    is_valid_price: Optional[bool] = FieldInfo(alias="isValidPrice", default=None)
    """Whether price is valid for chart display"""

    native_volume: Optional[float] = FieldInfo(alias="nativeVolume", default=None)
    """Transaction volume in native token"""

    pool_id: Optional[str] = FieldInfo(alias="poolId", default=None)
    """Pool where trade occurred"""

    timestamp: Optional[datetime] = None

    trader_address: Optional[str] = FieldInfo(alias="traderAddress", default=None)
    """Trader wallet address"""

    tx_hash: Optional[str] = FieldInfo(alias="txHash", default=None)
    """Transaction signature"""

    type: Optional[Literal["buy", "sell"]] = None

    usd_price: Optional[float] = FieldInfo(alias="usdPrice", default=None)
    """Price at transaction time in USD"""

    usd_volume: Optional[float] = FieldInfo(alias="usdVolume", default=None)
    """Transaction volume in USD"""


class V1GetTokenTransactionsResponse(BaseModel):
    next: Optional[str] = None
    """Pagination cursor"""

    txs: Optional[List[Tx]] = None

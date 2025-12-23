# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .swap_stats import SwapStats
from .token_audit import TokenAudit

__all__ = ["JupiterToken", "FirstPool"]


class FirstPool(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)


class JupiterToken(BaseModel):
    id: Optional[str] = None
    """Token mint address"""

    audit: Optional[TokenAudit] = None

    circ_supply: Optional[float] = FieldInfo(alias="circSupply", default=None)

    decimals: Optional[int] = None

    fdv: Optional[float] = None

    first_pool: Optional[FirstPool] = FieldInfo(alias="firstPool", default=None)

    holder_count: Optional[int] = FieldInfo(alias="holderCount", default=None)

    icon: Optional[str] = None

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    liquidity: Optional[float] = None

    mcap: Optional[float] = None

    name: Optional[str] = None

    organic_score: Optional[float] = FieldInfo(alias="organicScore", default=None)

    organic_score_label: Optional[Literal["high", "medium", "low"]] = FieldInfo(alias="organicScoreLabel", default=None)

    price_block_id: Optional[int] = FieldInfo(alias="priceBlockId", default=None)

    stats1h: Optional[SwapStats] = None

    stats24h: Optional[SwapStats] = None

    stats5m: Optional[SwapStats] = None

    stats6h: Optional[SwapStats] = None

    symbol: Optional[str] = None

    token_program: Optional[str] = FieldInfo(alias="tokenProgram", default=None)

    total_supply: Optional[float] = FieldInfo(alias="totalSupply", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    usd_price: Optional[float] = FieldInfo(alias="usdPrice", default=None)

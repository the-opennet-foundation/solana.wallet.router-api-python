# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SolanaGetStatusResponse"]


class SolanaGetStatusResponse(BaseModel):
    block: Optional[int] = None
    """Current block height"""

    sol_price: Optional[float] = FieldInfo(alias="solPrice", default=None)
    """Current SOL price in USD"""

    tps: Optional[float] = None
    """Transactions per second"""

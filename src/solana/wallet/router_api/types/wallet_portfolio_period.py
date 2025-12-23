# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WalletPortfolioPeriod"]


class WalletPortfolioPeriod(BaseModel):
    total_percentage: Optional[float] = FieldInfo(alias="totalPercentage", default=None)
    """PnL percentage for the period"""

    total_pnl: Optional[float] = FieldInfo(alias="totalPnl", default=None)
    """PnL for the period in USD"""

    total_pnl_native: Optional[float] = FieldInfo(alias="totalPnlNative", default=None)
    """PnL for the period in SOL"""

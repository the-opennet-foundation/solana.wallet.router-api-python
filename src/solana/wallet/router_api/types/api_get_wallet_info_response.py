# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .wallet_portfolio_period import WalletPortfolioPeriod

__all__ = ["APIGetWalletInfoResponse", "RecentTransaction", "Token", "JupiterPortfolio"]


class RecentTransaction(BaseModel):
    err: bool
    """Whether the transaction failed"""

    signature: str
    """Transaction signature"""

    slot: int
    """Slot number"""

    block_time: Optional[int] = FieldInfo(alias="blockTime", default=None)
    """Block timestamp (Unix seconds)"""


class Token(BaseModel):
    amount: float
    """Token balance (UI amount, not raw)"""

    decimals: int
    """Token decimals"""

    mint: str
    """Token mint address"""


class JupiterPortfolio(BaseModel):
    day1: Optional[WalletPortfolioPeriod] = None

    day30: Optional[WalletPortfolioPeriod] = None

    day7: Optional[WalletPortfolioPeriod] = None

    net_worth: Optional[float] = FieldInfo(alias="netWorth", default=None)
    """Total portfolio value in USD"""

    net_worth_native: Optional[float] = FieldInfo(alias="netWorthNative", default=None)
    """Total portfolio value in SOL"""

    total_assets_in_positions: Optional[float] = FieldInfo(alias="totalAssetsInPositions", default=None)
    """Number of assets in positions"""

    total_percentage: Optional[float] = FieldInfo(alias="totalPercentage", default=None)
    """Total PnL percentage"""

    total_pnl: Optional[float] = FieldInfo(alias="totalPnl", default=None)
    """Total profit/loss in USD"""

    total_pnl_native: Optional[float] = FieldInfo(alias="totalPnlNative", default=None)
    """Total profit/loss in SOL"""

    total_sol_balance: Optional[float] = FieldInfo(alias="totalSolBalance", default=None)
    """Total SOL balance"""

    total_usdc_balance: Optional[float] = FieldInfo(alias="totalUsdcBalance", default=None)
    """Total USDC balance"""


class APIGetWalletInfoResponse(BaseModel):
    recent_transactions: List[RecentTransaction] = FieldInfo(alias="recentTransactions")

    sol_balance: float = FieldInfo(alias="solBalance")
    """SOL balance in SOL (not lamports)"""

    tokens: List[Token]

    jupiter_portfolio: Optional[JupiterPortfolio] = FieldInfo(alias="jupiterPortfolio", default=None)

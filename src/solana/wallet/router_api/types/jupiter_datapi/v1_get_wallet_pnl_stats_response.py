# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V1GetWalletPnlStatsResponse",
    "V1GetWalletPnlStatsResponseItem",
    "V1GetWalletPnlStatsResponseItemStats",
    "V1GetWalletPnlStatsResponseItemStats_1d",
    "V1GetWalletPnlStatsResponseItemStats_30d",
    "V1GetWalletPnlStatsResponseItemStats_7d",
    "V1GetWalletPnlStatsResponseItemStatsTotal",
]


class V1GetWalletPnlStatsResponseItemStats_1d(BaseModel):
    net_worth: Optional[float] = FieldInfo(alias="netWorth", default=None)

    net_worth_native: Optional[float] = FieldInfo(alias="netWorthNative", default=None)

    total_percentage: Optional[float] = FieldInfo(alias="totalPercentage", default=None)

    total_pnl: Optional[float] = FieldInfo(alias="totalPnl", default=None)

    total_pnl_native: Optional[float] = FieldInfo(alias="totalPnlNative", default=None)


class V1GetWalletPnlStatsResponseItemStats_30d(BaseModel):
    net_worth: Optional[float] = FieldInfo(alias="netWorth", default=None)

    net_worth_native: Optional[float] = FieldInfo(alias="netWorthNative", default=None)

    total_percentage: Optional[float] = FieldInfo(alias="totalPercentage", default=None)

    total_pnl: Optional[float] = FieldInfo(alias="totalPnl", default=None)

    total_pnl_native: Optional[float] = FieldInfo(alias="totalPnlNative", default=None)


class V1GetWalletPnlStatsResponseItemStats_7d(BaseModel):
    net_worth: Optional[float] = FieldInfo(alias="netWorth", default=None)

    net_worth_native: Optional[float] = FieldInfo(alias="netWorthNative", default=None)

    total_percentage: Optional[float] = FieldInfo(alias="totalPercentage", default=None)

    total_pnl: Optional[float] = FieldInfo(alias="totalPnl", default=None)

    total_pnl_native: Optional[float] = FieldInfo(alias="totalPnlNative", default=None)


class V1GetWalletPnlStatsResponseItemStatsTotal(BaseModel):
    net_worth: Optional[float] = FieldInfo(alias="netWorth", default=None)

    net_worth_native: Optional[float] = FieldInfo(alias="netWorthNative", default=None)

    total_percentage: Optional[float] = FieldInfo(alias="totalPercentage", default=None)

    total_pnl: Optional[float] = FieldInfo(alias="totalPnl", default=None)

    total_pnl_native: Optional[float] = FieldInfo(alias="totalPnlNative", default=None)


class V1GetWalletPnlStatsResponseItemStats(BaseModel):
    api_1d: Optional[V1GetWalletPnlStatsResponseItemStats_1d] = FieldInfo(alias="1d", default=None)

    api_30d: Optional[V1GetWalletPnlStatsResponseItemStats_30d] = FieldInfo(alias="30d", default=None)

    api_7d: Optional[V1GetWalletPnlStatsResponseItemStats_7d] = FieldInfo(alias="7d", default=None)

    total: Optional[V1GetWalletPnlStatsResponseItemStatsTotal] = None


class V1GetWalletPnlStatsResponseItem(BaseModel):
    stats: Optional[V1GetWalletPnlStatsResponseItemStats] = None

    total_assets_in_positions: Optional[float] = FieldInfo(alias="totalAssetsInPositions", default=None)

    total_sol_balance: Optional[float] = FieldInfo(alias="totalSolBalance", default=None)

    total_usdc_balance: Optional[float] = FieldInfo(alias="totalUsdcBalance", default=None)


V1GetWalletPnlStatsResponse: TypeAlias = Dict[str, V1GetWalletPnlStatsResponseItem]

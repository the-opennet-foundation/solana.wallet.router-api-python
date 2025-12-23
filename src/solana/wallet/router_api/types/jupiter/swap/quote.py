# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Quote", "RoutePlan", "RoutePlanSwapInfo"]


class RoutePlanSwapInfo(BaseModel):
    amm_key: Optional[str] = FieldInfo(alias="ammKey", default=None)
    """AMM pool address"""

    fee_amount: Optional[str] = FieldInfo(alias="feeAmount", default=None)

    fee_mint: Optional[str] = FieldInfo(alias="feeMint", default=None)

    in_amount: Optional[str] = FieldInfo(alias="inAmount", default=None)

    input_mint: Optional[str] = FieldInfo(alias="inputMint", default=None)

    label: Optional[str] = None
    """DEX label (e.g., "Raydium", "Orca")"""

    out_amount: Optional[str] = FieldInfo(alias="outAmount", default=None)

    output_mint: Optional[str] = FieldInfo(alias="outputMint", default=None)


class RoutePlan(BaseModel):
    percent: Optional[int] = None
    """Percentage of route through this step"""

    swap_info: Optional[RoutePlanSwapInfo] = FieldInfo(alias="swapInfo", default=None)


class Quote(BaseModel):
    in_amount: str = FieldInfo(alias="inAmount")
    """Input amount in smallest units"""

    input_mint: str = FieldInfo(alias="inputMint")
    """Input token mint address"""

    out_amount: str = FieldInfo(alias="outAmount")
    """Expected output amount in smallest units"""

    output_mint: str = FieldInfo(alias="outputMint")
    """Output token mint address"""

    other_amount_threshold: Optional[str] = FieldInfo(alias="otherAmountThreshold", default=None)
    """Minimum output amount (with slippage)"""

    price_impact_pct: Optional[str] = FieldInfo(alias="priceImpactPct", default=None)
    """Price impact percentage"""

    route_plan: Optional[List[RoutePlan]] = FieldInfo(alias="routePlan", default=None)

    slippage_bps: Optional[int] = FieldInfo(alias="slippageBps", default=None)
    """Slippage in basis points"""

    swap_mode: Optional[Literal["ExactIn", "ExactOut"]] = FieldInfo(alias="swapMode", default=None)

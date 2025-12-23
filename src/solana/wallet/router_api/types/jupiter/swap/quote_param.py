# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["QuoteParam", "RoutePlan", "RoutePlanSwapInfo"]


class RoutePlanSwapInfo(TypedDict, total=False):
    amm_key: Annotated[str, PropertyInfo(alias="ammKey")]
    """AMM pool address"""

    fee_amount: Annotated[str, PropertyInfo(alias="feeAmount")]

    fee_mint: Annotated[str, PropertyInfo(alias="feeMint")]

    in_amount: Annotated[str, PropertyInfo(alias="inAmount")]

    input_mint: Annotated[str, PropertyInfo(alias="inputMint")]

    label: str
    """DEX label (e.g., "Raydium", "Orca")"""

    out_amount: Annotated[str, PropertyInfo(alias="outAmount")]

    output_mint: Annotated[str, PropertyInfo(alias="outputMint")]


class RoutePlan(TypedDict, total=False):
    percent: int
    """Percentage of route through this step"""

    swap_info: Annotated[RoutePlanSwapInfo, PropertyInfo(alias="swapInfo")]


class QuoteParam(TypedDict, total=False):
    in_amount: Required[Annotated[str, PropertyInfo(alias="inAmount")]]
    """Input amount in smallest units"""

    input_mint: Required[Annotated[str, PropertyInfo(alias="inputMint")]]
    """Input token mint address"""

    out_amount: Required[Annotated[str, PropertyInfo(alias="outAmount")]]
    """Expected output amount in smallest units"""

    output_mint: Required[Annotated[str, PropertyInfo(alias="outputMint")]]
    """Output token mint address"""

    other_amount_threshold: Annotated[str, PropertyInfo(alias="otherAmountThreshold")]
    """Minimum output amount (with slippage)"""

    price_impact_pct: Annotated[str, PropertyInfo(alias="priceImpactPct")]
    """Price impact percentage"""

    route_plan: Annotated[Iterable[RoutePlan], PropertyInfo(alias="routePlan")]

    slippage_bps: Annotated[int, PropertyInfo(alias="slippageBps")]
    """Slippage in basis points"""

    swap_mode: Annotated[Literal["ExactIn", "ExactOut"], PropertyInfo(alias="swapMode")]

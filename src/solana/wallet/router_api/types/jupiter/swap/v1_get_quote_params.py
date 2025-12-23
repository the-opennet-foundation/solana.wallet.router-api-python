# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["V1GetQuoteParams"]


class V1GetQuoteParams(TypedDict, total=False):
    amount: Required[int]
    """Input amount in smallest units (lamports for SOL)"""

    input_mint: Required[Annotated[str, PropertyInfo(alias="inputMint")]]
    """Input token mint address"""

    output_mint: Required[Annotated[str, PropertyInfo(alias="outputMint")]]
    """Output token mint address"""

    as_legacy_transaction: Annotated[bool, PropertyInfo(alias="asLegacyTransaction")]
    """Return legacy transaction format"""

    only_direct_routes: Annotated[bool, PropertyInfo(alias="onlyDirectRoutes")]
    """Only use direct routes (no intermediate tokens)"""

    slippage_bps: Annotated[int, PropertyInfo(alias="slippageBps")]
    """Slippage tolerance in basis points (100 = 1%)"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .quote_param import QuoteParam

__all__ = ["V1ExecuteSwapParams"]


class V1ExecuteSwapParams(TypedDict, total=False):
    quote_response: Required[Annotated[QuoteParam, PropertyInfo(alias="quoteResponse")]]

    user_public_key: Required[Annotated[str, PropertyInfo(alias="userPublicKey")]]
    """User's wallet public key"""

    dynamic_compute_unit_limit: Annotated[bool, PropertyInfo(alias="dynamicComputeUnitLimit")]
    """Enable dynamic compute unit limit"""

    prioritization_fee_lamports: Annotated[Optional[int], PropertyInfo(alias="prioritizationFeeLamports")]
    """Priority fee in lamports"""

    wrap_unwrap_sol: Annotated[bool, PropertyInfo(alias="wrapUnwrapSOL")]
    """Automatically wrap/unwrap SOL"""

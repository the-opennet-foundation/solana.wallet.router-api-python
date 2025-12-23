# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PhantomGetPerpTrendingMarketsParams"]


class PhantomGetPerpTrendingMarketsParams(TypedDict, total=False):
    chain_id: Annotated[str, PropertyInfo(alias="chainId")]
    """Chain ID for the markets"""

    limit: str
    """Maximum number of results"""

    sort_by: Annotated[Literal["volume", "openInterest", "fundingRate"], PropertyInfo(alias="sortBy")]
    """Sort field"""

    sort_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortDirection")]
    """Sort direction"""

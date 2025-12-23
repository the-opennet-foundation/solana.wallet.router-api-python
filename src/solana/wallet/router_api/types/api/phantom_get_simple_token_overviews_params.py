# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PhantomGetSimpleTokenOverviewsParams"]


class PhantomGetSimpleTokenOverviewsParams(TypedDict, total=False):
    token_addresses: Required[Annotated[str, PropertyInfo(alias="tokenAddresses")]]
    """Comma-separated token mint addresses"""

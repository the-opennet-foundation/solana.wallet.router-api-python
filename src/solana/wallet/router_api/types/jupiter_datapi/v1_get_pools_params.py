# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1GetPoolsParams"]


class V1GetPoolsParams(TypedDict, total=False):
    asset_ids: Required[Annotated[str, PropertyInfo(alias="assetIds")]]
    """Comma-separated token mint addresses"""

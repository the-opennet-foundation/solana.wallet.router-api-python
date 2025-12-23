# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TokenListParams"]


class TokenListParams(TypedDict, total=False):
    category: Literal["trending", "new", "topvolume"]
    """Token category to fetch"""

    interval: Literal["5m", "1h", "6h", "24h"]
    """Time interval for statistics"""

    limit: int
    """Maximum number of tokens to return (max 100)"""

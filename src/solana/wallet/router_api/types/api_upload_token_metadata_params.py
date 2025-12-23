# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APIUploadTokenMetadataParams"]


class APIUploadTokenMetadataParams(TypedDict, total=False):
    mint: Required[str]
    """Token mint address"""

    token_logo: Required[Annotated[str, PropertyInfo(alias="tokenLogo")]]
    """Base64-encoded token logo image (data URL format)"""

    token_name: Required[Annotated[str, PropertyInfo(alias="tokenName")]]
    """Token name"""

    token_symbol: Required[Annotated[str, PropertyInfo(alias="tokenSymbol")]]
    """Token ticker symbol"""

    user_wallet: Required[Annotated[str, PropertyInfo(alias="userWallet")]]
    """User's wallet address (pool creator)"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APISendTransactionParams"]


class APISendTransactionParams(TypedDict, total=False):
    signed_transaction: Required[Annotated[str, PropertyInfo(alias="signedTransaction")]]
    """Base64-encoded signed transaction"""

    additional_signers: Annotated[Iterable[object], PropertyInfo(alias="additionalSigners")]
    """Additional signers (keypairs)"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1ExecuteSwapResponse"]


class V1ExecuteSwapResponse(BaseModel):
    last_valid_block_height: Optional[int] = FieldInfo(alias="lastValidBlockHeight", default=None)

    swap_transaction: Optional[str] = FieldInfo(alias="swapTransaction", default=None)
    """Base64-encoded transaction"""

    transaction: Optional[str] = None
    """Alternative field for base64-encoded transaction"""

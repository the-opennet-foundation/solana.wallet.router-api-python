# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["APISendTransactionResponse"]


class APISendTransactionResponse(BaseModel):
    signature: Optional[str] = None
    """Transaction signature"""

    success: Optional[bool] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["APIUploadTokenMetadataResponse"]


class APIUploadTokenMetadataResponse(BaseModel):
    pool_tx: Optional[str] = FieldInfo(alias="poolTx", default=None)
    """Base64-encoded pool creation transaction"""

    success: Optional[bool] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["V1GetTokenHoldersResponse", "Holder", "HolderTag"]


class HolderTag(BaseModel):
    id: Optional[str] = None
    """Short tag identifier"""

    name: Optional[str] = None
    """Full tag name"""


class Holder(BaseModel):
    address: Optional[str] = None
    """Holder wallet address"""

    amount: Optional[float] = None
    """Token amount held"""

    tags: Optional[List[HolderTag]] = None


class V1GetTokenHoldersResponse(BaseModel):
    count: Optional[int] = None

    holders: Optional[List[Holder]] = None

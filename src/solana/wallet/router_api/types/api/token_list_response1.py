# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["TokenListResponse", "AllCategoriesTokenListResponse"]


class AllCategoriesTokenListResponse(BaseModel):
    new: Optional[TokenListResponse] = None

    topvolume: Optional[TokenListResponse] = None

    trending: Optional[TokenListResponse] = None


TokenListResponse: TypeAlias = Union[TokenListResponse, AllCategoriesTokenListResponse]

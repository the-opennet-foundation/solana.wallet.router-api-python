# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .pool import Pool
from ..._models import BaseModel

__all__ = ["GetTokenResponse"]


class GetTokenResponse(BaseModel):
    pools: Optional[List[Pool]] = None

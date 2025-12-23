# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TokenRetrieveResponse"]


class TokenRetrieveResponse(BaseModel):
    address: Optional[str] = None
    """Token mint address"""

    decimals: Optional[int] = None

    logo_uri: Optional[str] = FieldInfo(alias="logoURI", default=None)
    """Token logo URL"""

    name: Optional[str] = None

    price: Optional[float] = None

    symbol: Optional[str] = None

    usd_price: Optional[float] = FieldInfo(alias="usdPrice", default=None)

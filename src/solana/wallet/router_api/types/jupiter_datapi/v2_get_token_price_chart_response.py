# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["V2GetTokenPriceChartResponse", "Candle"]


class Candle(BaseModel):
    close: Optional[float] = None

    high: Optional[float] = None

    low: Optional[float] = None

    open: Optional[float] = None

    time: Optional[int] = None
    """Unix timestamp"""

    volume: Optional[float] = None


class V2GetTokenPriceChartResponse(BaseModel):
    candles: Optional[List[Candle]] = None

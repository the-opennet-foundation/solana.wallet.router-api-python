# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..jupiter.tokens.swap_stats import SwapStats
from ..jupiter.tokens.token_audit import TokenAudit

__all__ = ["Pool", "BaseAsset", "BaseAssetFirstPool"]


class BaseAssetFirstPool(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    dex: Optional[str] = None


class BaseAsset(BaseModel):
    id: str
    """Token mint address"""

    decimals: int
    """Token decimals"""

    name: str
    """Token name"""

    organic_score_label: Literal["high", "medium", "low"] = FieldInfo(alias="organicScoreLabel")
    """Organic score category"""

    symbol: str
    """Token ticker symbol"""

    token_program: str = FieldInfo(alias="tokenProgram")
    """Token program ID (SPL Token or Token-2022)"""

    audit: Optional[TokenAudit] = None

    circ_supply: Optional[float] = FieldInfo(alias="circSupply", default=None)
    """Circulating supply"""

    ct_likes: Optional[int] = FieldInfo(alias="ctLikes", default=None)
    """Crypto Twitter likes count"""

    dev: Optional[str] = None
    """Developer wallet address"""

    fdv: Optional[float] = None
    """Fully diluted valuation in USD"""

    first_pool: Optional[BaseAssetFirstPool] = FieldInfo(alias="firstPool", default=None)

    graduated_at: Optional[datetime] = FieldInfo(alias="graduatedAt", default=None)
    """When the token graduated from bonding curve"""

    graduated_pool: Optional[str] = FieldInfo(alias="graduatedPool", default=None)
    """Graduated pool ID"""

    holder_count: Optional[int] = FieldInfo(alias="holderCount", default=None)
    """Number of token holders"""

    icon: Optional[str] = None
    """Token logo URL"""

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)
    """Whether the token is verified"""

    launchpad: Optional[
        Literal[
            "pump.fun",
            "virtuals",
            "daos.fun",
            "time.fun",
            "GoFundMeme",
            "dealr.fun",
            "Dialect",
            "met-dbc",
            "letsbonk.fun",
            "Raydium",
            "cook.meme",
            "Believe",
            "boop",
            "xcombinator",
            "mentat.fun",
        ]
    ] = None
    """Launchpad platform (pump.fun, met-dbc, etc.)"""

    liquidity: Optional[float] = None
    """Total liquidity in USD"""

    mcap: Optional[float] = None
    """Market capitalization in USD"""

    organic_score: Optional[float] = FieldInfo(alias="organicScore", default=None)
    """Organic trading score (0-100)"""

    price_block_id: Optional[int] = FieldInfo(alias="priceBlockId", default=None)
    """Block ID of last price update"""

    smart_ct_likes: Optional[int] = FieldInfo(alias="smartCtLikes", default=None)
    """Smart money CT likes count"""

    stats1h: Optional[SwapStats] = None

    stats24h: Optional[SwapStats] = None

    stats5m: Optional[SwapStats] = None

    stats6h: Optional[SwapStats] = None

    telegram: Optional[str] = None
    """Telegram group URL"""

    total_supply: Optional[float] = FieldInfo(alias="totalSupply", default=None)
    """Total supply"""

    twitter: Optional[str] = None
    """Twitter/X handle or URL"""

    usd_price: Optional[float] = FieldInfo(alias="usdPrice", default=None)
    """Current price in USD"""

    website: Optional[str] = None
    """Project website URL"""


class Pool(BaseModel):
    id: str
    """Pool ID"""

    base_asset: BaseAsset = FieldInfo(alias="baseAsset")

    chain: str
    """Blockchain (e.g., "solana")"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Pool creation timestamp"""

    dex: str
    """DEX name (e.g., "jupiter", "raydium")"""

    type: str
    """Pool type (e.g., "amm")"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Last update timestamp"""

    bonding_curve: Optional[float] = FieldInfo(alias="bondingCurve", default=None)
    """Bonding curve progress percentage (0-100)"""

    is_unreliable: Optional[bool] = FieldInfo(alias="isUnreliable", default=None)
    """Whether the pool data may be unreliable"""

    volume24h: Optional[float] = None
    """24-hour trading volume in USD"""

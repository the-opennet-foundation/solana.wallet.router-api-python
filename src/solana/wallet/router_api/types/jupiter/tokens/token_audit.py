# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TokenAudit"]


class TokenAudit(BaseModel):
    dev_balance_percentage: Optional[float] = FieldInfo(alias="devBalancePercentage", default=None)
    """Developer balance percentage"""

    dev_migrations: Optional[int] = FieldInfo(alias="devMigrations", default=None)
    """Number of dev migrations"""

    freeze_authority_disabled: Optional[bool] = FieldInfo(alias="freezeAuthorityDisabled", default=None)
    """Whether freeze authority is disabled"""

    lp_burned_percentage: Optional[float] = FieldInfo(alias="lpBurnedPercentage", default=None)
    """Percentage of LP tokens burned"""

    mint_authority_disabled: Optional[bool] = FieldInfo(alias="mintAuthorityDisabled", default=None)
    """Whether mint authority is disabled (renounced)"""

    top_holders_percentage: Optional[float] = FieldInfo(alias="topHoldersPercentage", default=None)
    """Percentage held by top holders"""

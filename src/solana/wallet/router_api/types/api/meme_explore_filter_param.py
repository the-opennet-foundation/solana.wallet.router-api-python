# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["MemeExploreFilterParam"]


class MemeExploreFilterParam(TypedDict, total=False):
    platforms_filter: Annotated[SequenceNotStr[str], PropertyInfo(alias="platformsFilter")]
    """Launchpad platforms to include"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .meme_explore_filter_param import MemeExploreFilterParam

__all__ = ["PhantomExploreMemeTokensParams"]


class PhantomExploreMemeTokensParams(TypedDict, total=False):
    about_to_graduate_filter: Annotated[MemeExploreFilterParam, PropertyInfo(alias="aboutToGraduateFilter")]

    graduated_filter: Annotated[MemeExploreFilterParam, PropertyInfo(alias="graduatedFilter")]

    new_filter: Annotated[MemeExploreFilterParam, PropertyInfo(alias="newFilter")]

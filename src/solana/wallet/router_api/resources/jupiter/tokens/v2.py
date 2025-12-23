# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.jupiter.tokens import v2_list_recent_params, v2_list_top_traded_params, v2_list_top_trending_params
from ....types.jupiter.tokens.v2_list_recent_response import V2ListRecentResponse
from ....types.jupiter.tokens.v2_list_top_traded_response import V2ListTopTradedResponse
from ....types.jupiter.tokens.v2_list_top_trending_response import V2ListTopTrendingResponse

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)

    def list_recent(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListRecentResponse:
        """
        Fetches recently listed tokens on Jupiter.

        Args:
          limit: Maximum number of tokens

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/jupiter/tokens/v2/recent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, v2_list_recent_params.V2ListRecentParams),
            ),
            cast_to=V2ListRecentResponse,
        )

    def list_top_traded(
        self,
        interval: Literal["5m", "1h", "6h", "24h"],
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListTopTradedResponse:
        """
        Fetches top traded tokens by volume for a specific time interval.

        Args:
          limit: Maximum number of tokens

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not interval:
            raise ValueError(f"Expected a non-empty value for `interval` but received {interval!r}")
        return self._get(
            f"/jupiter/tokens/v2/toptraded/{interval}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, v2_list_top_traded_params.V2ListTopTradedParams),
            ),
            cast_to=V2ListTopTradedResponse,
        )

    def list_top_trending(
        self,
        interval: Literal["5m", "1h", "6h", "24h"],
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListTopTrendingResponse:
        """
        Fetches top trending tokens for a specific time interval.

        Args:
          limit: Maximum number of tokens

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not interval:
            raise ValueError(f"Expected a non-empty value for `interval` but received {interval!r}")
        return self._get(
            f"/jupiter/tokens/v2/toptrending/{interval}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, v2_list_top_trending_params.V2ListTopTrendingParams),
            ),
            cast_to=V2ListTopTrendingResponse,
        )


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)

    async def list_recent(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListRecentResponse:
        """
        Fetches recently listed tokens on Jupiter.

        Args:
          limit: Maximum number of tokens

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/jupiter/tokens/v2/recent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"limit": limit}, v2_list_recent_params.V2ListRecentParams),
            ),
            cast_to=V2ListRecentResponse,
        )

    async def list_top_traded(
        self,
        interval: Literal["5m", "1h", "6h", "24h"],
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListTopTradedResponse:
        """
        Fetches top traded tokens by volume for a specific time interval.

        Args:
          limit: Maximum number of tokens

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not interval:
            raise ValueError(f"Expected a non-empty value for `interval` but received {interval!r}")
        return await self._get(
            f"/jupiter/tokens/v2/toptraded/{interval}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"limit": limit}, v2_list_top_traded_params.V2ListTopTradedParams),
            ),
            cast_to=V2ListTopTradedResponse,
        )

    async def list_top_trending(
        self,
        interval: Literal["5m", "1h", "6h", "24h"],
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListTopTrendingResponse:
        """
        Fetches top trending tokens for a specific time interval.

        Args:
          limit: Maximum number of tokens

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not interval:
            raise ValueError(f"Expected a non-empty value for `interval` but received {interval!r}")
        return await self._get(
            f"/jupiter/tokens/v2/toptrending/{interval}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, v2_list_top_trending_params.V2ListTopTrendingParams
                ),
            ),
            cast_to=V2ListTopTrendingResponse,
        )


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.list_recent = to_raw_response_wrapper(
            v2.list_recent,
        )
        self.list_top_traded = to_raw_response_wrapper(
            v2.list_top_traded,
        )
        self.list_top_trending = to_raw_response_wrapper(
            v2.list_top_trending,
        )


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.list_recent = async_to_raw_response_wrapper(
            v2.list_recent,
        )
        self.list_top_traded = async_to_raw_response_wrapper(
            v2.list_top_traded,
        )
        self.list_top_trending = async_to_raw_response_wrapper(
            v2.list_top_trending,
        )


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.list_recent = to_streamed_response_wrapper(
            v2.list_recent,
        )
        self.list_top_traded = to_streamed_response_wrapper(
            v2.list_top_traded,
        )
        self.list_top_trending = to_streamed_response_wrapper(
            v2.list_top_trending,
        )


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.list_recent = async_to_streamed_response_wrapper(
            v2.list_recent,
        )
        self.list_top_traded = async_to_streamed_response_wrapper(
            v2.list_top_traded,
        )
        self.list_top_trending = async_to_streamed_response_wrapper(
            v2.list_top_trending,
        )

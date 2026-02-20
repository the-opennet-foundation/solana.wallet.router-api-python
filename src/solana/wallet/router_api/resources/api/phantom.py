# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.api import (
    phantom_search_spl_tokens_params,
    phantom_explore_meme_tokens_params,
    phantom_get_single_token_stats_params,
    phantom_get_perp_trending_markets_params,
    phantom_get_simple_token_overviews_params,
)
from ..._base_client import make_request_options
from ...types.api.meme_explore_filter_param import MemeExploreFilterParam
from ...types.api.phantom_search_spl_tokens_response import PhantomSearchSplTokensResponse
from ...types.api.phantom_explore_meme_tokens_response import PhantomExploreMemeTokensResponse
from ...types.api.phantom_get_single_token_stats_response import PhantomGetSingleTokenStatsResponse
from ...types.api.phantom_get_perp_trending_markets_response import PhantomGetPerpTrendingMarketsResponse
from ...types.api.phantom_get_simple_token_overviews_response import PhantomGetSimpleTokenOverviewsResponse

__all__ = ["PhantomResource", "AsyncPhantomResource"]


class PhantomResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhantomResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return PhantomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhantomResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#with_streaming_response
        """
        return PhantomResourceWithStreamingResponse(self)

    def explore_meme_tokens(
        self,
        *,
        about_to_graduate_filter: MemeExploreFilterParam | Omit = omit,
        graduated_filter: MemeExploreFilterParam | Omit = omit,
        new_filter: MemeExploreFilterParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhantomExploreMemeTokensResponse:
        """
        Fetches meme token explore data from Phantom API, organized into buckets (new,
        aboutToGraduate, graduated) filtered by launchpad platforms.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/phantom/meme-explore",
            body=maybe_transform(
                {
                    "about_to_graduate_filter": about_to_graduate_filter,
                    "graduated_filter": graduated_filter,
                    "new_filter": new_filter,
                },
                phantom_explore_meme_tokens_params.PhantomExploreMemeTokensParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhantomExploreMemeTokensResponse,
        )

    def get_perp_trending_markets(
        self,
        *,
        chain_id: str | Omit = omit,
        limit: str | Omit = omit,
        sort_by: Literal["volume", "openInterest", "fundingRate"] | Omit = omit,
        sort_direction: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhantomGetPerpTrendingMarketsResponse:
        """
        Fetches trending perpetual markets data from Phantom.

        Args:
          chain_id: Chain ID for the markets

          limit: Maximum number of results

          sort_by: Sort field

          sort_direction: Sort direction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/phantom/perp-trending-markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "chain_id": chain_id,
                        "limit": limit,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                    },
                    phantom_get_perp_trending_markets_params.PhantomGetPerpTrendingMarketsParams,
                ),
            ),
            cast_to=PhantomGetPerpTrendingMarketsResponse,
        )

    def get_simple_token_overviews(
        self,
        *,
        token_addresses: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhantomGetSimpleTokenOverviewsResponse:
        """
        Fetches basic overview data for one or more tokens.

        Args:
          token_addresses: Comma-separated token mint addresses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/phantom/simple-token-overviews",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"token_addresses": token_addresses},
                    phantom_get_simple_token_overviews_params.PhantomGetSimpleTokenOverviewsParams,
                ),
            ),
            cast_to=PhantomGetSimpleTokenOverviewsResponse,
        )

    def get_single_token_stats(
        self,
        *,
        token_address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhantomGetSingleTokenStatsResponse:
        """
        Fetches detailed trading statistics for a specific token.

        Args:
          token_address: Token mint address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/phantom/single-token-stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"token_address": token_address},
                    phantom_get_single_token_stats_params.PhantomGetSingleTokenStatsParams,
                ),
            ),
            cast_to=PhantomGetSingleTokenStatsResponse,
        )

    def search_spl_tokens(
        self,
        *,
        charts: Literal["true", "false"] | Omit = omit,
        page: str | Omit = omit,
        query: str | Omit = omit,
        sniper: Literal["true", "false"] | Omit = omit,
        sort_by: Literal[
            "volume-desc", "volume-asc", "marketcap-desc", "marketcap-asc", "liquidity-desc", "liquidity-asc"
        ]
        | Omit = omit,
        time_range: Literal["5m", "1h", "8h", "24h"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhantomSearchSplTokensResponse:
        """
        Search and filter SPL tokens with various sorting and filtering options.

        Args:
          charts: Include spark charts data

          page: Page number (0-indexed)

          query: Search query string

          sniper: Enable sniper mode

          sort_by: Sort field and direction

          time_range: Time range for statistics

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/phantom/search-bot-spl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "charts": charts,
                        "page": page,
                        "query": query,
                        "sniper": sniper,
                        "sort_by": sort_by,
                        "time_range": time_range,
                    },
                    phantom_search_spl_tokens_params.PhantomSearchSplTokensParams,
                ),
            ),
            cast_to=PhantomSearchSplTokensResponse,
        )


class AsyncPhantomResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhantomResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhantomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhantomResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#with_streaming_response
        """
        return AsyncPhantomResourceWithStreamingResponse(self)

    async def explore_meme_tokens(
        self,
        *,
        about_to_graduate_filter: MemeExploreFilterParam | Omit = omit,
        graduated_filter: MemeExploreFilterParam | Omit = omit,
        new_filter: MemeExploreFilterParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhantomExploreMemeTokensResponse:
        """
        Fetches meme token explore data from Phantom API, organized into buckets (new,
        aboutToGraduate, graduated) filtered by launchpad platforms.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/phantom/meme-explore",
            body=await async_maybe_transform(
                {
                    "about_to_graduate_filter": about_to_graduate_filter,
                    "graduated_filter": graduated_filter,
                    "new_filter": new_filter,
                },
                phantom_explore_meme_tokens_params.PhantomExploreMemeTokensParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhantomExploreMemeTokensResponse,
        )

    async def get_perp_trending_markets(
        self,
        *,
        chain_id: str | Omit = omit,
        limit: str | Omit = omit,
        sort_by: Literal["volume", "openInterest", "fundingRate"] | Omit = omit,
        sort_direction: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhantomGetPerpTrendingMarketsResponse:
        """
        Fetches trending perpetual markets data from Phantom.

        Args:
          chain_id: Chain ID for the markets

          limit: Maximum number of results

          sort_by: Sort field

          sort_direction: Sort direction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/phantom/perp-trending-markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "chain_id": chain_id,
                        "limit": limit,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                    },
                    phantom_get_perp_trending_markets_params.PhantomGetPerpTrendingMarketsParams,
                ),
            ),
            cast_to=PhantomGetPerpTrendingMarketsResponse,
        )

    async def get_simple_token_overviews(
        self,
        *,
        token_addresses: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhantomGetSimpleTokenOverviewsResponse:
        """
        Fetches basic overview data for one or more tokens.

        Args:
          token_addresses: Comma-separated token mint addresses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/phantom/simple-token-overviews",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"token_addresses": token_addresses},
                    phantom_get_simple_token_overviews_params.PhantomGetSimpleTokenOverviewsParams,
                ),
            ),
            cast_to=PhantomGetSimpleTokenOverviewsResponse,
        )

    async def get_single_token_stats(
        self,
        *,
        token_address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhantomGetSingleTokenStatsResponse:
        """
        Fetches detailed trading statistics for a specific token.

        Args:
          token_address: Token mint address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/phantom/single-token-stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"token_address": token_address},
                    phantom_get_single_token_stats_params.PhantomGetSingleTokenStatsParams,
                ),
            ),
            cast_to=PhantomGetSingleTokenStatsResponse,
        )

    async def search_spl_tokens(
        self,
        *,
        charts: Literal["true", "false"] | Omit = omit,
        page: str | Omit = omit,
        query: str | Omit = omit,
        sniper: Literal["true", "false"] | Omit = omit,
        sort_by: Literal[
            "volume-desc", "volume-asc", "marketcap-desc", "marketcap-asc", "liquidity-desc", "liquidity-asc"
        ]
        | Omit = omit,
        time_range: Literal["5m", "1h", "8h", "24h"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhantomSearchSplTokensResponse:
        """
        Search and filter SPL tokens with various sorting and filtering options.

        Args:
          charts: Include spark charts data

          page: Page number (0-indexed)

          query: Search query string

          sniper: Enable sniper mode

          sort_by: Sort field and direction

          time_range: Time range for statistics

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/phantom/search-bot-spl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "charts": charts,
                        "page": page,
                        "query": query,
                        "sniper": sniper,
                        "sort_by": sort_by,
                        "time_range": time_range,
                    },
                    phantom_search_spl_tokens_params.PhantomSearchSplTokensParams,
                ),
            ),
            cast_to=PhantomSearchSplTokensResponse,
        )


class PhantomResourceWithRawResponse:
    def __init__(self, phantom: PhantomResource) -> None:
        self._phantom = phantom

        self.explore_meme_tokens = to_raw_response_wrapper(
            phantom.explore_meme_tokens,
        )
        self.get_perp_trending_markets = to_raw_response_wrapper(
            phantom.get_perp_trending_markets,
        )
        self.get_simple_token_overviews = to_raw_response_wrapper(
            phantom.get_simple_token_overviews,
        )
        self.get_single_token_stats = to_raw_response_wrapper(
            phantom.get_single_token_stats,
        )
        self.search_spl_tokens = to_raw_response_wrapper(
            phantom.search_spl_tokens,
        )


class AsyncPhantomResourceWithRawResponse:
    def __init__(self, phantom: AsyncPhantomResource) -> None:
        self._phantom = phantom

        self.explore_meme_tokens = async_to_raw_response_wrapper(
            phantom.explore_meme_tokens,
        )
        self.get_perp_trending_markets = async_to_raw_response_wrapper(
            phantom.get_perp_trending_markets,
        )
        self.get_simple_token_overviews = async_to_raw_response_wrapper(
            phantom.get_simple_token_overviews,
        )
        self.get_single_token_stats = async_to_raw_response_wrapper(
            phantom.get_single_token_stats,
        )
        self.search_spl_tokens = async_to_raw_response_wrapper(
            phantom.search_spl_tokens,
        )


class PhantomResourceWithStreamingResponse:
    def __init__(self, phantom: PhantomResource) -> None:
        self._phantom = phantom

        self.explore_meme_tokens = to_streamed_response_wrapper(
            phantom.explore_meme_tokens,
        )
        self.get_perp_trending_markets = to_streamed_response_wrapper(
            phantom.get_perp_trending_markets,
        )
        self.get_simple_token_overviews = to_streamed_response_wrapper(
            phantom.get_simple_token_overviews,
        )
        self.get_single_token_stats = to_streamed_response_wrapper(
            phantom.get_single_token_stats,
        )
        self.search_spl_tokens = to_streamed_response_wrapper(
            phantom.search_spl_tokens,
        )


class AsyncPhantomResourceWithStreamingResponse:
    def __init__(self, phantom: AsyncPhantomResource) -> None:
        self._phantom = phantom

        self.explore_meme_tokens = async_to_streamed_response_wrapper(
            phantom.explore_meme_tokens,
        )
        self.get_perp_trending_markets = async_to_streamed_response_wrapper(
            phantom.get_perp_trending_markets,
        )
        self.get_simple_token_overviews = async_to_streamed_response_wrapper(
            phantom.get_simple_token_overviews,
        )
        self.get_single_token_stats = async_to_streamed_response_wrapper(
            phantom.get_single_token_stats,
        )
        self.search_spl_tokens = async_to_streamed_response_wrapper(
            phantom.search_spl_tokens,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
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
from ...types.api import token_list_params
from ..._base_client import make_request_options
from ...types.api.get_token_response import GetTokenResponse
from ...types.api.token_list_response import TokenListResponse

__all__ = ["TokensResource", "AsyncTokensResource"]


class TokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return TokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#with_streaming_response
        """
        return TokensResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetTokenResponse:
        """
        Fetches detailed token information and pool data for a specific token mint
        address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/tokens/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetTokenResponse,
        )

    def list(
        self,
        *,
        category: Literal["trending", "new", "topvolume"] | Omit = omit,
        interval: Literal["5m", "1h", "6h", "24h"] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenListResponse:
        """Fetches token lists by category.

        If no category is specified, returns all
        categories (trending, new, topvolume) in a single response.

        Args:
          category: Token category to fetch

          interval: Time interval for statistics

          limit: Maximum number of tokens to return (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            TokenListResponse,
            self._get(
                "/api/tokens",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "category": category,
                            "interval": interval,
                            "limit": limit,
                        },
                        token_list_params.TokenListParams,
                    ),
                ),
                cast_to=cast(Any, TokenListResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#with_streaming_response
        """
        return AsyncTokensResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetTokenResponse:
        """
        Fetches detailed token information and pool data for a specific token mint
        address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/tokens/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetTokenResponse,
        )

    async def list(
        self,
        *,
        category: Literal["trending", "new", "topvolume"] | Omit = omit,
        interval: Literal["5m", "1h", "6h", "24h"] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenListResponse:
        """Fetches token lists by category.

        If no category is specified, returns all
        categories (trending, new, topvolume) in a single response.

        Args:
          category: Token category to fetch

          interval: Time interval for statistics

          limit: Maximum number of tokens to return (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            TokenListResponse,
            await self._get(
                "/api/tokens",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "category": category,
                            "interval": interval,
                            "limit": limit,
                        },
                        token_list_params.TokenListParams,
                    ),
                ),
                cast_to=cast(Any, TokenListResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class TokensResourceWithRawResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

        self.retrieve = to_raw_response_wrapper(
            tokens.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tokens.list,
        )


class AsyncTokensResourceWithRawResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

        self.retrieve = async_to_raw_response_wrapper(
            tokens.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tokens.list,
        )


class TokensResourceWithStreamingResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

        self.retrieve = to_streamed_response_wrapper(
            tokens.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tokens.list,
        )


class AsyncTokensResourceWithStreamingResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

        self.retrieve = async_to_streamed_response_wrapper(
            tokens.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tokens.list,
        )

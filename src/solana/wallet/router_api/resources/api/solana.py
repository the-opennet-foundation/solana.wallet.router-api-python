# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.api.solana_get_status_response import SolanaGetStatusResponse

__all__ = ["SolanaResource", "AsyncSolanaResource"]


class SolanaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SolanaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return SolanaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SolanaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#with_streaming_response
        """
        return SolanaResourceWithStreamingResponse(self)

    def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SolanaGetStatusResponse:
        """Returns current SOL price, block height, and transactions per second (TPS)."""
        return self._get(
            "/api/solana/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SolanaGetStatusResponse,
        )


class AsyncSolanaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSolanaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSolanaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSolanaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#with_streaming_response
        """
        return AsyncSolanaResourceWithStreamingResponse(self)

    async def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SolanaGetStatusResponse:
        """Returns current SOL price, block height, and transactions per second (TPS)."""
        return await self._get(
            "/api/solana/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SolanaGetStatusResponse,
        )


class SolanaResourceWithRawResponse:
    def __init__(self, solana: SolanaResource) -> None:
        self._solana = solana

        self.get_status = to_raw_response_wrapper(
            solana.get_status,
        )


class AsyncSolanaResourceWithRawResponse:
    def __init__(self, solana: AsyncSolanaResource) -> None:
        self._solana = solana

        self.get_status = async_to_raw_response_wrapper(
            solana.get_status,
        )


class SolanaResourceWithStreamingResponse:
    def __init__(self, solana: SolanaResource) -> None:
        self._solana = solana

        self.get_status = to_streamed_response_wrapper(
            solana.get_status,
        )


class AsyncSolanaResourceWithStreamingResponse:
    def __init__(self, solana: AsyncSolanaResource) -> None:
        self._solana = solana

        self.get_status = async_to_streamed_response_wrapper(
            solana.get_status,
        )

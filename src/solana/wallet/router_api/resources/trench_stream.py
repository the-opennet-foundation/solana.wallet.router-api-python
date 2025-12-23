# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["TrenchStreamResource", "AsyncTrenchStreamResource"]


class TrenchStreamResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrenchStreamResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return TrenchStreamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrenchStreamResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#with_streaming_response
        """
        return TrenchStreamResourceWithStreamingResponse(self)

    def connect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """WebSocket endpoint for real-time token and transaction updates.

        Connect using
        `wss://paxsol.paxeer.app/trench-stream/ws`

        **Message Types:**

        - Token updates
        - New transactions
        - Price changes
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/trench-stream/ws",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTrenchStreamResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrenchStreamResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrenchStreamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrenchStreamResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#with_streaming_response
        """
        return AsyncTrenchStreamResourceWithStreamingResponse(self)

    async def connect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """WebSocket endpoint for real-time token and transaction updates.

        Connect using
        `wss://paxsol.paxeer.app/trench-stream/ws`

        **Message Types:**

        - Token updates
        - New transactions
        - Price changes
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/trench-stream/ws",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TrenchStreamResourceWithRawResponse:
    def __init__(self, trench_stream: TrenchStreamResource) -> None:
        self._trench_stream = trench_stream

        self.connect = to_raw_response_wrapper(
            trench_stream.connect,
        )


class AsyncTrenchStreamResourceWithRawResponse:
    def __init__(self, trench_stream: AsyncTrenchStreamResource) -> None:
        self._trench_stream = trench_stream

        self.connect = async_to_raw_response_wrapper(
            trench_stream.connect,
        )


class TrenchStreamResourceWithStreamingResponse:
    def __init__(self, trench_stream: TrenchStreamResource) -> None:
        self._trench_stream = trench_stream

        self.connect = to_streamed_response_wrapper(
            trench_stream.connect,
        )


class AsyncTrenchStreamResourceWithStreamingResponse:
    def __init__(self, trench_stream: AsyncTrenchStreamResource) -> None:
        self._trench_stream = trench_stream

        self.connect = async_to_streamed_response_wrapper(
            trench_stream.connect,
        )

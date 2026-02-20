# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SwapResource", "AsyncSwapResource"]


class SwapResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> SwapResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return SwapResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SwapResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#with_streaming_response
        """
        return SwapResourceWithStreamingResponse(self)


class AsyncSwapResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSwapResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSwapResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSwapResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#with_streaming_response
        """
        return AsyncSwapResourceWithStreamingResponse(self)


class SwapResourceWithRawResponse:
    def __init__(self, swap: SwapResource) -> None:
        self._swap = swap

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self._swap.v1)


class AsyncSwapResourceWithRawResponse:
    def __init__(self, swap: AsyncSwapResource) -> None:
        self._swap = swap

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self._swap.v1)


class SwapResourceWithStreamingResponse:
    def __init__(self, swap: SwapResource) -> None:
        self._swap = swap

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self._swap.v1)


class AsyncSwapResourceWithStreamingResponse:
    def __init__(self, swap: AsyncSwapResource) -> None:
        self._swap = swap

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self._swap.v1)

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .swap.swap import (
    SwapResource,
    AsyncSwapResource,
    SwapResourceWithRawResponse,
    AsyncSwapResourceWithRawResponse,
    SwapResourceWithStreamingResponse,
    AsyncSwapResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .tokens.tokens import (
    TokensResource,
    AsyncTokensResource,
    TokensResourceWithRawResponse,
    AsyncTokensResourceWithRawResponse,
    TokensResourceWithStreamingResponse,
    AsyncTokensResourceWithStreamingResponse,
)

__all__ = ["JupiterResource", "AsyncJupiterResource"]


class JupiterResource(SyncAPIResource):
    @cached_property
    def tokens(self) -> TokensResource:
        return TokensResource(self._client)

    @cached_property
    def swap(self) -> SwapResource:
        return SwapResource(self._client)

    @cached_property
    def with_raw_response(self) -> JupiterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return JupiterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JupiterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#with_streaming_response
        """
        return JupiterResourceWithStreamingResponse(self)


class AsyncJupiterResource(AsyncAPIResource):
    @cached_property
    def tokens(self) -> AsyncTokensResource:
        return AsyncTokensResource(self._client)

    @cached_property
    def swap(self) -> AsyncSwapResource:
        return AsyncSwapResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncJupiterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJupiterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJupiterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#with_streaming_response
        """
        return AsyncJupiterResourceWithStreamingResponse(self)


class JupiterResourceWithRawResponse:
    def __init__(self, jupiter: JupiterResource) -> None:
        self._jupiter = jupiter

    @cached_property
    def tokens(self) -> TokensResourceWithRawResponse:
        return TokensResourceWithRawResponse(self._jupiter.tokens)

    @cached_property
    def swap(self) -> SwapResourceWithRawResponse:
        return SwapResourceWithRawResponse(self._jupiter.swap)


class AsyncJupiterResourceWithRawResponse:
    def __init__(self, jupiter: AsyncJupiterResource) -> None:
        self._jupiter = jupiter

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithRawResponse:
        return AsyncTokensResourceWithRawResponse(self._jupiter.tokens)

    @cached_property
    def swap(self) -> AsyncSwapResourceWithRawResponse:
        return AsyncSwapResourceWithRawResponse(self._jupiter.swap)


class JupiterResourceWithStreamingResponse:
    def __init__(self, jupiter: JupiterResource) -> None:
        self._jupiter = jupiter

    @cached_property
    def tokens(self) -> TokensResourceWithStreamingResponse:
        return TokensResourceWithStreamingResponse(self._jupiter.tokens)

    @cached_property
    def swap(self) -> SwapResourceWithStreamingResponse:
        return SwapResourceWithStreamingResponse(self._jupiter.swap)


class AsyncJupiterResourceWithStreamingResponse:
    def __init__(self, jupiter: AsyncJupiterResource) -> None:
        self._jupiter = jupiter

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithStreamingResponse:
        return AsyncTokensResourceWithStreamingResponse(self._jupiter.tokens)

    @cached_property
    def swap(self) -> AsyncSwapResourceWithStreamingResponse:
        return AsyncSwapResourceWithStreamingResponse(self._jupiter.swap)

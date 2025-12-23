# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v2 import (
    V2Resource,
    AsyncV2Resource,
    V2ResourceWithRawResponse,
    AsyncV2ResourceWithRawResponse,
    V2ResourceWithStreamingResponse,
    AsyncV2ResourceWithStreamingResponse,
)
from .v1.v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["JupiterDatapiResource", "AsyncJupiterDatapiResource"]


class JupiterDatapiResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        return V1Resource(self._client)

    @cached_property
    def v2(self) -> V2Resource:
        return V2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> JupiterDatapiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return JupiterDatapiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JupiterDatapiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#with_streaming_response
        """
        return JupiterDatapiResourceWithStreamingResponse(self)


class AsyncJupiterDatapiResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        return AsyncV1Resource(self._client)

    @cached_property
    def v2(self) -> AsyncV2Resource:
        return AsyncV2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncJupiterDatapiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJupiterDatapiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJupiterDatapiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#with_streaming_response
        """
        return AsyncJupiterDatapiResourceWithStreamingResponse(self)


class JupiterDatapiResourceWithRawResponse:
    def __init__(self, jupiter_datapi: JupiterDatapiResource) -> None:
        self._jupiter_datapi = jupiter_datapi

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self._jupiter_datapi.v1)

    @cached_property
    def v2(self) -> V2ResourceWithRawResponse:
        return V2ResourceWithRawResponse(self._jupiter_datapi.v2)


class AsyncJupiterDatapiResourceWithRawResponse:
    def __init__(self, jupiter_datapi: AsyncJupiterDatapiResource) -> None:
        self._jupiter_datapi = jupiter_datapi

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self._jupiter_datapi.v1)

    @cached_property
    def v2(self) -> AsyncV2ResourceWithRawResponse:
        return AsyncV2ResourceWithRawResponse(self._jupiter_datapi.v2)


class JupiterDatapiResourceWithStreamingResponse:
    def __init__(self, jupiter_datapi: JupiterDatapiResource) -> None:
        self._jupiter_datapi = jupiter_datapi

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self._jupiter_datapi.v1)

    @cached_property
    def v2(self) -> V2ResourceWithStreamingResponse:
        return V2ResourceWithStreamingResponse(self._jupiter_datapi.v2)


class AsyncJupiterDatapiResourceWithStreamingResponse:
    def __init__(self, jupiter_datapi: AsyncJupiterDatapiResource) -> None:
        self._jupiter_datapi = jupiter_datapi

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self._jupiter_datapi.v1)

    @cached_property
    def v2(self) -> AsyncV2ResourceWithStreamingResponse:
        return AsyncV2ResourceWithStreamingResponse(self._jupiter_datapi.v2)

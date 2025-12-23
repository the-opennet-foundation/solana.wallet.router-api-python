# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
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
from ..._base_client import make_request_options
from ...types.jupiter_datapi import v2_get_token_price_chart_params
from ...types.jupiter_datapi.v2_get_token_price_chart_response import V2GetTokenPriceChartResponse

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

    def get_token_price_chart(
        self,
        asset_id: str,
        *,
        base_asset: str,
        candles: int,
        from_: Union[int, Union[str, datetime]],
        interval: Literal[
            "1_SECOND",
            "15_SECOND",
            "30_SECOND",
            "1_MINUTE",
            "3_MINUTE",
            "5_MINUTE",
            "15_MINUTE",
            "30_MINUTE",
            "1_HOUR",
            "2_HOUR",
            "4_HOUR",
            "8_HOUR",
            "12_HOUR",
            "1_DAY",
            "1_WEEK",
            "1_MONTH",
        ],
        to: Union[int, Union[str, datetime]],
        type: Literal["price", "mcap"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2GetTokenPriceChartResponse:
        """
        Fetches OHLCV candlestick data for charting.

        Args:
          base_asset: Base asset for price calculation

          candles: Number of candles to return

          from_: Start timestamp (Unix seconds or ISO date)

          interval: Candlestick interval

          to: End timestamp (Unix seconds or ISO date)

          type: Chart type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get(
            f"/jupiter-datapi/v2/charts/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "base_asset": base_asset,
                        "candles": candles,
                        "from_": from_,
                        "interval": interval,
                        "to": to,
                        "type": type,
                    },
                    v2_get_token_price_chart_params.V2GetTokenPriceChartParams,
                ),
            ),
            cast_to=V2GetTokenPriceChartResponse,
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

    async def get_token_price_chart(
        self,
        asset_id: str,
        *,
        base_asset: str,
        candles: int,
        from_: Union[int, Union[str, datetime]],
        interval: Literal[
            "1_SECOND",
            "15_SECOND",
            "30_SECOND",
            "1_MINUTE",
            "3_MINUTE",
            "5_MINUTE",
            "15_MINUTE",
            "30_MINUTE",
            "1_HOUR",
            "2_HOUR",
            "4_HOUR",
            "8_HOUR",
            "12_HOUR",
            "1_DAY",
            "1_WEEK",
            "1_MONTH",
        ],
        to: Union[int, Union[str, datetime]],
        type: Literal["price", "mcap"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2GetTokenPriceChartResponse:
        """
        Fetches OHLCV candlestick data for charting.

        Args:
          base_asset: Base asset for price calculation

          candles: Number of candles to return

          from_: Start timestamp (Unix seconds or ISO date)

          interval: Candlestick interval

          to: End timestamp (Unix seconds or ISO date)

          type: Chart type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._get(
            f"/jupiter-datapi/v2/charts/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "base_asset": base_asset,
                        "candles": candles,
                        "from_": from_,
                        "interval": interval,
                        "to": to,
                        "type": type,
                    },
                    v2_get_token_price_chart_params.V2GetTokenPriceChartParams,
                ),
            ),
            cast_to=V2GetTokenPriceChartResponse,
        )


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.get_token_price_chart = to_raw_response_wrapper(
            v2.get_token_price_chart,
        )


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.get_token_price_chart = async_to_raw_response_wrapper(
            v2.get_token_price_chart,
        )


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.get_token_price_chart = to_streamed_response_wrapper(
            v2.get_token_price_chart,
        )


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.get_token_price_chart = async_to_streamed_response_wrapper(
            v2.get_token_price_chart,
        )

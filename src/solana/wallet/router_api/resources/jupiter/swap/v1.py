# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ....types.jupiter.swap import Quote, v1_get_quote_params, v1_execute_swap_params
from ....types.jupiter.swap.quote import Quote
from ....types.jupiter.swap.quote_param import QuoteParam
from ....types.jupiter.swap.v1_execute_swap_response import V1ExecuteSwapResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def execute_swap(
        self,
        *,
        quote_response: QuoteParam,
        user_public_key: str,
        dynamic_compute_unit_limit: bool | Omit = omit,
        prioritization_fee_lamports: Optional[int] | Omit = omit,
        wrap_unwrap_sol: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ExecuteSwapResponse:
        """Creates a swap transaction from a quote.

        Returns a base64-encoded transaction
        that needs to be signed and submitted to the network.

        Args:
          user_public_key: User's wallet public key

          dynamic_compute_unit_limit: Enable dynamic compute unit limit

          prioritization_fee_lamports: Priority fee in lamports

          wrap_unwrap_sol: Automatically wrap/unwrap SOL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/jupiter/swap/v1/swap",
            body=maybe_transform(
                {
                    "quote_response": quote_response,
                    "user_public_key": user_public_key,
                    "dynamic_compute_unit_limit": dynamic_compute_unit_limit,
                    "prioritization_fee_lamports": prioritization_fee_lamports,
                    "wrap_unwrap_sol": wrap_unwrap_sol,
                },
                v1_execute_swap_params.V1ExecuteSwapParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ExecuteSwapResponse,
        )

    def get_quote(
        self,
        *,
        amount: int,
        input_mint: str,
        output_mint: str,
        as_legacy_transaction: bool | Omit = omit,
        only_direct_routes: bool | Omit = omit,
        slippage_bps: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Quote:
        """Gets a quote for swapping tokens.

        Returns the best route and expected output
        amount.

        Args:
          amount: Input amount in smallest units (lamports for SOL)

          input_mint: Input token mint address

          output_mint: Output token mint address

          as_legacy_transaction: Return legacy transaction format

          only_direct_routes: Only use direct routes (no intermediate tokens)

          slippage_bps: Slippage tolerance in basis points (100 = 1%)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/jupiter/swap/v1/quote",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "amount": amount,
                        "input_mint": input_mint,
                        "output_mint": output_mint,
                        "as_legacy_transaction": as_legacy_transaction,
                        "only_direct_routes": only_direct_routes,
                        "slippage_bps": slippage_bps,
                    },
                    v1_get_quote_params.V1GetQuoteParams,
                ),
            ),
            cast_to=Quote,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solana.wallet.router-api-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def execute_swap(
        self,
        *,
        quote_response: QuoteParam,
        user_public_key: str,
        dynamic_compute_unit_limit: bool | Omit = omit,
        prioritization_fee_lamports: Optional[int] | Omit = omit,
        wrap_unwrap_sol: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ExecuteSwapResponse:
        """Creates a swap transaction from a quote.

        Returns a base64-encoded transaction
        that needs to be signed and submitted to the network.

        Args:
          user_public_key: User's wallet public key

          dynamic_compute_unit_limit: Enable dynamic compute unit limit

          prioritization_fee_lamports: Priority fee in lamports

          wrap_unwrap_sol: Automatically wrap/unwrap SOL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/jupiter/swap/v1/swap",
            body=await async_maybe_transform(
                {
                    "quote_response": quote_response,
                    "user_public_key": user_public_key,
                    "dynamic_compute_unit_limit": dynamic_compute_unit_limit,
                    "prioritization_fee_lamports": prioritization_fee_lamports,
                    "wrap_unwrap_sol": wrap_unwrap_sol,
                },
                v1_execute_swap_params.V1ExecuteSwapParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ExecuteSwapResponse,
        )

    async def get_quote(
        self,
        *,
        amount: int,
        input_mint: str,
        output_mint: str,
        as_legacy_transaction: bool | Omit = omit,
        only_direct_routes: bool | Omit = omit,
        slippage_bps: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Quote:
        """Gets a quote for swapping tokens.

        Returns the best route and expected output
        amount.

        Args:
          amount: Input amount in smallest units (lamports for SOL)

          input_mint: Input token mint address

          output_mint: Output token mint address

          as_legacy_transaction: Return legacy transaction format

          only_direct_routes: Only use direct routes (no intermediate tokens)

          slippage_bps: Slippage tolerance in basis points (100 = 1%)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/jupiter/swap/v1/quote",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "amount": amount,
                        "input_mint": input_mint,
                        "output_mint": output_mint,
                        "as_legacy_transaction": as_legacy_transaction,
                        "only_direct_routes": only_direct_routes,
                        "slippage_bps": slippage_bps,
                    },
                    v1_get_quote_params.V1GetQuoteParams,
                ),
            ),
            cast_to=Quote,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.execute_swap = to_raw_response_wrapper(
            v1.execute_swap,
        )
        self.get_quote = to_raw_response_wrapper(
            v1.get_quote,
        )


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.execute_swap = async_to_raw_response_wrapper(
            v1.execute_swap,
        )
        self.get_quote = async_to_raw_response_wrapper(
            v1.get_quote,
        )


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.execute_swap = to_streamed_response_wrapper(
            v1.execute_swap,
        )
        self.get_quote = to_streamed_response_wrapper(
            v1.get_quote,
        )


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.execute_swap = async_to_streamed_response_wrapper(
            v1.execute_swap,
        )
        self.get_quote = async_to_streamed_response_wrapper(
            v1.get_quote,
        )

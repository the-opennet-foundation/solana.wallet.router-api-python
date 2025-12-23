# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from .assets import (
    AssetsResource,
    AsyncAssetsResource,
    AssetsResourceWithRawResponse,
    AsyncAssetsResourceWithRawResponse,
    AssetsResourceWithStreamingResponse,
    AsyncAssetsResourceWithStreamingResponse,
)
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
from ....types.jupiter_datapi import (
    v1_get_pools_params,
    v1_get_wallet_pnl_stats_params,
    v1_get_token_transactions_params,
)
from ....types.api.get_token_response import GetTokenResponse
from ....types.jupiter_datapi.v1_get_token_holders_response import V1GetTokenHoldersResponse
from ....types.jupiter_datapi.v1_get_wallet_pnl_stats_response import V1GetWalletPnlStatsResponse
from ....types.jupiter_datapi.v1_get_token_transactions_response import V1GetTokenTransactionsResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def assets(self) -> AssetsResource:
        return AssetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def get_pools(
        self,
        *,
        asset_ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetTokenResponse:
        """
        Fetches pool and token information for specified asset IDs.

        Args:
          asset_ids: Comma-separated token mint addresses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/jupiter-datapi/v1/pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"asset_ids": asset_ids}, v1_get_pools_params.V1GetPoolsParams),
            ),
            cast_to=GetTokenResponse,
        )

    def get_token_holders(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetTokenHoldersResponse:
        """
        Fetches top holders for a specific token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get(
            f"/jupiter-datapi/v1/holders/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetTokenHoldersResponse,
        )

    def get_token_transactions(
        self,
        asset_id: str,
        *,
        from_ts: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        offset: str | Omit = omit,
        offset_ts: Union[str, datetime] | Omit = omit,
        to_ts: Union[str, datetime] | Omit = omit,
        trader_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetTokenTransactionsResponse:
        """
        Fetches recent swap transactions for a specific token.

        Args:
          from_ts: Filter transactions from this timestamp

          limit: Maximum number of transactions

          offset: Pagination offset token

          offset_ts: Offset timestamp for pagination

          to_ts: Filter transactions until this timestamp

          trader_address: Filter by trader wallet address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get(
            f"/jupiter-datapi/v1/txs/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_ts": from_ts,
                        "limit": limit,
                        "offset": offset,
                        "offset_ts": offset_ts,
                        "to_ts": to_ts,
                        "trader_address": trader_address,
                    },
                    v1_get_token_transactions_params.V1GetTokenTransactionsParams,
                ),
            ),
            cast_to=V1GetTokenTransactionsResponse,
        )

    def get_wallet_pnl_stats(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetWalletPnlStatsResponse:
        """
        Fetches profit and loss statistics for a wallet address.

        Args:
          address: Wallet address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/jupiter-datapi/v1/pnl-stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"address": address}, v1_get_wallet_pnl_stats_params.V1GetWalletPnlStatsParams),
            ),
            cast_to=V1GetWalletPnlStatsResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def get_pools(
        self,
        *,
        asset_ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetTokenResponse:
        """
        Fetches pool and token information for specified asset IDs.

        Args:
          asset_ids: Comma-separated token mint addresses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/jupiter-datapi/v1/pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"asset_ids": asset_ids}, v1_get_pools_params.V1GetPoolsParams),
            ),
            cast_to=GetTokenResponse,
        )

    async def get_token_holders(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetTokenHoldersResponse:
        """
        Fetches top holders for a specific token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._get(
            f"/jupiter-datapi/v1/holders/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetTokenHoldersResponse,
        )

    async def get_token_transactions(
        self,
        asset_id: str,
        *,
        from_ts: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        offset: str | Omit = omit,
        offset_ts: Union[str, datetime] | Omit = omit,
        to_ts: Union[str, datetime] | Omit = omit,
        trader_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetTokenTransactionsResponse:
        """
        Fetches recent swap transactions for a specific token.

        Args:
          from_ts: Filter transactions from this timestamp

          limit: Maximum number of transactions

          offset: Pagination offset token

          offset_ts: Offset timestamp for pagination

          to_ts: Filter transactions until this timestamp

          trader_address: Filter by trader wallet address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._get(
            f"/jupiter-datapi/v1/txs/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_ts": from_ts,
                        "limit": limit,
                        "offset": offset,
                        "offset_ts": offset_ts,
                        "to_ts": to_ts,
                        "trader_address": trader_address,
                    },
                    v1_get_token_transactions_params.V1GetTokenTransactionsParams,
                ),
            ),
            cast_to=V1GetTokenTransactionsResponse,
        )

    async def get_wallet_pnl_stats(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetWalletPnlStatsResponse:
        """
        Fetches profit and loss statistics for a wallet address.

        Args:
          address: Wallet address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/jupiter-datapi/v1/pnl-stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"address": address}, v1_get_wallet_pnl_stats_params.V1GetWalletPnlStatsParams
                ),
            ),
            cast_to=V1GetWalletPnlStatsResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.get_pools = to_raw_response_wrapper(
            v1.get_pools,
        )
        self.get_token_holders = to_raw_response_wrapper(
            v1.get_token_holders,
        )
        self.get_token_transactions = to_raw_response_wrapper(
            v1.get_token_transactions,
        )
        self.get_wallet_pnl_stats = to_raw_response_wrapper(
            v1.get_wallet_pnl_stats,
        )

    @cached_property
    def assets(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self._v1.assets)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.get_pools = async_to_raw_response_wrapper(
            v1.get_pools,
        )
        self.get_token_holders = async_to_raw_response_wrapper(
            v1.get_token_holders,
        )
        self.get_token_transactions = async_to_raw_response_wrapper(
            v1.get_token_transactions,
        )
        self.get_wallet_pnl_stats = async_to_raw_response_wrapper(
            v1.get_wallet_pnl_stats,
        )

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self._v1.assets)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.get_pools = to_streamed_response_wrapper(
            v1.get_pools,
        )
        self.get_token_holders = to_streamed_response_wrapper(
            v1.get_token_holders,
        )
        self.get_token_transactions = to_streamed_response_wrapper(
            v1.get_token_transactions,
        )
        self.get_wallet_pnl_stats = to_streamed_response_wrapper(
            v1.get_wallet_pnl_stats,
        )

    @cached_property
    def assets(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self._v1.assets)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.get_pools = async_to_streamed_response_wrapper(
            v1.get_pools,
        )
        self.get_token_holders = async_to_streamed_response_wrapper(
            v1.get_token_holders,
        )
        self.get_token_transactions = async_to_streamed_response_wrapper(
            v1.get_token_transactions,
        )
        self.get_wallet_pnl_stats = async_to_streamed_response_wrapper(
            v1.get_wallet_pnl_stats,
        )

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self._v1.assets)

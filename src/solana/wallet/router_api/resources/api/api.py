# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ... import _resource
from .solana import (
    SolanaResource,
    AsyncSolanaResource,
    SolanaResourceWithRawResponse,
    AsyncSolanaResourceWithRawResponse,
    SolanaResourceWithStreamingResponse,
    AsyncSolanaResourceWithStreamingResponse,
)
from .tokens import (
    TokensResource,
    AsyncTokensResource,
    TokensResourceWithRawResponse,
    AsyncTokensResourceWithRawResponse,
    TokensResourceWithStreamingResponse,
    AsyncTokensResourceWithStreamingResponse,
)
from ...types import api_send_transaction_params, api_upload_token_metadata_params
from .phantom import (
    PhantomResource,
    AsyncPhantomResource,
    PhantomResourceWithRawResponse,
    AsyncPhantomResourceWithRawResponse,
    PhantomResourceWithStreamingResponse,
    AsyncPhantomResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.api_get_wallet_info_response import APIGetWalletInfoResponse
from ...types.api_send_transaction_response import APISendTransactionResponse
from ...types.api_upload_token_metadata_response import APIUploadTokenMetadataResponse

__all__ = ["APIResource", "AsyncAPIResource"]


class APIResource(_resource.SyncAPIResource):
    @cached_property
    def tokens(self) -> TokensResource:
        return TokensResource(self._client)

    @cached_property
    def solana(self) -> SolanaResource:
        return SolanaResource(self._client)

    @cached_property
    def phantom(self) -> PhantomResource:
        return PhantomResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return APIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#with_streaming_response
        """
        return APIResourceWithStreamingResponse(self)

    def get_wallet_info(
        self,
        address: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIGetWalletInfoResponse:
        """
        Fetches comprehensive wallet data including SOL balance, SPL token holdings,
        recent transactions, and Jupiter portfolio PnL statistics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return self._get(
            f"/api/wallet/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIGetWalletInfoResponse,
        )

    def send_transaction(
        self,
        *,
        signed_transaction: str,
        additional_signers: Iterable[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APISendTransactionResponse:
        """
        Broadcasts a signed Solana transaction to the network.

        Args:
          signed_transaction: Base64-encoded signed transaction

          additional_signers: Additional signers (keypairs)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/send-transaction",
            body=maybe_transform(
                {
                    "signed_transaction": signed_transaction,
                    "additional_signers": additional_signers,
                },
                api_send_transaction_params.APISendTransactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APISendTransactionResponse,
        )

    def upload_token_metadata(
        self,
        *,
        mint: str,
        token_logo: str,
        token_name: str,
        token_symbol: str,
        user_wallet: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIUploadTokenMetadataResponse:
        """
        Uploads token logo and metadata to R2 storage, then creates a Meteora Dynamic
        Bonding Curve pool transaction for the token.

        Args:
          mint: Token mint address

          token_logo: Base64-encoded token logo image (data URL format)

          token_name: Token name

          token_symbol: Token ticker symbol

          user_wallet: User's wallet address (pool creator)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/upload",
            body=maybe_transform(
                {
                    "mint": mint,
                    "token_logo": token_logo,
                    "token_name": token_name,
                    "token_symbol": token_symbol,
                    "user_wallet": user_wallet,
                },
                api_upload_token_metadata_params.APIUploadTokenMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIUploadTokenMetadataResponse,
        )


class AsyncAPIResource(_resource.AsyncAPIResource):
    @cached_property
    def tokens(self) -> AsyncTokensResource:
        return AsyncTokensResource(self._client)

    @cached_property
    def solana(self) -> AsyncSolanaResource:
        return AsyncSolanaResource(self._client)

    @cached_property
    def phantom(self) -> AsyncPhantomResource:
        return AsyncPhantomResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/solana.wallet.router-api-python#with_streaming_response
        """
        return AsyncAPIResourceWithStreamingResponse(self)

    async def get_wallet_info(
        self,
        address: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIGetWalletInfoResponse:
        """
        Fetches comprehensive wallet data including SOL balance, SPL token holdings,
        recent transactions, and Jupiter portfolio PnL statistics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return await self._get(
            f"/api/wallet/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIGetWalletInfoResponse,
        )

    async def send_transaction(
        self,
        *,
        signed_transaction: str,
        additional_signers: Iterable[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APISendTransactionResponse:
        """
        Broadcasts a signed Solana transaction to the network.

        Args:
          signed_transaction: Base64-encoded signed transaction

          additional_signers: Additional signers (keypairs)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/send-transaction",
            body=await async_maybe_transform(
                {
                    "signed_transaction": signed_transaction,
                    "additional_signers": additional_signers,
                },
                api_send_transaction_params.APISendTransactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APISendTransactionResponse,
        )

    async def upload_token_metadata(
        self,
        *,
        mint: str,
        token_logo: str,
        token_name: str,
        token_symbol: str,
        user_wallet: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIUploadTokenMetadataResponse:
        """
        Uploads token logo and metadata to R2 storage, then creates a Meteora Dynamic
        Bonding Curve pool transaction for the token.

        Args:
          mint: Token mint address

          token_logo: Base64-encoded token logo image (data URL format)

          token_name: Token name

          token_symbol: Token ticker symbol

          user_wallet: User's wallet address (pool creator)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/upload",
            body=await async_maybe_transform(
                {
                    "mint": mint,
                    "token_logo": token_logo,
                    "token_name": token_name,
                    "token_symbol": token_symbol,
                    "user_wallet": user_wallet,
                },
                api_upload_token_metadata_params.APIUploadTokenMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIUploadTokenMetadataResponse,
        )


class APIResourceWithRawResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

        self.get_wallet_info = to_raw_response_wrapper(
            api.get_wallet_info,
        )
        self.send_transaction = to_raw_response_wrapper(
            api.send_transaction,
        )
        self.upload_token_metadata = to_raw_response_wrapper(
            api.upload_token_metadata,
        )

    @cached_property
    def tokens(self) -> TokensResourceWithRawResponse:
        return TokensResourceWithRawResponse(self._api.tokens)

    @cached_property
    def solana(self) -> SolanaResourceWithRawResponse:
        return SolanaResourceWithRawResponse(self._api.solana)

    @cached_property
    def phantom(self) -> PhantomResourceWithRawResponse:
        return PhantomResourceWithRawResponse(self._api.phantom)


class AsyncAPIResourceWithRawResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

        self.get_wallet_info = async_to_raw_response_wrapper(
            api.get_wallet_info,
        )
        self.send_transaction = async_to_raw_response_wrapper(
            api.send_transaction,
        )
        self.upload_token_metadata = async_to_raw_response_wrapper(
            api.upload_token_metadata,
        )

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithRawResponse:
        return AsyncTokensResourceWithRawResponse(self._api.tokens)

    @cached_property
    def solana(self) -> AsyncSolanaResourceWithRawResponse:
        return AsyncSolanaResourceWithRawResponse(self._api.solana)

    @cached_property
    def phantom(self) -> AsyncPhantomResourceWithRawResponse:
        return AsyncPhantomResourceWithRawResponse(self._api.phantom)


class APIResourceWithStreamingResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

        self.get_wallet_info = to_streamed_response_wrapper(
            api.get_wallet_info,
        )
        self.send_transaction = to_streamed_response_wrapper(
            api.send_transaction,
        )
        self.upload_token_metadata = to_streamed_response_wrapper(
            api.upload_token_metadata,
        )

    @cached_property
    def tokens(self) -> TokensResourceWithStreamingResponse:
        return TokensResourceWithStreamingResponse(self._api.tokens)

    @cached_property
    def solana(self) -> SolanaResourceWithStreamingResponse:
        return SolanaResourceWithStreamingResponse(self._api.solana)

    @cached_property
    def phantom(self) -> PhantomResourceWithStreamingResponse:
        return PhantomResourceWithStreamingResponse(self._api.phantom)


class AsyncAPIResourceWithStreamingResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

        self.get_wallet_info = async_to_streamed_response_wrapper(
            api.get_wallet_info,
        )
        self.send_transaction = async_to_streamed_response_wrapper(
            api.send_transaction,
        )
        self.upload_token_metadata = async_to_streamed_response_wrapper(
            api.upload_token_metadata,
        )

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithStreamingResponse:
        return AsyncTokensResourceWithStreamingResponse(self._api.tokens)

    @cached_property
    def solana(self) -> AsyncSolanaResourceWithStreamingResponse:
        return AsyncSolanaResourceWithStreamingResponse(self._api.solana)

    @cached_property
    def phantom(self) -> AsyncPhantomResourceWithStreamingResponse:
        return AsyncPhantomResourceWithStreamingResponse(self._api.phantom)

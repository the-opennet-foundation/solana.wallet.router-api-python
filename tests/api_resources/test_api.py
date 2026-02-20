# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from solana.wallet.router_api import SolanaWalletRouterAPI, AsyncSolanaWalletRouterAPI
from solana.wallet.router_api.types import (
    APIGetWalletInfoResponse,
    APISendTransactionResponse,
    APIUploadTokenMetadataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_wallet_info(self, client: SolanaWalletRouterAPI) -> None:
        api = client.api.get_wallet_info(
            "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
        )
        assert_matches_type(APIGetWalletInfoResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_wallet_info(self, client: SolanaWalletRouterAPI) -> None:
        response = client.api.with_raw_response.get_wallet_info(
            "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(APIGetWalletInfoResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_wallet_info(self, client: SolanaWalletRouterAPI) -> None:
        with client.api.with_streaming_response.get_wallet_info(
            "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(APIGetWalletInfoResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_wallet_info(self, client: SolanaWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.api.with_raw_response.get_wallet_info(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_transaction(self, client: SolanaWalletRouterAPI) -> None:
        api = client.api.send_transaction(
            signed_transaction="signedTransaction",
        )
        assert_matches_type(APISendTransactionResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_transaction_with_all_params(self, client: SolanaWalletRouterAPI) -> None:
        api = client.api.send_transaction(
            signed_transaction="signedTransaction",
            additional_signers=[{}],
        )
        assert_matches_type(APISendTransactionResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_transaction(self, client: SolanaWalletRouterAPI) -> None:
        response = client.api.with_raw_response.send_transaction(
            signed_transaction="signedTransaction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(APISendTransactionResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_transaction(self, client: SolanaWalletRouterAPI) -> None:
        with client.api.with_streaming_response.send_transaction(
            signed_transaction="signedTransaction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(APISendTransactionResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_token_metadata(self, client: SolanaWalletRouterAPI) -> None:
        api = client.api.upload_token_metadata(
            mint="mint",
            token_logo="data:image/png;base64,iVBORw0KGgo...",
            token_name="My Token",
            token_symbol="MTK",
            user_wallet="userWallet",
        )
        assert_matches_type(APIUploadTokenMetadataResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload_token_metadata(self, client: SolanaWalletRouterAPI) -> None:
        response = client.api.with_raw_response.upload_token_metadata(
            mint="mint",
            token_logo="data:image/png;base64,iVBORw0KGgo...",
            token_name="My Token",
            token_symbol="MTK",
            user_wallet="userWallet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(APIUploadTokenMetadataResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload_token_metadata(self, client: SolanaWalletRouterAPI) -> None:
        with client.api.with_streaming_response.upload_token_metadata(
            mint="mint",
            token_logo="data:image/png;base64,iVBORw0KGgo...",
            token_name="My Token",
            token_symbol="MTK",
            user_wallet="userWallet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(APIUploadTokenMetadataResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPI:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_wallet_info(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        api = await async_client.api.get_wallet_info(
            "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
        )
        assert_matches_type(APIGetWalletInfoResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_wallet_info(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.api.with_raw_response.get_wallet_info(
            "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(APIGetWalletInfoResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_wallet_info(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.api.with_streaming_response.get_wallet_info(
            "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(APIGetWalletInfoResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_wallet_info(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.api.with_raw_response.get_wallet_info(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_transaction(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        api = await async_client.api.send_transaction(
            signed_transaction="signedTransaction",
        )
        assert_matches_type(APISendTransactionResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_transaction_with_all_params(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        api = await async_client.api.send_transaction(
            signed_transaction="signedTransaction",
            additional_signers=[{}],
        )
        assert_matches_type(APISendTransactionResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_transaction(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.api.with_raw_response.send_transaction(
            signed_transaction="signedTransaction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(APISendTransactionResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_transaction(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.api.with_streaming_response.send_transaction(
            signed_transaction="signedTransaction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(APISendTransactionResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_token_metadata(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        api = await async_client.api.upload_token_metadata(
            mint="mint",
            token_logo="data:image/png;base64,iVBORw0KGgo...",
            token_name="My Token",
            token_symbol="MTK",
            user_wallet="userWallet",
        )
        assert_matches_type(APIUploadTokenMetadataResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload_token_metadata(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.api.with_raw_response.upload_token_metadata(
            mint="mint",
            token_logo="data:image/png;base64,iVBORw0KGgo...",
            token_name="My Token",
            token_symbol="MTK",
            user_wallet="userWallet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(APIUploadTokenMetadataResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload_token_metadata(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.api.with_streaming_response.upload_token_metadata(
            mint="mint",
            token_logo="data:image/png;base64,iVBORw0KGgo...",
            token_name="My Token",
            token_symbol="MTK",
            user_wallet="userWallet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(APIUploadTokenMetadataResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

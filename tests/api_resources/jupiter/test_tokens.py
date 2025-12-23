# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from solana.wallet.router_api import SolanaWalletRouterAPI, AsyncSolanaWalletRouterAPI
from solana.wallet.router_api.types.jupiter import TokenRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SolanaWalletRouterAPI) -> None:
        token = client.jupiter.tokens.retrieve(
            "mint",
        )
        assert_matches_type(TokenRetrieveResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SolanaWalletRouterAPI) -> None:
        response = client.jupiter.tokens.with_raw_response.retrieve(
            "mint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenRetrieveResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SolanaWalletRouterAPI) -> None:
        with client.jupiter.tokens.with_streaming_response.retrieve(
            "mint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenRetrieveResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SolanaWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mint` but received ''"):
            client.jupiter.tokens.with_raw_response.retrieve(
                "",
            )


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        token = await async_client.jupiter.tokens.retrieve(
            "mint",
        )
        assert_matches_type(TokenRetrieveResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.jupiter.tokens.with_raw_response.retrieve(
            "mint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenRetrieveResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.jupiter.tokens.with_streaming_response.retrieve(
            "mint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenRetrieveResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mint` but received ''"):
            await async_client.jupiter.tokens.with_raw_response.retrieve(
                "",
            )

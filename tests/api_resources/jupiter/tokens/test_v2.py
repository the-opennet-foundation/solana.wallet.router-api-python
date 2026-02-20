# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from solana.wallet.router_api import SolanaWalletRouterAPI, AsyncSolanaWalletRouterAPI
from solana.wallet.router_api.types.jupiter.tokens import (
    V2ListRecentResponse,
    V2ListTopTradedResponse,
    V2ListTopTrendingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recent(self, client: SolanaWalletRouterAPI) -> None:
        v2 = client.jupiter.tokens.v2.list_recent()
        assert_matches_type(V2ListRecentResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recent_with_all_params(self, client: SolanaWalletRouterAPI) -> None:
        v2 = client.jupiter.tokens.v2.list_recent(
            limit=0,
        )
        assert_matches_type(V2ListRecentResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_recent(self, client: SolanaWalletRouterAPI) -> None:
        response = client.jupiter.tokens.v2.with_raw_response.list_recent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ListRecentResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_recent(self, client: SolanaWalletRouterAPI) -> None:
        with client.jupiter.tokens.v2.with_streaming_response.list_recent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ListRecentResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_top_traded(self, client: SolanaWalletRouterAPI) -> None:
        v2 = client.jupiter.tokens.v2.list_top_traded(
            interval="5m",
        )
        assert_matches_type(V2ListTopTradedResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_top_traded_with_all_params(self, client: SolanaWalletRouterAPI) -> None:
        v2 = client.jupiter.tokens.v2.list_top_traded(
            interval="5m",
            limit=0,
        )
        assert_matches_type(V2ListTopTradedResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_top_traded(self, client: SolanaWalletRouterAPI) -> None:
        response = client.jupiter.tokens.v2.with_raw_response.list_top_traded(
            interval="5m",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ListTopTradedResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_top_traded(self, client: SolanaWalletRouterAPI) -> None:
        with client.jupiter.tokens.v2.with_streaming_response.list_top_traded(
            interval="5m",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ListTopTradedResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_top_trending(self, client: SolanaWalletRouterAPI) -> None:
        v2 = client.jupiter.tokens.v2.list_top_trending(
            interval="5m",
        )
        assert_matches_type(V2ListTopTrendingResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_top_trending_with_all_params(self, client: SolanaWalletRouterAPI) -> None:
        v2 = client.jupiter.tokens.v2.list_top_trending(
            interval="5m",
            limit=0,
        )
        assert_matches_type(V2ListTopTrendingResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_top_trending(self, client: SolanaWalletRouterAPI) -> None:
        response = client.jupiter.tokens.v2.with_raw_response.list_top_trending(
            interval="5m",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ListTopTrendingResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_top_trending(self, client: SolanaWalletRouterAPI) -> None:
        with client.jupiter.tokens.v2.with_streaming_response.list_top_trending(
            interval="5m",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ListTopTrendingResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV2:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recent(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v2 = await async_client.jupiter.tokens.v2.list_recent()
        assert_matches_type(V2ListRecentResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recent_with_all_params(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v2 = await async_client.jupiter.tokens.v2.list_recent(
            limit=0,
        )
        assert_matches_type(V2ListRecentResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_recent(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.jupiter.tokens.v2.with_raw_response.list_recent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2ListRecentResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_recent(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.jupiter.tokens.v2.with_streaming_response.list_recent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ListRecentResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_top_traded(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v2 = await async_client.jupiter.tokens.v2.list_top_traded(
            interval="5m",
        )
        assert_matches_type(V2ListTopTradedResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_top_traded_with_all_params(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v2 = await async_client.jupiter.tokens.v2.list_top_traded(
            interval="5m",
            limit=0,
        )
        assert_matches_type(V2ListTopTradedResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_top_traded(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.jupiter.tokens.v2.with_raw_response.list_top_traded(
            interval="5m",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2ListTopTradedResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_top_traded(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.jupiter.tokens.v2.with_streaming_response.list_top_traded(
            interval="5m",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ListTopTradedResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_top_trending(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v2 = await async_client.jupiter.tokens.v2.list_top_trending(
            interval="5m",
        )
        assert_matches_type(V2ListTopTrendingResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_top_trending_with_all_params(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v2 = await async_client.jupiter.tokens.v2.list_top_trending(
            interval="5m",
            limit=0,
        )
        assert_matches_type(V2ListTopTrendingResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_top_trending(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.jupiter.tokens.v2.with_raw_response.list_top_trending(
            interval="5m",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2ListTopTrendingResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_top_trending(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.jupiter.tokens.v2.with_streaming_response.list_top_trending(
            interval="5m",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ListTopTrendingResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

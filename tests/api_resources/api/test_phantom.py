# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from solana.wallet.router_api import SolanaWalletRouterAPI, AsyncSolanaWalletRouterAPI
from solana.wallet.router_api.types.api import (
    PhantomSearchSplTokensResponse,
    PhantomExploreMemeTokensResponse,
    PhantomGetSingleTokenStatsResponse,
    PhantomGetPerpTrendingMarketsResponse,
    PhantomGetSimpleTokenOverviewsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhantom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_explore_meme_tokens(self, client: SolanaWalletRouterAPI) -> None:
        phantom = client.api.phantom.explore_meme_tokens()
        assert_matches_type(PhantomExploreMemeTokensResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_explore_meme_tokens_with_all_params(self, client: SolanaWalletRouterAPI) -> None:
        phantom = client.api.phantom.explore_meme_tokens(
            about_to_graduate_filter={
                "platforms_filter": [
                    "Pumpfun",
                    "Bonk",
                    "Raydium Launch Labs",
                    "Believe",
                    "Meteora DBC",
                    "MoonShot",
                    "Jupiter Studio",
                ]
            },
            graduated_filter={
                "platforms_filter": [
                    "Pumpfun",
                    "Bonk",
                    "Raydium Launch Labs",
                    "Believe",
                    "Meteora DBC",
                    "MoonShot",
                    "Jupiter Studio",
                ]
            },
            new_filter={
                "platforms_filter": [
                    "Pumpfun",
                    "Bonk",
                    "Raydium Launch Labs",
                    "Believe",
                    "Meteora DBC",
                    "MoonShot",
                    "Jupiter Studio",
                ]
            },
        )
        assert_matches_type(PhantomExploreMemeTokensResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_explore_meme_tokens(self, client: SolanaWalletRouterAPI) -> None:
        response = client.api.phantom.with_raw_response.explore_meme_tokens()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phantom = response.parse()
        assert_matches_type(PhantomExploreMemeTokensResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_explore_meme_tokens(self, client: SolanaWalletRouterAPI) -> None:
        with client.api.phantom.with_streaming_response.explore_meme_tokens() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phantom = response.parse()
            assert_matches_type(PhantomExploreMemeTokensResponse, phantom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_perp_trending_markets(self, client: SolanaWalletRouterAPI) -> None:
        phantom = client.api.phantom.get_perp_trending_markets()
        assert_matches_type(PhantomGetPerpTrendingMarketsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_perp_trending_markets_with_all_params(self, client: SolanaWalletRouterAPI) -> None:
        phantom = client.api.phantom.get_perp_trending_markets(
            chain_id="chainId",
            limit="limit",
            sort_by="volume",
            sort_direction="asc",
        )
        assert_matches_type(PhantomGetPerpTrendingMarketsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_perp_trending_markets(self, client: SolanaWalletRouterAPI) -> None:
        response = client.api.phantom.with_raw_response.get_perp_trending_markets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phantom = response.parse()
        assert_matches_type(PhantomGetPerpTrendingMarketsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_perp_trending_markets(self, client: SolanaWalletRouterAPI) -> None:
        with client.api.phantom.with_streaming_response.get_perp_trending_markets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phantom = response.parse()
            assert_matches_type(PhantomGetPerpTrendingMarketsResponse, phantom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_simple_token_overviews(self, client: SolanaWalletRouterAPI) -> None:
        phantom = client.api.phantom.get_simple_token_overviews(
            token_addresses="tokenAddresses",
        )
        assert_matches_type(PhantomGetSimpleTokenOverviewsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_simple_token_overviews(self, client: SolanaWalletRouterAPI) -> None:
        response = client.api.phantom.with_raw_response.get_simple_token_overviews(
            token_addresses="tokenAddresses",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phantom = response.parse()
        assert_matches_type(PhantomGetSimpleTokenOverviewsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_simple_token_overviews(self, client: SolanaWalletRouterAPI) -> None:
        with client.api.phantom.with_streaming_response.get_simple_token_overviews(
            token_addresses="tokenAddresses",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phantom = response.parse()
            assert_matches_type(PhantomGetSimpleTokenOverviewsResponse, phantom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_single_token_stats(self, client: SolanaWalletRouterAPI) -> None:
        phantom = client.api.phantom.get_single_token_stats(
            token_address="tokenAddress",
        )
        assert_matches_type(PhantomGetSingleTokenStatsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_single_token_stats(self, client: SolanaWalletRouterAPI) -> None:
        response = client.api.phantom.with_raw_response.get_single_token_stats(
            token_address="tokenAddress",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phantom = response.parse()
        assert_matches_type(PhantomGetSingleTokenStatsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_single_token_stats(self, client: SolanaWalletRouterAPI) -> None:
        with client.api.phantom.with_streaming_response.get_single_token_stats(
            token_address="tokenAddress",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phantom = response.parse()
            assert_matches_type(PhantomGetSingleTokenStatsResponse, phantom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_spl_tokens(self, client: SolanaWalletRouterAPI) -> None:
        phantom = client.api.phantom.search_spl_tokens()
        assert_matches_type(PhantomSearchSplTokensResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_spl_tokens_with_all_params(self, client: SolanaWalletRouterAPI) -> None:
        phantom = client.api.phantom.search_spl_tokens(
            charts="true",
            page="page",
            query="query",
            sniper="true",
            sort_by="volume-desc",
            time_range="5m",
        )
        assert_matches_type(PhantomSearchSplTokensResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_spl_tokens(self, client: SolanaWalletRouterAPI) -> None:
        response = client.api.phantom.with_raw_response.search_spl_tokens()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phantom = response.parse()
        assert_matches_type(PhantomSearchSplTokensResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_spl_tokens(self, client: SolanaWalletRouterAPI) -> None:
        with client.api.phantom.with_streaming_response.search_spl_tokens() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phantom = response.parse()
            assert_matches_type(PhantomSearchSplTokensResponse, phantom, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPhantom:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_explore_meme_tokens(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        phantom = await async_client.api.phantom.explore_meme_tokens()
        assert_matches_type(PhantomExploreMemeTokensResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_explore_meme_tokens_with_all_params(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        phantom = await async_client.api.phantom.explore_meme_tokens(
            about_to_graduate_filter={
                "platforms_filter": [
                    "Pumpfun",
                    "Bonk",
                    "Raydium Launch Labs",
                    "Believe",
                    "Meteora DBC",
                    "MoonShot",
                    "Jupiter Studio",
                ]
            },
            graduated_filter={
                "platforms_filter": [
                    "Pumpfun",
                    "Bonk",
                    "Raydium Launch Labs",
                    "Believe",
                    "Meteora DBC",
                    "MoonShot",
                    "Jupiter Studio",
                ]
            },
            new_filter={
                "platforms_filter": [
                    "Pumpfun",
                    "Bonk",
                    "Raydium Launch Labs",
                    "Believe",
                    "Meteora DBC",
                    "MoonShot",
                    "Jupiter Studio",
                ]
            },
        )
        assert_matches_type(PhantomExploreMemeTokensResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_explore_meme_tokens(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.api.phantom.with_raw_response.explore_meme_tokens()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phantom = await response.parse()
        assert_matches_type(PhantomExploreMemeTokensResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_explore_meme_tokens(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.api.phantom.with_streaming_response.explore_meme_tokens() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phantom = await response.parse()
            assert_matches_type(PhantomExploreMemeTokensResponse, phantom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_perp_trending_markets(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        phantom = await async_client.api.phantom.get_perp_trending_markets()
        assert_matches_type(PhantomGetPerpTrendingMarketsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_perp_trending_markets_with_all_params(
        self, async_client: AsyncSolanaWalletRouterAPI
    ) -> None:
        phantom = await async_client.api.phantom.get_perp_trending_markets(
            chain_id="chainId",
            limit="limit",
            sort_by="volume",
            sort_direction="asc",
        )
        assert_matches_type(PhantomGetPerpTrendingMarketsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_perp_trending_markets(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.api.phantom.with_raw_response.get_perp_trending_markets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phantom = await response.parse()
        assert_matches_type(PhantomGetPerpTrendingMarketsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_perp_trending_markets(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.api.phantom.with_streaming_response.get_perp_trending_markets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phantom = await response.parse()
            assert_matches_type(PhantomGetPerpTrendingMarketsResponse, phantom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_simple_token_overviews(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        phantom = await async_client.api.phantom.get_simple_token_overviews(
            token_addresses="tokenAddresses",
        )
        assert_matches_type(PhantomGetSimpleTokenOverviewsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_simple_token_overviews(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.api.phantom.with_raw_response.get_simple_token_overviews(
            token_addresses="tokenAddresses",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phantom = await response.parse()
        assert_matches_type(PhantomGetSimpleTokenOverviewsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_simple_token_overviews(
        self, async_client: AsyncSolanaWalletRouterAPI
    ) -> None:
        async with async_client.api.phantom.with_streaming_response.get_simple_token_overviews(
            token_addresses="tokenAddresses",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phantom = await response.parse()
            assert_matches_type(PhantomGetSimpleTokenOverviewsResponse, phantom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_single_token_stats(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        phantom = await async_client.api.phantom.get_single_token_stats(
            token_address="tokenAddress",
        )
        assert_matches_type(PhantomGetSingleTokenStatsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_single_token_stats(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.api.phantom.with_raw_response.get_single_token_stats(
            token_address="tokenAddress",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phantom = await response.parse()
        assert_matches_type(PhantomGetSingleTokenStatsResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_single_token_stats(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.api.phantom.with_streaming_response.get_single_token_stats(
            token_address="tokenAddress",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phantom = await response.parse()
            assert_matches_type(PhantomGetSingleTokenStatsResponse, phantom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_spl_tokens(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        phantom = await async_client.api.phantom.search_spl_tokens()
        assert_matches_type(PhantomSearchSplTokensResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_spl_tokens_with_all_params(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        phantom = await async_client.api.phantom.search_spl_tokens(
            charts="true",
            page="page",
            query="query",
            sniper="true",
            sort_by="volume-desc",
            time_range="5m",
        )
        assert_matches_type(PhantomSearchSplTokensResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_spl_tokens(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.api.phantom.with_raw_response.search_spl_tokens()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phantom = await response.parse()
        assert_matches_type(PhantomSearchSplTokensResponse, phantom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_spl_tokens(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.api.phantom.with_streaming_response.search_spl_tokens() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phantom = await response.parse()
            assert_matches_type(PhantomSearchSplTokensResponse, phantom, path=["response"])

        assert cast(Any, response.is_closed) is True

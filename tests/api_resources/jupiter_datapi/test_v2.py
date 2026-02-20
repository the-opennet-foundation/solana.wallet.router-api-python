# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from solana.wallet.router_api import SolanaWalletRouterAPI, AsyncSolanaWalletRouterAPI
from solana.wallet.router_api.types.jupiter_datapi import V2GetTokenPriceChartResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_token_price_chart(self, client: SolanaWalletRouterAPI) -> None:
        v2 = client.jupiter_datapi.v2.get_token_price_chart(
            asset_id="assetId",
            base_asset="baseAsset",
            candles=0,
            from_=0,
            interval="1_SECOND",
            to=0,
        )
        assert_matches_type(V2GetTokenPriceChartResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_token_price_chart_with_all_params(self, client: SolanaWalletRouterAPI) -> None:
        v2 = client.jupiter_datapi.v2.get_token_price_chart(
            asset_id="assetId",
            base_asset="baseAsset",
            candles=0,
            from_=0,
            interval="1_SECOND",
            to=0,
            type="price",
        )
        assert_matches_type(V2GetTokenPriceChartResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_token_price_chart(self, client: SolanaWalletRouterAPI) -> None:
        response = client.jupiter_datapi.v2.with_raw_response.get_token_price_chart(
            asset_id="assetId",
            base_asset="baseAsset",
            candles=0,
            from_=0,
            interval="1_SECOND",
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2GetTokenPriceChartResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_token_price_chart(self, client: SolanaWalletRouterAPI) -> None:
        with client.jupiter_datapi.v2.with_streaming_response.get_token_price_chart(
            asset_id="assetId",
            base_asset="baseAsset",
            candles=0,
            from_=0,
            interval="1_SECOND",
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2GetTokenPriceChartResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_token_price_chart(self, client: SolanaWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.jupiter_datapi.v2.with_raw_response.get_token_price_chart(
                asset_id="",
                base_asset="baseAsset",
                candles=0,
                from_=0,
                interval="1_SECOND",
                to=0,
            )


class TestAsyncV2:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_token_price_chart(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v2 = await async_client.jupiter_datapi.v2.get_token_price_chart(
            asset_id="assetId",
            base_asset="baseAsset",
            candles=0,
            from_=0,
            interval="1_SECOND",
            to=0,
        )
        assert_matches_type(V2GetTokenPriceChartResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_token_price_chart_with_all_params(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v2 = await async_client.jupiter_datapi.v2.get_token_price_chart(
            asset_id="assetId",
            base_asset="baseAsset",
            candles=0,
            from_=0,
            interval="1_SECOND",
            to=0,
            type="price",
        )
        assert_matches_type(V2GetTokenPriceChartResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_token_price_chart(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.jupiter_datapi.v2.with_raw_response.get_token_price_chart(
            asset_id="assetId",
            base_asset="baseAsset",
            candles=0,
            from_=0,
            interval="1_SECOND",
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2GetTokenPriceChartResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_token_price_chart(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.jupiter_datapi.v2.with_streaming_response.get_token_price_chart(
            asset_id="assetId",
            base_asset="baseAsset",
            candles=0,
            from_=0,
            interval="1_SECOND",
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2GetTokenPriceChartResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_token_price_chart(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.jupiter_datapi.v2.with_raw_response.get_token_price_chart(
                asset_id="",
                base_asset="baseAsset",
                candles=0,
                from_=0,
                interval="1_SECOND",
                to=0,
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from solana.wallet.router_api import SolanaWalletRouterAPI, AsyncSolanaWalletRouterAPI
from solana.wallet.router_api.types.jupiter_datapi.v1 import AssetGetDescriptionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_description(self, client: SolanaWalletRouterAPI) -> None:
        asset = client.jupiter_datapi.v1.assets.get_description(
            "assetId",
        )
        assert_matches_type(AssetGetDescriptionResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_description(self, client: SolanaWalletRouterAPI) -> None:
        response = client.jupiter_datapi.v1.assets.with_raw_response.get_description(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetGetDescriptionResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_description(self, client: SolanaWalletRouterAPI) -> None:
        with client.jupiter_datapi.v1.assets.with_streaming_response.get_description(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetGetDescriptionResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_description(self, client: SolanaWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.jupiter_datapi.v1.assets.with_raw_response.get_description(
                "",
            )


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_description(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        asset = await async_client.jupiter_datapi.v1.assets.get_description(
            "assetId",
        )
        assert_matches_type(AssetGetDescriptionResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_description(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.jupiter_datapi.v1.assets.with_raw_response.get_description(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetGetDescriptionResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_description(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.jupiter_datapi.v1.assets.with_streaming_response.get_description(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetGetDescriptionResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_description(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.jupiter_datapi.v1.assets.with_raw_response.get_description(
                "",
            )

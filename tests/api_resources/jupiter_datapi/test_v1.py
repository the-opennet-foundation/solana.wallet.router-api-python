# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from solana.wallet.router_api import SolanaWalletRouterAPI, AsyncSolanaWalletRouterAPI
from solana.wallet.router_api._utils import parse_datetime
from solana.wallet.router_api.types.api import GetTokenResponse
from solana.wallet.router_api.types.jupiter_datapi import (
    V1GetTokenHoldersResponse,
    V1GetWalletPnlStatsResponse,
    V1GetTokenTransactionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_pools(self, client: SolanaWalletRouterAPI) -> None:
        v1 = client.jupiter_datapi.v1.get_pools(
            asset_ids="assetIds",
        )
        assert_matches_type(GetTokenResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_pools(self, client: SolanaWalletRouterAPI) -> None:
        response = client.jupiter_datapi.v1.with_raw_response.get_pools(
            asset_ids="assetIds",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(GetTokenResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_pools(self, client: SolanaWalletRouterAPI) -> None:
        with client.jupiter_datapi.v1.with_streaming_response.get_pools(
            asset_ids="assetIds",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(GetTokenResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_token_holders(self, client: SolanaWalletRouterAPI) -> None:
        v1 = client.jupiter_datapi.v1.get_token_holders(
            "assetId",
        )
        assert_matches_type(V1GetTokenHoldersResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_token_holders(self, client: SolanaWalletRouterAPI) -> None:
        response = client.jupiter_datapi.v1.with_raw_response.get_token_holders(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetTokenHoldersResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_token_holders(self, client: SolanaWalletRouterAPI) -> None:
        with client.jupiter_datapi.v1.with_streaming_response.get_token_holders(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetTokenHoldersResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_token_holders(self, client: SolanaWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.jupiter_datapi.v1.with_raw_response.get_token_holders(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_token_transactions(self, client: SolanaWalletRouterAPI) -> None:
        v1 = client.jupiter_datapi.v1.get_token_transactions(
            asset_id="assetId",
        )
        assert_matches_type(V1GetTokenTransactionsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_token_transactions_with_all_params(self, client: SolanaWalletRouterAPI) -> None:
        v1 = client.jupiter_datapi.v1.get_token_transactions(
            asset_id="assetId",
            from_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset="offset",
            offset_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            to_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            trader_address="traderAddress",
        )
        assert_matches_type(V1GetTokenTransactionsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_token_transactions(self, client: SolanaWalletRouterAPI) -> None:
        response = client.jupiter_datapi.v1.with_raw_response.get_token_transactions(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetTokenTransactionsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_token_transactions(self, client: SolanaWalletRouterAPI) -> None:
        with client.jupiter_datapi.v1.with_streaming_response.get_token_transactions(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetTokenTransactionsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_token_transactions(self, client: SolanaWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.jupiter_datapi.v1.with_raw_response.get_token_transactions(
                asset_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_wallet_pnl_stats(self, client: SolanaWalletRouterAPI) -> None:
        v1 = client.jupiter_datapi.v1.get_wallet_pnl_stats(
            address="address",
        )
        assert_matches_type(V1GetWalletPnlStatsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_wallet_pnl_stats(self, client: SolanaWalletRouterAPI) -> None:
        response = client.jupiter_datapi.v1.with_raw_response.get_wallet_pnl_stats(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetWalletPnlStatsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_wallet_pnl_stats(self, client: SolanaWalletRouterAPI) -> None:
        with client.jupiter_datapi.v1.with_streaming_response.get_wallet_pnl_stats(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetWalletPnlStatsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_pools(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v1 = await async_client.jupiter_datapi.v1.get_pools(
            asset_ids="assetIds",
        )
        assert_matches_type(GetTokenResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_pools(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.jupiter_datapi.v1.with_raw_response.get_pools(
            asset_ids="assetIds",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(GetTokenResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_pools(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.jupiter_datapi.v1.with_streaming_response.get_pools(
            asset_ids="assetIds",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(GetTokenResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_token_holders(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v1 = await async_client.jupiter_datapi.v1.get_token_holders(
            "assetId",
        )
        assert_matches_type(V1GetTokenHoldersResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_token_holders(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.jupiter_datapi.v1.with_raw_response.get_token_holders(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetTokenHoldersResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_token_holders(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.jupiter_datapi.v1.with_streaming_response.get_token_holders(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetTokenHoldersResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_token_holders(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.jupiter_datapi.v1.with_raw_response.get_token_holders(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_token_transactions(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v1 = await async_client.jupiter_datapi.v1.get_token_transactions(
            asset_id="assetId",
        )
        assert_matches_type(V1GetTokenTransactionsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_token_transactions_with_all_params(
        self, async_client: AsyncSolanaWalletRouterAPI
    ) -> None:
        v1 = await async_client.jupiter_datapi.v1.get_token_transactions(
            asset_id="assetId",
            from_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset="offset",
            offset_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            to_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            trader_address="traderAddress",
        )
        assert_matches_type(V1GetTokenTransactionsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_token_transactions(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.jupiter_datapi.v1.with_raw_response.get_token_transactions(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetTokenTransactionsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_token_transactions(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.jupiter_datapi.v1.with_streaming_response.get_token_transactions(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetTokenTransactionsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_token_transactions(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.jupiter_datapi.v1.with_raw_response.get_token_transactions(
                asset_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_wallet_pnl_stats(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v1 = await async_client.jupiter_datapi.v1.get_wallet_pnl_stats(
            address="address",
        )
        assert_matches_type(V1GetWalletPnlStatsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_wallet_pnl_stats(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.jupiter_datapi.v1.with_raw_response.get_wallet_pnl_stats(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetWalletPnlStatsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_wallet_pnl_stats(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.jupiter_datapi.v1.with_streaming_response.get_wallet_pnl_stats(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetWalletPnlStatsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

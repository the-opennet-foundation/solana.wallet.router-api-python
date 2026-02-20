# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from solana.wallet.router_api import SolanaWalletRouterAPI, AsyncSolanaWalletRouterAPI
from solana.wallet.router_api.types.jupiter.swap import (
    Quote,
    V1ExecuteSwapResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_swap(self, client: SolanaWalletRouterAPI) -> None:
        v1 = client.jupiter.swap.v1.execute_swap(
            quote_response={
                "in_amount": "inAmount",
                "input_mint": "inputMint",
                "out_amount": "outAmount",
                "output_mint": "outputMint",
            },
            user_public_key="userPublicKey",
        )
        assert_matches_type(V1ExecuteSwapResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_swap_with_all_params(self, client: SolanaWalletRouterAPI) -> None:
        v1 = client.jupiter.swap.v1.execute_swap(
            quote_response={
                "in_amount": "inAmount",
                "input_mint": "inputMint",
                "out_amount": "outAmount",
                "output_mint": "outputMint",
                "other_amount_threshold": "otherAmountThreshold",
                "price_impact_pct": "priceImpactPct",
                "route_plan": [
                    {
                        "percent": 0,
                        "swap_info": {
                            "amm_key": "ammKey",
                            "fee_amount": "feeAmount",
                            "fee_mint": "feeMint",
                            "in_amount": "inAmount",
                            "input_mint": "inputMint",
                            "label": "label",
                            "out_amount": "outAmount",
                            "output_mint": "outputMint",
                        },
                    }
                ],
                "slippage_bps": 0,
                "swap_mode": "ExactIn",
            },
            user_public_key="userPublicKey",
            dynamic_compute_unit_limit=True,
            prioritization_fee_lamports=0,
            wrap_unwrap_sol=True,
        )
        assert_matches_type(V1ExecuteSwapResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute_swap(self, client: SolanaWalletRouterAPI) -> None:
        response = client.jupiter.swap.v1.with_raw_response.execute_swap(
            quote_response={
                "in_amount": "inAmount",
                "input_mint": "inputMint",
                "out_amount": "outAmount",
                "output_mint": "outputMint",
            },
            user_public_key="userPublicKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ExecuteSwapResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute_swap(self, client: SolanaWalletRouterAPI) -> None:
        with client.jupiter.swap.v1.with_streaming_response.execute_swap(
            quote_response={
                "in_amount": "inAmount",
                "input_mint": "inputMint",
                "out_amount": "outAmount",
                "output_mint": "outputMint",
            },
            user_public_key="userPublicKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ExecuteSwapResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_quote(self, client: SolanaWalletRouterAPI) -> None:
        v1 = client.jupiter.swap.v1.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
        )
        assert_matches_type(Quote, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_quote_with_all_params(self, client: SolanaWalletRouterAPI) -> None:
        v1 = client.jupiter.swap.v1.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
            as_legacy_transaction=True,
            only_direct_routes=True,
            slippage_bps=0,
        )
        assert_matches_type(Quote, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_quote(self, client: SolanaWalletRouterAPI) -> None:
        response = client.jupiter.swap.v1.with_raw_response.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(Quote, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_quote(self, client: SolanaWalletRouterAPI) -> None:
        with client.jupiter.swap.v1.with_streaming_response.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(Quote, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_swap(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v1 = await async_client.jupiter.swap.v1.execute_swap(
            quote_response={
                "in_amount": "inAmount",
                "input_mint": "inputMint",
                "out_amount": "outAmount",
                "output_mint": "outputMint",
            },
            user_public_key="userPublicKey",
        )
        assert_matches_type(V1ExecuteSwapResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_swap_with_all_params(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v1 = await async_client.jupiter.swap.v1.execute_swap(
            quote_response={
                "in_amount": "inAmount",
                "input_mint": "inputMint",
                "out_amount": "outAmount",
                "output_mint": "outputMint",
                "other_amount_threshold": "otherAmountThreshold",
                "price_impact_pct": "priceImpactPct",
                "route_plan": [
                    {
                        "percent": 0,
                        "swap_info": {
                            "amm_key": "ammKey",
                            "fee_amount": "feeAmount",
                            "fee_mint": "feeMint",
                            "in_amount": "inAmount",
                            "input_mint": "inputMint",
                            "label": "label",
                            "out_amount": "outAmount",
                            "output_mint": "outputMint",
                        },
                    }
                ],
                "slippage_bps": 0,
                "swap_mode": "ExactIn",
            },
            user_public_key="userPublicKey",
            dynamic_compute_unit_limit=True,
            prioritization_fee_lamports=0,
            wrap_unwrap_sol=True,
        )
        assert_matches_type(V1ExecuteSwapResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute_swap(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.jupiter.swap.v1.with_raw_response.execute_swap(
            quote_response={
                "in_amount": "inAmount",
                "input_mint": "inputMint",
                "out_amount": "outAmount",
                "output_mint": "outputMint",
            },
            user_public_key="userPublicKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ExecuteSwapResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute_swap(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.jupiter.swap.v1.with_streaming_response.execute_swap(
            quote_response={
                "in_amount": "inAmount",
                "input_mint": "inputMint",
                "out_amount": "outAmount",
                "output_mint": "outputMint",
            },
            user_public_key="userPublicKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ExecuteSwapResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_quote(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v1 = await async_client.jupiter.swap.v1.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
        )
        assert_matches_type(Quote, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_quote_with_all_params(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        v1 = await async_client.jupiter.swap.v1.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
            as_legacy_transaction=True,
            only_direct_routes=True,
            slippage_bps=0,
        )
        assert_matches_type(Quote, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_quote(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.jupiter.swap.v1.with_raw_response.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(Quote, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_quote(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.jupiter.swap.v1.with_streaming_response.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(Quote, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

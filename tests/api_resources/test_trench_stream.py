# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from solana.wallet.router_api import SolanaWalletRouterAPI, AsyncSolanaWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrenchStream:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect(self, client: SolanaWalletRouterAPI) -> None:
        trench_stream = client.trench_stream.connect()
        assert trench_stream is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: SolanaWalletRouterAPI) -> None:
        response = client.trench_stream.with_raw_response.connect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trench_stream = response.parse()
        assert trench_stream is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: SolanaWalletRouterAPI) -> None:
        with client.trench_stream.with_streaming_response.connect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trench_stream = response.parse()
            assert trench_stream is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTrenchStream:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        trench_stream = await async_client.trench_stream.connect()
        assert trench_stream is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        response = await async_client.trench_stream.with_raw_response.connect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trench_stream = await response.parse()
        assert trench_stream is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncSolanaWalletRouterAPI) -> None:
        async with async_client.trench_stream.with_streaming_response.connect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trench_stream = await response.parse()
            assert trench_stream is None

        assert cast(Any, response.is_closed) is True

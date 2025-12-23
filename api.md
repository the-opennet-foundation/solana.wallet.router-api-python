# API

Types:

```python
from solana.wallet.router_api.types import (
    WalletPortfolioPeriod,
    APIGetWalletInfoResponse,
    APISendTransactionResponse,
    APIUploadTokenMetadataResponse,
)
```

Methods:

- <code title="get /api/wallet/{address}">client.api.<a href="./src/solana/wallet/router_api/resources/api/api.py">get_wallet_info</a>(address) -> <a href="./src/solana/wallet/router_api/types/api_get_wallet_info_response.py">APIGetWalletInfoResponse</a></code>
- <code title="post /api/send-transaction">client.api.<a href="./src/solana/wallet/router_api/resources/api/api.py">send_transaction</a>(\*\*<a href="src/solana/wallet/router_api/types/api_send_transaction_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/api_send_transaction_response.py">APISendTransactionResponse</a></code>
- <code title="post /api/upload">client.api.<a href="./src/solana/wallet/router_api/resources/api/api.py">upload_token_metadata</a>(\*\*<a href="src/solana/wallet/router_api/types/api_upload_token_metadata_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/api_upload_token_metadata_response.py">APIUploadTokenMetadataResponse</a></code>

## Tokens

Types:

```python
from solana.wallet.router_api.types.api import (
    GetTokenResponse,
    Pool,
    TokenListResponse,
    TokenListResponse,
)
```

Methods:

- <code title="get /api/tokens/{id}">client.api.tokens.<a href="./src/solana/wallet/router_api/resources/api/tokens.py">retrieve</a>(id) -> <a href="./src/solana/wallet/router_api/types/api/get_token_response.py">GetTokenResponse</a></code>
- <code title="get /api/tokens">client.api.tokens.<a href="./src/solana/wallet/router_api/resources/api/tokens.py">list</a>(\*\*<a href="src/solana/wallet/router_api/types/api/token_list_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/api/token_list_response.py">TokenListResponse</a></code>

## Solana

Types:

```python
from solana.wallet.router_api.types.api import SolanaGetStatusResponse
```

Methods:

- <code title="get /api/solana/status">client.api.solana.<a href="./src/solana/wallet/router_api/resources/api/solana.py">get_status</a>() -> <a href="./src/solana/wallet/router_api/types/api/solana_get_status_response.py">SolanaGetStatusResponse</a></code>

## Phantom

Types:

```python
from solana.wallet.router_api.types.api import (
    MemeExploreFilter,
    PhantomExploreMemeTokensResponse,
    PhantomGetPerpTrendingMarketsResponse,
    PhantomGetSimpleTokenOverviewsResponse,
    PhantomGetSingleTokenStatsResponse,
    PhantomSearchSplTokensResponse,
)
```

Methods:

- <code title="post /api/phantom/meme-explore">client.api.phantom.<a href="./src/solana/wallet/router_api/resources/api/phantom.py">explore_meme_tokens</a>(\*\*<a href="src/solana/wallet/router_api/types/api/phantom_explore_meme_tokens_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/api/phantom_explore_meme_tokens_response.py">PhantomExploreMemeTokensResponse</a></code>
- <code title="get /api/phantom/perp-trending-markets">client.api.phantom.<a href="./src/solana/wallet/router_api/resources/api/phantom.py">get_perp_trending_markets</a>(\*\*<a href="src/solana/wallet/router_api/types/api/phantom_get_perp_trending_markets_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/api/phantom_get_perp_trending_markets_response.py">PhantomGetPerpTrendingMarketsResponse</a></code>
- <code title="get /api/phantom/simple-token-overviews">client.api.phantom.<a href="./src/solana/wallet/router_api/resources/api/phantom.py">get_simple_token_overviews</a>(\*\*<a href="src/solana/wallet/router_api/types/api/phantom_get_simple_token_overviews_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/api/phantom_get_simple_token_overviews_response.py">PhantomGetSimpleTokenOverviewsResponse</a></code>
- <code title="get /api/phantom/single-token-stats">client.api.phantom.<a href="./src/solana/wallet/router_api/resources/api/phantom.py">get_single_token_stats</a>(\*\*<a href="src/solana/wallet/router_api/types/api/phantom_get_single_token_stats_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/api/phantom_get_single_token_stats_response.py">PhantomGetSingleTokenStatsResponse</a></code>
- <code title="get /api/phantom/search-bot-spl">client.api.phantom.<a href="./src/solana/wallet/router_api/resources/api/phantom.py">search_spl_tokens</a>(\*\*<a href="src/solana/wallet/router_api/types/api/phantom_search_spl_tokens_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/api/phantom_search_spl_tokens_response.py">PhantomSearchSplTokensResponse</a></code>

# Jupiter

## Tokens

Types:

```python
from solana.wallet.router_api.types.jupiter import TokenRetrieveResponse
```

Methods:

- <code title="get /jupiter/tokens/v1/{mint}">client.jupiter.tokens.<a href="./src/solana/wallet/router_api/resources/jupiter/tokens/tokens.py">retrieve</a>(mint) -> <a href="./src/solana/wallet/router_api/types/jupiter/token_retrieve_response.py">TokenRetrieveResponse</a></code>

### V2

Types:

```python
from solana.wallet.router_api.types.jupiter.tokens import (
    JupiterToken,
    SwapStats,
    TokenAudit,
    V2ListRecentResponse,
    V2ListTopTradedResponse,
    V2ListTopTrendingResponse,
)
```

Methods:

- <code title="get /jupiter/tokens/v2/recent">client.jupiter.tokens.v2.<a href="./src/solana/wallet/router_api/resources/jupiter/tokens/v2.py">list_recent</a>(\*\*<a href="src/solana/wallet/router_api/types/jupiter/tokens/v2_list_recent_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/jupiter/tokens/v2_list_recent_response.py">V2ListRecentResponse</a></code>
- <code title="get /jupiter/tokens/v2/toptraded/{interval}">client.jupiter.tokens.v2.<a href="./src/solana/wallet/router_api/resources/jupiter/tokens/v2.py">list_top_traded</a>(interval, \*\*<a href="src/solana/wallet/router_api/types/jupiter/tokens/v2_list_top_traded_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/jupiter/tokens/v2_list_top_traded_response.py">V2ListTopTradedResponse</a></code>
- <code title="get /jupiter/tokens/v2/toptrending/{interval}">client.jupiter.tokens.v2.<a href="./src/solana/wallet/router_api/resources/jupiter/tokens/v2.py">list_top_trending</a>(interval, \*\*<a href="src/solana/wallet/router_api/types/jupiter/tokens/v2_list_top_trending_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/jupiter/tokens/v2_list_top_trending_response.py">V2ListTopTrendingResponse</a></code>

## Swap

### V1

Types:

```python
from solana.wallet.router_api.types.jupiter.swap import Quote, V1ExecuteSwapResponse
```

Methods:

- <code title="post /jupiter/swap/v1/swap">client.jupiter.swap.v1.<a href="./src/solana/wallet/router_api/resources/jupiter/swap/v1.py">execute_swap</a>(\*\*<a href="src/solana/wallet/router_api/types/jupiter/swap/v1_execute_swap_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/jupiter/swap/v1_execute_swap_response.py">V1ExecuteSwapResponse</a></code>
- <code title="get /jupiter/swap/v1/quote">client.jupiter.swap.v1.<a href="./src/solana/wallet/router_api/resources/jupiter/swap/v1.py">get_quote</a>(\*\*<a href="src/solana/wallet/router_api/types/jupiter/swap/v1_get_quote_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/jupiter/swap/quote.py">Quote</a></code>

# JupiterDatapi

## V1

Types:

```python
from solana.wallet.router_api.types.jupiter_datapi import (
    V1GetTokenHoldersResponse,
    V1GetTokenTransactionsResponse,
    V1GetWalletPnlStatsResponse,
)
```

Methods:

- <code title="get /jupiter-datapi/v1/pools">client.jupiter_datapi.v1.<a href="./src/solana/wallet/router_api/resources/jupiter_datapi/v1/v1.py">get_pools</a>(\*\*<a href="src/solana/wallet/router_api/types/jupiter_datapi/v1_get_pools_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/api/get_token_response.py">GetTokenResponse</a></code>
- <code title="get /jupiter-datapi/v1/holders/{assetId}">client.jupiter_datapi.v1.<a href="./src/solana/wallet/router_api/resources/jupiter_datapi/v1/v1.py">get_token_holders</a>(asset_id) -> <a href="./src/solana/wallet/router_api/types/jupiter_datapi/v1_get_token_holders_response.py">V1GetTokenHoldersResponse</a></code>
- <code title="get /jupiter-datapi/v1/txs/{assetId}">client.jupiter_datapi.v1.<a href="./src/solana/wallet/router_api/resources/jupiter_datapi/v1/v1.py">get_token_transactions</a>(asset_id, \*\*<a href="src/solana/wallet/router_api/types/jupiter_datapi/v1_get_token_transactions_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/jupiter_datapi/v1_get_token_transactions_response.py">V1GetTokenTransactionsResponse</a></code>
- <code title="get /jupiter-datapi/v1/pnl-stats">client.jupiter_datapi.v1.<a href="./src/solana/wallet/router_api/resources/jupiter_datapi/v1/v1.py">get_wallet_pnl_stats</a>(\*\*<a href="src/solana/wallet/router_api/types/jupiter_datapi/v1_get_wallet_pnl_stats_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/jupiter_datapi/v1_get_wallet_pnl_stats_response.py">V1GetWalletPnlStatsResponse</a></code>

### Assets

Types:

```python
from solana.wallet.router_api.types.jupiter_datapi.v1 import AssetGetDescriptionResponse
```

Methods:

- <code title="get /jupiter-datapi/v1/assets/{assetId}/description">client.jupiter_datapi.v1.assets.<a href="./src/solana/wallet/router_api/resources/jupiter_datapi/v1/assets.py">get_description</a>(asset_id) -> <a href="./src/solana/wallet/router_api/types/jupiter_datapi/v1/asset_get_description_response.py">AssetGetDescriptionResponse</a></code>

## V2

Types:

```python
from solana.wallet.router_api.types.jupiter_datapi import V2GetTokenPriceChartResponse
```

Methods:

- <code title="get /jupiter-datapi/v2/charts/{assetId}">client.jupiter_datapi.v2.<a href="./src/solana/wallet/router_api/resources/jupiter_datapi/v2.py">get_token_price_chart</a>(asset_id, \*\*<a href="src/solana/wallet/router_api/types/jupiter_datapi/v2_get_token_price_chart_params.py">params</a>) -> <a href="./src/solana/wallet/router_api/types/jupiter_datapi/v2_get_token_price_chart_response.py">V2GetTokenPriceChartResponse</a></code>

# TrenchStream

Methods:

- <code title="get /trench-stream/ws">client.trench_stream.<a href="./src/solana/wallet/router_api/resources/trench_stream.py">connect</a>() -> None</code>

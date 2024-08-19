from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True, kw_only=True)
class DexStats:
    trades: int
    tvl: str
    unique_wallets: int
    volume_usd: str


@dataclass_json
@dataclass(frozen=True, kw_only=True)
class PoolStats:
    apy: str | None = None
    base_id: str
    base_liquidity: str
    base_name: str
    base_symbol: str
    base_volume: str
    last_price: str
    lp_price: str | None = None
    lp_price_usd: str
    pool_address: str
    quote_id: str
    quote_liquidity: str
    quote_name: str
    quote_symbol: str
    quote_volume: str
    router_address: str
    url: str


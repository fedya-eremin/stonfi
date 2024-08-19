from dataclasses_json import dataclass_json
from dataclasses import dataclass

@dataclass_json
@dataclass(frozen=True, kw_only=True)
class Pool:
    address: str
    apy_1d: str | None = None
    apy_30d: str | None = None
    apy_7d: str | None = None
    collected_token0_protocol_fee: str
    collected_token1_protocol_fee: str
    deprecated: bool
    lp_account_address: str | None = None
    lp_balance: str | None = None
    lp_fee: str
    lp_price_usd: str | None = None
    lp_total_supply: str
    lp_total_supply_usd: str | None = None
    lp_wallet_address: str | None = None
    protocol_fee: str
    protocol_fee_address: str
    ref_fee: str | None = None
    reserve0: str
    reserve1: str
    router_address: str
    token0_address: str
    token0_balance: str | None = None
    token1_address: str
    token1_balance: str | None = None


from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json



@dataclass_json
@dataclass(frozen=True, kw_only=True)
class SwapSimulateData:
    offer_address: str
    ask_address: str
    units: str
    slippage_tolerance: str
    referral_address: str | None = None
    referral_fee_bps: str | None = None


@dataclass_json
@dataclass(frozen=True, kw_only=True)
class SwapResponse:
    ask_address: str
    ask_jetton_wallet: str
    ask_units: str
    fee_address: str
    fee_percent: str
    fee_units: str
    min_ask_units: str
    offer_address: str
    offer_jetton_wallet: str
    offer_units: str
    pool_address: str
    price_impact: str
    router_address: str
    slippage_tolerance: str
    swap_rate: str



@dataclass_json
@dataclass(frozen=True, kw_only=True)
class SwapStatus:
    address: str | None = None
    balance_deltas: str | None = None
    coins: str | None = None
    exit_code: str | None = None
    logical_time: str | None = None
    query_id: str | None = None
    tx_hash: str | None = None
    type: str = field(metadata=config(field_name="@type"))

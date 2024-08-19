from dataclasses import dataclass
from dataclasses_json import dataclass_json

from stonfi.types.asset import Asset

@dataclass_json
@dataclass(frozen=True, kw_only=True)
class OperationStat:
    asset0_address: str
    asset0_amount: str
    asset0_delta: str
    asset0_reserve: str
    asset1_address: str
    asset1_amount: str
    asset1_delta: str
    asset1_reserve: str
    destination_wallet_address: str
    exit_code: str
    fee_asset_address: str | None = None
    lp_fee_amount: str
    lp_token_delta: str
    lp_token_supply: str
    operation_type: str
    pool_address: str
    pool_tx_hash: str
    pool_tx_lt: int
    pool_tx_timestamp: str
    protocol_fee_amount: str
    referral_address: str | None = None
    referral_fee_amount: str
    router_address: str
    success: bool
    wallet_address: str
    wallet_tx_hash: str
    wallet_tx_lt: int
    wallet_tx_timestamp: str

@dataclass_json
@dataclass(frozen=True, kw_only=True)
class Operation:
    asset0_info: Asset
    asset1_info: Asset
    operation: OperationStat

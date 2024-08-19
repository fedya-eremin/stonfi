from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass(frozen=True, kw_only=True)
class FarmNftReward:
    address: str
    amount: str

@dataclass_json
@dataclass(frozen=True, kw_only=True)
class FarmNft:
    address: str
    create_timestamp: str
    min_unstake_timestamp: str
    nonclaimed_rewards: str
    rewards: list[FarmNftReward]
    staked_tokens: str
    status: str

@dataclass_json
@dataclass(frozen=True, kw_only=True)
class FarmMinterReward:
    address: str
    remaining_rewards: str
    reward_rate_24h: str
    status: str

@dataclass_json
@dataclass(frozen=True, kw_only=True)
class Farm:
    locked_total_lp: str
    min_stake_duration_s: str
    minter_address: str
    nft_infos: list[FarmNft]
    pool_address: str
    reward_token_address: str
    rewards: list[FarmMinterReward]
    status: str
    apy: str | None = None
    locked_total_lp_usd: str | None = None


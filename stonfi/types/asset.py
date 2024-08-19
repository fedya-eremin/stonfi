from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import StrEnum



class AssetKind(StrEnum):
    JETTON = "Jetton"
    WTON = "Wton"
    TON = "Ton"
    NOT_AN_ASSET = "NotAnAsset"

@dataclass_json
@dataclass(frozen=True, kw_only=True)
class Asset:
    balance: str | None = None
    blacklisted: bool
    community: bool
    contract_address: str
    default_symbol: bool
    deprecated: bool
    dex_price_usd: str | None = None
    dex_usd_price: str | None = None
    display_name: str | None = None
    image_url: str | None = None
    kind: AssetKind
    symbol: str
    tags: list[str]
    taxable: bool
    third_party_price_usd: str | None = None
    third_party_usd_price: str | None = None
    wallet_address: str | None = None
    decimals: int
    priority: int

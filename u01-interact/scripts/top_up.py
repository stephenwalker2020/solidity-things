#!/usr/bin/python3
from datetime import datetime
from brownie import accounts, Contract
from brownie.network.gas.strategies import GasNowScalingStrategy

DEPLOYER = accounts.load("deployer")
BOR_ADDRESS = "0x3c9d6c1C73b31c837832c72E04D3152f051fc1A9"
bor = Contract.from_explorer(BOR_ADDRESS)
gas_strategy = GasNowScalingStrategy("standard", "fast")

sr_ppt = "0xcF4f8A5e19a1C7AC69729aa215A46ac24E7090d6"
sr_obtc = "0xF29E1BE74D1F9e3436E8b7AD2756f19A904E7b48"

spf = "0x7b9a695421FfB5D0EAF1a634d85524e07d4662eE"
sp_dai = "0x41edC2C7212367FC59983890aad48B92b0Fe296d"
sp_usdc = "0x89F0112A9c75D987686C608ca1840f9C7344B7fF"
sp_weth = "0xe42b6deA46AA64120b95e75D084f42579ED8a384"
sp_usdt = "0xA6172034B1750842f12de7722Bb6cD5D4f107761"

sp_yfi = "0xb035Dd8e7Ebb8B73A99270A12DE9D448d15de2bf"
sp_yfii = "0xC80DBede0E3CabC52c5a4a3bc9611913e49b8dCc"
sp_link = "0xEa8BBbb296D9d15e91E65ea2b189663805BB5916"
sp_band = "0xF99125968D45f88d625ADCF79700628ACDA65D6b"
sp_nest = "0xfaacABc2468736f43eDC57f5e6080B8b48BbD050"

sp_hbtc = "0xb09a612Ebe2AA5750C51eb317820C6f2866A9ca6"

cover = ""
curve = "0x7f1AE7A1fC275B5B9C3ad4497Fa94E3b9424E76e"

def ppt_obtc():
    pass

def sp_first():
    pass

def sp_second():
    pass

def hbtc():
    HBTC_CONTRACT_ADDRESS = "0x0316EB71485b0Ab14103307bf65a021042c6d380"
    SATELLITE_POOL_ADDRESS = "0xb09a612Ebe2AA5750C51eb317820C6f2866A9ca6"
    SATELLITE_POOL_FACTORY_ADDRESS = "0x7b9a695421FfB5D0EAF1a634d85524e07d4662eE"
    # spf = SatellitePoolFactory.at(SATELLITE_POOL_FACTORY_ADDRESS)
    spf_contract = Contract.from_explorer(spf)
    sp_contract = Contract.from_explorer(sp_hbtc)
    print("spf address", spf.address)
    peroidFinish = datetime.fromtimestamp(sp_contract.periodFinish())
    print("peroidFinish {}", peroidFinish.strftime("%Y-%m-%d %H:%M:%S"))
    # sp = SatellitePool(spf.poolByStakingToken(HBTC_CONTRACT_ADDRESS))
    # print("sp address", sp)
    # transfer bor
    bor.transfer(SATELLITE_POOL_FACTORY_ADDRESS, 9*10**18, {'from': DEPLOYER, 'gas_price': gas_strategy})
    spf.notifyRewardAmount(HBTC_CONTRACT_ADDRESS, 3*24*3600, 9*10**18, {'from': DEPLOYER, 'gas_price': gas_strategy})

def cover():
    pass

def curve():
    pass
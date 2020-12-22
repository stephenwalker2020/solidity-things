#!/usr/bin/python3
from datetime import datetime
import time
from brownie import accounts, Contract, chain
from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie.network.web3 import Web3


BOR_ADDRESS = "0x3c9d6c1C73b31c837832c72E04D3152f051fc1A9"
bor = Contract.from_explorer(BOR_ADDRESS)
gas_strategy = GasNowScalingStrategy("standard", "fast")

sr_ppt = "0xcF4f8A5e19a1C7AC69729aa215A46ac24E7090d6"
sr_obtc = "0xF29E1BE74D1F9e3436E8b7AD2756f19A904E7b48"

spf_address = "0x7b9a695421FfB5D0EAF1a634d85524e07d4662eE"
sp_dai_address = "0x41edC2C7212367FC59983890aad48B92b0Fe296d"
sp_usdc_address = "0x89F0112A9c75D987686C608ca1840f9C7344B7fF"
sp_weth_address = "0xe42b6deA46AA64120b95e75D084f42579ED8a384"
sp_usdt_address = "0xA6172034B1750842f12de7722Bb6cD5D4f107761"

sp_yfi_address = "0xb035Dd8e7Ebb8B73A99270A12DE9D448d15de2bf"
sp_yfii_address = "0xC80DBede0E3CabC52c5a4a3bc9611913e49b8dCc"
sp_link_address = "0xEa8BBbb296D9d15e91E65ea2b189663805BB5916"
sp_band_address = "0xF99125968D45f88d625ADCF79700628ACDA65D6b"
sp_nest_address = "0xfaacABc2468736f43eDC57f5e6080B8b48BbD050"

sp_hbtc_address = "0xb09a612Ebe2AA5750C51eb317820C6f2866A9ca6"

cover = ""
curve = "0x7f1AE7A1fC275B5B9C3ad4497Fa94E3b9424E76e"

def _sp_top_up(amount, sp_addrs, pool_len, days=7):
    spf = Contract.from_explorer(spf_address)
    for addr in sp_addrs:
        sp = Contract.from_explorer(addr)
        staking_token_address = sp.stakingToken()
        remaining_time = sp.periodFinish() - chain[-1].timestamp
        print(remaining_time)
        if remaining_time >= 0:
            raise ValueError("satellite pool {} period not finish, finished in {}".format(addr, datetime.fromtimestamp(sp.periodFinish()).strftime("%Y-%m-%d %H:%M:%S")))
    exit(1)
    DEPLOYER = accounts.load("deployer")
    bor.transfer(spf_address, amount*days*pool_len*10**18, {'from': DEPLOYER, 'gas_price': gas_strategy})
    for addr in sp_addrs:
        sp = Contract.from_explorer(addr)
        staking_token_address = sp.stakingToken()
        spf.notifyRewardAmount(staking_token_address, days*24*3600, amount*days*10**18, {'from': DEPLOYER, 'gas_price': gas_strategy})


def ppt():
    pass

def obtc():
    pass

def sp_first():
    amount = float(input("input amount per day:"))
    sp_addrs = [sp_dai_address, sp_usdc_address, sp_weth_address, sp_usdt_address]
    _sp_top_up(amount, sp_addrs, len(sp_addrs))

def sp_second():
    amount = float(input("input amount per day:"))
    sp_addrs = [sp_yfi_address, sp_yfii_address, sp_link_address, sp_band_address, sp_nest_address]
    _sp_top_up(amount, sp_addrs, len(sp_addrs))

def hbtc():
    amount = float(input("input amount per day:"))
    days= float(input("input days:"))
    sp_addrs = [sp_hbtc_address]
    _sp_top_up(amount, sp_addrs, len(sp_addrs), days=days)

def cover():
    pass

def curve():
    pass
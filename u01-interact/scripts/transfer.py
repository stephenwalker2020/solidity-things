#!/usr/bin/python3

from datetime import datetime
from brownie import accounts, Contract, chain
from brownie.network.gas.strategies import GasNowScalingStrategy

BOR_ADDRESS = "0x3c9d6c1C73b31c837832c72E04D3152f051fc1A9"
bor = Contract.from_explorer(BOR_ADDRESS)
gas_strategy = GasNowScalingStrategy("standard", "fast")

def transfer():
    to = input("to address:")
    amount = input("transfer amount:")
    DEPLOYER = accounts.load("deployer")
    bor.transfer(to, amount*10**18, {'from': DEPLOYER, 'gas_price': gas_strategy})
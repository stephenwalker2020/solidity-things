#!/usr/bin/python3

from brownie import accounts, TimeDistribution, Bor
from brownie.network.gas.strategies import GasNowScalingStrategy
import getpass

gas_strategy = GasNowScalingStrategy("standard", "fast")

BOR_ADDRESS = "0x3c9d6c1C73b31c837832c72E04D3152f051fc1A9"
bor = Bor.at(BOR_ADDRESS)

deployer = accounts.load("deployer")

def addInfoUser():
    pass
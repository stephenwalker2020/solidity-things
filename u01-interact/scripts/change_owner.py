#!/usr/bin/pyhon3

from brownie import accounts, Contract, OToken
from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie.network.web3 import Web3
import time


# timelock_address = "0x264423694764326cBB0Ea6917aA80f89F0B051B0"
timelock_address = "0xcf5f738C89162e64F64D2E2A85b5544A438503F6"

# boringdao_address = "0x23244c5D46899f1eDa3F935AFE2A826A773Fb93f"
boringdao_address = "0xe3547Ba476907cEbe554aB2a1c9f64378fb14f3b"

obtc_address = "0x8064d9Ae6cDf087b1bcd5BDf3531bD5d8C537a68"

gas_strategy = GasNowScalingStrategy("standard", "fast")
admin_role = Web3.toHex(0).ljust(66, '0')
# rop = accounts.load("rop1")

def change(contract_address, user_id):
    user = accounts.load(user_id)
    print("admin role {}".format(admin_role))
    con = Contract.from_explorer(contract_address)
    con.grantRole(admin_role, timelock_address, {'from': user, 'gas_strategy': gas_strategy})
    count = con.getRoleMemberCount(admin_role)
    print("admin has {}".format(count))
    count = con.getRoleMemberCount(admin_role)
    print("admin has {}".format(count))


def change_boringdao():
    change(boringdao_address, 'deployer')

def change_obtc():
    change(obtc_address, 'deployer')


def add_trustee():
    timelock = Contract.from_explorer(timelock_address)
    calldata = Contract.from_explorer(boringdao_address).addTrustee.encode_input(timelock_address)
    pre = Web3.toHex(0).ljust(66, '0')
    timelock.schedule(boringdao_address, 0, calldata, pre, pre, 10, {'from': rop, 'gas_price': gas_strategy})
    time.sleep(20)
    timelock.execute(boringdao_address, 0, calldata, pre, pre, {'from': rop, 'gas_price': gas_strategy})

def main():
    pass
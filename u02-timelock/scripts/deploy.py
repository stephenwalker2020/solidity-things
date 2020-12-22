#!/usr/bin/python3

from brownie import accounts, Contract, BoringDAOTimelock
from dotenv import load_dotenv
import os
load_dotenv()

def main():
    user = accounts.add(os.getenv("private_key"))
    print(user)
    timelock = BoringDAOTimelock.deploy(24*3600, [user], [user], {'from': user})
    print("timelock {}".format(timelock.address))
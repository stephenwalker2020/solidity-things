#!/usr/bin/python3

from brownie import accounts, Contract
from brownie.convert.datatypes import UNITS
from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie.network.web3 import Web3
from brownie.convert.datatypes import HexString

gas_strategy = GasNowScalingStrategy("standard", "fast")

def set():
    btcPrice = "22724"
    hbtcPrice = "22478"
    borPrice = "275.33"
    wethPrice = "610.06"
    usdtPrice = "1"
    usdcPrice = "1"
    daiPrice = "1"
    yfiPrice = "24577"
    yfiiPrice = "1613.25"
    linkPrice = "12.46"
    bandPrice = "6.2"
    nestPrice = "0.034"
    symbols_str = ['BTC', 'HBTC', 'BOR', 'WETH', 'USDT', 'USDC', 'DAI', 'YFI', 'YFII', 'LINK', 'BAND', 'NEST']
    symbols = list(map(lambda s: Web3.toHex(text=s).ljust(66, '0'), symbols_str))
    # print(symbols)
    prices_str = [btcPrice, hbtcPrice, borPrice, wethPrice, usdtPrice, usdcPrice, daiPrice, yfiPrice, yfiiPrice, linkPrice, bandPrice, nestPrice]
    prices = list(map(lambda p: Web3.toWei(p, 'ether'), prices_str))
    # print(prices)
    if len(symbols) != len(prices):
        raise ValueError("symbols length not equal prices");
    for i in range(0, len(symbols)):
        print("{} {}, {} {}".format(symbols_str[i], prices_str[i], symbols[i], prices[i]))
    confirm = input("price is y/n: ")
    if confirm != 'y':
        raise ValueError("prices is not ok")
    deployer = accounts.load('deployer')
    oracle = Contract.from_explorer("0x43B41E120FF06622D122d5B54FA378ADE1E7D4cb")
    oracle.setMultiPrice(symbols, prices, {'from': deployer, 'gas_price': gas_strategy})
    print("Good job, set price successful!")

def main():
    set()
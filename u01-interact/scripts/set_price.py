#!/usr/bin/python3

from brownie import accounts, Contract
from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie.network.web3 import Web3
from pycoingecko import CoinGeckoAPI

gas_strategy = GasNowScalingStrategy("standard", "fast")

def get_prices(symbols):
    prices = []
    cg = CoinGeckoAPI()
    symbol_ids = list(filter(lambda c: c['symbol'].upper() in symbols, cg.get_coins_list()))
    print(symbol_ids)
    for s in symbols:
        coin = list(filter(lambda c: c['symbol'].upper()==s, symbol_ids))
        assert len(coin) == 1
        price = cg.get_price(coin[0]['id'], vs_currencies='usd')[coin[0]['id']]['usd']
        prices.append(str(price))
    print(prices)
    return prices

def set():
    symbols_str = ['BTC', 'HBTC', 'BOR', 'WETH', 'USDT', 'USDC', 'DAI', 'YFI', 'YFII', 'LINK', 'BAND', 'NEST']
    symbols = list(map(lambda s: Web3.toHex(text=s).ljust(66, '0'), symbols_str))
    # print(symbols)
    prices_str = get_prices(symbols_str)
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
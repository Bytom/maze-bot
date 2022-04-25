import requests
import getpass
import time
import sys

import eth_account
import os

from web3 import Web3
import json
import codecs
from collections import defaultdict

from bmc_sdk.constants import Direction
from bmc_sdk.bmc_client import BmcClient
from bmc_sdk.constants import EthNet
from bmc_sdk.bmc_client import ETH_ADDRESS

from bmc_sdk.log_service import log_service_manager
from bmc_sdk.maze_client import MazeClient
from bmc_sdk.util import load_json, save_json


class MazeQuery(object):
    @staticmethod
    def create_account(password, filepath):
        # 创建账户
        w3 = Web3()
        account = w3.eth.account.create()
        # private_key = account.key.hex()
        address = account.address
        keystore = account.encrypt(password)

        save_json(filepath, keystore)
        return {
            "status": "success",
            "data": {
                "address": address,
                "filepath": filepath
            }
        }

    @staticmethod
    def update_account():
        pass

    @staticmethod
    def query_account(network, address):
        client = MazeClient(address=address, private_key="", network=network)
        asset_data = client.get_balance_from_bmc_wallet()
        query_assets_contracts = [(dic["asset"]["symbol"].lower(),
                                   dic["asset"]["contract_address"].lower()) for dic in asset_data["data"]]
        balances = []

        contract_dic = {}
        for asset, contract_address in query_assets_contracts:
            contract_dic[asset] = contract_address

            if asset == "btm":
                contract_address = ETH_ADDRESS
            bal = client.get_token_balance(contract_address)
            balances.append({
                "asset": asset,
                "balance": bal
            })

        own_nfts = []
        data = client.query_erc721_by_address(address)
        for dic in data["data"]["tokens"]:
            erc721Address = dic["contract"]["id"]
            tokenId = dic["tokenId"]
            own_nfts.append({
                "erc721Address": erc721Address,
                "tokenId": tokenId,
                "id": f"{erc721Address}:{tokenId}"
            })
            # print(f"[query_account] now has nft: {contract_address}:{token_id}")
            # seller, deposit, current_price, started_at = client.get_auction(
            #     Web3.toChecksumAddress(contract_address), int(token_id))
            # print(f"[query_account] {seller}, {deposit}, {current_price}, {started_at}!")

        return {
            "status": "success",
            "data": {
                "balances": balances,
                "own-nfts": own_nfts
            }
        }

    @staticmethod
    def query_account_income(network, address):
        pass

    @staticmethod
    def buy_nft(network, erc721Address, tokenId, deposit, password, filepath):
        client = MazeClient.init_from_keystore(filepath, password, network)
        data = client.bid_auction(erc721Address, tokenId, deposit)
        log_service_manager.write_log(f"[buy_nft] data:{data}!")
        tx_hash = ""
        return {
            "status": "success",
            "data": {
                "txHash": tx_hash,
                "error": ""
            }
        }

    @staticmethod
    def adjust_nft_deposit(network, erc721Address, tokenId, amount, password, filepath):
        client = MazeClient.init_from_keystore(filepath, password, network)
        if amount > 0:
            data = client.increase_deposit(erc721Address, tokenId, amount)
        else:
            data = client.decrease_deposit(erc721Address, tokenId, abs(amount))
        log_service_manager.write_log(f"[adjust_nft_caution_money] data:{data}!")
        tx_hash = ""
        return {
            "status": "success",
            "data": {
                "txHash": tx_hash,
                "error": ""
            }
        }

    @staticmethod
    def apply_offer(network, erc721Address, tokenId, price, deposit, password, filepath):
        log_service_manager.write_log("[apply_offer]")
        client = MazeClient.init_from_keystore(filepath, password, network)
        deadline = int(time.time()) + 10 * 60
        data = client.apply_offer(erc721Address, tokenId, price, deposit, deadline)
        # client = MazeClient.init_from_keystore(filepath, password, network)
        # if amount > 0:
        #     data = client.apply_offer()
        # else:
        log_service_manager.write_log(f"[apply_offer] data:{data}!")

    @staticmethod
    def give_nft(network, erc721Address, tokenId, toAddress, password, filepath):
        log_service_manager.write_log("[give_nft]")

    @staticmethod
    def query_nft_detail(network, erc721Address, tokenId):
        log_service_manager.write_log("[query_nft_detail]")
        #
        # client = MazeClient.get_auction(erc721Address, tokenId)
        # log_service_manager.write_log("[query_nft_detail]")

    @staticmethod
    def query_author(network, address):
        pass

    @staticmethod
    def query_market_info(network, market_type, limit):
        pass

    @staticmethod
    def work(method, network, js_data):
        ret = {
            "status": "failed"
        }
        if method == "create-account":
            password = js_data["password"]
            filepath = js_data["filepath"]
            ret = MazeQuery.create_account(password, filepath)
        elif method == "update-account":
            ret = MazeQuery.update_account()
        elif method == "query-account":
            address = js_data["address"]
            ret = MazeQuery.query_account(network, address)
        elif method == "query-account-income":
            address = js_data["address"]
            ret = MazeQuery.query_account_income(network, address)
        elif method == "buy-nft":
            erc721Address = js_data["erc721Address"]
            tokenId = js_data["tokenId"]
            deposit = js_data["deposit"]
            password = js_data["password"]
            filepath = js_data["filepath"]
            ret = MazeQuery.buy_nft(network, erc721Address, tokenId, deposit, password, filepath)
        elif method == "adjust-nft-deposit":
            erc721Address = js_data["erc721Address"]
            tokenId = js_data["tokenId"]
            deposit = js_data["deposit"]
            password = js_data["password"]
            filepath = js_data["filepath"]
            ret = MazeQuery.adjust_nft_deposit(network, erc721Address, tokenId, deposit, password, filepath)
        elif method == "apply-offer":
            erc721Address = js_data["erc721Address"]
            tokenId = js_data["tokenId"]
            price = js_data["price"]
            deposit = js_data["deposit"]
            password = js_data["password"]
            filepath = js_data["filepath"]
            ret = MazeQuery.apply_offer(network, erc721Address, tokenId, price, deposit, password, filepath)
        elif method == "give-nft":
            erc721Address = js_data["erc721Address"]
            tokenId = js_data["tokenId"]
            toAddress = js_data["toAddress"]
            password = js_data["password"]
            filepath = js_data["filepath"]
            ret = MazeQuery.give_nft(network, erc721Address, tokenId, toAddress, password, filepath)

        elif method == "query-nft-detail":
            erc721Address = js_data["erc721Address"]
            tokenId = js_data["tokenId"]
            ret = MazeQuery.query_nft_detail(network, erc721Address, tokenId)

        elif method == "query-author":
            address = js_data["address"]
            ret = MazeQuery.query_author(network, address)

        elif method == "query-market-info":
            market_type = js_data["market_type"]
            limit = js_data["limit"]
            ret = MazeQuery.query_market_info(network, market_type, limit)

        print(ret)


if __name__ == "__main__":
    if len(sys.argv) > 3:
        method = sys.argv[1]
        network = sys.argv[2]
        msg = sys.argv[3]
        data = json.loads(msg)
        print(data)

        print(MazeQuery.work(method, network, data))

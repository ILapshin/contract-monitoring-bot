from web3 import Web3

from config import WEB3_PROVIDER_URL, CONTRACT_ADDRESS, ABI, DISTRIBUTOR_ADDRESS


w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)


def get_events(from_block=None):
    return contract.events.TotalDistribution().get_logs(
        fromBlock=from_block, toBlock="latest"
    )


def get_distributor_balance():
    return w3.eth.get_balance(DISTRIBUTOR_ADDRESS)


def get_block_timestamp(block_number):
    block = w3.eth.get_block(block_number)
    return block["timestamp"]

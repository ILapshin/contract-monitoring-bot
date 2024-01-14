import time

from web3 import Web3

from bot_service.message_template import MESSAGE_TEMPLATE
from database import crud
from web3_service import service
from config import DISTRIBUTOR_ADDRESS


def beautify_amount(amount):
    if amount == 0:
        return "0.00"

    amount = round(Web3.from_wei(amount, "ether"), 2)
    amount = str(amount)
    amount = amount.split(".")
    res = ""
    for i, digit in enumerate(amount[0]):
        res += digit
        if (len(amount[0]) - 1 - i) % 3 == 0:
            res += ","
    res = res[:-1] + "." + amount[1]
    return res


def parse_time_gap(gap_timestamp):
    now = time.time()
    diff = now - gap_timestamp
    return f"{int(diff // 3600)}h{int((diff % 3600) // 60)}m"


def prepare_message():
    day_events = crud.get_day_events()

    if not day_events:
        return MESSAGE_TEMPLATE.format(
            start_gap=">24h",
            end_gap=">24h",
            aix_processed="0.00",
            aix_distributed="0.00",
            eth_bought="0.00",
            eth_distributed="0.00",
            distributor_address=DISTRIBUTOR_ADDRESS,
            distributor_balance=beautify_amount(service.get_distributor_balance()),
        )

    return MESSAGE_TEMPLATE.format(
        start_gap=parse_time_gap(day_events[0].timestamp),
        end_gap=parse_time_gap(day_events[-1].timestamp),
        aix_processed=beautify_amount(
            sum([event.input_aix_amount for event in day_events])
        ),
        aix_distributed=beautify_amount(
            sum([event.distributed_aix_amount for event in day_events])
        ),
        eth_bought=beautify_amount(
            sum([event.swapped_eth_amount for event in day_events])
        ),
        eth_distributed=beautify_amount(
            sum([event.distributed_eth_amount for event in day_events])
        ),
        distributor_address=DISTRIBUTOR_ADDRESS,
        distributor_balance=beautify_amount(service.get_distributor_balance()),
    )

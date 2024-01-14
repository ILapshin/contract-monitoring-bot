from web3_service import service
from database import crud, schemas


def fetch_events():
    last_block = crud.get_last_block_number()

    from_block = last_block + 1 if last_block else 0

    raw_events = service.get_events(from_block=from_block)

    if not raw_events:
        return

    events = [
        schemas.EventSchema(
            transaction_hash=event["transactionHash"],
            block_number=event["blockNumber"],
            input_aix_amount=event["args"]["inputAixAmount"],
            distributed_aix_amount=event["args"]["distributedAixAmount"],
            swapped_eth_amount=event["args"]["swappedEthAmount"],
            distributed_eth_amount=event["args"]["distributedEthAmount"],
            timestamp=service.get_block_timestamp(event["blockNumber"]),
        )
        for event in raw_events
    ]

    crud.add_events(events)

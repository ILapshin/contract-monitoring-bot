from pydantic import BaseModel
from pydantic.types import StrictBytes


class EventSchema(BaseModel):
    transaction_hash: StrictBytes
    block_number: int
    input_aix_amount: int
    distributed_aix_amount: int
    swapped_eth_amount: int
    distributed_eth_amount: int
    timestamp: int

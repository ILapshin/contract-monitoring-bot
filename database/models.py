from sqlalchemy import Column, Integer, BINARY, BigInteger, Numeric
from sqlalchemy.types import LargeBinary

from database.database import Base


class Event(Base):
    __tablename__ = "event"

    transaction_hash = Column(LargeBinary, primary_key=True)
    input_aix_amount = Column(Numeric)
    distributed_aix_amount = Column(Numeric)
    swapped_eth_amount = Column(Numeric)
    distributed_eth_amount = Column(Numeric)
    block_number = Column(Integer)
    timestamp = Column(Integer)

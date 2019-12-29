from classes.chain import Chain
from classes.block import Block
from classes.data import Data

from datetime import datetime

chain = Chain()

data = Data("senderKey", "receiverKey", 123456, datetime)
block = Block(1, "genesisBlock", data)

chain.addNewBlock(block)
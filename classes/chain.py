from datetime import datetime
from .block import Block

class Chain:
    chain = []

    def __init__(self):
        self.createGenesisBlock()
    
    def createGenesisBlock(self):
        return Block(0, "genesisHash", datetime);

    def addNewBlock(self, block):
        self.chain.append(block)

    def isChainValid(self):
        for idx, block in self.chain:
            if block.isBlockValid() == False:
                return False

            if block.previousHash != chain[idx - 1].blockHash:
                return False

        return True
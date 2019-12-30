from datetime import datetime
from .block import Block

class Chain:
    chain = []

    def __init__(self):
        self.addNewBlock(
            self.createGenesisBlock()
        )
    
    def createGenesisBlock(self):
        return Block(0, None, None);

    def addNewBlock(self, block):
        self.chain.append(block)

    def isChainValid(self):
        for idx in range(len(self.chain)):
           if self.chain[idx].isBlockValid() == False:
               return False

           if self.chain[idx].previousHash != self.chain[idx - 1].blockHash:
               return False

        return True
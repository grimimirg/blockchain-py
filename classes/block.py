class Block:
    def __init__(self, index, previousHash, data):
        self.index = index
        self.blockHash = self.calculateBlockHash()
        self.previousHash = previousHash
        self.data = data
    
    def calculateBlockHash(self):
        return hash(
            self.data.senderKey +
            self.data.receiverKey +
            self.data.amount +
            self.data.timestamp
        )

    def isBlockValid(self):
        return self.blockHash == self.calculateBlockHash()
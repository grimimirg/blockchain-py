class Block:
    index = None
    blockHash = None
    previousHash = None
    data = None

    def __init__(self, index, previousHash, data):
        self.index = index
        self.data = data
        self.blockHash = self.calculateBlockHash()
        self.previousHash = previousHash
    
    def calculateBlockHash(self):
        if self.data is not None:
            return hash(
                self.data.senderKey
                + self.data.receiverKey
                + str(self.data.amount)
                + str(self.data.timestamp)
            )
        return None

    def isBlockValid(self):
        return self.blockHash == self.calculateBlockHash()
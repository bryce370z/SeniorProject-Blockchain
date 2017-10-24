import hashlib as hasher


class Block:
    index = None
    timestamp = None
    header = None
    data = None
    previous_hash = None

    def __init__(self, index, timestamp, header, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.header = header
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256(str(self.index).encode('utf-8') +
                            str(self.timestamp).encode('utf-8') +
                            str(self.header).encode('utf-8') +
                            str(self.data).encode('utf-8') +
                            str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

import hashlib as hasher


class Block:
    def __init__(self, index, timpstamp, data, previous_hash):
        self.index = index
        self.timestamp = timpstamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(string.encode('utf-8'))
        return sha.hexdigest()

from CS690.SnakeCoin.Block import Block
from datetime import datetime
import json


def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = f"Hey! I'm block {this_index}"
    return Block(this_index, this_timestamp, this_data, last_block.hash)


def form_data(sender, receiver, amount):
    return json.dumps({"from": sender, "to": receiver, "amount": amount})


def start():
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    num_blocks = 20

    for i in range(num_blocks):
        new_block = next_block(previous_block)
        blockchain.append(new_block)
        previous_block = new_block
        print(f"Block #{new_block.index} has been added!")
        print(f"Hash: {new_block.hash}\n")

if __name__ == '__main__':
    start()

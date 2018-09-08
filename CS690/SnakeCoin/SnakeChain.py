from CS690.SnakeCoin.Block import Block
from datetime import datetime
import json
from flask import Flask, request
import requests


node = Flask(__name__)

this_nodes_transactions = list()
blockchain = list()
peer_nodes = list()


def create_genesis_block():
    return Block(0, datetime.now(), {"proof-of-work": 9, "transaction": list()}, "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = f"Hey! I'm block {this_index}"
    return Block(this_index, this_timestamp, this_data, last_block.hash)


def form_data(sender, receiver, amount):
    return json.dumps({"from": sender, "to": receiver, "amount": amount})


def test_local_chain():
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    num_blocks = 20

    for i in range(num_blocks):
        new_block = next_block(previous_block)
        blockchain.append(new_block)
        previous_block = new_block
        print(f"Block #{new_block.index} has been added!")
        print(f"Hash: {new_block.hash}\n")


@node.route('/txion', methods=['POST'])
def transaction():
    if request.method != 'POST':
        return "Not a POST request\n"
    new_txion = request.get_json()
    this_nodes_transactions.append(new_txion)
    print("New transaction")
    print(f"From {new_txion['from']}")
    print(f"To {new_txion['to']}")
    print(f"Amount {new_txion['amount']}")
    return "Transaction submission successful\n"


def proof_of_work(last_proof):
    incrementor = last_proof + 1
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1
    return incrementor


@node.route('/mine', methods=['GET'])
def mine():
    global blockchain, this_nodes_transactions
    miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"

    last_block = blockchain[-1]
    last_proof = last_block.data['proof-of-work']
    proof = proof_of_work(last_proof)
    this_nodes_transactions.append(
        {"from": "network", "to": miner_address, "amount": 1}
    )
    new_block_data = {
        "proof-of-work": proof,
        "transaction": list(this_nodes_transactions)
    }
    new_block_timestamp = this_timestamp = datetime.now()
    this_nodes_transactions[:] = []
    mined_block = Block(
        last_block.index + 1,
        new_block_timestamp,
        new_block_data,
        last_block.hash
    )
    blockchain.append(mined_block)
    return json.dumps({
        "index": last_block.index + 1,
        "timestamp": str(new_block_timestamp),
        "data": new_block_data,
        "hash": last_block.hash
    }) + "\n"


@node.route('/blocks', methods=['GET'])
def get_blocks():
    def block_to_dict(block):
        return {
            "index": str(block.index),
            "timestamp": str(block.timestamp),
            "data": str(block.data),
            "hash": str(block.hash)
        }

    return json.dumps([block_to_dict(block) for block in blockchain])


def find_new_chains():
    other_chains = list()
    for node_url in peer_nodes:
        block = requests.get(node_url + "/blocks").content
        block = json.loads(block)
        other_chains.append(block)
    return other_chains


def consensus():
    global blockchain
    other_chains = find_new_chains()
    longest_chain = blockchain
    for chain in other_chains:
        if len(longest_chain) < len(chain):
            longest_chain = chain
    blockchain = longest_chain

if __name__ == '__main__':
    blockchain.append(create_genesis_block())
    node.run()

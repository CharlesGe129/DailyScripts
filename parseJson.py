with open("/Users/charles/charles/university/Big data/P1-CharlesGe129/input/log.txt", 'r') as f:
    a = f.read()
    f.close()

import json
a = '{"index": 1, "timestamp": "2018-09-07 17:21:50.010302", "data": {"proof-of-work": 18, "transaction": [{"from": "akjflw", "to": "fjlakdj", "amount": 3}, {"from": "network", "to": "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi", "amount": 1}]}, "hash": "ab3f63db14db3f78d5530b55fe4960bafb53724b906bbb2f188d8d2aa521ad74"}'
print(json.dumps(json.loads(a), indent=2))

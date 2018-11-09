class Bucket:
    def __init__(self, i, size):
        self.i = i
        self.size = size
        self.values = list()

    def append(self, num):
        self.values.append(num)

    def is_full(self):
        return len(self.values) >= self.size

    @staticmethod
    def com_bits(num, full_bits):
        rs = bin(num)[2:]
        while len(rs) < full_bits:
            rs = '0' + rs
        return rs

    def split(self, full_bits):
        rs = [Bucket(self.i+1, self.size), Bucket(self.i+1, self.size)]
        for num in self.values:
            value_bin_str = Bucket.com_bits(num, full_bits)
            # print(f"num={num}, value={value_bin_str}, i={self.i}")
            if value_bin_str[self.i] == '1':
                rs[1].append(num)
            else:
                rs[0].append(num)
        # print(f"Split Bucket {self} to\nBucket[0]: {rs[0]}\nBucket[1]: {rs[1]}")
        return rs

    def __str__(self):
        return f"i={self.i}, values={str(self.values)}"


class ExtHashTable:
    def __init__(self, full_bits, bucket_size, hash_func):
        self.i = 1
        self.full_bits = full_bits
        self.bucket_size = bucket_size
        self.hash_func = hash_func
        self.buckets = dict()
        for index in range(2):
            self.buckets[index] = Bucket(1, bucket_size)

    def add(self, num_str):
        num = int(num_str, 2)
        value_bin_str = Bucket.com_bits(self.hash_func(num), self.full_bits)
        print(f"Insert {num}={value_bin_str}")
        self.check_full(value_bin_str)
        value_bin = int(value_bin_str[:self.i], 2)
        # print(f"bin[:{self.i}]={value_bin}")
        self.buckets[value_bin].append(num)
        print(str(self))

    def check_full(self, value_str):
        value_bin = int(value_str[:self.i], 2)
        # print(f"check str={value_str}, value={value_bin}")
        bucket = self.buckets[value_bin]
        if not bucket.is_full():
            return
        # Expand
        split_buckets = bucket.split(self.full_bits)
        if bucket.i == self.i:
            self.expand_i()
            self.buckets[2*value_bin] = split_buckets[0]
            self.buckets[2*value_bin + 1] = split_buckets[1]
        else:
            adjust_start = value_bin
            while adjust_start >= 0 and self.buckets[adjust_start] is bucket:
                adjust_start -= 1
            adjust_start += 1
            adjust_end = value_bin
            while adjust_end < len(self.buckets) and self.buckets[adjust_end] is bucket:
                adjust_end += 1
            adjust_mid = (adjust_start + adjust_end)//2
            # print(f"adjust_start={adjust_start}, end={adjust_end}, mid={adjust_mid}")
            for j in range(adjust_start, adjust_mid):
                self.buckets[j] = split_buckets[0]
            for j in range(adjust_mid, adjust_end):
                self.buckets[j] = split_buckets[1]
        # print(str(self))
        self.check_full(value_str)

    def expand_i(self):
        buckets = dict()
        # print('expand_i')
        for index in range(2**self.i):
            # print(f"new[{index*2}] = new[{index*2 + 1}] = old[{index}]")
            buckets[index*2] = self.buckets[index]
            buckets[index*2 + 1] = self.buckets[index]
        self.i += 1
        self.buckets = buckets

    def __str__(self):
        rs = f"i={self.i}, bits={self.full_bits}, bucket_size={self.bucket_size}"
        j = 0
        while j < len(self.buckets):
            keys = [j]
            bucket = self.buckets[j]
            while j + 1 < len(self.buckets) and self.buckets[j+1] is bucket:
                j += 1
                keys.append(j)
            j += 1
            rs += f"\n{', '.join([bin(key)[2:] for key in keys])} ----> {str(bucket)}"
        return rs + '\n'


def hash_func_06(num):
    return num


def hash_func_08(num):
    return num % 8


def test():
    a = ExtHashTable(6, 3, hash_func_06)
    a.add('0b010000')
    a.add('0b011010')
    a.add('0b111100')
    a.add('0b001110')
    a.add('0b010111')
    a.add('0b011010')
    assert a.buckets[0] is a.buckets[1]
    assert a.buckets[0].i == 2
    assert a.buckets[0].values == [14]
    assert a.buckets[2].i == 3
    assert a.buckets[2].values == [16, 23]
    assert a.buckets[3].i == 3
    assert a.buckets[3].values == [26, 26]
    assert a.buckets[4] is a.buckets[5] is a.buckets[6] is a.buckets[7]
    assert a.buckets[5].i == 1
    assert a.buckets[5].values == [60]


def p06():
    a = ExtHashTable(4, 2, hash_func_06)
    nums = ['0b1111', '0b1110', '0b1101', '0b1100', '0b1011', '0b1010', '0b1001', '0b1000',
            '0b0111', '0b0110', '0b0101', '0b0100', '0b0011', '0b0010', '0b0001', '0b0000', ]
    [a.add(each) for each in nums]


def p08():
    a = ExtHashTable(3, 3, hash_func_08)
    nums = ['0b10', '0b11', '0b101', '0b111', '0b11', '0b1', '0b11', '0b111', '0b101', '0b111']
    [a.add(each) for each in nums]

# test()
# p06()
p08()

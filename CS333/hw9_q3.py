TR = 10000
TS = 5000


def cal_join_size(v1, v2):
    b = min(v1, v2)
    t1 = TR / v1
    t2 = TS / v2
    print(f"If V(R, b)={v1}, V(S, b)={v2}")
    print(f"min(v1, v2)={b}, t1={t1}, t2={t2}")
    if t1 == t2 == 1:
        return b
    elif t1 == 1 or t2 == 1:
        return max(t1, t2) * b
    else:
        return t1 * t2 * b


print(cal_join_size(40, 10))
print(cal_join_size(900, 1000))
print(cal_join_size(1, 2))
print(cal_join_size(5000, 2000))

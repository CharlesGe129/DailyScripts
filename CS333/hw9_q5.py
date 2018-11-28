def cal_join_size(t1, t2, v1, v2):
    return t1*t2/v1/v2


def cal_sum_size(r, s, t):
    print(f"r={r}, s={s}, t={t}")
    r_s = cal_join_size(r, s, 200, 200)
    r_t = cal_join_size(r, t, 100, 200)
    s_t = cal_join_size(s, t, 50, 1)
    print(f"R&S={r_s}, R&T={r_t}, S&T={s_t}, sum={r_s+r_t+s_t}\n")


def construct_db(r, s, t):
    with open('r.txt', 'w') as f1, open('s.txt', 'w') as f2, open('t.txt', 'w') as f3:
        pass
    i = 1
    j = 1
    k = 1
    with open('r.txt', 'a') as f1, open('s.txt', 'a') as f2, open('t.txt', 'a') as f3:
        for a in range(r):
            f1.write(f"{i},{j},{k}\n")
            i = i + 1 if i != 50 else 1
            j = j + 1 if j != 100 else 1
            k = k + 1 if k != 200 else 1
        for a in range(s):
            f2.write(f"{i},{j},{k}\n")
            i = i + 1 if i != 200 else 1
            j = j + 1 if j != 20 else 1
            k = k + 1 if k != 40 else 1
        for a in range(t):
            f3.write(f"{i},{j},{k}\n")
            i = i + 1 if i != 100 else 1
            j = j + 1 if j != 50 else 1
            k = k + 1 if k != 80 else 1



# cal_sum_size(200000, 900, 400)
# cal_sum_size(100000, 200, 500)
# cal_sum_size(1000, 500, 100)

print(10000*5000/40)
print(10000*5000/1000)
print(10000*5000/2)
print(10000*5000/5000)

# construct_db(5000, 1000, 4000)
cal_sum_size(5000, 1000, 4000)
# construct_db(200, 2000, 5000)
cal_sum_size(200, 2000, 5000)
# construct_db(10000, 1000, 100)
cal_sum_size(10000, 1000, 100)

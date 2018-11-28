precision = 4


def square_root(target: float, func):
    if target <= 0:
        return "Error"
    elif 0 < target < 1:
        return func(target, target / 2, target) if (target / 2) ** 2 > target else func(target, 0, target / 2)
    else:
        return func(target, target / 2, target) if (target/2) ** 2 < target else func(target, 0, target / 2)


def search(target, low, high):
    # low ** 2 < target < high ** 2
    print(f"target={target}, low={low}, high={high}")
    if round(low, precision) == round(high, precision):
        return round(low, precision)
    mid = (low + high)/2
    return search(target, mid, high) if mid ** 2 < target else search(target, low, mid)


def search_loop(target, low, high):
    while True:
        print(f"target={target}, low={low}, high={high}")
        if round(low, precision) == round(high, precision):
            return round(low, precision)
        mid = (low + high) / 2
        if mid ** 2 < target:
            low = mid
        else:
            high = mid


print(square_root(987654321, search))

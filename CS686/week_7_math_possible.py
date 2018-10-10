def math_possible(numbers, target):
    # print(f"try, {target},  {numbers}")
    if not numbers and target == 0:
        return True
    elif not numbers:
        return False

    numbers = numbers.copy()
    pop_num = numbers[0]
    numbers.pop(0)
    if math_possible(numbers, target + pop_num):
        print(f"{target+pop_num}-{pop_num}={target}")
        return True
    if math_possible(numbers, target - pop_num):
        print(f"{target-pop_num}+{pop_num}={target}")
        return True
    if math_possible(numbers, target * pop_num):
        print(f"{target*pop_num}/{pop_num}={target}")
        return True
    if math_possible(numbers, target / pop_num):
        print(f"{target/pop_num}*{pop_num}={target}")
        return True
    return False

print(math_possible([1, 2], 5))
print(math_possible([2, 10], 5))
print(math_possible([2, 3, 4, 5], 29))

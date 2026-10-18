import random

def shuffle(lst):
    result = []
    while len(lst) > 0:
        e = random.choice(lst)
        result.append(e)
        lst.remove(e)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("섞기 전: ", numbers)
print("섞은 후: ", shuffle(numbers.copy()))
import math, time


def og_prime(goto):
    prime_array = [2, 3]
    ct = 2
    test_num = 5
    is_prime = True
    k = 0

    begin_time = time.time()

    while ct < goto:
        sqrt = math.sqrt(test_num)  # The improvement!
        while prime_array[k] <= sqrt and is_prime:
            if test_num % prime_array[k] == 0:
                is_prime = False
            k += 1
        if is_prime:
            prime_array.append(test_num)
            ct = ct + 1
        if (test_num + 1) % 6 == 0:
            test_num = test_num + 2
        else:
            test_num = test_num + 4
        is_prime = True
        k = 0

    delta_time = time.time() - begin_time
    return delta_time

def new_prime(goto):
    prime_array = [2, 3]
    ct = 2
    test_num = 5
    is_prime = True
    k = 0

    begin_time = time.time()

    while ct < goto:
        sqrt = math.sqrt(test_num)
        c_prime = prime_array[k]
        while c_prime <= sqrt and is_prime:
            if test_num % c_prime == 0:
                is_prime = False
            k += 1
            c_prime = prime_array[k]
        if is_prime:
            prime_array.append(test_num)
            ct = ct + 1
        if (test_num + 1) % 6 == 0:
            test_num = test_num + 2
        else:
            test_num = test_num + 4
        is_prime = True
        k = 0

    delta_time = time.time() - begin_time
    return delta_time


def compare_time_avg(_runs, func1, func2, param):
    t1, t2 = [], []
    for i in range(_runs):
        t1.append(func1(param))
        t2.append(func2(param))

    return sum(t1) / len(t1), sum(t2) / len(t2)

def time_print(seconds):
    hours, rem = divmod(seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))


count = int(input("Input count: "))

# time_print(new_prime(count))
runs = int(input("Input runs: "))

x, y = compare_time_avg(runs, og_prime, new_prime, count)

print("OG:")
time_print(x)
print("NEW:")
time_print(y)

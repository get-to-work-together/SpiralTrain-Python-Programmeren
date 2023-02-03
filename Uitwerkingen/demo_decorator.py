import time

def log(f):
    def inner(*arg):
        print(f'Function {f.__name__} called with arguments {arg}.')
        t0 = time.time()
        returned_value = f(*arg)
        time.sleep(0)
        t1 = time.time()
        print('Done. Duration: ', t1 - t0)
        return returned_value
    return inner


@log
def telop_maal_2(x, y):
    return 2 * (x + y)

@log
def telop_maal_5(x, y):
    return 6 * (x + y)

print(telop_maal_2(5, 7))
print(telop_maal_5(5, 7))
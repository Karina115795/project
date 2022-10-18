def _min(arr):
    min_ = arr[0]
    for i in arr:
        if i < min_:
            min_ = i
    return min_


def _max(arr):
    max_ = arr[0]
    for i in arr:
        if i > max_:
            max_ = i
    return max_


def _sum(arr):
    sum_ = 0
    for i in arr:
        sum_ += i
    return sum_


def _mult(arr):
    mult_ = 1
    for i in arr:
        mult_ *= i
    return mult_


def read(name):
    f = open(name)
    array = list(map(int, f.readline().split()))
    return array


def main():
    arr_ = read('text_2.txt')
    return _min(arr_), _max(arr_), _mult(arr_), _sum(arr_),


if __name__ == '__main__':
    print(*main())

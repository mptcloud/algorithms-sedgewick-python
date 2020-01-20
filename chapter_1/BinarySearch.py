import sys

class BinarySearch:

    @staticmethod
    def index_of(key, lst):
        assert isinstance(key, int)
        assert isinstance(lst, (list, tuple))

        low, high = 0, len(lst) - 1

        while low <= high:
            mid = int((high + low) / 2)
            if lst[mid] == key:
                return mid
            elif lst[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == '__main__':
    with open('num_whitelist.txt') as f:
        whitelist = [[int(x) for x in line.split()] for line in f]

        whitelist.sort()

        while True:
            input = int(input())
            if input == '':
                break
            else:
                key = input
                if BinarySearch.index_of(key, whitelist) == -1:
                    print(str(key) + '\n')


import os
import sys

class BinarySearch:

    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

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
    WHITELIST_PATH = os.path.join(BinarySearch.ROOT_PATH, 'libs', 'num_whitelist.txt')
    INPUT_PATH = os.path.join(BinarySearch.ROOT_PATH, 'libs', sys.argv[1])

    with open(INPUT_PATH) as f:
        contents = f.read()
    print(contents)

    with open(WHITELIST_PATH) as f:
        whitelist_2d = [[int(x) for x in line.split()] for line in f]
        whitelist = [x for sub_lst in whitelist_2d for x in sub_lst]

        whitelist.sort()

        # while True:
        #     program_input = int(input())
        #     if program_input == '':
        #         break
        #     else:
        #         key = program_input
        #         if BinarySearch.index_of(key, whitelist) == -1:
        #             print(str(key))


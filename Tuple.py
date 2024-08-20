if __name__ == '__main__':
    n = int(input())  # read the number of elements in the tuple
    integer_list = map(int, input().split())  # read n space-separated integers and convert them to an integer list
    t = tuple(integer_list)  # convert the integer list to a tuple
    print(hash(t))  # print the hash of the tuple

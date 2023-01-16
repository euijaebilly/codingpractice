def dupchecker(count, k):
    result = False
    for i in range(len(count)):
        for j in range(i, len(count)):
            if i != j and count[i] == count[j] and abs(i - j) <= k:
                result = True

    return result

if __name__ == '__main__':
    count = [int(i) for i in input("nums = ").split(',')]
    k = int(input("k = "))
    print(dupchecker(count, k))


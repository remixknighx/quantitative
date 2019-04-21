# -*- coding: utf-8 -*-


def maxDifference(a):
    max_diff = -1
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] - a[i] > max_diff:
                max_diff = a[j] - a[i]
    return max_diff


if __name__ == '__main__':
    arr = [7, 2, 3, 10, 2, 4, 8, 1]
    print(maxDifference(arr))

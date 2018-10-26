'''
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.
For example, there are n = 7 socks with colors arr = [1,2,1,2,3,2,1] . There is one pair of color 1 and one of color 2.
There are three odd socks left, one of each color. The number of pairs is 2 .
Write code for this problem.
'''


from __future__ import print_function


def main():
    n = int(input().strip())
    c = list(map(int, input().strip().split(' ')))
    pairs = 0
    c.sort()
    c.append('-1')
    i = 0
    while i < n:
        if c[i] == c[i + 1]:
            pairs = pairs + 1
            i += 2
        else:
            i += 1
    print(pairs)


if __name__ == '__main__':
    main()

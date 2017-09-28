"""

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

"""
import collections

from copy import deepcopy


def pandigital():
    sum = 0
    products = {}
    for i in range(1, 2000):
        used_digits = collections.defaultdict(bool)
        temp = i
        skip = False
        while temp != 0:
            if temp % 10 == 0 or used_digits[temp % 10]:
                skip = True
                temp = 0
            else:
                used_digits[temp % 10] = True
                temp //= 10

        if skip:
            continue

        for j in range(1, 2000):
            if i == j:
                continue

            skip = False
            temp_used_digits = deepcopy(used_digits)
            temp = j
            while temp != 0:
                if temp % 10 == 0 or temp_used_digits[temp % 10]:
                    skip = True
                    temp = 0
                else:
                    temp_used_digits[temp % 10] = True
                    temp //= 10

            if skip:
                continue


            product = i * j

            temp = product
            while temp != 0:
                if temp % 10 == 0 or temp_used_digits[temp % 10]:
                    skip = True
                    temp = 0
                else:
                    temp_used_digits[temp % 10] = True
                    temp //= 10

            if skip:
                continue

            if len(temp_used_digits.keys()) is 9 and products.get(product, None) is None:
                print(i, "*", j, "=", product)
                products[product] = product
                sum += product


    return sum


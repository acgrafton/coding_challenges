"""


Your quirky boss collects rare, old coins...

They found out you're a programmer and asked you to solve something they've been wondering for a long time.

Write a function that, given:

    an amount of money
    a list of coin denominations

computes the number of ways to make the amount of money with coins of the available denominations.

Example: for amount=4 (4¢) and denominations=[1,2,3] (1¢, 2¢ and 3¢), 
your program would output 4—the number of ways to make 4¢ with those denominations:

    1¢, 1¢, 1¢, 1¢
    1¢, 1¢, 2¢
    1¢, 3¢
    2¢, 2¢

Pseudocode

init count of denominations
for each number in denom:
    init remainder of dividing amount by the number
        if the remainder == 0:
            increment count
        else:
            divide next number in denom
                if the remainder == 0:
                    increment count
                else:
                    try the next one..

base case
if len(denom) == 1 and amount divides evenly by the denom
    return 1

"""

import unittest

def make_change(amount, denominations, index, memo={}):
    if amount == 0:
        return 1
    if index >= len(denominations):
        return 0
    key = f'{amount}-{index}'
    if key in memo:
        return memo[key]
    amount_with_denom = 0
    poss = 0
    while amount_with_denom <= amount:
        remaining = amount - amount_with_denom
        poss += make_change(remaining, denominations, index + 1)
        amount_with_denom += denominations[index] 
    memo[key] = poss
    return poss


def change_possibilities(amount, denominations):
    return make_change(amount, denominations, 0)


# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    # def test_change_for_one_dollar(self):
    #     actual = change_possibilities(100, (1, 5, 10, 25, 50))
    #     expected = 292
    #     self.assertEqual(actual, expected)


unittest.main(verbosity=2)
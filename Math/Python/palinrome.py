'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

'''


def is_palindrome(x):
    num = str(x)
    if num == num[::-1]:
        return True
    else:
        return False


def check_palindrome_better(number):
    rev = 0
    original_num = number

    while number > 0:
        last_digit = number % 10
        rev = rev * 10 + last_digit
        number //= 10

    return original_num == reversed


if __name__ == "__main__":
    num = 121
    print(is_palindrome(num))
    print(check_palindrome_better(num))

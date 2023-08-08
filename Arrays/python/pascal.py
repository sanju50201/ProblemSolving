""" 
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]

"""


def get_row(rowIndex):
    row = [1]
    for i in range(1, rowIndex + 1):
        next_row = [1]
        for j in range(1, i):
            next_row.append(row[j - 1] + row[j])
        next_row.append(1)
        row = next_row
    return row


if __name__ == "__main__":
    rowIndex = 3
    print(get_row(rowIndex))

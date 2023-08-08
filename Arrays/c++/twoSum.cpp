#include <iostream>
#include <unordered_set>
using namespace std;

int twoSum(int arr[], int target)
{
    int n = sizeof(arr) / sizeof(arr[0]);
    unordered_set<int> numToIndex;
    for (int i = 0; i < n; i++)
    {
        int complement = target - i;
        if (numToIndex.find(complement) != numToIndex.end())
        {
            return i;
        }
    }
}

int main()
{
}
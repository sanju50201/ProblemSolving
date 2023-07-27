#include <iostream>
#include <limits>
using namespace std;

int reverse(int x)
{
    int rev = 0;

    while (x != 0)
    {
        if (rev > numeric_limits<int>::max() / 10 || rev < numeric_limits<int>::min())
        {
            return 0;
        }
        rev = rev * 10 + x % 10;
        x = x / 10;
    }
    return rev;
}

int main()
{
    int num;
    cout << "Enter an Integer:\n";
    cin >> num;
    cout << "Reverse is: " << reverse(num) << "\n";
    return 0;
}
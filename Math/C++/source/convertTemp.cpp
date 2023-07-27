#include <iostream>
#include <iomanip>
#include <sstream>
using namespace std;

string convertTemp(float celsius)
{

    float kelvin = celsius + 273.15;
    float fahrenheit = (celsius * 1.80 + 32.00);

    stringstream stream;
    stream << fixed << setprecision(5) << "Kelvin: " << kelvin << "Fahrenheit: " << fahrenheit;
    return stream.str();
}

int main()
{
    float celsius;
    cout << "Enter Temp in Celsius: "
         << "\n";
    cin >> celsius;
    cout << convertTemp(celsius) << "\n";
    return 0;
}
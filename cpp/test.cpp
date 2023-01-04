#include <iostream>
#include <iomanip>

using namespace std;

string operator * (string a, unsigned int b) {
    string output = "";
    while (b--) {
        output += a;
    }
    return output;
}

int main()
{
    string gwia = "*";
    string spaw = " ";
    int last = 1;
    int wysokosc = 5;
    cout << "Podaj wysokość: ";
    cin >> wysokosc;
    for (int i = 1; i <= wysokosc; i++){
        if (i != 1)
            last+=2;
        int ilo2 = wysokosc-i;
        cout << spaw * ilo2 << gwia*last << "\n";
    }

    return 0;
}
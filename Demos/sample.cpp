#include <iostream>
using namespace std;

int main() {
    cout << "Hello world";
    int a = 5; // this is an integer
    cout << a << '\n';
    a = "Hello"; // this is not allowed since we're assigning a string to an int variable
    cout << a << '\n';
}
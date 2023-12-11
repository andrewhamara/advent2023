#include <fstream>
#include <iostream>

using std::cout, std::endl, std::ifstream, std::string;

int main() {
  ifstream in("input.txt");

  long long total = 0;
  string line;

  while (getline(in, line)) {
    int current = 0;
    for (char c : line) {
      if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' ||
          c == '5' || c == '6' || c == '7' || c == '8' || c == '9')
      {
        current += (int(c) - '0') * 10;
        break;
      }
    }
    int length = line.length() - 1;
    while (length > -1) {
      char c = line[length];
      if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' ||
          c == '5' || c == '6' || c == '7' || c == '8' || c == '9')
      {
        current += int(c) - '0';
        break;
      }
      length--;
    }
    total += current;
  }
  cout << total << endl;
  return 0;
}

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <sstream>
#include <iterator>

using std::cout; using std::endl; using std::string; using std::ifstream;
using std::vector; using std::istringstream;

vector<int> parse(string s) {

  istringstream ss(s);
  vector<string> vals;
  string cur;

  vector<int> result;

  while (getline(ss, cur, ' '))
    vals.push_back(cur);

  vals[1].pop_back();
  int gameNumber = std::stoi(vals[1]);
  int maxReds = -1, maxBlues = -1, maxGreens = -1;
  bool valid = true;

  for (int i = 2; i < vals.size(); i += 2) {
    int count = std::stoi(vals[i]);
    int reds = 0, blues = 0, greens = 0;
    string color = vals[i+1];
    switch (color[0]) {
      case 'r':
        maxReds = std::max(maxReds, count);
        reds += count;
        break;
      case 'b':
        maxBlues = std::max(maxBlues, count);
        blues += count;
        break;
      case 'g':
        maxGreens = std::max(maxGreens, count);
        greens += count;
        break;
    }

    if (reds > 12 || greens > 13 || blues > 14) {
      valid = false;
    }
    if (color[color.size() - 1] == ';') {
      reds = 0; blues = 0; greens = 0;
    }
  }

  if (valid) {
    result.push_back(1);
  } else {
    result.push_back(0);
  }
  result.push_back(gameNumber);
  result.push_back(maxBlues);
  result.push_back(maxGreens);
  result.push_back(maxReds);

  return result;
}


int main() {
  ifstream in("input.txt");

  int total = 0;
  int totalMaxPower = 0;
  string line;
  while (getline(in, line)) {
    vector<int> cur = parse(line);
    if (cur[0] == 1) { // meaning that the game was valid
      total += cur[1];
    }
    totalMaxPower += (cur[2] * cur[3] * cur[4]);
  }
  cout << total << endl << totalMaxPower << endl;
  return 0;
}


CXX = g++

CXXFLAGS = -std=c++20 -Wall -Wextra -Wpedantic -Werror -O3 -g -Iinclude

SRC = solution.cpp

EXE = exe

all: $(EXE)

$(EXE): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(EXE)

clean:
	rm -f $(EXE)
	rm -rf *.dSYM

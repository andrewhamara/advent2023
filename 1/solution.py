def main():
    with open('input.txt') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            cur = ''
            for char in line:
                if char.isdigit():
                    cur += char
                    break
            for char in reversed(line):
                if char.isdigit():
                    cur += char
                    break
            total += int(cur)
    print(total)


if __name__ == "__main__":
    main()

def negatives_of(lines):
    return sum(1 for line in lines if float(line) < 0)

if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as file:
        print(negatives_of(file))
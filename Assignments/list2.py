def main():
    fname = input("Enter file name: ")
    if len(fname) < 1: fname = "mbox-short.txt"

    fh = open(fname)
    count = 0
    for line in fh:
        line = line.rstrip()
        if line.startswith("From "):
            lineList = list()
            lineList = line.split()
            print(lineList[1])
            count += 1
    print("There were", count, "lines in the file with From as the first word")

if __name__ == "__main__":
    main()

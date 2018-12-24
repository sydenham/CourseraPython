def main():
    fname = input("Enter file name: ")
    fh = open(fname)
    lst = list()
    for line in fh:
        lineList = list()
        lineList = line.split()
        for word in lineList:
            if word not in lst:
                lst.append(word)
    lst.sort()
    print(lst)

if __name__ == "__main__":
    main()
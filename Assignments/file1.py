def main():
    fname = input("Enter file name: ")
    fh = open(fname)
    file = fh.read()
    print(file.upper().rstrip())

if __name__ == "__main__":
    main()
def main():
    # Use the file name mbox-short.txt as the file name
    fname = input("Enter file name: ")
    fh = open(fname)
    countLines = 0
    addUp = float(0)
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"): continue
        countLines += 1
        addUp += float(line[19:].lstrip())
    print("Average spam confidence:", addUp / countLines)


if __name__ == "__main__":
    main()
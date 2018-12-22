def main():
    fhandle = open(r"C:\Users\Admin\Desktop\mbox-short.txt")
    count = dict()
    for each_line in fhandle:
        if each_line.startswith("From "):
            word = each_line.split()[1]
            count[word] = count.get(word, 0) + 1
    bigcount = None
    bigword = 0
    for k, v in count.items():
        if bigcount is None or v > bigcount:
            bigcount = v
            bigword = k
    print(bigword, bigcount)



if __name__ == "__main__":
    main()
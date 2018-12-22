def main():
    handle = open(r"C:\Users\Admin\Desktop\mbox-short.txt")
    counts = dict()
    for line in handle:
        if line.startswith("From "):
            hour = line.split()[5].split(":")[0]
            counts[hour] = counts.get(hour, 0) + 1
    lst = sorted([ (k, v) for k, v in counts.items()])
    for k, v in lst:
        print(k, v)


if __name__ == "__main__":
    main()
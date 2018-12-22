import  re

def main():
    fhandle = open(r'C:\Users\User\Desktop\regex_sum_167590.txt')
    total = 0
    # for line in fhandle:
    #     numbers = re.findall('[0-9]+', line)
    #     if numbers is None: continue
    #     for i in numbers:
    #         total += int(i)
    # print(total)
    print(sum([ int(i) for i in re.findall('[0-9]+',fhandle.read())] ) )
if __name__ == "__main__":
    main()
def count(s):
    zeros =[i for i in s if i == "0"]
    ones = [i for i in s if i == "1"]
    # for i in bits:
    #     if i == "0":
    #         zeros.append(i)
    #     else:
    #         ones.append(i)
    return min(len(zeros), len(ones))
    # if len(zeros) < len(ones):
    #     s = s.replace("0", "1")
    #     return len(zeros)
    # else:
    #     s = s.replace("1", "0")
    #     return len(ones)

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4

bits = "1111"
zeros =[]
ones = []
for i in bits:
    if i == "0":
        zeros.append(i)
    else:
        ones.append(i)

if len(zeros) < len(ones):
    bits = bits.replace("0", "1")
    print(len(zeros))
else:
    bits = bits.replace("1", "0")
    print(len(ones))

print()
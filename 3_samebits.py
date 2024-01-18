def count(s):
    zeros =[i for i in s if i == "0"]
    ones = [i for i in s if i == "1"]
    return min(len(zeros), len(ones))
    

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4

# I forgot about the count method for strings
# no need to creat two lists with that

# Course Solution ---
    

# def count(s):
#     return min(s.count("0"), s.count("1"))
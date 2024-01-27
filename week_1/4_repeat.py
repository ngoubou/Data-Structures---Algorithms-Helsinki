# def find(s):
#     return

# if __name__ == "__main__":
#     print(find("aaa")) # 1
#     print(find("abcd")) # 4
#     print(find("abcabcabcabc")) # 3
#     print(find("aybabtuaybabtu")) # 7
#     print(find("abcabca")) # 7

s = "abcabcabcabc"


total = []
for i in range(len(s)):
    count = 1
    for j in range(i+1, len(s)):
        if s[i] == s[j]: #sourcery skip
            pass
        else:
            count += 1
    total.append(count)

print(max(total))
print(count)

## Not completed yet! TBD
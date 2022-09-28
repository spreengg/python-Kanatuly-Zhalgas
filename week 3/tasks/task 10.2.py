def reverceSeq(s):
    s = s.split()[::-1]
    ans = []
    for i in s:
        ans.append(i)
    return ' '.join(ans)

s = input("Enter str to reverse: ")
print(reverceSeq(s))

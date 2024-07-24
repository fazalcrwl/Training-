# List of strings
strs = ["flower", "flow", "flight"]

r = ""
if not strs:
    print(r)
else:
    
    for i in range(len(strs[0])):
        count = 0
    
        for j in range(len(strs)):
            if i < len(strs[j]) and strs[j][i] == strs[0][i]:
                count += 1
            else:
                break
    
        if count == len(strs):
            r += strs[0][i]
        else:
            break

    print(r)

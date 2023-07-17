def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return prefix
        prefix += char

    return prefix

string1 = ["flower", "flow", "flight"]
print(longest_common_prefix(string1))

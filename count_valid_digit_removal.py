def solution(s, t):
    count = 0

    for i in range(len(s)):
        if s[i].isdigit():
            removed_s = s[:i] + s[i + 1:]

            if removed_s < t:
                count += 1
    
    for i in range(len(t)):
        if t[i].isdigit():
            removed_t = t[:i] + t[i + 1:]
            
            if s < removed_t:
                count += 1

    return count


print(solution("ab12c", "1zz456"))
print(solution("ab12c", "ab24z"))
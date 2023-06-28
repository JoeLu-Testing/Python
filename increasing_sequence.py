def solution(sequence):
    removalCount = 0
    n = len(sequence)
    for i in range(1, n):
        if sequence[i] <= sequence[i - 1]:
            removalCount += 1
            if removalCount > 1:
                return False
            if i > 1 and sequence[i] <= sequence[i - 2]:
                if i < n - 1 and sequence[i + 1] <= sequence[i - 1]:
                    return False
    return True


sequence1 = [1, 3, 2, 1]
print(solution(sequence1))

sequence2 = [1, 3, 2]
print(solution(sequence2))

sequence3 = [2, 3, 1]
print(solution(sequence3))

sequence4 = [3, 2, 4]
print(solution(sequence4))  

sequence5 = [3, 6, 5, 8, 10, 20, 15]
print(solution(sequence5))

sequence6 = [1, 2, 1, 2]
print(solution(sequence6))
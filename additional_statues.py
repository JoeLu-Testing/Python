def solution(statues):
    statues.sort()
    additional_statues = 0

    for i in range(len(statues) - 1):
        diff = statues[i + 1] - statues[i]
        if diff > 1:
            additional_statues += diff - 1

    return additional_statues

statues = [6, 2, 3, 7]
print(solution(statues))


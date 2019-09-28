def solution(brown, red):
    if red == 1:
        return [3,3]
    for i in range(1, red):
        R = i
        if red % R == 0:
            C = red // R
        else:
            continue

        c = 1
        while True:
            if brown == (R + (2 * c)) * (C + (2 * c)) - red:
                return [C + (2 * c), R + (2 * c)]
            if (R + (2 * c)) * (C + (2 * c)) - red > brown:
                break
            c += 1

print(solution(8,1))
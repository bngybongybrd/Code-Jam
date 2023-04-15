def untie(case_no, c): 
    min = 0
    if all(i == c[0] for i in c):
        c += c[0]
    elif c[0] == c[-1]:
        for i in range(len(c)-1, 0, -1):
            if c[i-1] != c[-1]:
                c = c[i:] + c[:i]
                break
    counter = 1
    for i in range(len(c)-1):
        if c[i] == c[i+1]:
            counter += 1
        else:
            min += counter // 2
            counter = 1
    min += counter // 2
    output = f'Case #{case_no}: {min}'
    return output

cases = int(input())
ans = []
for i in range(cases):
    c = input()
    ans.append(untie(i+1, c))
for i in ans:
    print(i)
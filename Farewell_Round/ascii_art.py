import math

def ascii_art(test_no, n):
    a = n // 26
    count = 0
    iteration = 1
    while count < a:
        if count+iteration > a:
            break
        count += iteration
        iteration += 1
    left_over = n - count*26
    char = math.ceil(left_over/iteration)
    if char == 0:
        output = f'Case #{test_no}: Z'
    else:  
        output = f'Case #{test_no}: {chr(64+char)}'
    return output
         
cases = int(input())
ans = []
for i in range(cases):
    n = int(input())
    ans.append(ascii_art(i+1, n))
for i in ans:
    print(i)
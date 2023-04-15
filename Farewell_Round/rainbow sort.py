def rainbow_sort(test_no, card_list):
    flag = True
    while flag:
        for i in range(len(card_list)-2):
            try:
                card_list.index(card_list[i], i+2)
            except ValueError:
                continue
            else:
                return f'Case #{test_no}: IMPOSSIBLE'
                
    final = set(card_list)
    final = ' '.join(final)
    return f'Case #{test_no}: {final}'

cases = int(input())
ans = []
for i in range(cases):
    n = int(input())
    cards = [int(i) for i in input().split()]
    ans.append(rainbow_sort(i+1, cards))
for i in ans:
    print(i)
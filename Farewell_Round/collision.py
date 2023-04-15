def collision(test_no, dd, word_list):
    encodes = []
    for word in word_list:
        a = ''
        for letter in word:
            a += str(dd[ord(letter)-65])
        encodes.append(a)
    if len(encodes) == len(set(encodes)):
        output = f'Case #{test_no}: NO'
    else:
        output = f'Case #{test_no}: YES'
    return output

cases = int(input())
ans = []
for i in range(cases):
    n = [int(i) for i in input().split()]
    num_words = int(input())
    words = []
    for x in range(num_words):
        word = input()
        words.append(word)
    ans.append(collision(i+1, n, words))
for i in ans:
    print(i)
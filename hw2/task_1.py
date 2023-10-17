word1 = input(f"Введите слово на латинице\n")
word1_len = len(word1.strip())
idx = word1_len // 2

if word1_len % 2 == 0:
    print(word1[idx - 1:idx + 1])
else:
    print(word1[idx])

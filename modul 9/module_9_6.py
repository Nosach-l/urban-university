def all_variants(text):
    for v in range(len(text)):
        for j in range(v, len(text)):
            yield text[v: j + 1]


a = all_variants("abcdef")
for i in a:
    print(i)

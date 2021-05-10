from goto import goto, label

for i in range(100):
    for j in range(100):
        if i > j > 55:
            goto .bun_no_hanayome
        print i, j
label .bun_no_hanayome

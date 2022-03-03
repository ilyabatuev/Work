from sys import argv


if len(argv) < 2:
    with open(file="bakery.csv", mode="r", encoding="utf-8") as bul_num:
        for line in bul_num:
            print(line)
if len(argv) == 2:
    i = int("".join(argv[1:]))
    list_bul = []
    with open(file="bakery.csv", mode="r", encoding="utf-8") as bul_num:
        for line in bul_num:
            list_bul.append(line)
    print("".join(list_bul[i - 1:]))
if len(argv) > 2:
    i, l = "".join(argv[1:])
    list_bul2 = []
    with open(file="bakery.csv", mode="r", encoding="utf-8") as bul_num2:
        for line in bul_num2:
            list_bul2.append(line)
    print("".join(list_bul2[int(i) - 1:int(l)]))
from sys import argv
numb = argv[1:]
with open(file="bakery.csv", mode="a", encoding="utf-8") as bul_num:
    bul_num.write("".join(numb) + '\n')
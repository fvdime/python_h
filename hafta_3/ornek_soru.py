def palindram(*dram):
    toplam = 0
    for sayi in dram:
        if str(sayi) == str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -= sayi
    return toplam

print(palindram(10, 101, 55, 40, 9009))
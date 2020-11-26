def rom_to_num(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = roman[s[len(s)-1]]
    for i in range(len(s)-1, 0, -1):
        current = roman[s[i]]
        prev = roman[s[i-1]]
        number += prev if prev >= current else -prev
    return number


print(rom_to_num("MDCCLI"))
print(rom_to_num("MMCMLIII"))
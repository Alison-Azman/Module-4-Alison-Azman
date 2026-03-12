def romanToInt(self, s: str) -> int:
    roman ={ 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total=0

    for char in range(len(s)-1):
        if roman[s[char]]<roman[s[char+1]]:
            total-=roman[s[char]]
        else:
            total+=roman[s[char]]

    total+= roman[s[-1]]
    return total




print(romanToInt(None, "MCMXCIV"))

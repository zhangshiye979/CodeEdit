# https://leetcode.com/problems/roman-to-integer/description/
roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

s = "MCMXCIV"
val = 0
tmpCh = ''
for ch in s:
    val += roman[ch]
    if tmpCh != '':
        if roman[tmpCh] < roman[ch]:
            val =val -2*roman[tmpCh]
    tmpCh = ch
print(val)
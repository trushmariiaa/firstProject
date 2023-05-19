# 6
# kompresja_prosta
# def rle(string):
#     if not string:
#         return ''
#
#     result = ''
#     prev_char = ''
#     count = 1
#
#     for char in string:
#         if char != prev_char:
#             if prev_char:
#                 result += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#
#     result += str(count) + prev_char
#     return result
#
# if __name__ == "__main__":
#     print(rle("AAAABBBCCDBBB"))

# szyfr Cezara

# def isLower(znak):
#     if znak >= "a" and znak <= "z":
#         return True
#     return False
#
# def isUpper(znak):
#     if znak >= "A" and znak <= "Z":
#         return True
#     return False
#
# 2
# def szyfrcezara(tekst,kod):
#     zaszyfrowane = ''
#     for znak in tekst:
#         nowy = ord(znak)
#         if isLower(znak):
#             nowy = (nowy + kod - 97) % 26 + 97
#         elif isUpper(znak):
#             nowy = (nowy + kod - 65) % 26 + 65
#         zaszyfrowane += chr(nowy)
#     return zaszyfrowane
#
# print(szyfrcezara("Warszawa",3))
# print(szyfrcezara("Warszawa",3),-3)
# 4
# def getmask():
#     m = ''
#     i = ord("0")
#     k = ord("9")+1
#     while i < k:
#         m+= chr(i)
#         i += 1
#     i = ord("A")
#     k = ord("Z") + 1
#     while i < k :
#         m+= chr(i)
#         i += 1
#     return m
# maska = getmask()
#
# def dec2Any(liczba,system):
#     tmp = ''
#     while liczba > 0:
#         tmp+= maska[liczba%system]
#         liczba//=system
#     i = len(tmp)
#     sliczba = ''
#     while i > 0:
#         sliczba += tmp[i-1]
#         i-=1
#     return sliczba
#
# print("zad4")
# print(dec2Any(215,12))

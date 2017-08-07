symbols = '!@#$%^'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

#List comprehension
symbols2 = '@!#@#@(#*@)'
codes2 = [ord(symbol) for symbol in symbols2]
print(codes2)

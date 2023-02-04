d = input('Enter String: ')

bin_num = ''.join([format(byte, "08b") for byte in d.encode()])
print(bin_num)

f = []
nul = 0

for i in range(1, len(bin_num)+1):
    if i % 8 == 0:
        f.append(bin_num[nul:i])
        nul = i

print(f)

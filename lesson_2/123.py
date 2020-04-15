n = int(input('n = '))
q = -0.5
b1 = 1
bn = b1 * pow(q, n-1)
sn = (bn * q - b1)/(q - 1)
print(sn)
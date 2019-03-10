L1=[2,4,9,16,25]
L2=[2,4,9,16,25]
L3=[2,4,9,16,25]

# Первый способ
for i in range(len(L1)):
    L1[i]=L1[i]**(1/2)

print(L1)

# Второй способ
print(list(map((lambda x:x**(1/2)),L2)))

# Третий способ
print([x**(1/2) for x in L3])

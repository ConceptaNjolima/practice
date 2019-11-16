
x = [3, 1, 4, 3, 8]

n = len(x)

for i in range(0, n):
    for j in reversed(range(i+1, n)):
        # print("i =", i, ",  j =", j, ",  and x =", x)
        if x[j] < x[j-1]:
            # interchange using temp variable
            temp = x[j-1]
            x[j-1] = x[j]
            x[j] = temp
            print("i =", i, ",  j =", j, ",  and x =", x)

tup= "age", 12,["maths", "Eng"]
new_tup= str(tup).split(" ")
print(new_tup)
print(type(new_tup))







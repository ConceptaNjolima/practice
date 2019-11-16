# number=int(input("Enter the total of the numbers you want"))
# # arr=map(int,input().split())
# # maxi=max(arr,default=0)
# # for i in arr:
# #     if i==maxi:
# #         arr.remove(i)
# # maximum=max(arr,default=0)
# # print(maximum)
# def enter_number():
#     value_entered=int(input("Enter number between 1 and 4"))
#     return value_entered
# number=enter_number()
x = [4, 3, 2, 1, 0]

n = len(x)
count_escaped = 0
count = 0
for i in x:
    print("first",count)
    for j in range(0,n):
        print("second", count)
        for k in x:
            if x[k]>x[k-1]:
                print("third",count)
                break
#  from Discrete Mathematics Class
for i in range(0, n):
    for j in reversed(range(i + 1, n)):
        print(x)
        if x[j] >= x[j - 1]:
            count_escaped = count_escaped + 1
            for k in range(0, new_n):
                break

        elif x[j] < x[j - 1]:
            count = count + 1
            # interchange using temp variable
            temp = x[j - 1]
            x[j - 1] = x[j]
            x[j] = temp


print(x, count, count_escaped)


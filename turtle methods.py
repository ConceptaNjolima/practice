# # #
# # # def apple_tree(pear):
# # #     orange = str(pear)
# # #     sum = 0
# # #     for i in range(len(orange)):
# # #         sum += int(orange[i])
# # #     return sum
# # # apple_tree("mango")
# #
# # import turtle
# # wn=turtle.Screen()
# # radius =10
# # user=int(input("number"))
# # for i in range(user):
# #     turtle.speed(0)
# #     turtle.forward(100)
# #     angle=(360/user)
# #     turtle.left(angle)
# # wn.exitonclick()
# fruit="mango"
# for i in fruit:
#     fruit.sort(reverse=True)
#
# print("LEts say this is {0} and this is {1}".format("All","us"))
import turtle

myturtle = turtle.Turtle()    # call initializer
# myturtle.setheading(67)
print(myturtle.heading())
wn=turtle.Screen()
wn.exitonclick()

import turtle
a = list(map(int, input().split()))
turtle.pencolor("red")
turtle.circle(max(a))
a.remove(max(a))
turtle.pencolor("black")
for i in range(len(a)):
    turtle.circle(a[i])

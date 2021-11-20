import turtle


def squares(a):
    for j in range(len(a)):
        for i in range(4):
            turtle.forward(a[j])
            turtle.right(90)


a = list(map(int, input().split()))
squares(a)

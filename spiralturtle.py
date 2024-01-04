import turtle

turtle.bgcolor("black")
seurat = turtle.Turtle()
width = 5
height = 7
dotDistance = 25
seurat.setpos(-250, 250)

def spiral(m, n):
    k = 0
    l = 0
    flag = 0
    seurat.color("white")

    while (k < m and l < n):
        if flag == 1:
            seurat.right(90)

        # printing the first row
        for i in range(l, n):
            seurat.forward(dotDistance)
        k += 1
        flag = 1
        seurat.right(90)

        # printing the last column
        for i in range(k, m):
            seurat.forward(dotDistance)
        n -= 1
        seurat.right(90)

        if k < m:
            # printing the last row
            for i in range(n - 1, l - 1, -1):
                seurat.forward(dotDistance)
            m -= 1
            seurat.right(90)

        if l < n:
            # printing the first column
            for i in range(m - 1, k - 1, -1):
                seurat.forward(dotDistance)
            l += 1

spiral(20, 20)
turtle.done()

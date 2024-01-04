def magicSquare(n):
    magicsquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicsquare.append(l)
    
    i=n//2
    j=n-1
    count=1
    num=n*n
    
    while count<=num:
        if i==-1 and j==n:
            j=n-2
            i=0
        else:
            if i==-1:
                i=n-1
            if j==n:
                j=0
                
        if magicsquare[i][j]!=0:
            i=i+1
            j=j-2
            continue
        
        magicsquare[i][j]=count
        count+=1
            
        i=i-1
        j=j+1
        
    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j],end=' ')
        print()
            
    print("The sum of any row/column/diagonal is",(n*(n**2+1)/2))
n=int(input("Enter order of matrix : "))
magicSquare(n)

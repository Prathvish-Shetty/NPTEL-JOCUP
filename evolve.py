import random
def evolve(x):
    index=random.randint(0,len(x)-1)
    p=random.randint(0,100)
    print(p)
    for p in range(1,100):
        if p==0:
            x[index]=1
        else:
            x[index]=0
            
with open('f1.txt','r+') as f:
    x=f.read()
    x=list(x)
    print(x)
    for i in range(0,10000):
        evolve(x)
    print(x)
f.close()
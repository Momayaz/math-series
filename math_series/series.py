def nums(n):
    if n == 1:
        return 0
    if n == 5:
        return (n*8)
   


def fibonacci(n):
   fvl,svl = 0,1
   
   arr = [0,1]
   for i in range(0,n-1):
       fvl,svl = svl,fvl+svl
       arr.append(svl)
   return svl
print(fibonacci(4))


def lucas(n):
    fvl,svl = 2,1
    arr=[2,1]
    for i in range(n-1):
        fvl,svl = svl,fvl+svl
        arr.append(svl)
    return svl
print(lucas(5))

def sum_series(n,fvl,svl):
    if fvl==0 and svl==1:
        return fibonacci(n)
    if fvl==2 and svl==1:
        return lucas(n)
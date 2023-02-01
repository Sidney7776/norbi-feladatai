prim_teszt=3
prim_max=20
i=2
prim=True
print ("Starting...")
while prim_teszt<=prim_max:
    while i<prim_teszt:
        if (prim_teszt%i==0):
            prim=False
            break
        i=i+1
    if prim==True:
        print(prim_teszt)
    prim_teszt=prim_teszt+1
    prim=True
    i=2
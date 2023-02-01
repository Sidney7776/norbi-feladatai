szam_kezd=3
szam_veg=10000
i=1
oszto=0
n=128
print ("Starting...")
while szam_kezd<=szam_veg:
    while i<=szam_kezd:
        if (szam_kezd%i==0):
            oszto=oszto+1
            if(oszto>n): break
        i=i+1
    if(szam_kezd%1000 == 0): print ("itt tartok:", szam_kezd)
    if oszto==n:
        print(szam_kezd)
    szam_kezd=szam_kezd+1
    i=1
    oszto=0
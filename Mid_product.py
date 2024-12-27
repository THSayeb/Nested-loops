num = int(input("Enter a number : "))
t = num 
j = num
numlen = 0

while t > 0 or t < -1:
    numlen = numlen+1 
    t = int(t/10)

if numlen >= 4:
    numlen = int(numlen/2)
    chk = 0 

    while num > 0 or num < -1:
        rem = num%10

        if chk == numlen:
            midone = rem
        elif chk == (numlen-1):
            midtwo = rem
        num = int(num / 10)
        chk = chk + 1
    prod = midone * midtwo

    print("\nProducts of mid digits (", str(midone), "*", str(midtwo), ") =", prod)

else:
    print("\nIt's not a 4 or more than 4-digit number!")


        

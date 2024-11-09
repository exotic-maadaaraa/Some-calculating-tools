
print('welcome')
print('1.addition')
print('2.subtraction')
print('3.multiplication')
print('4.divison')
print('5.factorial')
x=int(input('enter your choice:1/2/3/4/5'))
if x==1:
   a1=float(input('enter the first number'))
   a2=float(input('enter the first number'))
   print('the sum is:',a1+a2)
elif x==2:
    s1=float(input('enter the first number'))
    s2=float(input('enter the second number'))
    print('the difference is:',s1-s2)
elif x==3:
   m1=float(input('enter the first number'))
   m2=float(input('enter the second number'))
   print('the multiplication is:',m1*m2)
elif x==4:
   d1=float(input('enter the first number'))
   d2=float(input('enter the second number'))
   print('the divison is:',d1/d2)
elif x==5:
    num=int(input('enter the number'))
    fact=1
    a=1
    while a<=num:
        fact=fact*a
        a=a+1
    print('the factorial of the no is:',fact)

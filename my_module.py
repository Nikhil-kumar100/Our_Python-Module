#User defined module
def add(a,b):
 return a+b
def sub(a,b):
 return a-b
def mul(a,b):
 return a*b
def divide(a,b):
 return a//b
def greatest_in_two(a,b):
 if a>b:
  return a
 else:
  return b
def greatest_in_three(a,b,c):
 if a>b and a>c:
  return a
 elif b>a and b>c:
  return b
 else:
  return c
def fact(n):
 if n==0 or n==1:
  return 1
 else:
  return n*(fact(n-1))
def fabunacci(r):
 a=0
 b=1
 print(a,b,end=" ")
 for i in range(2,r):
  c=a+b
  print(c,end=" ")
  a=b
  b=c
def sum_of_digits(n):
 sum=0
 for i in str(n):
  sum+=int(i)
 return sum
def Armstrong(n):
  sum=0
  m=n
  length=len(str(n))
  for i in str(n):
   sum+=int(i)**length
  if sum==m:
   return "Armstrong"
  else:
   return "Not Armstrong"
def Prime_number(n):
  c=0
  for i in range(1,n+1):
   if n%i==0:
    c+=1
  if c==2:
   return "Prime"
  else:
   return "Not prime"
def sqrt(n):
  return n**0.5
def even_odd(n):
 if n%2==0: 
  return "Even"
 else:
  return "Odd"
def roots(a,b,c):
 d=(b*b)-(4*a*c)
 if d<0:
  return "Imaginary Roots"
 else:
  Root1=(-b+d**0.5)//2*a 
  Root2=(-b-d**0.5)//2*a
  return Root1,Root2
def quardinate(x,y):
 if x>0 and y>0:
  return "Both points lies on First qurdrant"
 elif x>0 and y<0:
  return "Both points lies on Fourth qurdrant"
 elif x<0 and y>0:
  return "Both points lies on  Second qurdrant"
 elif x<0 and y<0:
  return "Both points lies on Third qurdrant"
 elif x==0 and y!=0:
  return "Y-Axis"
 elif y==0 and x!=0:
  return "X-Axis"
 else:
  return "Both points are lies on Origin"
def table(n):
 i=1
 while i<=10:
  table=n*i
  print(n,"*",i,"=",table)
  i=i+1 
def reverse_digit(n):
 rev=0
 while n>0:
  d=n%10
  rev=rev*10+d
  n=n//10
 return rev
def convert_binary_to_decimal(n):
 decimal=0
 i=0
 while n>0:
  r=n%10
  if r!=0 and r!=1:
   decimal=0
   break
  else:
   decimal+=(r*pow(2,i))
   n=n//10
  i+=1 
 if decimal==0:
  return "Invalid User Entered"
 else:
  return decimal  
def convert_decimal_to_binary(n):
 binary=""
 if n==0:
  return "0"
 else:
  while n!=0:
   r=n%2
   binary=str(r)+binary
   n=n//2
  return binary
def Sum_and_Avg_of_List(n):
   my_list=[]
   print("Enter ",n," elements : ")
   for i in range(0,n):
    m=int(input(""))
    my_list.append(m)
    Sum=sum(my_list)
    Avg=Sum/len(my_list)
   return Sum,Avg
def vowel_in_str(String):
 vowel="aeiouAEIOU"
 dict={}
 for i in String:
  if i in vowel:
   dict[i]=String.count(i)
 return dict
def Create_dict(term):
  dict={}
  while True:
   try:
    if term>=0:
      break 
    else:
     term1=int(input("Please! Enter a non negative number : "))
     term=term1
   except ValueError:
    term2=int(input("Invalid Entered . Please Enter only number : "))
    term=term2   
  for i in range(0,term):
    key=input("Enter key : ")
    value=input("Enter value : ")
    dict[key]=value
  return dict
   
   
   
 


  




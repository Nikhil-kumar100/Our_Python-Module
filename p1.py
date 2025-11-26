import my_module
while True:
 ch=int(input("Press\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Find greatest among two number\n6. Find greatest among three number\n7. Factorial of given number\n8.Fabunacci series\n9.  Sum of digits\n10. Check Armstrong Number\n11. Check Prime number\n12. Find square Root\n13. Check Even odd\n14. Find roots of quadratic equation\n15. Quadrant checking\n16. Find table of any number\n17. Find Reverse of any number\n18. Convert Binary to Decimal\n19. Convert Decimal to Binary\n20. Find Sum and Average in list\n21. Count vowel in given String\n22. Create dictionary by taking input\n23. Exit\n"))
 if ch==1:
  x=int(input("Enter first number : "))
  y=int(input("Enter second number : "))
  s=my_module.add(x,y)
  print("Sum : ",s)
 elif ch==2:
  x=int(input("Enter first number : "))
  y=int(input("Enter second number : "))
  s=my_module.sub(x,y)
  print("Subraction : ",s)
 elif ch==3:
  x=int(input("Enter first number : "))
  y=int(input("Enter second number : "))
  m=my_module.mul(x,y)
  print("Multiplication : ",m)  
 elif ch==4:
  x=int(input("Enter first number : "))
  y=int(input("Enter second number : "))
  d=my_module.divide(x,y)
  print("Division : ",d)  
 elif ch==5:
  x=int(input("Enter first number : "))
  y=int(input("Enter second number : "))
  x=my_module.greatest_in_two(x,y) 
  print("Greatest : ",x)  
 elif ch==6:
  x=int(input("Enter first number : "))
  y=int(input("Enter second number : "))
  z=int(input("Enter third number : "))
  r=my_module.greatest_in_three(x,y,z) 
  print("Greatest : ",r)
 elif ch==7:
      n=int(input("Enter any number which you want to calculate fact : "))
      fact=my_module.fact(n)
      print("Factorial = ",fact)
 elif ch==8:
    r=int(input("Enter any range to calculate fabunacci : "))
    my_module.fabunacci(r)
    print("\n")
 elif ch==9:
   n=int(input("Enter any number which you want to sum : "))
   s=my_module.sum_of_digits(n)   
   print("Sum of digits : ",s)
 elif ch==10:
   n=int(input("Enter any number to calculate Armstrong or not : "))
   result=my_module.Armstrong(n)  
   print(result)
 elif ch==11:
   n=int(input("Enter any number to check prime or not : "))
   result=my_module.Prime_number(n)  
   print(result)
 elif ch==12:
  n=int(input("Enter a number to find square root : "))
  Sqt=my_module.sqrt(n)
  print("Square root : ",Sqt)
 elif ch==13 :
   n=int(input("Enter any number to check Even or odd : "))
   result=my_module.even_odd(n)
   print(result)
 elif ch==14:
   a=int(input("Enter first number : ")) 
   b=int(input("Enter second number : ")) 
   c=int(input("Enter third number : ")) 
   result=my_module.roots(a,b,c) 
   print(result)  
 elif ch==15:
   a=int(input("Enter first quardinate : "))   
   b=int(input("Enter first quardinate : "))   
   q=my_module.quardinate(a,b)
   print(q)
 elif ch==16:
   n=int(input("Enter any number to find table : "))
   my_module.table(n)
 elif ch==17:
  n=int(input("Enter any number to find reverse : "))  
  rev=my_module.reverse_digit(n)
  print("Reverse : ",rev)
 elif ch==18:
   n=int(input("Enter binary number : "))
   decimal=my_module.convert_binary_to_decimal(n)
   print(decimal)
 elif ch==19:
   n=int(input("Enter Decimal number : "))
   binary=my_module.convert_decimal_to_binary(n)
   print(binary)
 elif ch==20:
   l=int(input("Enter length of list : "))
   result=my_module.Sum_and_Avg_of_List(l) 
   print(result)
 elif ch==21:
   String=input("Enter any String : ") 
   c=my_module.vowel_in_str(String) 
   print(c)
 elif ch==22:
   term=int(input("Enter the number of key-value pairs you want to add : "))
   dict=my_module.Create_dict(term) 
   print(dict) 
 elif ch==23:
  break
 n=input("Do you want to perform tasks again ? ")
 if n=="y" or n=="Y" or n=="yes" or n=="Yes":
    pass
 else:
   break
print("Badhai ho ! App loop se bahar aa gaye ")
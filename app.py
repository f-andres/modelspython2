print ("Calculando");

num = 4

factorial = 1

if num < 0:
   print("Error")
elif num == 0:
   print("El factorial de 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("El factorial de",num,"es",factorial)
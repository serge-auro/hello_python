#import my_test_package as mtp
#print(dir(myTestPackage))
#mtp.python.hello("Serge")

import lessons.arithmetic as aa

a = 4
b = 7
print(f"a = {a}, b = {b}")
print("#2 умножение, деление, сложение, вычитание: ",
      aa.multiplication(a, b), ", ",
      aa.division(a, b), ", ",
      aa.addition(a, b), ", ",
      aa.subtraction(a, b), ", ")

import math
import array
from math import exp 
n=0
denominador = pow(2, n)

valorX = 1
j = 0
h = 1 / 1


funcionX= valorX* exp (valorX*valorX*-1)
funciondX= exp(valorX*valorX*-1)- valorX* 2* exp (valorX*valorX*-1)
print("F(x)               Fd(x)                  F(X)-h         Fd(x)-h        error")
for i in range(0, 65):

    if ( 1/pow(2, i) == 0):
        funcionxh = ((funcionX + 1/pow(2, i)) -funcionX  )  /  i/pow(2, i)
        derivada = (funciondX + 1/pow(2, i)  ) / i/pow(2, i)
        funcionxh2 = (funcionX + 1/pow(2, i)  ) / 2 * i/pow(2, i) 
        derivada2 = (funciondX + 1/pow(2, i)  + funciondX - 1/pow(2, i) ) / 2 * i/pow(2, i)
        print(str(i) + "  " + str(funcionxh) + "  "+ str(derivada) + "    " + str(float(funcionxh2)) + "    "+ str(derivada2) ) 
        print(" ")
    else:
        print("error                                            " + str(i))


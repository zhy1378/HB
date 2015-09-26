#from math import Math
import math
#    ΔP = 0.95 * (M)1/3 / R + 3.9 * (M)2/3 / R2 + 13.0 * M / R3
M = 1000
R = 8000
if R > math.pow(M, 0.5):
	target = R
	R = math.pow(M, 0.5)
n1 = 0.95 * math.pow(M, 0.33333) / R
n2 = 3.9 * math.pow(M, 0.66667) / math.pow(R, 2)
n3 = 13.0 * M / math.pow(R, 3)
atm = n1 + n2 + n3
atm = atm / math.pow(target / R, 2.5)
print(n1)
print(n2)
print(n3)
pa = 101325 * atm
psi = 14.69595 * atm
print("ATM = " + str(atm))
print("Pa = " + str(pa))
print("PSI = " + str(psi))
import math

# i=355.84u^10.294
# i=2
u1 = 2 / 355.84
u1 = math.pow(u1, 1 / 10.294)
print("x1 = {}".format(u1))
# i=8
u2 = 8 / 355.84
u2 = math.pow(u2, 1 / 10.294)
print("x2 = {}".format(u2))
r1 = u1 / 0.002
r2 = u2 / 0.008
print("r1 = {}".format(r1))
print("r2 = {}".format(r2))

import math

u2 = 1.2349
u1 = 0.12917
i2 = 10.42
i1 = 1.7
r_a = 2
i2 = i2 * 1e-3
i1 = i1 * 1e-3
# r_x= (u2 - u1) / (i2 - i1)-r_a
# according regression argument in excel
regression_k = 8.4122
regression_k = regression_k * 1e-3
r_x = 1 / regression_k - r_a
delta_u = 2e-4 * u2 + 1e-4
# delta_i is mA! so i2 * 1000
delta_i = 0.012 * i2 * 1000 + 3 * 0.01
# convert mA to A
delta_i = delta_i * 1e-3
delta_r = math.sqrt((delta_u / (u2 - u1)) ** 2 + (delta_i / (i2 - i1)) ** 2)
print("delta_r = {}".format(delta_r))
abs_delta_r = delta_r * r_x
print("r_x = {}±{}".format(r_x, abs_delta_r))

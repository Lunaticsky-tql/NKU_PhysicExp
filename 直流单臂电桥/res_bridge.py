import math


def calc_s(delta_i, delta_r, r):
    return delta_i * r / delta_r


def calc_rho_x(S, rho_0=1e-3, rho_c=1e-3, is_swap=False):
    if is_swap:
        rho_c = 0
    G_err = 0.1 / S
    return math.sqrt(rho_0 * rho_0 + rho_c * rho_c + G_err * G_err)


# r0=5001.8
# rx=r0/100
# delta_r0=20
# delta_i=26.7
# s=calc_s(delta_i,delta_r0,r0)
# print("S={0}".format(s))
# rho_x=calc_rho_x(s,is_swap=False,rho_c=2e-3)
# delta_rx=rx*rho_x
# print("rho_x={0}".format(rho_x))
# print("Rx={0}±{1}".format(rx,delta_rx))

r0_1 = 1183.9
r0_2 = 1183.8
delta_r0 = 1.5
delta_i_1 = 27.9
delta_i_2 = 27.8
s_1 = calc_s(delta_i_1, delta_r0, r0_1)
s_2 = calc_s(delta_i_2, delta_r0, r0_2)
print("s_1={}".format(s_1))
print("s_2={}".format(s_2))
rho_x_1 = calc_rho_x(s_1, is_swap=False)
print("换臂前rho_x={}".format(rho_x_1))
avg_r_x = (r0_1 + r0_2) / 2
avg_s = (s_1 + s_2) / 2
rho_x_2 = calc_rho_x(avg_s, is_swap=True)
print("换臂后rho_x={}".format(rho_x_2))
delta_rx_1 = r0_1 * rho_x_1
delta_rx_2 = avg_r_x * rho_x_2
print("换臂前Rx={0}±{1}".format(r0_1, delta_rx_1))
print("换臂后Rx={0}±{1}".format(avg_r_x, delta_rx_2))

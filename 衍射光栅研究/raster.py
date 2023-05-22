import math


# 角度转弧度
def radian(angle):
    return angle / 180 * math.pi


def dm2d(d, m):
    return d + m / 60


def d2dm(d):
    return int(d), int((d - int(d)) * 60)


def dm_add(d1, m1, d2, m2):
    d = d1 + d2
    m = m1 + m2
    if m >= 60:
        d += 1
        m -= 60
    return d, m


def dm_sub(d1, m1, d2, m2):
    d = d1 - d2
    m = m1 - m2
    if m < 0:
        d -= 1
        m += 60
    return d, m


def dm_avg(d1, m1, d2, m2):
    d = (d1 + d2) / 2
    m = (m1 + m2) / 2
    if m >= 60:
        d += 1
        m -= 60
    return d, m


d1p, m1p = 273, 39
d1n, m1n = 254, 40
d2p, m2p = 96, 31
d2n, m2n = 77, 41

d1pn, m1pn = dm_sub(d1p, m1p, d1n, m1n)
print(R"正偏心角度差：{}°{}′".format(d1pn, m1pn))
d2pn, m2pn = dm_sub(d2p, m2p, d2n, m2n)
print(R"负偏心角度差：{}°{}′".format(d2pn, m2pn))
avg_d, avg_m = dm_avg(d1pn, m1pn, d2pn, m2pn)
print(R"无偏心角度差：{}°{}′".format(avg_d, avg_m))
k = 1
lambda_0 = 546.1e-9
d = k * lambda_0 / math.sin(radian(dm2d(avg_d, avg_m) / 2))
print("d={}".format(d))
d1p, m1p = 284, 35
d1n, m1n = 243, 67
d2p, m2p = 105, 28
d2n, m2n = 64, 59
d1pn, m1pn = dm_sub(d1p, m1p, d1n, m1n)
print(R"正偏心角度差：{}°{}′".format(d1pn, m1pn))
d2pn, m2pn = dm_sub(d2p, m2p, d2n, m2n)
print(R"负偏心角度差：{}°{}′".format(d2pn, m2pn))
avg_d, avg_m = dm_avg(d1pn, m1pn, d2pn, m2pn)
print(R"无偏心角度差：{}°{}′".format(avg_d, avg_m))
phi_1 = dm2d(avg_d, avg_m)
k = 2
lambda_1 = d * math.sin(radian(phi_1 / 2)) / k
print("lambda_1={}".format(lambda_1))
lamda_1_true = 577.0e-9
error = (lambda_1 - lamda_1_true) / lamda_1_true
print("error_1={}".format(error))
d1p, m1p = 284, 30
d1n, m1n = 243, 52
d2p, m2p = 104, 33
d2n, m2n = 63, 59
d1pn, m1pn = dm_sub(d1p, m1p, d1n, m1n)
print(R"正偏心角度差：{}°{}′".format(d1pn, m1pn))
d2pn, m2pn = dm_sub(d2p, m2p, d2n, m2n)
print(R"负偏心角度差：{}°{}′".format(d2pn, m2pn))
avg_d, avg_m = dm_avg(d1pn, m1pn, d2pn, m2pn)
print(R"无偏心角度差：{}°{}′".format(avg_d, avg_m))
phi_2 = dm2d(avg_d, avg_m)
k = 2
lambda_2 = d * math.sin(radian(phi_2 / 2)) / k
print("lambda_2={}".format(lambda_2))
lamda_2_true = 579.1e-9
error = (lambda_2 - lamda_2_true) / lamda_2_true
print("error_2={}".format(error))
delta_phi = abs(phi_1 - phi_2)
print("delta_phi={}".format(delta_phi))
c = 2.1e-9
D = delta_phi / c
print("D={}".format(D))

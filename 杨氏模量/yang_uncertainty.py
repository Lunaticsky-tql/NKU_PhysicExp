import math

# t(0.683,2) = 1.32, t(0.683,3) = 1.20, etc.
ConfidenceProbability = [1.32, 1.20, 1.14, 1.11, 1.09, 1.08, 1.07, 1.06, 1.03, 1]


def get_uncertainty_a(data):
    """
    Calculate the uncertainty of the data.
    """
    n = len(data)
    t = 0
    if n == 0:
        raise ValueError("测量次数不能为零！")
    elif n < 3:
        print("测量次数不能少于三次！")
    elif n < 10:
        t = ConfidenceProbability[n - 3]
    elif n < 20:
        t = ConfidenceProbability[7]
    elif n == 20:
        t = ConfidenceProbability[8]
    else:
        t = ConfidenceProbability[9]
    x_sum = 0
    for i in range(n):
        x_sum += data[i]
    x_aver = x_sum / n
    x_SquDif = 0
    for i in range(n):
        x_SquDif += (data[i] - x_aver) ** 2
    s_x = math.sqrt(x_SquDif / (n - 1))
    s_x_bar = s_x / math.sqrt(n)
    ua = t * s_x_bar
    return ua


if __name__ == "__main__":
    # 金属丝伸长长度,单位cm
    N_list = [2.42, 2.445, 2.385, 2.195, 2.295]
    N_list = [i * 1e-2 for i in N_list]
    u_NA = get_uncertainty_a(N_list)
    u_NB = 5e-4 / math.sqrt(3)
    u_N = math.sqrt(u_NA ** 2 + u_NB ** 2)
    print("u_N = {}".format(u_N))
    # 金属丝直径,单位mm
    d_list = [0.796, 0.808, 0.800, 0.795, 0.798, 0.805]
    d_list = [i * 1e-3 for i in d_list]
    u_dA = get_uncertainty_a(d_list)
    u_dB = 4e-5 / math.sqrt(3)
    u_d = math.sqrt(u_dA ** 2 + u_dB ** 2)
    u_L = 5e-4
    u_D = 5e-4
    u_b = 5e-4
    D = 0.6998
    L = 0.3765
    m = 5
    g = 9.8
    d_sum = 0
    for i in range(len(d_list)):
        d_sum += d_list[i]
    d = d_sum/ len(d_list)
    b = 0.0460
    N_sum = 0
    for i in range(len(N_list)):
        N_sum += N_list[i]
    N = N_sum/ len(N_list)
    E = 32 * D * L * m * g / (math.pi * d * d * b * N)
    print("E = {}".format(E))
    # 科学计数法表示
    print("E = {:.2e}".format(E))
    u_E = math.sqrt(
        math.pow(u_L / L, 2) + math.pow(u_D / D, 2) + math.pow(u_N / N, 2) + math.pow(2*u_d / d, 2) + math.pow(
            u_b / b, 2)) * E
    print("u_E = {}".format(u_E))
    # 科学计数法表示
    print("u_E = {:.2e}".format(u_E))

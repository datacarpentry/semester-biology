"""Exponential growth debugging example"""

def get_pop_size_at_t(init_pop_size, reprod_rate, time_of_sample):
    n = init_pop_size
    for t in range(1, time_of_sample + 1):
        n_tplus1 = n + reprod_rate * n
        n = n_tplus1
    return n_tplus1

def doubling_time_exponential_growth(reprod_rate, init_pop_size):
    n = init_pop_size
    t = 0
    while n < 2 * init_pop_size:
        n = n + reprod_rate * n
    t += 1
    return t

#Problem 2
print get_pop_size_at_t(10, 0.152, 10)
print get_pop_size_at_t(10, 0.152, 50)
print get_pop_size_at_t(10, 0.152, 100)

#Problem 3
print doubling_time_exponential_growth(0.0001, 1000)
print doubling_time_exponential_growth(0.005, 1000)
print doubling_time_exponential_growth(0.21, 1000)
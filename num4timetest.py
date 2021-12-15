import timeit
code_to_test = """
import random
n = 1000
a = []
b = []
for i in range(n):
    a_el = random.triangular(0, 10)
    a.append(a_el)
    b_el = random.triangular(0, 10)
    b.append(b_el)
c = []
for i in range(n):
    c_el = a[i] * b[i]
    c.append(c_el)
"""
elapsed_time = timeit.timeit(code_to_test, number=100)
print(elapsed_time)

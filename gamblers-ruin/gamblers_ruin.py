import numpy as np

target = 100
start = 50
p = 0.49
q = 1 - p

Q = np.zeros((99, 99))

for i in range(99):
    if i > 0:
        Q[i, i-1] = q
    if i < 98:
        Q[i, i+1] = p

I = np.eye(99)
N = np.linalg.inv(I-Q)

start_idx = 49

expected_steps = np.sum(N[start_idx])

R_win = np.zeros(99)
R_win[98] = p
win_prob = np.dot(N[start_idx], R_win)

print(win_prob)
print(expected_steps)

import numpy as np

print("First array:")
r1, c1 = map(int, input("Enter rows columns: ").split())
a1 = np.array([int(input()) for _ in range(r1*c1)]).reshape((r1, c1))

print("Second array (same shape as first):")
r2, c2 = map(int, input("Enter rows columns: ").split())
a2 = np.array([int(input()) for _ in range(r2*c2)]).reshape((r2, c2))

axis = int(input("Enter axis to join (0 for vertical, 1 for horizontal): "))
if axis == 0:
    res = np.vstack((a1, a2))
else:
    res = np.hstack((a1, a2))
print("Joined array:")
print(res)

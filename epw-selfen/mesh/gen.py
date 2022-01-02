import numpy as np

kpt = np.array([[0.00 ,0.00, 0.00], [ 0.00, 0.00, 0.50], [0.333333, 0.3333333 ,0.0000], [ 0.333333 ,0.3333333, 0.5000], [0.5 , 0.0, 0.0 ]])


nkpt = 100

kx = []
ky = []
kz = []

for i in range(len(kpt) -1 ):
  for x in np.arange(0, 1, 0.01):
    vec = kpt[i] * (1e0 - x) + kpt[i + 1] * x
    kx.append(vec[0])
    ky.append(vec[1])
    kz.append(vec[2])

with open('kpt.dat', 'w') as f:
  f.write(str(len(kx)) + '\n')
  for i in range(len(kx)):
    f.write("{0:18.10f} {1:18.10f} {2:18.10f} 0.000001\n".format(kx[i], ky[i], kz[i]))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def read_ph(fname):
  x = [0e0]
  with open(fname, 'r') as f:
    line = f.readline().split()
    nbnd = int(line[2].strip(','))
    nkpt = int(line[4])


    ene  = [[] for i in range(nbnd)]
    
    line = f.readline().split()
    vec_old  = np.array( list(map(float, line)))

    line = f.readline().split()
    for i in range(min(nbnd, 10)):
      ene[i].append(float(line[i]))

    if nbnd > 10:
      line = f.readline().split()
      for i in range(nbnd - 10):
        ene[i + 10].append(float(line[i]))

    for i in range(nkpt-1):
      line = f.readline().split()
      vec_new  = np.array(list(map(float, line)))
      dis = np.linalg.norm(vec_new - vec_old)
      x.append(dis + x[-1])

      vec_old = vec_new

      line = f.readline().split()
      for j in range(min(nbnd, 10)):
        ene[j].append(float(line[j]))

      if nbnd > 10:
        line = f.readline().split()
        for i in range(nbnd - 10):
          ene[i + 10].append(float(line[i]))

  return x, ene

if __name__ == '__main__':
  qe_x, qe_ene   = read_ph('../bnd/bands.out')
  epw_x, epw_ene = read_ph('./band.eig')

  fig = plt.figure()
  ax  = fig.add_subplot(111)
  for i in range(len(qe_ene)):
      ax.scatter(qe_x, qe_ene[i], marker = 'o', color = 'r', s = 2)
  for i in range(len(epw_ene)):
      ax.scatter(epw_x, np.array(epw_ene[i]) , marker ='p', color = 'b', s = 0.5)
  ax.set_ylim(4,14)
  plt.savefig('Be-bnd.png', format = 'png', dpi = 400)

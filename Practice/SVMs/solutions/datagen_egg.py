import csv
import numpy as np

def to_csv(name, mode, data):
    with open(name, mode) as csvfile:
        w = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for d in data:
            w.writerow(d)
            
def gen_gauss(m, v, lab, nb):
    d = []
    for i in range(nb):
        d.append(np.concatenate((np.random.normal(loc=m, scale=v, size=2),[lab]),axis=0))
    return d
    
name = 'data2.csv'


n = 600

d = gen_gauss([0, 0], 0.75, +1, n)
delete = []
for i in range(len(d)):
    if (d[i][0]**2 + d[i][1]**2 < 1):
        if np.random.uniform(low=0.0, high=1.0, size=None) < 0.6:
            delete.append(i)
    if (d[i][0]**2 + d[i][1]**2 < 0.6):
        delete.append(i)
d = np.delete(d, delete, axis=0)
to_csv(name, 'w', d)


d = gen_gauss([0, 0], 0.75, -1, n)
delete = []
for i in range(len(d)):
    if (d[i][0]**2 + d[i][1]**2 > 1):
        delete.append(i)
d = np.delete(d, delete, axis=0)
to_csv(name, 'a', d)

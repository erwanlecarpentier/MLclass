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
    
name = 'data1.csv'
to_csv(name, 'w', gen_gauss([0, 0], 0.1, +1, 100))
to_csv(name, 'a', gen_gauss([1, 1], 0.1, -1, 100))

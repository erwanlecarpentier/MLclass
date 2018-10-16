import matplotlib.pyplot as plt

data_file = 'data/atheist.dat'
df = pd.read_csv(data_file, sep='\s+',
                 header=None,
                 names=['attendance', 'tolerance'])

print(df.shape, "# <-- (nrow, ncols)", "\n")
print(df.sample(5)) # print random rows

plt.scatter(df['attendance'], df['tolerance'])

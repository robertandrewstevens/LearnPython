import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(1983)

x = np.random.randn(1000)

sns.kdeplot(x)

plt.show()
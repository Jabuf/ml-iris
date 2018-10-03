# Load libraries
import dataset_import
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

print(dataset_import.shape)
print(dataset_import.head(20))
print(dataset_import.describe())
print(dataset_import.groupby('class').size())

# box and whisker plots
dataset_import.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
dataset_import.hist()
scatter_matrix(dataset_import)
plt.show()

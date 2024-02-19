import numpy as np


# mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements
def calculate(list):
  if (len(list) < 9):
    raise ValueError("List must contain nine numbers.")

  dt = np.array(list).reshape(3, 3)

  means = [
      dt.mean(axis=0).tolist(),
      dt.mean(axis=1).tolist(),
      dt.mean().tolist()
  ]
  variances = [
      dt.var(axis=0).tolist(),
      dt.var(axis=1).tolist(),
      dt.var().tolist()
  ]
  stds = [dt.std(axis=0).tolist(), dt.std(axis=1).tolist(), dt.std().tolist()]
  maxs = [dt.max(axis=0).tolist(), dt.max(axis=1).tolist(), dt.max().tolist()]
  mins = [dt.min(axis=0).tolist(), dt.min(axis=1).tolist(), dt.min().tolist()]
  sums = [dt.sum(axis=0).tolist(), dt.sum(axis=1).tolist(), dt.sum().tolist()]

  calculations = {
      'mean': means,
      'variance': variances,
      'standard deviation': stds,
      'max': maxs,
      'min': mins,
      'sum': sums
  }

  return calculations

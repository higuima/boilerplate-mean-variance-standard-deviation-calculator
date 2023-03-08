import numpy as np

def calculate(list):
  if len(list) == 9:
    list = np.array(list)
    array = list.reshape((3,3))
    calculations = {}
    calculations['mean'] = [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array)]
    calculations['variance'] = [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array.flatten())]
    calculations['standard deviation'] = [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array.flatten())]
    calculations['max'] = [np.amax(array, axis=0).tolist(), np.amax(array, axis=1).tolist(), np.amax(array.flatten())]
    calculations['min'] = [np.amin(array, axis=0).tolist(), np.amin(array, axis=1).tolist(), np.amin(array.flatten())]
    calculations['sum'] = [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array.flatten())]
  else:
    raise ValueError('List must contain nine numbers.')

  return calculations
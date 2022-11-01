import numpy as np
list = [0,1,2,3,4,5,6,7,8]
def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    calculations = {'mean':[],'variance':[],'standard deviation':[],'max':[],'min':[],'sum':[]}
    matrix = np.array(list)
    matrix = matrix.reshape(3,3)
    calculations['mean'] = mean(matrix)
    calculations['variance'] = var(matrix)
    calculations['standard deviation'] = std(matrix)
    calculations['min'] = min(matrix)
    calculations['max'] = max(matrix)
    calculations['sum'] = summed(matrix)
    return calculations

#splitting up each action to divide it up and make it visually clearer
def mean(arr):
    means = []
    means.append(arr.mean(axis=0).tolist())
    means.append(arr.mean(axis=1).tolist())
    means.append(arr.reshape(9).mean())
    return means
def var(arr):
    vars = []
    vars.append(np.var(arr, axis=0).tolist())
    vars.append(np.var(arr, axis=1).tolist())
    vars.append(np.var(arr.reshape(9)))
    return vars
def std(arr):
    stds = []
    stds.append(np.std(arr, axis=0).tolist())
    stds.append(np.std(arr, axis=1).tolist())
    stds.append(np.std(arr.reshape(9)))
    return stds
def max(arr):
    maxes = []
    maxes.append(arr.max(axis=0).tolist())
    maxes.append(arr.max(axis=1).tolist())
    maxes.append(arr.reshape(9).max())
    return maxes
def min(arr):
    mins = []
    mins.append(arr.min(axis=0).tolist())
    mins.append(arr.min(axis=1).tolist())
    mins.append(arr.reshape(9).min())
    return mins
def summed(arr):
    sums = []
    sums.append(arr.sum(axis=0).tolist())
    sums.append(arr.sum(axis=1).tolist())
    sums.append(arr.reshape(9).sum())
    return sums


print(calculate(list))
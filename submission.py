import numpy as np
import pandas as pd

# Function multiply list

def multiply_list(input_str:str) -> int:
  a = 1
  if input_str.strip() == '':
    return 0
  else: 
    for n in input_str.split(' '):
      try:
        if n=='':
          n_int = 1
        else:
          n_int = int(n)
        a*=n_int
      except ValueError:
        continue
  return a

# Function count common chars

def count_common_chars(input_words: str) -> int:
  words = input_words.split()
  return len(set(words[0]).intersection(set(words[1])))

# Function sum divisible by K

def sum_divisible_by_k(N: int, K: int) -> int:
  if N < 1 or K == 0:
    return -1
  else:
    a = 0
    for i in range(1, N+1):
      if i%K == 0:
        a+=i
      else:
        continue
  return a

# Function highest common factor

def highest_common_factor(N1: int, N2: int) -> int:
  while N2!=0:
    N1, N2 = N2, N1%N2
  return N1
       
# Function get minimum

def get_minimum(list_input:list) -> int:
  return min(list_input)

# Function rename col

def rename_col(dataframe: pd.DataFrame, old_name: str, new_name: str) -> pd.DataFrame:
  dataframe_copy = dataframe.copy()
  dataframe_copy.columns = [c if c != old_name else new_name for c in dataframe_copy.columns]
  return dataframe_copy

# Function standard deviation

def standard_deviation(series: pd.Series) -> float:
  return np.sqrt(sum((series -series.mean())**2)/(series.shape[0]))

# Function correlation sum

def correlation_sum(number_string: str) -> float:
  list_nums = np.array(number_string.split(' '))
  
  for l in list_nums:
    try:
      int(l)
    except ValueError:
      return 0

  array_reshaped = list_nums.reshape(3,3)
  dataframe_corr_sum = pd.DataFrame(array_reshaped).corr().sum().sum()
  return np.round(dataframe_corr_sum,1)

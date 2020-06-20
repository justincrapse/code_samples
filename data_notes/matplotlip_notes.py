from matplotlib import pyplot as plt
import pandas as pd
import random

pandas_df = pd.read_csv('data/top_100.csv')
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
rand_values = [random.randint(0, 9**5) for _ in range(len(alphabet))]
increasing_values = range(26)
to_pd_dict = {'Chars': alphabet, 'Values': rand_values, 'Increasing': list(increasing_values)}
rando_df = pd.DataFrame.from_dict(to_pd_dict)
print(rando_df.tail())
plt.plot(rando_df.Chars, rando_df.Values)

plt.show(rando_df.Chars, rando_df.Values)

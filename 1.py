#  Даны две независимые выборки. Не соблюдается условие нормальности
# x1 380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции

import numpy as np 
import scipy.stats as st

x = np.array([380, 420, 290 ])
y = np.array([140, 360, 200, 900])
Res = st.mannwhitneyu(x, y)
print(Res)
# MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)
# Вывод: статистической значимости нет, т.к pvalue > 5%

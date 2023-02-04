# Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.

import numpy as np 
import scipy.stats as st

a = np.array([150, 160, 165, 145, 155 ])
b = np.array([140, 155, 150, 130, 135 ])
Res = st.wilcoxon(a, b)
print(Res)
# WilcoxonResult(statistic=0.0, pvalue=0.0625)
# Вывод: статистических различий нет

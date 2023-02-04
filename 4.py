# Даны 3 группы учеников плавания.
# В 1 группе время на дистанцию 50 м составляют:
# 56, 60, 62, 55, 71, 67, 59, 58, 64, 67
# Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
# Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54
# Есть ли различия между группами?

import numpy as np 
import scipy.stats as st 

gr1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67 ])
gr2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53 ])
gr3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])
Res = st.kruskal(gr1, gr2, gr3)
print(Res)
# KruskalResult(statistic=5.465564058257224, pvalue=0.06503809985904942)
# Вывод: статистических различий нет
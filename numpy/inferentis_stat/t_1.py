import numpy as np
from scipy.stats import ttest_1samp

data=np.array([52.48357077, 49.30867849, 53.23844269, 57.61514928, 48.82923313, 48.82931522,
                 57.89606408, 53.83717365, 48.52156692, 52.47840057, 49.65614805, 53.80391238,
                 51.4536021, 53.34352827, 51.16911296, 51.17012286, 54.65648769, 49.16000721,
                 49.30532442, 54.02630684, 51.94099124, 47.79700287, 50.98728503, 50.25607035,
                 52.25505661, 48.71992414, 47.40106197, 52.30118364, 53.12593317, 47.76789008])
pop_mean=52
# Perform one-sample t-test
t_statistic, p_value = ttest_1samp(data, pop_mean)

print(f"t-Statistic: {t_statistic}")
print(f"p-Value: {p_value}")

alpha=0.05
if(p_value<alpha):
    print('we reject the null hypothese')
else:
    print('we fail to reject the null hypothese')

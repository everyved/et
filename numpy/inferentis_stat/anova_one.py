# from scipy.stats import f_oneway
from scipy.stats import *

# Example dataset for three groups
group1 = [52.4, 49.3, 53.2, 57.6, 48.8]
group2 = [48.5, 50.3, 53.8, 51.4, 54.0]
group3 = [47.7, 50.9, 52.2, 48.7, 47.4]

# Perform one-way ANOVA
f_statistic, p_value = f_oneway(group1, group2, group3)

print('\nf_statistic: ',f_statistic,'\np_value:',p_value)

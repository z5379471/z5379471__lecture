# WEEK 7
# 1. Pandas index ( .loc/ .iloc/ [])





print(ser)
#output:
# 2020‑01‑06    7.00
# 2020‑01‑07    7.10
# 2020‑01‑08    6.86
# 2020‑01‑09    6.95
# 2020‑01‑10    7.00
# 2020‑01‑13    7.02
# 2020‑01‑14    7.11
# 2020‑01‑15    7.04
# dtype: float64
# -->

# event studies in Finance
ser1 = ser.mean()
print(ser1)

# Import statsmodels.formula.api
import statsmodels.formula.api as smf

# Define the regression formula
FamaFrench_model = smf.ols(formula='____', data=FamaFrenchData)

# Fit the regression
FamaFrench_fit = FamaFrench_model.fit()

# Extract the adjusted r-squared
regression_adj_rsq = ____
print(regression_adj_rsq)


prc.sort_index(inplace = True)

rets = prc.loc['2020'].loc[:, 'Close'].pct_change()
print(rets)
avg_rets = rets.mean()
print(avg_rets)
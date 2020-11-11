# Financial-Logistic-Regression
Initial model to predict which companies are ready to be acquired

### Logistic Regression to Classify Companies’ Financial Results, Jan. 2019
A logistic regression model that predicts whether or not a company is ready to be acquired. Leverage, Net Working Capital and other financial indexes were used as features. A correlation analysis was made to avoid overfitting and the model had an f1-score of approx. 75% (Python, VBA)

## Further Information
The model is a multivariate logistic regression. It inputs features used to make the forecast and outputs a binary value (prepared or not prepared).\
At each iteration, the model updates the coefficients of the logarithmic curve, looking for the curve that best describes companies ready to go through an M&A process.\
Logistic regression was chosen for performing well with a small database and also for returning a binary forecast.

### Features
Management - Net profit Margin, EBITDA Growth\
Size - Net Equity, Net Revenue, Number of Employees\
Company Value - Enterprise Value (EV/marketEBITDA * EBITDA)\
Consolidation - Market Share, Market Herfindahl Index\
Leverage - Net Debt / EBITDA\
Liquidity - Current Assets - Stock / Current Liabilities\

### Data
Dataset contains 825 global energy enterprises (of which 233 have gone through a Merge & Acquisition process).\
The data almost exclusively follows the "Last Twelve Months" accounting standard.\
Further analysis can be found at M&Areadiness.xlsm.

### Methodology
Based on the paper “Predicting Takeover Targets, An Empirical Analysis of the European Market – Hendrik G. Froese”.\
Initially, data was harvested from Capital IQ's datasets, and processed using VBA.\
To select which features were actually relevant, features of pre-M&A firms were compared with features of post-M&A firms.\
To avoid overfitting, a pearson correlation analysis has been made.

### Evaluation
Performance was measured through precision, recall and f1-score.\
Precision mean: 75%
Recall mean: 81%
F1-Score mean: 75%

### Statistical problems / Improving points
The population's mean of the analysed data is unknown. Therefore, it's possible that the sample used does not represent the entire population. \
The companies' data should have been from the year they were sold, but this information was not available.\
The sample is relatively small, and most companies are large, which could result in a biased model.\


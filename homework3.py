#import pandas
import pandas as pa
import matplotlib.pyplot as plt
import pyEX as p
from statsmodels.tsa.stattools import adfuller
from random import random
from statsmodels.tsa.ar_model import AR

#define function for kpss test
from statsmodels.tsa.stattools import kpss
#get data
def GetData(fileName):
    return pa.read_csv(fileName, delim_whitespace=True, header=0, parse_dates=[0], index_col=0)

#read time series from the exchange.csv file 
exchangeRatesSeries = GetData('HW03_USD_TRY_Trading.txt')

#view last 60 records last minute and show the plot with rolling mean plot
firstmin = exchangeRatesSeries.head(-60)

rolling_mean = firstmin.Close.rolling(window=10).mean()
plt.plot(firstmin.Time, firstmin.Close, label='SMA', color='orange')
plt.plot(firstmin.Time, rolling_mean, label='1 min SMA', color='magenta')

plt.show()

def adf_test(timeseries):
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pa.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
       dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)

# i tried kpss but it didnt work
#define KPSS
#def kpss_test(timeseries):
#    print ('Results of KPSS Test:')
#    kpsstest = kpss(timeseries, regression='c')
#    kpss_output = pd.Series(kpsstest[0:3], index=['Test Statistic','p-value','Lags Used'])
#    for key,value in kpsstest[3].items():
#    kpss_output['Critical Value (%s)'%key] = value


#apply adf test and kpss test for last min on the series
adf_test(firstmin['Close'])


# estimation code
# contrived dataset
data = [x + random() for x in range(1, 100)]
# fit model
model = AR(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat)
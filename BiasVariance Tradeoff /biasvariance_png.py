import numpy as np
import matplotlib.pyplot as plt
import math as math
import random
import scipy.stats as st
from random import randrange, uniform
from matplotlib.backends.backend_pdf import PdfPages

noise = np.zeros(20)
x = np.zeros((100,20))
y = np.zeros((100,20))
mu, sigma = 0,1
for i in xrange(100):
	noise= np.random.normal(mu, sigma, 20)
	#noise.sort()
	x[i] = np.random.uniform(0, 5, 20)
	x[i].sort()
	y[i]=(2*(np.cos(2.8*x[i])))+7.5+noise


xv =np.random.uniform(0,5,100)
xv.sort()
yv = 2*(np.cos(2.8*xv))+7.5


coef1 = np.zeros((100,2))
coef2 = np.zeros((100,3))
coef3 = np.zeros((100,4))
coef4 = np.zeros((100,5))
coef5 = np.zeros((100,6))

for i in xrange(100):
	coef1[i] = np.polyfit(x[i],y[i],1)
	coef2[i] = np.polyfit(x[i],y[i],2)
	coef3[i] = np.polyfit(x[i],y[i],3)
	coef4[i] = np.polyfit(x[i],y[i],4)
	coef5[i] = np.polyfit(x[i],y[i],5)


    
plotx = np.linspace(0,5,100)
#plotx = np.arange(0,5,0.2) 

avgcoef1 = sum(coef1)/100
avgcoef2 = sum(coef2)/100
avgcoef3 = sum(coef3)/100
avgcoef4 = sum(coef4)/100
avgcoef5 = sum(coef5)/100

avgx = sum(x)/100;


fig = plt.figure(figsize=(11.6, 8), dpi=100)
plt.plot(plotx, np.polyval(coef1[0],plotx),color='black', label='Coef1 Fit')
plt.plot(plotx, np.polyval(coef1[1],plotx),color='black', label='Coef2 Fit')
plt.plot(plotx, np.polyval(coef1[2],plotx),color='black', label='Coef3 Fit')
plt.plot(plotx, np.polyval(coef1[3],plotx),color='black', label='Coef4 Fit')
plt.plot(plotx, np.polyval(coef1[4],plotx),color='black', label='Coef5 Fit')
plt.plot(plotx, np.polyval(avgcoef1,plotx),linestyle='--',color='red', label='Average Fit')
plt.xlabel('X-axis')
plt.ylabel('Polyfit 1')
plt.legend(loc='best', shadow=False)
plt.title('Polynomial Fit for Order 1')
fig.savefig('polyfit1.png') 
plt.close()


fig = plt.figure(figsize=(11.6, 8), dpi=100)
plt.plot(plotx, np.polyval(coef2[0],plotx),color='black', label='Coef1 Fit')
plt.plot(plotx, np.polyval(coef2[1],plotx),color='black', label='Coef2 Fit')
plt.plot(plotx, np.polyval(coef2[2],plotx),color='black', label='Coef3 Fit')
plt.plot(plotx, np.polyval(coef2[3],plotx),color='black', label='Coef4 Fit')
plt.plot(plotx, np.polyval(coef2[4],plotx),color='black', label='Coef5 Fit')
plt.plot(plotx, np.polyval(avgcoef2,plotx),linestyle='--',color='red', label='Average Fit')
plt.xlabel('X-axis')
plt.ylabel('Polyfit 2')
plt.legend(loc='best', shadow=False)
plt.title('Polynomial Fit for Order 2')
fig.savefig('polyfit2.png') 
plt.close()

fig = plt.figure(figsize=(11.6, 8), dpi=100)
plt.plot(plotx, np.polyval(coef3[0],plotx),color='black', label='Coef1 Fit')
plt.plot(plotx, np.polyval(coef3[1],plotx),color='black', label='Coef2 Fit')
plt.plot(plotx, np.polyval(coef3[2],plotx),color='black', label='Coef3 Fit')
plt.plot(plotx, np.polyval(coef3[3],plotx),color='black', label='Coef4 Fit')
plt.plot(plotx, np.polyval(coef3[4],plotx),color='black', label='Coef5 Fit')
plt.plot(plotx, np.polyval(avgcoef3,plotx),linestyle='--',color='red', label='Average Fit')
plt.xlabel('X-axis')
plt.ylabel('Polyfit 3')
plt.legend(loc='best', shadow=False)
plt.title('Polynomial Fit for Order 3')
fig.savefig('polyfit3.png') 
plt.close()

fig = plt.figure(figsize=(11.6, 8), dpi=100)
plt.plot(plotx, np.polyval(coef4[0],plotx),color='black', label='Coef1 Fit')
plt.plot(plotx, np.polyval(coef4[1],plotx),color='black', label='Coef2 Fit')
plt.plot(plotx, np.polyval(coef4[2],plotx),color='black', label='Coef3 Fit')
plt.plot(plotx, np.polyval(coef4[3],plotx),color='black', label='Coef4 Fit')
plt.plot(plotx, np.polyval(coef4[4],plotx),color='black', label='Coef5 Fit')
plt.plot(plotx, np.polyval(avgcoef4,plotx),linestyle='--',color='red', label='Average Fit')
plt.xlabel('X-axis')
plt.ylabel('Polyfit 4')
plt.legend(loc='best', shadow=False)
plt.title('Polynomial Fit for Order 4')
fig.savefig('polyfit4.png') 
plt.close()

fig = plt.figure(figsize=(11.6, 8), dpi=100)
plt.plot(plotx, np.polyval(coef5[0],plotx),color='black', label='Coef1 Fit')
plt.plot(plotx, np.polyval(coef5[1],plotx),color='black', label='Coef2 Fit')
plt.plot(plotx, np.polyval(coef5[2],plotx),color='black', label='Coef3 Fit')
plt.plot(plotx, np.polyval(coef5[3],plotx),color='black', label='Coef4 Fit')
plt.plot(plotx, np.polyval(coef5[4],plotx),color='black', label='Coef5 Fit')
plt.plot(plotx, np.polyval(avgcoef5,plotx),linestyle='--',color='red', label='Coef5 Fit')
plt.xlabel('X-axis')
plt.ylabel('Polyfit 5')
plt.legend(loc='best', shadow=False)
plt.title('Polynomial Fit for Order 5')
fig.savefig('polyfit5.png')   
plt.close()


bias = []     


bias.append((sum((np.polyval(avgcoef1,xv)-yv)**2)) / 100 ) 
bias.append((sum((np.polyval(avgcoef2,xv)-yv)**2)) / 100)
bias.append((sum((np.polyval(avgcoef3,xv)-yv)**2)) / 100)
bias.append((sum((np.polyval(avgcoef4,xv)-yv)**2)) / 100)
bias.append((sum((np.polyval(avgcoef5,xv)-yv)**2)) / 100)

varm = np.zeros((100,5))
for i in xrange(100):
    varm[i][0] = (sum((np.polyval(coef1[i],xv) - np.polyval(avgcoef1,xv))**2)) / 100
    varm[i][1] = (sum((np.polyval(coef2[i],xv) - np.polyval(avgcoef2,xv))**2)) / 100
    varm[i][2] = (sum((np.polyval(coef3[i],xv) - np.polyval(avgcoef3,xv))**2)) / 100
    varm[i][3] = (sum((np.polyval(coef4[i],xv) - np.polyval(avgcoef4,xv))**2)) / 100
    varm[i][4] = (sum((np.polyval(coef5[i],xv) - np.polyval(avgcoef5,xv))**2)) / 100

vars = sum(varm)/100

fig = plt.figure(figsize=(11.6, 8), dpi=100)
plt.plot(bias,'-.xk', label='Bias')
plt.plot(vars,'-xr', label = 'Variance')
plt.plot(bias+vars,'-.og', label = 'Error')
plt.xlabel('Order')
plt.ylabel('Error')
plt.legend(loc='best', shadow=False)
plt.title('Bias/Variance Dilemma')
fig.savefig('error.png') 
plt.close()    # close the figure
import numpy as np
import matplotlib.pyplot as plt
from LocalModule.Integration import *
import pandas as pd

t0 = 0
N0 = 100

k = 0.25*10**-11

h = 5*10**7     # △T
n = (3.5*10**9/h)+1

t1 = t0
N1 = N0
Nd = N0

tt = [t0]
NN = [N0]
zz = [N0]


def m(t, N_y):
    s = k*N_y**2
    return s


i = 0
while i < n-1:
    m1 = m(t1, Nd)
    Nd = Nd + h*m1 
    t1 = t1 + h
    m2 = m(t1, Nd)

    N1 = N1 + h*(m1 + m2)/2

    tt.append(t1)
    NN.append(N1)

    z = 1/(0.01-k*t1)
    zz.append(z)
    i = i+1


df = pd.DataFrame({'Time(s)': tt, 'N_2': NN})
df.to_excel(r'C:\Users\Anik Mandal\PycharmProjects\Sem_5\val_8_8_4.xlsx')
print(df)


plt.plot(tt, NN, 'r')
plt.plot(tt, zz, '--c')
plt.xlabel('Time(s)')

plt.ylabel('N')
plt.legend(['Curve through RK2 method', 'Actual Curve'])
plt.grid()
plt.show()

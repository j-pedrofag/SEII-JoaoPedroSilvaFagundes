from control.matlab import *
import numpy as np
import matplotlib.pyplot as plt
import math

def x_dot(t,x,u):
    A = np.array( [[-2., -9.],\
                  [ 1.,  0.]])
    B = np.array([[1.],\
                 [0.]])
    xkp1 = A @ x + B @ u
    return xkp1

def rk4(tk,h,xk,uk):
    xk = xk.reshape([2,1])
    uk = uk.reshape([1,1])
    k1 = x_dot(tk,xk,uk)
    k2 = x_dot(tk+h/2.0,xk+h*k1/2.0,uk)
    k3 = x_dot(tk+h/2.0,xk+h*k2/2.0,uk)
    k4 = x_dot(tk+h,xk+h*k3,uk)
    xkp1 = xk + (h/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)
    return xkp1.reshape([2,])

def compensador(G,Ms,ts=2):
	zeta = np.sqrt(np.log(Ms)**2/(np.pi**2+np.log(Ms)**2))
	wn = 4/(zeta*ts)
	polo = [zeta*wn,wn*np.sqrt(1-zeta*zeta)]
	poloComplex = -polo[0]+polo[1]*1j
	
	theta = math.atan2(polo[1],polo[0])
	phi = np.pi/2 - theta
	beta = (np.pi - theta)/2
	gamma = theta+beta-phi/2-np.pi/2
	a = polo[0] + polo[1]*np.tan(gamma)
	b = polo[0] + polo[1]*np.tan(gamma+phi)
	C = tf([1,a],[1,b])
	K = abs(1/(evalfr(C,poloComplex)*evalfr(G,poloComplex)))
	C = K*C
	return tf(C)

#Parâmetros

G = tf([9],[1,2,9])

#Letra a

C = compensador(G,0.1,2)
print(C)
T = feedback(C*G,1)
t = np.arange(0,10,1e-3)
u = t*0+1
y,x,*_ = lsim(T,u,t)

plt.figure('a')
plt.plot(x,y)
plt.title('Resposta ao degrau')
plt.grid()

#Letra b

Gss = tf2ss(G)
Ts = 0.01
Cz = c2d(C,Ts,method = 'zoh')
h = 1e-4
maxT = 10
mult = Ts/h
t = np.arange(0,maxT,h)
tu = np.arange(0,maxT,Ts)


x = np.zeros([2,len(t)])
u = np.zeros([len(tu)])
r = np.ones([len(t)-1])
y = np.zeros([len(t)-1])

tam = len(t)-1

ek_1 = 0
uk_1 = 0
p = 0
for k in range(tam):
    y[k] = Gss.C @ x[:,k]
    if (k%mult)==0:
        ek = r[k]-y[k]
        u[p] = 0.8607*uk_1 + 10*ek - 9.9257*ek_1 #Ts = 0,01
        ek_1 = ek
        uk_1 = u[p]
        p += 1
    x[:,k+1] = rk4(t[k],h,x[:,k],u[p-1])

plt.figure('b.1')
plt.subplot(2,1,1)
plt.plot(t,x[0,:])
plt.subplot(2,1,2)
plt.plot(t,x[1,:])

plt.figure('b.2')
plt.plot(t[0:-1],y)
plt.plot(t[0:-1],r)
plt.title('Runge- Kutta comparando degrau y =1')

plt.figure('b.3')
plt.plot(tu[0:len(u)],u)


plt.show()
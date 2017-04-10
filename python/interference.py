import matplotlib.pyplot as plt
import numpy as np

def SlowdownPlot(u, x):
    hpr_x = np.linspace(0, 1, num=1000, endpoint=False)
    # high bandwidth
    y = u - x

    #high priority bandwidth
    r1 = x * hpr_x
    #low priority bandwidth: y + low proiority bandwidth of x
    r2 = x * (1-hpr_x) + y

    # M/M/1: preemptive Priority queue with tow customer classes
    l_hp=1.0/(1-r1)
    l_lp=1.0/((1-r1)*(1-r1-r2))

    # M/M/1: nonpreemptive Priority queue with tow customer classes
    # high priority latency
    #l_hp=(1+r2)/(1-r1)
    # low priority latency
    #l_lp=(1-r1*(1-r1-r2))/((1-r1)*(1-r1-r2))

    perf_hp = 1.0/l_hp
    perf_lp = 1.0/l_lp
    # define performance is the reverse of average responds time
    perf_x_alone=1.0/(1.0/(1-x))

    #shared performance with priority scheduling
    perf_x_share_p=hpr_x*perf_hp + (1-hpr_x)*perf_lp

    #shared whith priority slowdwon to alone
    slowdown_x_y=perf_x_alone/perf_x_share_p
    slowdown_y_x=u/y

    #plot lines x
    #plt.plot(x, slowdown_x_y, 'red')
    #plt.plot(x, slowdown_y_x, 'blue')
    #plot lines based hpr_x
    #plt.plot(hpr_x, slowdown_x_y, 'red')
    #plt.plot(hpr_x, slowdown_y_x, 'blue')

    slowdown_min = abs(slowdown_x_y-slowdown_y_x).argmin()
    return slowdown_x_y[slowdown_min], perf_x_share_p[slowdown_min],\
            y, hpr_x[slowdown_min]

# max untility for acceptablly worse latency
# assump peak bandwidth equals 1
u = 0.8

# latency-sensitive group bandwidth (low bandwidth share)
x = np.linspace(0.001,u,num=1000,endpoint=False)

fig, axs = plt.subplots(2,2)
for i in x:
    sd, perf_x, y, hpr = SlowdownPlot(u, i)
    axs[0,0].plot(i, sd, 'ro')
    axs[0,1].plot(i, perf_x, 'bo')
    axs[1,0].plot(i, hpr, 'ro')
    axs[1,0].plot(i, i/(i+y), 'go')
    axs[1,1].plot(i, hpr*i, 'bo')

axs[0,0].set_title('Slowdown')
axs[0,1].set_title('Performance L-S')
axs[1,0].set_title('High Priority Ratio')
axs[1,1].set_title('High Priority Rate')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

def SlowdownPlot(u, x):
    hpr_x = np.linspace(0, 1, num=1000, endpoint=False)
    # high bandwidth
    y = u - x

    #high priority bandwidth
    r1 = x * hpr_x
    #r1 = x * hpr_x + y * (1-hpr_x)*y
    #low priority bandwidth: y + low proiority bandwidth of x
    r2 = x * (1-hpr_x) + y
    #r2 = x * (1-hpr_x) + y * hpr_x

    # M/M/1: preemptive Priority queue with tow customer classes
    # high priority latency
    #l_hp=1.0/(1-r1)
    # low priority latency
    #l_lp=1.0/((1-r1)*(1-r1-r2))

    # M/M/1: nonpreemptive Priority queue with tow customer classes,
    #       where clients are served one at a time to completion.
    #high priority latency
    l_hp=(1+r2)/(1-r1)
    #low priority latency
    l_lp=(1-r1*(1-r1-r2))/((1-r1)*(1-r1-r2))

    perf_hp = 1.0/l_hp
    perf_lp = 1.0/l_lp
    # define performance is the reverse of average responds time
    perf_x_alone=1.0/(1.0/(1-x))
    perf_y_alone=u
    #perf_y_alone=1.0/(1.0/(1-u))

    #shared performance with priority scheduling
    #perf_x_share_p=hpr_x*perf_hp + (1-hpr_x)*perf_lp
    perf_x_share_p=1.0/(hpr_x*l_hp+(1-hpr_x)*l_lp)
    perf_y_share_p=y
    #perf_y_share_p=1.0/l_lp

    #shared whith priority slowdwon to alone
    slowdown_x_y=perf_x_alone/perf_x_share_p
    slowdown_y_x=perf_y_alone/perf_y_share_p

    slowdown_min = abs(slowdown_x_y-slowdown_y_x).argmin()
    return slowdown_x_y[slowdown_min], \
            slowdown_y_x, \
            perf_x_share_p[slowdown_min], \
            perf_y_share_p, \
            hpr_x[slowdown_min], \
            perf_lp[slowdown_min], perf_hp[slowdown_min], \
            l_lp[slowdown_min], l_hp[slowdown_min]

# max untility for acceptablly worse latency
# assump peak bandwidth equals 1
u = 0.5

# latency-sensitive group bandwidth (low bandwidth share)
x = np.linspace(0.001,u/2,num=1000,endpoint=False)

fig, axs = plt.subplots(3,2)
for i in x:
    sd_x,sd_y,perf_x_share,perf_y_share,hpr,lp,hp,l_lp,l_hp = SlowdownPlot(u, i)
    axs[0,0].plot(i, sd_x, 'ro')
    axs[0,0].plot(i, sd_y, 'bo')
    axs[0,1].plot(i, perf_x_share, 'ro')
    axs[0,1].plot(i, perf_y_share, 'bo')
    axs[1,0].plot(i, hpr, 'ro')
    axs[1,1].plot(i, hpr*i, 'bo')
    axs[2,0].plot(i, hp,'ro')
    axs[2,0].plot(i, lp,'bo')
    axs[2,1].plot(i, l_hp, 'ro')
    axs[2,1].plot(i, l_lp, 'bo')

axs[0,0].set_title('Slowdown')
axs[0,1].set_title('Performance')
axs[1,0].set_title('High Priority Ratio')
axs[1,1].set_title('High Priority Rate')
axs[2,0].set_title('High Priority Performace')
axs[2,1].set_title('High Priority Latency')
plt.show()

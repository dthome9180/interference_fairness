import matplotlib.pyplot as plt
import numpy as np

# low bandwidth
x = np.linspace(0.001,1.0,num=1000,endpoint=False)

# max untility for acceptablly worse latency
#u = [0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]
u = [0.8]
"""
No priority scheduling
"""
"""
for t in u:
# high bandwidth
    y = t - x
#slowdown(x|y)
    plt.plot(x, 1/(1-(y/(1-x))))
#slowdown(y|x)
    plt.plot(x, 1/(1-(x/(1-y))))
"""
for t in u:
    # high bandwidth
    y = t - x
    # high priority ratio in x (latency sensitive)
    hpr_x = ((1/x)/((1/x)+(1/y)))
    # high priority bandwidth
    #r1 = x * hpr_x + y * (1-hpr_x) #this priority scheduling maybe not feasible
                                    #becasue the order between two queue need 
                                    #considered
    r1 = x * hpr_x
    #low priority bandwidth: y + low proiority bandwidth of x
    #r2 = x * (1-hpr_x) + y * hpr_x #not feasible see corresponding comments
    r2 = x * (1-hpr_x) + y
    # high priority latency
    l_hp=(1+r2)/(1-r1)
    # low priority latency
    l_lp=(1-r1*(1-r1-r2))/((1-r1)*(1-r1-r2))
    
    perf_x_alone=1-x
    perf_y_alone=1-y
    #shared performance with priority scheduling
    perf_x_share_p=1.0/(l_hp*hpr_x+l_lp*(1-hpr_x))
    perf_y_share_p=1.0/l_lp
    #shared performane without priority scheduling
    perf_share=1.0/(1.0/(1-t))
    
    slowdown_x_y=perf_x_alone/perf_x_share_p
    slowdown_y_x=perf_y_alone/perf_y_share_p
    #shared whith priority slowdwon to alone
    plt.plot(x, slowdown_x_y, 'red')
    plt.plot(x, slowdown_y_x, 'blue')
    #shared with priority slowdown to shared without priority
    plt.plot(x, perf_share/perf_x_share_p, 'black')
    plt.plot(x, perf_share/perf_y_share_p, 'green')

plt.show()


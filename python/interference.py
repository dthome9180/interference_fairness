import matplotlib.pyplot as plt
import numpy as np

# overall bandwidth for queue, peak bandwidth equals 1;
#u = [0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]
BW = 0.8

# bandwidth ratio of latency-sensitive group, 0 < p < 1
p = np.linspace(0.001,BW/2,num=1000,endpoint=False)

def FairnessPoint(BW, p):
    # latency-sensitive group badwidth and performance alone
    LowBW = BW * p
    Perf_LowBW_alone = 1.0/(1-LowBW)
    # bandwidth intensive group bandwidth and performance alone
    HighBW = BW - LowBW
    Perf_HighBW_alone = 1.0/(1-HighBW)

    # high priority ratio in x (latency sensitive)
    hpr = np.linspace(0,1.0,num=1000,endpoint=True)

    SlowdownPair = {}

    # assign h * LowBW high priority, others low priority
    for h in hpr:
        # high priority bandwidth
        HighPriBW = LowBW * h
        #low priority bandwidth
        LowPriBW = LowBW * (1-h) + HighBW

        HighPriRatio = HighPriBW/1
        LowPriRatio = LowPriBW/1

        # high priority Average Response Time (ART)
        ART_HighPriBW = (1+LowPriRatio)/(1-HighPriRatio)/1
        # low priority Average Response Time (ART)
        ART_LowPriBW = (1-HighPriRatio*(1-HighPriRatio-LowPriRatio))/\
                        ((1-HighPriRatio)*(1-HighPriRatio-LowPriRatio))/1

        #shared performance with priority scheduling
        ART_LowBW = ART_HighPriBW*h + ART_LowPriBW*(1-h)
        ART_HighBW = ART_LowPriBW

        Perf_LowBW = 1.0/ART_LowBW
        Perf_HighBW = 1.0/ART_HighBW

        Slowdown_LowBW = Perf_LowBW_alone/Perf_LowBW
        Slowdown_HighBW = Perf_HighBW_alone/Perf_HighBW

        #shared whith priority slowdwon to alone
        plt.plot(h, Slowdown_LowBW, 'red')
        plt.plot(h, Slowdown_HighBW, 'blue')

        SlowdownPair[h] = [Slowdown_LowBW, Slowdown_HighBW]

    #SlowdownFairDiff = abs(SlowdownPair[0][0]-SlowdownPair[0][1])
    #SlowdownFairPoint = 0
    return #SlowdownFairPoint

"""
    for t in hpr:
        if abs(SlowdownPair[t][0]-SlowdownPair[t][1])<SlowdownFairDiff:
            SlowdownFairDiff = abs(t[0][0]-t[0][1])
            SlowdownFairPoint = t
"""


FairnessPoint(BW,p)
print x

plt.show()

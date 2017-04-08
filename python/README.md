Long tail problem is a key issue that affects the performance of today's distributed data centers. The main reason is the existence of queues everywhere, and the fairness scheduling algorithm is used to allocate weights by actual bandwidth.Latency-sensitive applicationsare often require small bandwidth demand, but need allocating overprovisonal reserved bandwidth to ensure their latency. This makes small utilization of overall system.

To this end, we present a new priority shceduling algoritm for long tail problem without overprovisioned bandwidth allocation.

For a specifed overall bandwidth B, we partiton applications into two groups, latency-sensitive group and bandwidth-intensive one, which partition ratio is named p, 0 < p < 1. We assign high priority to subpart of latency-sensitive group demands, which ratio named h, 0 < h <1. Say, we give high priority to first B * p * h bandwidth of latency-sensitive application within each time interval, and the others B * p * (1-h) + B * (1-p) bandwidth low priority.
#!/usr/bin/env python3

import mesa
import pandas as pd
import matplotlib.pyplot as plt
from traffic_model import (
    TrafficModel,
    obstaculoAgent,
    banquetaAgent,
    PeatonAgent,
    IceCreamAgent,
    CarAgent,
)

batch_run_params = {
    "width": [30],
    "height": [30],
    "num_agents": [20],
}

data = mesa.batch_run(
    TrafficModel,
    batch_run_params,
    iterations=20,  # Number of iterations for each parameter combination
    max_steps=150,  # Number of steps for each run
)


df = pd.DataFrame(data)

df.to_csv("TrafficModel_Data.csv", index=False)

grouped_data = df.groupby('iteration').mean()

plt.figure(figsize=(10, 6))
# plt.plot(grouped_data['pasos'], label='Pasos')
plt.plot(grouped_data['chocados'], label='Peatones chocados')
plt.title('Peatones con semaforos en posición A')
plt.xlabel('Iteration')
plt.ylabel('Count')
plt.legend()
plt.show()

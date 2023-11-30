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
    "num_peatones": [30],
    "num_autos": [10],
}

data = mesa.batch_run(
    TrafficModel,
    batch_run_params,
    iterations=20,
    max_steps=150,
)

df = pd.DataFrame(data)

df.to_csv("TrafficModel_Data.csv", index=False)

grouped_data = df.groupby("iteration").mean()

plt.figure(figsize=(10, 6))
plt.bar(grouped_data.index, grouped_data["chocados"], label="Peatones chocados")
plt.title("Semaforos en posición B")
plt.xlabel("Iteración")
plt.ylabel("Cantidad")
plt.legend()
plt.savefig("PosicionB_Graph.png")
plt.show()

import mesa

# Data manipulation and analysis.
from traffic_model import (
    TrafficModel,
    obstaculoAgent,
    banquetaAgent,
    PeatonAgent,
    IceCreamAgent,
    CarAgent,
)


def agent_portrayal(agent):
    portrayal = {}
    if isinstance(agent, obstaculoAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "#5A9BD5"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True

    if agent.estado == 0:
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True
    elif agent.estado == 1:
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "green"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True
    if isinstance(agent, PeatonAgent):
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "#FF79C6"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.5
        portrayal["Filled"] = True

    if isinstance(agent, banquetaAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True
    if isinstance(agent, CarAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "#282A36"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True
    if isinstance(agent, IceCreamAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "#F1FA8C"
        portrayal["Layer"] = 1
        portrayal["Filled"] = True
        if agent.direccion in ["norte", "sur"]:
            portrayal["h"] = 2
            portrayal["w"] = 1
        elif agent.direccion in ["este", "oeste"]:
            portrayal["h"] = 1
            portrayal["w"] = 2

    return portrayal


grid = mesa.visualization.CanvasGrid(agent_portrayal, 30, 30)
server = mesa.visualization.ModularServer(
    TrafficModel,
    [grid],
    "Car Model",
    {"width": 30, "height": 30, "num_agents": 5},
)
server.port = 8521  # the default
server.launch()

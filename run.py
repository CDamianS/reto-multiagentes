import mesa
from mesa import Model
from mesa import Agent

# Data manipulation and analysis.
from mapa import (
    CarModel,
    obstaculoAgent,
    banquetaAgent, semaforoVAgent
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

    if isinstance(agent, banquetaAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True

    

    return portrayal


grid = mesa.visualization.CanvasGrid(agent_portrayal, 30, 30)
server = mesa.visualization.ModularServer(
    CarModel, [grid], "Car Model", {"width": 30, "height":30, "num_agents": 5}, 
)
server.port = 8521  # the default
server.launch()
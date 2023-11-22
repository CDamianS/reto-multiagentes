#!/usr/bin/env python3

#------------------------------------------------Imports---------------------------------------------------------------
from mesa import Agent
from mesa import Model
from mesa.time import RandomActivation
import mesa
import random
import networkx as nx
import json
import requests
#Arrays del diseño mapa. 

edificios = [(0,0),(0,1),(0,2), (1,0),(1,1),(1,2), (2,0),(2,1),(2,2),
             (0,10),(1,10),(2,10), (0,11),(1,11),(2,11),
             (0,19),(1,19),(2,19), (0,20),(1,20),(2,20),
             (0,28),(1,28),(2,28),(0,29),(1,29),(2,29),
             
             (10,0), (11,0),(12,0),(13,0),(14,0), (10,1), (11,1),(12,1),(13,1),(14,1), (10,2), (11,2),(12,2),(13,2),(14,2),
             
             (10,10), (11,10),(12,10),(13,10),(14,10), (15,10), (16,10),(17,10),(18,10),(19,10),(20,10),
             (10,11), (11,11),(12,11),(13,11),(14,11), (15,11), (16,11),(17,11),(18,11),(19,11),(20,11),
             (10,12), (11,12),(12,12),(13,12),(14,12), (15,12), (16,12),(17,12),(18,12),(19,12),(20,12),
             (10,13), (11,13),(12,13),(13,13),(14,13), (15,13), (16,13),(17,13),(18,13),(19,13),(20,13),
             (10,14), (11,14),(12,14),(13,14),(14,14), (15,14), (16,14),(17,14),(18,14),(19,14),(20,14),
             (10,15), (11,15),(12,15),(13,15),(14,15), (15,15), (16,15),(17,15),(18,15),(19,15),(20,15),
             (10,16), (11,16),(12,16),(13,16),(14,16), (15,16), (16,16),(17,16),(18,16),(19,16),(20,16),
             (10,17), (11,17),(12,17),(13,17),(14,17), (15,17), (16,17),(17,17),(18,17),(19,17),(20,17),
             (10,18), (11,18),(12,18),(13,18),(14,18), (15,18), (16,18),(17,18),(18,18),(19,18),(20,18),
             (10,19), (11,19),(12,19),(13,19),(14,19), (15,19), (16,19),(17,19),(18,19),(19,19),(20,19),
             (10,20), (11,20),(12,20),(13,20),(14,20), (15,20), (16,20),(17,20),(18,20),(19,20),(20,20),

             (10,28), (11,28), (12,28), (10,29), (11,29), (12,29),

             (18,28), (19,28), (20,28), (18,29), (19,29),  (20, 29),

             (20,0), (20,1), (20,2),

             (28,0), (29,0), (28,1), (29,1), (28,2), (29,2),

             (28,10), (29,10), (28,11), (29,11),

             (28,20), (29,20), (28,19), (29,19),

             (28,29), (29,29), (28,28), (29,28),
             ]
banqueta = [(0, 3), (1, 3), (2,3), (3,3), (3,2),(3,1), (3,0),
            
            (0, 9), (1, 9), (2,9), (3,9),(0, 12), (1, 12), (2,12), (3,12),(3,10),(3,11),

            (0, 18), (1, 18), (2,18), (3,18), (0,21), (1,21), (2,21), (3,21),(3, 19),(3,20),

            (0,27), (1,27), (2,27), (3,27), (3,28), (3,29),

            (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 16), (9, 17), (9, 18), (9, 19), (9, 20), (9, 21),
            (21, 9), (21, 10), (21, 11), (21, 12), (21, 13), (21, 14), (21, 15), (21, 16), (21, 17), (21, 18), (21, 19), (21, 20), (21, 21),
            (10, 21), (11, 21), (12, 21), (13, 21), (14, 21), (15, 21), (16, 21), (17, 21), (18, 21), (19, 21), (20, 21),
            (10, 9), (11, 9), (12, 9), (13, 9), (14, 9), (15, 9), (16, 9), (17, 9), (18, 9), (19, 9), (20, 9),

            (9,0), (9,1),(9,2),(9,3), (15,0), (15,1),(15,2),(15,3), (10,3),(11,3),(12,3),(13,3),(14,3),

            (19, 0), (19,1), (19,2), (19,3), (21, 0), (21,1), (21,2), (21,3), (20,3),

            (9,27),(9,28),(9,29), (13,27),(13,28),(13,29), (10,27),(11,27),(12,27),

            (17,27), (17,28), (17,29), (21,27), (21,28), (21,29), (18,27),(19,27),(20,27),

            (27,0), (27,1), (27,2), (27,3),(27,9), (27,10), (27,11), (27,12),(27,18), (27,19), (27,20), (27,21),
            (27,29), (27,28), (27,27),

            (28,3),(29,3),(28,9),(29,9),(28,12),(29,12),(28,18),(29,18),(28,21),(29,21),(28,27),(29,27),
            ]

semaforosV = [(4,3),(5,3),(6,3),(7,3),(8,3), (4,9),(5,9),(6,9),(7,9),(8,9), (4,21),(5,21),(6,21),(7,21),(8,21), (4,27),(5,27),(6,27),(7,27),(8,27),
              (22,3),(23,3),(24,3),(25,3),(26,3), (22,9),(23,9),(24,9),(25,9),(26,9), (22,21),(23,21),(24,21),(25,21),(26,21), (22,27),(23,27),(24,27),(25,27),(26,27),]

semaforosH = [(3,4),(3,5),(3,6),(3,7),(3,8),(9,4),(9,5),(9,6),(9,7),(9,8),(21,4),(21,5),(21,6),(21,7),(21,8),(27,4),(27,5),(27,6),(27,7),(27,8),
              (3,22),(3,23),(3,24),(3,25),(3,26),(9,22),(9,23),(9,24),(9,25),(9,26),(21,22),(21,23),(21,24),(21,25),(21,26),(27,22),(27,23),(27,24),(27,25),(27,26),
              (3,13),(3,14),(3,15),(3,16),(3,17),(27,13),(27,14),(27,15),(27,16),(27,17),]

puntos_llegada_peatones = []

puntos_salida_peatones = []

puntos_llegada_autos = []

puntos_salida_autos = []

#-------------------------------------------------------------------------------------

#----------------------------------------Agentes-------------------------------------------------------
class obstaculoAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.agentT = 0  # Obstacle
        self.estado = 3

    def step(self):
        pass

class banquetaAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.agentT = 0  # Obstacle
        self.estado = 3

    def step(self):
        pass    


class semaforoVAgent(Agent): #Semaforos Verticales
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.agentT = 2  # Semaforo
        self.estado = 1  # Color del semaforo 0 = rojo 1 = verde 2 = amarillo
        self.paso = 0

    def change(self):
        self.estado = 0

    def changeB(self):
        self.estado = 1

    def add(self):
        self.paso += 1

    def step(self):
        if (self.paso % 10) == 0:
            if self.estado == 0:
                self.change()
            else:
                self.changeB()
        self.add()
        pass


class semaforoRAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.agentT = 2  # Semaforo
        self.estado = 0  # Color del semaforo 0 = rojo 1 = verde 2 = amarillo
        self.paso = 0

    def change(self):
        self.estado = 1

    def changeB(self):
        self.estado = 0

    def add(self):
        self.paso += 1

    def step(self):
        if (self.paso % 10) == 0:
            if self.estado == 0:
                self.change()
            else:
                self.changeB()
        self.add()
        pass

# -------------------------------------------------------------MODEL---------------------------------------------------------------------
class CarModel(Model):
    def __init__(self, width, height, num_agents):
        self.num_agents = num_agents
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        o = 0

        # Create the obstacles
        for i in edificios:
            # print("Mapa")
            pavA = obstaculoAgent(o, self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA, (x, y))
            o += 1

            # Create the obstacles
        for i in banqueta:
            # print("Mapa")
            pavA = banquetaAgent(o, self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA, (x, y))
            o += 1

        for i in semaforosV:
            # print("Mapa")
            pavA = semaforoVAgent(o, self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA, (x, y))
            o += 1

        for i in semaforosH:
            # print("Mapa")
            pavA = semaforoRAgent(o, self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA, (x, y))
            o += 1
        


    def step(self):
        self.schedule.step()
        self.step_count += 1  # Incrementar el contador de pasos en cada llamada a step
        # Condición de finalización: terminar después de 100 pasos
        if self.step_count >= 100:
            self.running = False
        self.send_positions_to_server()  # Añadir esta línea al final de step
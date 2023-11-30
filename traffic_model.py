#!/usr/bin/env python3

# ------------------------------------------------Imports---------------------------------------------------------------
from mesa import Agent
from mesa import Model
from mesa.time import RandomActivation
import mesa
import random
import networkx as nx
import json
import requests

# Arrays del diseño mapa.

edificios = [
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 0),
    (2, 1),
    (2, 2),
    (0, 10),
    (1, 10),
    (2, 10),
    (0, 11),
    (1, 11),
    (2, 11),
    (0, 19),
    (1, 19),
    (2, 19),
    (0, 20),
    (1, 20),
    (2, 20),
    (0, 28),
    (1, 28),
    (2, 28),
    (0, 29),
    (1, 29),
    (2, 29),
    (10, 0),
    (11, 0),
    (12, 0),
    (13, 0),
    (14, 0),
    (10, 1),
    (11, 1),
    (12, 1),
    (13, 1),
    (14, 1),
    (10, 2),
    (11, 2),
    (12, 2),
    (13, 2),
    (14, 2),
    (10, 10),
    (11, 10),
    (12, 10),
    (13, 10),
    (14, 10),
    (15, 10),
    (16, 10),
    (17, 10),
    (18, 10),
    (19, 10),
    (20, 10),
    (10, 11),
    (11, 11),
    (12, 11),
    (13, 11),
    (14, 11),
    (15, 11),
    (16, 11),
    (17, 11),
    (18, 11),
    (19, 11),
    (20, 11),
    (10, 12),
    (11, 12),
    (12, 12),
    (13, 12),
    (14, 12),
    (15, 12),
    (16, 12),
    (17, 12),
    (18, 12),
    (19, 12),
    (20, 12),
    (10, 13),
    (11, 13),
    (12, 13),
    (13, 13),
    (14, 13),
    (15, 13),
    (16, 13),
    (17, 13),
    (18, 13),
    (19, 13),
    (20, 13),
    (10, 14),
    (11, 14),
    (12, 14),
    (13, 14),
    (14, 14),
    (15, 14),
    (16, 14),
    (17, 14),
    (18, 14),
    (19, 14),
    (20, 14),
    (10, 15),
    (11, 15),
    (12, 15),
    (13, 15),
    (14, 15),
    (15, 15),
    (16, 15),
    (17, 15),
    (18, 15),
    (19, 15),
    (20, 15),
    (10, 16),
    (11, 16),
    (12, 16),
    (13, 16),
    (14, 16),
    (15, 16),
    (16, 16),
    (17, 16),
    (18, 16),
    (19, 16),
    (20, 16),
    (10, 17),
    (11, 17),
    (12, 17),
    (13, 17),
    (14, 17),
    (15, 17),
    (16, 17),
    (17, 17),
    (18, 17),
    (19, 17),
    (20, 17),
    (10, 18),
    (11, 18),
    (12, 18),
    (13, 18),
    (14, 18),
    (15, 18),
    (16, 18),
    (17, 18),
    (18, 18),
    (19, 18),
    (20, 18),
    (10, 19),
    (11, 19),
    (12, 19),
    (13, 19),
    (14, 19),
    (15, 19),
    (16, 19),
    (17, 19),
    (18, 19),
    (19, 19),
    (20, 19),
    (10, 20),
    (11, 20),
    (12, 20),
    (13, 20),
    (14, 20),
    (15, 20),
    (16, 20),
    (17, 20),
    (18, 20),
    (19, 20),
    (20, 20),
    (10, 28),
    (11, 28),
    (12, 28),
    (10, 29),
    (11, 29),
    (12, 29),
    (18, 28),
    (19, 28),
    (20, 28),
    (18, 29),
    (19, 29),
    (20, 29),
    (20, 0),
    (20, 1),
    (20, 2),
    (28, 0),
    (29, 0),
    (28, 1),
    (29, 1),
    (28, 2),
    (29, 2),
    (28, 10),
    (29, 10),
    (28, 11),
    (29, 11),
    (28, 20),
    (29, 20),
    (28, 19),
    (29, 19),
    (28, 29),
    (29, 29),
    (28, 28),
    (29, 28),
]
banqueta = [
    (0, 3),
    (1, 3),
    (2, 3),
    (3, 3),
    (3, 2),
    (3, 1),
    (3, 0),
    (0, 9),
    (1, 9),
    (2, 9),
    (3, 9),
    (0, 12),
    (1, 12),
    (2, 12),
    (3, 12),
    (3, 10),
    (3, 11),
    (0, 18),
    (1, 18),
    (2, 18),
    (3, 18),
    (0, 21),
    (1, 21),
    (2, 21),
    (3, 21),
    (3, 19),
    (3, 20),
    (0, 27),
    (1, 27),
    (2, 27),
    (3, 27),
    (3, 28),
    (3, 29),
    (9, 9),
    (9, 10),
    (9, 11),
    (9, 12),
    (9, 13),
    (9, 14),
    (9, 15),
    (9, 16),
    (9, 17),
    (9, 18),
    (9, 19),
    (9, 20),
    (9, 21),
    (21, 9),
    (21, 10),
    (21, 11),
    (21, 12),
    (21, 13),
    (21, 14),
    (21, 15),
    (21, 16),
    (21, 17),
    (21, 18),
    (21, 19),
    (21, 20),
    (21, 21),
    (10, 21),
    (11, 21),
    (12, 21),
    (13, 21),
    (14, 21),
    (15, 21),
    (16, 21),
    (17, 21),
    (18, 21),
    (19, 21),
    (20, 21),
    (10, 9),
    (11, 9),
    (12, 9),
    (13, 9),
    (14, 9),
    (15, 9),
    (16, 9),
    (17, 9),
    (18, 9),
    (19, 9),
    (20, 9),
    (9, 0),
    (9, 1),
    (9, 2),
    (9, 3),
    (15, 0),
    (15, 1),
    (15, 2),
    (15, 3),
    (10, 3),
    (11, 3),
    (12, 3),
    (13, 3),
    (14, 3),
    (19, 0),
    (19, 1),
    (19, 2),
    (19, 3),
    (21, 0),
    (21, 1),
    (21, 2),
    (21, 3),
    (20, 3),
    (9, 27),
    (9, 28),
    (9, 29),
    (13, 27),
    (13, 28),
    (13, 29),
    (10, 27),
    (11, 27),
    (12, 27),
    (17, 27),
    (17, 28),
    (17, 29),
    (21, 27),
    (21, 28),
    (21, 29),
    (18, 27),
    (19, 27),
    (20, 27),
    (27, 0),
    (27, 1),
    (27, 2),
    (27, 3),
    (27, 9),
    (27, 10),
    (27, 11),
    (27, 12),
    (27, 18),
    (27, 19),
    (27, 20),
    (27, 21),
    (27, 29),
    (27, 28),
    (27, 27),
    (28, 3),
    (29, 3),
    (28, 9),
    (29, 9),
    (28, 12),
    (29, 12),
    (28, 18),
    (29, 18),
    (28, 21),
    (29, 21),
    (28, 27),
    (29, 27),
    # Camellones horizontales
    (0, 6),
    (1, 6),
    (2, 6),
    (3, 6),
    (9, 6),
    (10, 6),
    (11, 6),
    (12, 6),
    (13, 6),
    (14, 6),
    (15, 6),
    (19, 6),
    (20, 6),
    (21, 6),
    (27, 6),
    (28, 6),
    (29, 6),
    (0, 24),
    (1, 24),
    (2, 24),
    (3, 24),
    (9, 24),
    (10, 24),
    (11, 24),
    (12, 24),
    (13, 24),
    (17, 24),
    (18, 24),
    (19, 24),
    (20, 24),
    (21, 24),
    (27, 24),
    (28, 24),
    (29, 24),
    (0, 15),
    (1, 15),
    (2, 15),
    (3, 15),
    (27, 15),
    (28, 15),
    (29, 15),
    # Camellones verticales
    (6, 0),
    (6, 1),
    (6, 2),
    (6, 3),
    (6, 9),
    (6, 10),
    (6, 11),
    (6, 12),
    (6, 13),
    (6, 14),
    (6, 15),
    (6, 16),
    (6, 17),
    (6, 18),
    (6, 19),
    (6, 20),
    (6, 21),
    (6, 27),
    (6, 28),
    (6, 29),
    (24, 0),
    (24, 1),
    (24, 2),
    (24, 3),
    (24, 9),
    (24, 10),
    (24, 11),
    (24, 12),
    (24, 13),
    (24, 14),
    (24, 15),
    (24, 16),
    (24, 17),
    (24, 18),
    (24, 19),
    (24, 20),
    (24, 21),
    (24, 27),
    (24, 28),
    (24, 29),
]

# Posicion A
# semaforosV = [
#     (7, 3),
#     (8, 3),
#     (4, 9),
#     (5, 9),
#     (7, 21),
#     (8, 21),
#     (4, 27),
#     (5, 27),
#     (25, 3),
#     (26, 3),
#     (22, 9),
#     (23, 9),
#     (25, 21),
#     (26, 21),
#     (22, 27),
#     (23, 27),
# ]

# semaforosH = [
#     (3, 4),
#     (3, 5),
#     (9, 7),
#     (9, 8),
#     (21, 4),
#     (21, 5),
#     (27, 7),
#     (27, 8),
#     (3, 22),
#     (3, 23),
#     (9, 25),
#     (9, 26),
#     (21, 22),
#     (21, 23),
#     (27, 25),
#     (27, 26),
#     (3, 13),
#     (3, 14),
#     (27, 16),
#     (27, 17),
# ]

# Sin semaforos
# semaforosV = []
# semaforosH = []

# Posiciones B
semaforosV = [
    (7, 3),
    (8, 3),
    (9, 4),
    (9, 5),
    #
    (3, 7),
    (3, 8),
    (4, 9),
    (5, 9),
    #
    (7, 21),
    (8, 21),
    (9, 22),
    (9, 23),
    #
    (4, 27),
    (5, 27),
    (3, 25),
    (3, 26),
    #
    (25, 3),
    (26, 3),
    (27, 4),
    (27, 5),
    #
    (22, 9),
    (23, 9),
    (21, 8),
    (21, 7),
    #
    (25, 21),
    (26, 21),
    (27, 22),
    (27, 23),
    #
    (22, 27),
    (23, 27),
    (21, 26),
    (21, 25),
]

semaforosH = [
    (3, 4),
    (3, 5),
    (4, 3),
    (5, 3),
    #
    (9, 7),
    (9, 8),
    (7, 9),
    (8, 9),
    #
    (21, 4),
    (21, 5),
    (22, 3),
    (23, 3),
    #
    (27, 7),
    (27, 8),
    (26, 9),
    (25, 9),
    #
    (3, 22),
    (3, 23),
    (4, 21),
    (5, 21),
    #
    (9, 25),
    (9, 26),
    (8, 27),
    (7, 27),
    #
    (21, 22),
    (21, 23),
    (22, 21),
    (23, 21),
    #
    (27, 25),
    (27, 26),
    (26, 27),
    (25, 27),
    #
    (3, 13),
    (3, 14),
    #
    (27, 16),
    (27, 17),
]

# Posicion C
# semaforosV = [
#     (7, 2),
#     (8, 2),
#     (4, 10),
#     (5, 10),
#     (7, 20),
#     (8, 20),
#     (4, 28),
#     (5, 28),
#     (25, 2),
#     (26, 2),
#     (22, 10),
#     (23, 10),
#     (25, 20),
#     (26, 20),
#     (22, 28),
#     (23, 28),
# ]

# semaforosH = [
#     (2, 4),
#     (2, 5),
#     (10, 7),
#     (10, 8),
#     (21, 3),
#     (21, 3),
#     (28, 7),
#     (28, 8),
#     (2, 22),
#     (2, 23),
#     (10, 25),
#     (10, 26),
#     (20, 22),
#     (20, 23),
#     (28, 25),
#     (28, 26),
#     (2, 13),
#     (2, 14),
#     (28, 16),
#     (28, 17),
# ]

puntos_salida_autos = [
    # First street
    (4, 0),
    (5, 0),
    (7, 29),
    (8, 29),
    # Second street
    (16, 0),
    (16, 29),
    # Third street
    (22, 0),
    (23, 0),
    (25, 29),
    (26, 29),
    # Parallel start
    (0, 7),
    (0, 8),
    (0, 16),
    (0, 17),
    (0, 25),
    (0, 26),
    # Parallel end
    (29, 4),
    (29, 5),
    (29, 13),
    (29, 14),
    (29, 22),
    (29, 23),
]

puntos_llegada_autos = [
    # First street
    (7, 0),
    (8, 0),
    (4, 29),
    (5, 29),
    # Second street
    (18, 0),
    (14, 29),
    # Third street
    (25, 0),
    (26, 0),
    (22, 29),
    (23, 29),
    # Parallel start
    (0, 4),
    (0, 5),
    (0, 13),
    (0, 14),
    (0, 22),
    (0, 23),
    # Parallel end
    (29, 7),
    (29, 8),
    (29, 16),
    (29, 17),
    (29, 25),
    (29, 26),
]


puntos_peatones = [
    (3, 0),
    (9, 0),
    (15, 0),
    (19, 0),
    (21, 0),
    (27, 0),
    (3, 29),
    (9, 29),
    (13, 29),
    (17, 29),
    (21, 29),
    (27, 29),
    (0, 3),
    (0, 9),
    (0, 12),
    (0, 18),
    (0, 21),
    (0, 27),
    (29, 3),
    (29, 9),
    (29, 12),
    (29, 18),
    (29, 21),
    (29, 27),
]

grafo_peatones = {
    # Origins
    (3, 0): {(3, 3): 3},
    (9, 0): {(9, 3): 3},
    (15, 0): {(15, 3): 3},
    (19, 0): {(19, 3): 3},
    (21, 0): {(21, 3): 3},
    (27, 0): {(27, 3): 3},
    (3, 29): {(3, 27): 3},
    (9, 29): {(9, 27): 3},
    (13, 29): {(13, 27): 3},
    (17, 29): {(17, 27): 3},
    (21, 29): {(21, 27): 3},
    (27, 29): {(27, 27): 3},
    (0, 3): {(3, 3): 3},
    (0, 9): {(3, 9): 3},
    (0, 12): {(3, 12): 3},
    (0, 18): {(3, 18): 3},
    (0, 21): {(3, 21): 3},
    (0, 27): {(3, 27): 3},
    (29, 3): {(27, 3): 2},
    (29, 9): {(27, 9): 2},
    (29, 12): {(27, 12): 2},
    (29, 18): {(27, 18): 2},
    (29, 21): {(27, 21): 2},
    (29, 27): {(27, 27): 2},
    # corners
    (3, 3): {(3, 9): 6, (9, 3): 6},
    (9, 3): {(9, 9): 6, (15, 3): 6},
    (15, 3): {(19, 3): 4},
    (19, 3): {(21, 3): 2},
    (21, 3): {(21, 9): 6, (27, 3): 6},
    (27, 3): {(27, 9): 6},
    (3, 27): {(9, 27): 6, (3, 21): 6},
    (9, 27): {(9, 21): 6, (13, 27): 4},
    (13, 27): {(17, 27): 4},
    (17, 27): {(21, 27): 4},
    (21, 27): {(27, 27): 6, (21, 21): 6},
    (27, 27): {(27, 21): 6},
    # Center
    (3, 9): {(3, 12): 3, (9, 9): 6},
    (3, 12): {(3, 18): 6},
    (3, 18): {(3, 21): 3},
    (3, 21): {(3, 27): 6, (9, 21): 6},
    (27, 9): {(21, 9): 6, (27, 12): 3},
    (27, 12): {(27, 18): 6},
    (27, 18): {(27, 21): 3},
    (27, 21): {(27, 27): 6, (21, 21): 6},
    # Roundabout
    (9, 9): {(9, 21): 11},
    (9, 21): {(21, 21): 11},
    (21, 21): {(21, 9): 11},
    (21, 9): {(9, 9): 11},
}

puntos_carros = [
    (8, 0),
    (18, 0),
    (26, 0),
    (0, 4),
    (29, 8),
    (0, 13),
    (29, 17),
    (0, 22),
    (29, 26),
    (4, 29),
    (14, 29),
    (22, 29),
]

# para pruebas solamente
puntos_extras_carros = [
    (8, 0),
    (18, 0),
    (26, 0),
    (0, 4),
    (29, 8),
    (0, 13),
    (29, 17),
    (0, 22),
    (29, 26),
    (4, 29),
    (14, 29),
    (22, 29),
    (4, 4),
    (16, 4),
    (22, 4),
    (4, 8),
    (4, 17),
    (4, 26),
    (8, 26),
    (16, 26),
    (26, 4),
    (26, 13),
    (26, 22),
    (26, 26),
    (8, 4),
    (18, 4),
    (8, 8),
    (22, 8),
    (26, 8),
    (4, 13),
    (26, 17),
    (22, 22),
    (8, 22),
    (4, 22),
    (22, 26),
    (14, 26),
]

llegada_carros = [
    (4, 0),
    (16, 0),
    (22, 0),
    (29, 4),
    (0, 8),
    (0, 17),
    (0, 26),
    (29, 4),
    (29, 13),
    (29, 22),
    (26, 29),
]

grafo_carros = {
    # Salida
    (8, 0): {(8, 4): 4},
    (18, 0): {(18, 4): 4},
    (26, 0): {(26, 4): 4},
    (0, 4): {(4, 4): 4},
    (29, 8): {(26, 8): 3},
    (0, 13): {(4, 13): 4},
    (29, 17): {(26, 17): 3},
    (0, 22): {(4, 22): 4},
    (29, 26): {(26, 26): 3},
    (4, 29): {(4, 26): 3},
    (14, 29): {(14, 26): 3},
    (22, 29): {(22, 26): 3},
    # Llegada
    (4, 4): {(4, 0): 4, (8, 4): 4},
    (16, 4): {(16, 0): 4, (18, 4): 2},
    (22, 4): {(22, 0): 4, (26, 4): 4},
    (4, 8): {(0, 8): 4, (4, 4): 4},
    (4, 17): {(0, 17): 4, (4, 13): 4},
    (4, 26): {(0, 26): 4, (4, 22): 4},
    (8, 26): {(8, 29): 3, (4, 26): 4},
    (16, 26): {(16, 29): 3, (14, 26): 2},
    (26, 4): {(29, 4): 3, (26, 8): 4},
    (26, 13): {(29, 13): 3, (26, 17): 4},
    (26, 22): {(29, 22): 3, (26, 26): 4},
    (26, 26): {(26, 29): 3, (22, 26): 4},
    # Los demas
    (8, 4): {(16, 4): 8, (8, 8): 4},
    (18, 4): {(22, 4): 4},
    (8, 8): {(4, 8): 4, (8, 22): 14},
    (22, 8): {(22, 4): 4, (8, 8): 14},
    (26, 8): {(22, 8): 4, (26, 13): 5},
    (4, 13): {(4, 8): 4},
    (26, 17): {(26, 22): 5},
    (22, 22): {(22, 8): 14, (26, 22): 4},
    (8, 22): {(22, 22): 14, (8, 26): 4},
    (4, 22): {(8, 22): 4, (4, 17): 5},
    (22, 26): {(16, 26): 6, (22, 22): 4},
    (14, 26): {(8, 26): 6},
}

recorrido_icecream = [
    # Llegada
    (26, 4),
    (26, 26),
    (4, 26),
    (4, 4),
]


# -------------------------------------------------------------------------------------


# ----------------------------------------Agentes-------------------------------------------------------
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


class semaforoVAgent(Agent):  # Semaforos Verticales
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.agentT = 2  # Semaforo
        self.estado = 1  # Color del semaforo 0 = rojo 1 = verde 2 = amarillo
        self.paso = 0

    def step(self):
        if (self.paso % 10) == 0:
            if self.estado == 0:
                self.estado = 1
            else:
                self.estado = 0
        self.paso += 1
        pass


class semaforoRAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.agentT = 2  # Semaforo
        self.estado = 0  # Color del semaforo 0 = rojo 1 = verde 2 = amarillo
        self.paso = 0

    def step(self):
        if (self.paso % 10) == 0:
            if self.estado == 1:
                self.estado = 0
            else:
                self.estado = 1
        self.paso += 1
        pass


class PeatonAgent(Agent):
    def __init__(self, unique_id, model, pos, destino):
        super().__init__(unique_id, model)
        self.pos = pos
        self.destino = destino
        self.estado = 4
        self.chocado = False
        self.ruta = model.dijkstra(pos, self.destino, self.model.graph_peatones)
        self.step_count = 0  # Contador de pasos

    def move(self):
        if len(self.ruta) > 1:
            siguiente_paso = self.ruta[1]

            dx = siguiente_paso[0] - self.pos[0]
            dy = siguiente_paso[1] - self.pos[1]

            if dx != 0:
                new_pos = (self.pos[0] + (dx // abs(dx)), self.pos[1])
            elif dy != 0:
                new_pos = (self.pos[0], self.pos[1] + (dy // abs(dy)))
            else:
                new_pos = self.pos
                self.ruta = self.ruta[1:]

            cell_contents = self.model.grid.get_cell_list_contents([new_pos])
            for content in cell_contents:
                if (
                    isinstance(content, (semaforoRAgent, semaforoVAgent))
                    and content.estado == 1
                    and random.randrange(99) < 94
                ):
                    return

            # Si no hay nada avanza
            self.model.grid.move_agent(self, new_pos)
            self.pos = new_pos
            self.step_count += 1
        else:
            self.destino = random.choice(puntos_peatones)
            self.ruta = self.model.dijkstra(
                self.pos, self.destino, self.model.graph_peatones
            )
            return

    def step(self):
        if not self.chocado:
            self.move()


class CarAgent(Agent):
    def __init__(self, unique_id, model, pos, destino):
        super().__init__(unique_id, model)
        self.pos = pos
        self.destino = destino
        self.estado = 3
        self.direccion = "norte"
        self.ruta = model.dijkstra(pos, destino, self.model.graph_carros)

        self.step_count = 0  # Contador de pasos

    def move(self):
        if len(self.ruta) > 1:
            siguiente_paso = self.ruta[1]

            dx = siguiente_paso[0] - self.pos[0]
            dy = siguiente_paso[1] - self.pos[1]

            if dx != 0:
                if dx > 0:
                    self.direccion = "este"
                else:
                    self.direccion = "oeste"
                new_pos = (self.pos[0] + (dx // abs(dx)), self.pos[1])
            elif dy != 0:
                # Define la direccion
                if dy > 0:
                    self.direccion = "norte"
                else:
                    self.direccion = "sur"
                new_pos = (self.pos[0], self.pos[1] + (dy // abs(dy)))
            else:
                new_pos = self.pos
                self.ruta = self.ruta[1:]

            # Si es semaforo espera, si es peaton, quizas atropella
            cell_contents = self.model.grid.get_cell_list_contents([new_pos])
            for content in cell_contents:
                if (
                    isinstance(content, PeatonAgent)
                    and content.chocado != True
                    # 80% de probabilidad de choque
                    and random.randrange(9) < 7
                ):
                    content.chocado = True
                    self.model.chocados += 1
                if (
                    isinstance(content, (semaforoRAgent, semaforoVAgent))
                    and content.estado == 0
                ):
                    return

            # Si es carro espera
            car_agents = [
                obj
                for obj in cell_contents
                if isinstance(obj, CarAgent) or isinstance(obj, IceCreamAgent)
            ]
            if car_agents:
                return

            # Si no hay nada avanza
            self.model.grid.move_agent(self, new_pos)
            self.pos = new_pos
            self.step_count += 1
        else:
            new_pos = random.choice(puntos_carros)
            self.model.grid.move_agent(self, new_pos)
            self.pos = new_pos
            self.ruta = self.model.dijkstra(
                self.pos, random.choice(llegada_carros), self.model.graph_carros
            )

    def step(self):
        self.move()


class IceCreamAgent(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos
        self.coordenadas = recorrido_icecream
        self.estado = 3
        self.direccion = "norte"
        self.step_count = 0

    def move(self):
        if not self.coordenadas:
            self.coordenadas = recorrido_icecream

        siguiente_paso = self.coordenadas[0]

        dx = siguiente_paso[0] - self.pos[0]
        dy = siguiente_paso[1] - self.pos[1]

        if dx != 0:
            if dx > 0:
                self.direccion = "este"
            else:
                self.direccion = "oeste"
            new_pos = (self.pos[0] + (dx // abs(dx)), self.pos[1])
        elif dy != 0:
            # Define la direccion
            if dy > 0:
                self.direccion = "norte"
            else:
                self.direccion = "sur"
            new_pos = (self.pos[0], self.pos[1] + (dy // abs(dy)))
        else:
            new_pos = self.pos
            self.coordenadas = self.coordenadas[1:]

            # Si es semaforo espera, si es peaton, quizas atropella
            cell_contents = self.model.grid.get_cell_list_contents([new_pos])
            for content in cell_contents:
                if (
                    isinstance(content, (semaforoRAgent, semaforoVAgent))
                    and content.estado == 0
                ):
                    return
                if (
                    isinstance(content, PeatonAgent)
                    and content.chocado != True
                    and random.randrange(10) < 5
                ):
                    content.chocado = True
                    self.model.chocados += 1

            # Si es carro espera
            car_agents = [
                obj
                for obj in cell_contents
                if isinstance(obj, CarAgent) or isinstance(obj, IceCreamAgent)
            ]
            if car_agents:
                return

        # Si no hay nada avanza
        self.model.grid.move_agent(self, new_pos)
        self.pos = new_pos
        self.step_count += 1

    def step(self):
        self.move()


# -------------------------------------------------------------MODEL---------------------------------------------------------------------
class TrafficModel(Model):
    def __init__(self, width, height, num_peatones, num_autos):
        self.num_peatones = num_peatones
        self.num_autos = num_autos
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.graph_peatones = nx.Graph()
        self.graph_carros = nx.DiGraph()
        self.step_count = 0
        self.chocados = 0
        self.datacollector = mesa.DataCollector(
            {
                "chocados": "chocados",
            }
        )
        o = 0

        for node, connections in grafo_peatones.items():
            for neighbor, cost in connections.items():
                self.graph_peatones.add_edge(node, neighbor, weight=cost)

        for node, connections in grafo_carros.items():
            for neighbor, cost in connections.items():
                self.graph_carros.add_edge(node, neighbor, weight=cost)

        self.running = True

        # Djikstra
        self.puntos_inicio_peatones = random.choices(
            puntos_peatones, k=self.num_peatones
        )
        self.lineas_llegada_peatones = random.choices(
            puntos_peatones, k=self.num_peatones
        )

        self.puntos_inicio_carros = random.sample(puntos_extras_carros, num_autos)
        self.lineas_llegada_carros = llegada_carros

        for punto, destino in zip(
            self.puntos_inicio_peatones, self.lineas_llegada_peatones
        ):
            x, y = punto
            persona = PeatonAgent(o, model=self, pos=(x, y), destino=destino)
            self.schedule.add(persona)
            self.grid.place_agent(persona, (x, y))
            o += 1

        for punto in self.puntos_inicio_carros:
            x, y = punto
            carro = CarAgent(
                o,
                model=self,
                pos=(x, y),
                destino=random.choice(self.lineas_llegada_carros),
            )
            self.schedule.add(carro)
            self.grid.place_agent(carro, (x, y))
            o += 1

        # IceCream
        icecream = IceCreamAgent(o, model=self, pos=(4, 4))
        self.schedule.add(icecream)
        self.grid.place_agent(icecream, (4, 4))
        o += 1

        # Create the obstacles
        for i in edificios:
            pavA = obstaculoAgent(o, self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA, (x, y))
            o += 1

        for i in banqueta:
            pavA = banquetaAgent(o, self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA, (x, y))
            o += 1

        for i in semaforosV:
            pavA = semaforoVAgent(o, self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA, (x, y))
            o += 1

        for i in semaforosH:
            pavA = semaforoRAgent(o, self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA, (x, y))
            o += 1

    def dijkstra(self, inicio, destino, grafo):
        ruta_mas_corta = nx.shortest_path(
            grafo, source=inicio, target=destino, weight="weight"
        )
        return ruta_mas_corta

    def send_positions_to_server(self):
        positions_data = {
            f"car_{car_agent_agent.unique_id}": [
                car_agent_agent.pos[0],
                car_agent_agent.pos[1],
            ]
            for car_agent_agent in self.schedule.agents
            if isinstance(car_agent_agent, CarAgent)
        }

        positions_dataH = {
            f"car_{IceCreamAgent_agent.unique_id}": [
                IceCreamAgent_agent.pos[0],
                IceCreamAgent_agent.pos[1],
            ]
            for IceCreamAgent_agent in self.schedule.agents
            if isinstance(IceCreamAgent_agent, IceCreamAgent)
        }

        positions_dataCompas = {
            f"peaton_{PeatonAgent_agent.unique_id}": [
                PeatonAgent_agent.pos[0],
                PeatonAgent_agent.pos[1],
                PeatonAgent_agent.chocado,
            ]
            for PeatonAgent_agent in self.schedule.agents
            if isinstance(PeatonAgent_agent, PeatonAgent)
        }
        semaforoR_data = {
            f"semaforo_{semaforoRAgent_agent.unique_id}": [
                semaforoRAgent_agent.estado,
                semaforoRAgent_agent.pos[0],
                semaforoRAgent_agent.pos[1],
            ]
            for semaforoRAgent_agent in self.schedule.agents
            if isinstance(semaforoRAgent_agent, semaforoRAgent)
        }

        semaforoV_data = {
            f"semaforo_{semaforoRAgent_agent.unique_id}": [
                semaforoRAgent_agent.estado,
                semaforoRAgent_agent.pos[0],
                semaforoRAgent_agent.pos[1],
            ]
            for semaforoRAgent_agent in self.schedule.agents
            if isinstance(semaforoRAgent_agent, semaforoVAgent)
        }

        semaforoV_data |= semaforoR_data

        requests.post("http://127.0.0.1:5000/update_positions", json=positions_data)
        requests.post(
            "http://127.0.0.1:5000/update_positionsCompas", json=positions_dataCompas
        )
        requests.post(
            "http://127.0.0.1:5000/update_positionsHelado", json=positions_dataH
        )
        requests.post("http://127.0.0.1:5000/update_estados", json=semaforoV_data)

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        self.step_count += 1  # Incrementar el contador de pasos en cada llamada a step
        if self.step_count >= 250:
            self.running = False
        self.send_positions_to_server()  # Añadir esta línea al final de step

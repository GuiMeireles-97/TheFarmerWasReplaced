import Utilidades

def drone_function():
    Utilidades.random_hat_change()
    for i in range(get_world_size()):
        Utilidades.plantar(Entities.Pumpkin, 1)        
        move(North)

while True:
    if spawn_drone(drone_function):
        move(East)
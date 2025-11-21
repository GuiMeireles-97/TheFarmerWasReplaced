def plantar():
    harvest()
    arar(Grounds.Soil)
    plant(Entities.Cactus)
    
def arar(tipo):
    if get_ground_type() != tipo:
        till()
    
def drone_function():
    for i in range(get_world_size()):
        plantar()
        move(North)
        
def main():
    while get_pos_x() <= (get_world_size() - 1):
        
        if spawn_drone(drone_function):
            
            move(East)
        
main()
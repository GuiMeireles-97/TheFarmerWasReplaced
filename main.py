import Funcoes

quantidade_minima = 445000

while True:
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            
            Funcoes.verificar_inventario(0)
            spawn_drone(Funcoes.plantar_e_colher(5))
            Funcoes.plantar_e_colher(Funcoes.tipo_planta)
            move(North)
        move(East)
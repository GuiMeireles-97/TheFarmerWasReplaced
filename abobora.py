#clear()
q_maxima_drones = max_drones()
global q_abobora
q_abobora = 0
abobora_final = q_maxima_drones * q_maxima_drones

set_world_size(q_maxima_drones)

def moveback():
    y_atual = get_pos_y()
    if y_atual > q_maxima_drones // 2:
        while y_atual != 0:
            move(North)
            y_atual = get_pos_y()
    else:
        while y_atual != 0:
            move(South)
            y_atual = get_pos_y()


def rega():
    if get_water() < 0.8:
        use_item(Items.Water)

def arar(ground):
    if get_ground_type() != ground:
        till()


def plantar():
    if get_entity_type() != Entities.Pumpkin:
        arar(Grounds.Soil)
        harvest()
        plant(Entities.Pumpkin)
        

def contagem_replanta():
    # posicao = [get_pos_x(), get_pos_y()]
    if get_entity_type() == Entities.Pumpkin:
        
        global q_abobora
        q_abobora += 1

    else:
        plant(Entities.Pumpkin)

    return q_abobora


def func_drone():
    global q_abobora

    for y in range(q_maxima_drones):
        rega()
        plantar()
        move(North)
    
    while q_abobora != abobora_final:
        global q_abobora
        rega()
        q_abobora = contagem_replanta()
        move(North)


def main_drone():
    while num_drones() < q_maxima_drones:
        rega()
        spawn_drone(func_drone)
        move(East)

    for y in range(q_maxima_drones):
        rega()
        plantar()
        move(North)

    global q_abobora
    while q_abobora < abobora_final:
        rega()
        q_abobora = contagem_replanta()
        move(North)

    harvest()
    global q_abobora
    q_abobora = 0
    moveback()

while True:
    
    main_drone()
    #moveback()



    
        

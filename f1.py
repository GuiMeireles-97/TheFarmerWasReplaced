q_maxima_drones = max_drones()


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
            
            
            
moveback()
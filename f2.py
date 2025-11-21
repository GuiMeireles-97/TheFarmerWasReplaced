def mover_para(x, y):
    while get_pos_x() < x:
        move(East)
    while get_pos_x() > x:
        move(West)
    while get_pos_y() < y:
        move(North)
    while get_pos_y() > y:
        move(South)

def gerar_labirinto():
    plant(Entities.Bush)
    use_item(Items.Weird_Substance)

def main():
    world = get_world_size()
    d = max_drones()

    # Grade mais quadrada possível
    cols = 1
    while cols * cols < d:
        cols += 1
    rows = (d + cols - 1) // cols   # ceil(d / cols)

    cell_w = world // cols
    cell_h = world // rows

    for i in range(d):
        col = i % cols
        row = i // cols

        center_x = col*cell_w + cell_w//2
        center_y = row*cell_h + cell_h//2

        # mover o drone "principal" até a posição alvo
        mover_para(center_x, center_y)

        # spawnar o drone que fará o labirinto
        spawn_drone(gerar_labirinto)

        # mover para próxima célula
        move(East)

main()

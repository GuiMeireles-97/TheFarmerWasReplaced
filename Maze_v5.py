import Utilidades

farm_size = get_world_size()
total_drones = max_drones()

def reutiliza():
    substance = 2 #Alterar para quantidade de vezes que o labirinto deve ser reutilizado
    return substance


def initialize_maze(size):
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, size)


def solve_maze(substance):
    quant_substancia = 1
    index = 0
    tesouro = Entities.Treasure
    direcoes = [North, East, South, West]
    
    while not quant_substancia == (substance + 1):
        pos_atual_x = get_pos_x()
        pos_atual_y = get_pos_y()
        
        move(direcoes[index % 4])
        index += 1
        
        if pos_atual_x == get_pos_x() and pos_atual_y == get_pos_y():
            index += 2
            
        if get_entity_type() == tesouro:
            #print(quant_substancia, sub_final)
            if quant_substancia != substance:
                usar = quant_substancia * 2
                use_item(Items.Weird_Substance, usar)
                quant_substancia += 1
            else:
                harvest()
                break



def moveto(x, y):
    while get_pos_x() < x:
        move(East)
    while get_pos_x() > x:
        move(West)
    while get_pos_y() < y:
        move(North)
    while get_pos_y() > y:
        move(South)


def position(index):
    farm_size = get_world_size()
    total_drones = max_drones()
    cols = 1

    while ((cols * cols) < total_drones):
        cols += 1
    
    lines = (total_drones + cols - 1) // cols
    
    cell_w = farm_size // cols
    cell_h = farm_size // lines

    coluna = index % cols
    linha = index // cols

    drone_x = coluna*cell_w + cell_w//2
    drone_y = linha*cell_h + cell_h//2

    return drone_x, drone_y



def get_maze_size():
    farm_size = get_world_size()
    total_drones = max_drones()
    cols = 1

    while ((cols * cols) < total_drones):
        cols += 1
    
    lines = (total_drones + cols - 1) // cols

    maze_size = farm_size // cols
    #maze_size = 4
    return maze_size


def func_drone(i):
    Utilidades.random_hat_change()
    
    total_drones = max_drones()
    drone_pos = position(i)

    moveto(drone_pos[0], drone_pos[1])
    do_a_flip()
    
    maze_size = get_maze_size()
    
    while True:
        
        moveto(drone_pos[0], drone_pos[1])
        initialize_maze(maze_size)
        substance = reutiliza()
        solve_maze(substance)


def spawn_drone_arg(fn, arg):
    def callback():
        return fn(arg)
    return spawn_drone(callback)


def main():
    change_hat(Hats.Carrot_Hat)
    index = total_drones - 1
    main_drone_pos = position(index)
    #print(main_drone_pos)
    moveto(main_drone_pos[0], main_drone_pos[1])

    for i in range(total_drones - 1):
        spawn_drone_arg(func_drone, i)
        
    do_a_flip()
    
    maze_size = get_maze_size()
    
    while True:
        
        moveto(main_drone_pos[0], main_drone_pos[1])
        initialize_maze(maze_size)
        substance = reutiliza()
        solve_maze(substance)


Utilidades.random_hat_change()
    
while True:
    if num_drones() == 1:
        main()
        
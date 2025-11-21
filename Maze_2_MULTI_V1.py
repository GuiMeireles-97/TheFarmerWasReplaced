def moveto(x, y):
    posicao_alvo = [x, y]
    posicao_atual = [get_pos_x(), get_pos_y()]
    #print(posicao_atual)

    while not posicao_atual == posicao_alvo:
        posicao_atual = [get_pos_x(), get_pos_y()]

        if (posicao_atual[0] == posicao_alvo[0]) and (posicao_atual[1] == posicao_alvo[1]):
            return
        
        if not posicao_atual[0] == posicao_alvo[0]:
            move(East)
        
        if not posicao_atual[1] == posicao_alvo[1]:
            move(North)
        
        if posicao_atual[1] >= (get_world_size() - 1):
            return y
def generate_maze():        
    for i in range(4):
        move(East)
        
    criar_labirinto(8)
    solucionar(5)
    
def criar_labirinto(tamanho):
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, tamanho)
    
def solucionar(substancia):
    tesouro = Entities.Treasure
    direcoes = [North, East, South, West]
    quant_substancia = 1
    index = 0
    
    while not quant_substancia == (substancia + 1):
        pos_atual_x = get_pos_x()
        pos_atual_y = get_pos_y()
        
        move(direcoes[index % 4])
        index += 1
        
        if pos_atual_x == get_pos_x() and pos_atual_y == get_pos_y():
            index += 2
            
        if get_entity_type() == tesouro:
            #print(quant_substancia, sub_final)
            if quant_substancia != substancia:
                usar = quant_substancia * 2
                use_item(Items.Weird_Substance, usar)
                quant_substancia += 1
            else:
                harvest()
                break
    
    
    
x, y = 0, 0
maze_size = 4

for drones in range(max_drones()):
    moveto(x, y)
    spawn_drone(generate_maze)
    y += 6
    if y > get_world_size():
        y = 0
    elif y >= (get_world_size() - 2):
        x += 5
    if x > get_world_size():
        x = 0
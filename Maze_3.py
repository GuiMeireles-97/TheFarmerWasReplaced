def procura():
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
        
       
def criar_labirinto(tamanho):
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, tamanho) 
    
    
x_alvo, y_alvo = get_world_size() // 2, get_world_size() // 2
moveto(x_alvo, y_alvo)
criar_labirinto(get_world_size())

drones = num_drones()
max_drones = max_drones()

for drones in max_drones(num_drones()):
    spawn_drone(procura)

procura()

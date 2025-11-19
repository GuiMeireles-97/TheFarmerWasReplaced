metade_fazenda = get_world_size()  // 2
abaixo_drone = get_entity_type()
#substancia_estranha = get_world_size() // 4
tesouro_x, tesouro_y = 0, 0

def moveto(x, y):
    for pos_atual_x in range(x):
        for pos_atual_y in range(y):
            pos_atual_y = get_pos_y()
            
            if pos_atual_y == y:
                break
            move(North) 
            
        pos_atual_x = get_pos_x()
        if pos_atual_x == x:
            break
        move(East) 

def gerar_labirinto(substancia):
    #metade_fazenda = get_world_size()  // 2
    #moveto(metade_fazenda, metade_fazenda)
    
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, substancia)


def resolver_labririnto(x, y, substancia):
    quant_substancia = 1
    index = 0
    tesouro = Entities.Treasure
    direcoes = [North, East, South, West]
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
    
#tesouro_x, tesouro_y = measure()
#print(tesouro_x, tesouro_y)
#moveto(tesouro_x, tesouro_y)


#abaixo_drone = get_entity_type()
#if abaixo_drone == Entities.Treasure:
    #harvest()

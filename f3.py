dict_items = {Items.Hay:Entities.Grass, Items.Wood:Entities.Tree,
Items.Carrot:Entities.Carrot, Items.Pumpkin:Entities.Pumpkin,
 Items.Power:Entities.Sunflower}

posicao_inicial = [0, 0]


def regar():
    if (get_water() < 0.6):
        use_item(Items.Water)
        
def Arar_Terra(solo):
    if get_ground_type() != solo:
        till()

def verificar_inventario(dict_items):
    quantidade_itens = 0
    quantidade_minima = 1000000
    
    for item in dict_items:
        quantidade_itens = num_items(item)
        #print(quantidade_itens)
                
        if quantidade_itens <= quantidade_minima:
            break

    return item
        
def plantar(item):
    
   def abobora():


   # for i in range(get_world_size()):
        for i in range(get_world_size()):
            # posicao_atual = [get_pos_x(), get_pos_y()]
            # if posicao_atual == posicao_inicial:
            #     return posicao_atual
            
            if can_harvest() and (get_entity_type != Entities.Pumpkin):
                harvest()
            
            regar()
            
            if item == Entities.Grass:
                Arar_Terra(Grounds.Grassland)

            if (item == Entities.Carrot) or (item == Entities.Pumpkin) or (item == Entities.Sunflower):
                Arar_Terra(Grounds.Soil)
            
            if item == Entities.Tree:

                x = get_pos_x()
                y = get_pos_y()
                
                if ((x + y) % 2 == 0):
                    plant(Entities.Bush)
                    
                else:
                    plant(Entities.Tree)
 
            #if item == Entities.Pumpkin:
                #a

            if item != Entities.Grass:
                plant(item)
                
            #use_item(Items.Fertilizer)
            
            move(North)

    #    move(East)
       
   
   
while True:
    
    item_faltante = verificar_inventario(dict_items)
    item_faltante = dict_items[item_faltante]
    for i in range(get_world_size()):
        
        def plantar_item_faltante():
            plantar(item_faltante)
            #print(item_faltante)
       
        if item_faltante:
            #plantar(item_faltante)
            if spawn_drone(plantar_item_faltante):
                move(East)
                #print(item_faltante)
            
    
    
    
     
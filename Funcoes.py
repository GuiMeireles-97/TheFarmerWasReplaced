lista_itens = [Items.Hay, Items.Wood, Items.Carrot, Items.Pumpkin, Items.Power]
lista_plantas = [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot, Entities.Pumpkin, Entities.Sunflower]
quantidade_itens, quantidade_minima = 0, 500000

x, y = get_pos_x(), get_pos_y()
tamanho_fazenda = get_world_size()
tamanho_abobora = 0


def posicao_atual():
    global x
    global y
    global tamanho_fazenda
    global pos_atual
    x = get_pos_x()
    y = get_pos_y()
    pos_atual = x + y
    tamanho_fazenda = get_world_size() * get_world_size()
    

# Rega o chão se o nivel de agua for menor que 0.3
def regar():
    if (get_water() < 0.6):
        use_item(Items.Water)
        
def Arar_Terra(solo):
    if get_ground_type() != solo:
        till()

def colher_pumpkin():
    posicao_atual()
    global pos_atual
    global tamanho_fazenda
    global tamanho_abobora

    if get_entity_type() == Entities.Dead_Pumpkin:
        plant(Entities.Pumpkin)
    if pos_atual == 0.0:
        tamanho_abobora = 0
    if can_harvest():
            tamanho_abobora += 1
            #print(tamanho_abobora)
    if tamanho_abobora == tamanho_fazenda and can_harvest():
        harvest()            
    
        
def colher(tipo_planta):
    if tipo_planta == 4:
        colher_pumpkin()
    if can_harvest() and not tipo_planta == 4:
        harvest()
        
        
def verificar_inventario(verificar_item):
    quantidade_itens = num_items(lista_itens[verificar_item])
    while quantidade_itens >= quantidade_minima:
        quantidade_itens = num_items(lista_itens[verificar_item])
        #print(quantidade_itens)
        verificar_item += 1
    global tipo_planta
    tipo_planta = verificar_item
    
    
        

def plantar_e_colher (tipo_planta):
    posicao_atual()
    colher(tipo_planta)
    
    
    if (tipo_planta == 0):
        Arar_Terra(Grounds.Grassland)
        #if x == 0 and y == 0:
            #change_hat(Hats.Straw_Hat)
        #plant(Entities.Grass)
    
        
    if (tipo_planta == 1 or tipo_planta == 2):
        posicao_atual()
        regar()
        #change_hat(Hats.Tree_Hat)
        global x
        global y
        if ((x + y) % 2 == 0):
            plant(Entities.Bush)
        else:
            plant(Entities.Tree)
    
    
    if (tipo_planta == 3):
        #change_hat(Hats.Carrot_Hat)
        regar()
        Arar_Terra(Grounds.Soil)
        plant(Entities.Carrot)
        
        
    if (tipo_planta == 4):
        Arar_Terra(Grounds.Soil)
        regar()
        plant(Entities.Pumpkin)
        
    if (tipo_planta == 5):
        Arar_Terra(Grounds.Soil)
        regar()
        plant(Entities.Sunflower)
        
        
    use_item(Items.Fertilizer)  
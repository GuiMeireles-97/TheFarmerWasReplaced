# Randomiza o chapéu utilizado:
def random_hat_change():
    hats = [
Hats.Brown_Hat, Hats.Carrot_Hat, Hats.Gold_Hat, Hats.Gray_Hat,
Hats.Green_Hat, Hats.Pumpkin_Hat, Hats.Purple_Hat, Hats.Straw_Hat,
Hats.Sunflower_Hat, Hats.Traffic_Cone, Hats.Tree_Hat, Hats.Wizard_Hat,
Hats.Golden_Sunflower_Hat, Hats.Cactus_Hat
]
    index = random() * len(hats) // 1        
    change_hat(hats[index])   
    
    
# Define tipo de chão Ground.Soil ou Grouns.Grassland
def till_ground(solo):
    if get_ground_type() != solo:
        till()
        
        
# Rega do solo:
def regar(water):
    if get_water() < water:
        use_item(Items.Water, 4)
        
def plantar(planta, substancia):
    if planta == Entities.Pumpkin:
        solo = Grounds.Soil
    
    till_ground(solo)
    regar(0.6)    
    #plant(planta)
    if plant(planta) == True and substancia == True:
        use_item(Items.Fertilizer)
    
    
# Movimentação para X e Y específfico:        
def moveto(x, y):
    while get_pos_x() < x:
        move(East)
    while get_pos_x() > x:
        move(West)
    while get_pos_y() < y:
        move(North)
    while get_pos_y() > y:
        move(South)
        
def random_hat_change():
    hats = [
Hats.Brown_Hat, Hats.Carrot_Hat, Hats.Gold_Hat, Hats.Gray_Hat,
Hats.Green_Hat, Hats.Pumpkin_Hat, Hats.Purple_Hat, Hats.Straw_Hat,
Hats.Sunflower_Hat, Hats.Traffic_Cone, Hats.Tree_Hat, Hats.Wizard_Hat
]
    index = random() * len(hats) // 1
        
    #print(hats[index])
    change_hat(hats[index])   
    
import Maze

#def lab():
metade_fazenda = get_world_size()  // 2
tamanho_maze = 8
Substancia = 1

Maze.moveto(metade_fazenda, metade_fazenda)

while True:
    Maze.moveto(metade_fazenda, metade_fazenda)
    Maze.gerar_labirinto(tamanho_maze)

    tesouro_x, tesouro_y = measure()
    #print(tesouro_x, tesouro_y)

    Maze.resolver_labririnto(tesouro_x, tesouro_y, Substancia)        
#Maze.moveto(tesouro_x, tesouro_y)
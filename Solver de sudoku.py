tablero =[
    [9,2,0,0,5,0,0,0,0],
    [0,1,0,9,0,0,5,0,6],
    [4,0,0,0,0,0,1,0,8],
    [0,4,0,0,0,5,9,0,0],
    [7,3,8,6,0,0,4,0,0],
    [5,0,0,0,0,3,0,1,0],
    [1,8,0,5,6,4,0,3,0],
    [0,0,0,0,0,2,0,8,0],
    [0,0,0,8,0,0,0,4,5]
]


#Función para resolver el sudoku#
def solucion(tab):
    
    encontrar = encontrar_vacio(tab)
    if not encontrar:
        return True
    else:
        fila, columna = encontrar   

    for i in range (1,10):
        if valido(tab, i, (fila, columna)):
            tab[fila][columna] = i
        
            if solucion(tab):
                return True
        
            tab[fila][columna] = 0


#Función para mostrar en la consola el tablero que se tenga#
def print_tablero(tab):  
    for i in range(len(tab)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
    
        for j in range(len(tab[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(tab[i][j])
            else:
                print(str(tab[i][j]) + " ", end="")
                

#Función para encontrar las casillas vacías del tablero#
def encontrar_vacio(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 0:
                return (i, j)
            
    return None

#Función para comprobar si el numero colocado es valido#
def valido(tab, num, pos):
    #Comprobar fila#
    for i in range(len(tab[0])):
        if tab[pos[0]][i] == num and pos[1] != i:
            return False
    
    #Comprobar columna#
    for i in range(len(tab)):
        if tab[i][pos[1]] == num and pos[0] != i:
            return False
    
    #Comprobar celda#
    celda_x = pos[1] // 3
    celda_y = pos[0] // 3
    for i in range(celda_y * 3, celda_y * 3 + 3):
        for j in range(celda_x * 3, celda_x * 3 + 3):
            if tab[i][j] == num and (i, j) != pos:
                return False
    return True


print_tablero(tablero)
solucion(tablero)       
print("-------------------------")
print_tablero(tablero)          
                   
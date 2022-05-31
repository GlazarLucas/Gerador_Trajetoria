import numpy as np
import matplotlib.pyplot as mp

'''           
        A funcao equacao_da_reta recebe um array de pontos (nx2) que sao as coordenadas de uma reta,
   atraves desses pontos encontramos a equacao da reta que passa por esses pontos.Como resultado
   retornamos os parametros a e b da equacao da reta,como no modelo asseguir.
   
        y = a*x + b                                                        

'''

def equacao_da_reta(pontos):
    
    num_linhas=pontos.shape[0]
    b=0
    
    if (pontos[num_linhas-1,0] - pontos[0,0]) == 0:
        
        a = 'inf'
        b = 'nan'
        
    else:
        
        a = (pontos[num_linhas-1,1] - pontos[0,1])/(pontos[num_linhas-1,0] - pontos[0,0])
        b = pontos[0,1] - a*pontos[0,0]
        

    return (a,b)



'''           
            A funcao angulo_reta calcula o angulo de direcao da reta que passa pelos pontos fornecidos.
        tomando como referencia o eixo x e o sentido anti horario de crescimento retorna o angulo em graus.

'''

def angulo_reta_atraves_pontos(pontos):
    
    a,b = equacao_da_reta(pontos)
    tam_pontos = pontos.shape[0]
    sentido_x = "indefinido"
    sentido_y = 'indefinido'
    
    '''
            Testa se a reta nao e paralela ao eixo y
            
    '''
    
    if a != 'inf':    
        
        angulo = (np.arctan(a)/(2*np.pi))*360
        
        '''
        
                Avalia o sentido de crescimento do eixo y
        
        '''
        
        aux = pontos[tam_pontos-1,1] - pontos[1,1] 
        if aux > 0:
            sentido_y = 'positivo'
        else:
            sentido_y = 'negativo'
            
        '''
        
                Avalia o sentido de crescimento do eixo x
        
        '''
        
        aux = pontos[tam_pontos-1,0] - pontos[0,0]
        if aux > 0:
            sentido_x = 'positivo'
        else:
            sentido_x = 'negativo'    
        
        '''
        
                Testas casos baseado no sentido de crescimento dos eixos para
                calcular o angulo entre a reta e o eixo x.
        
        '''
        
        
        if sentido_x == 'positivo' and sentido_y == 'positivo':
            
            angulo = angulo
        
        if sentido_x == 'negativo' and sentido_y == 'positivo':
            
            angulo = 180 + angulo
    
        if sentido_x == 'negativo' and sentido_y == 'negativo':
            
            angulo = 180 + angulo
    
        if sentido_x == 'positivo' and sentido_y == 'negativo':
            
            angulo = 360 + angulo
    
    
    
    else:
        angulo = 90
    
    return angulo


'''           
        A funcao reta_perpendicular recebe os parametros a,b da reta 1 e a origem da reta 2 .Como resultado
   retornamos os parametros a e b da reta 2, que e perpendicular a reta 1.Como no modelo asseguir.
   
        y = a*x + b                                                        

'''

def reta_perpendicular(a1,b1,origem):
    
    angulo = np.arctan(a1)
    a2 = np.tan(angulo + np.pi/2)
    b2 = origem[1] - a2*origem[0]
    
        

    return (a2,b2)    
    
    
        
    
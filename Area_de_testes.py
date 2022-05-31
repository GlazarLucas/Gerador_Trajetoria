import numpy as np
import matplotlib.pyplot as mp
from Funcoes_Geometricas import * 
from Funcoes_Auxiliares_Funcoes_Geometricas import *

''' Area de Testes '''

num_pontos_reta= 100
num_pontos_curva = 100
origem = [0,0]
inclinacao = 30
arco= 0.25
lado ='d'
comprimento_reta = 5 
comprimento_curva = 5*arco*2*np.pi


reta1  = Reta([0,0],origem,comprimento_reta,num_pontos_reta,inclinacao)
curva1 = Curva(reta1.get_pontos(),[reta1.get_pontos()[num_pontos_reta-1,0],reta1.get_pontos()[num_pontos_reta-1,1]],comprimento_curva,num_pontos_curva,arco,lado)
#reta2 = Reta(curva1.get_pontos(),[curva1.get_pontos()[num_pontos_curva-1,0],curva1.get_pontos()[num_pontos_curva-1,1]],comprimento_reta,num_pontos_reta,inclinacao)

pontos = np.concatenate([reta1.get_pontos(),curva1.get_pontos()])
mp.plot(pontos[:,0],pontos[:,1])

import numpy as np
import matplotlib.pyplot as mp

'''O Objetivo desse codigo e criar figuras gometricas'''


'''   Funcoes para a criacao das figuras geometricas   '''

class Segmento():
    
    '''
    
            Os segmentos utilizados nesse codigo sao retas e arcos de circulo.
        O segmento tras todas as propriedades e metodos necessarios
        de um objeto geometrico utilizado nesse programa. 
    
    '''
    
    def __init__(self,segmento_anterior,origem,comprimento,num_pontos):
        
        self.segmento_anterior= segmento_anterior
        self.origem = origem
        self.comprimento = comprimento
        self.num_pontos = num_pontos
        self.pontos = np.zeros([num_pontos,2])
            
    def get_pontos(self):
        
        return self.pontos
    
    def equacao_da_reta(self,pontos):
        
        '''
        
                Calcula a equacao da reta que passa pelos dois ultimos pontos dos pontos
            dos pontos fornecidos,retornando os parametros a e b da equacao,como no
            modelo abaixo.
            
                y = a*x + b
            
                Caso a reta seja perpendicular ao eixo x o metodo retorna a = inf e
            b = nan.
        
        '''
        
        num_pontos = pontos.shape[0] 
        b=0
        
        if (pontos[num_pontos-1,0] - pontos[num_pontos-2,0]) == 0:
            
            a = 'inf'
            b = 'nan'
            
        else:
            
            a = (pontos[num_pontos-1,1] - pontos[num_pontos-2,1])/(pontos[num_pontos-1,0] -pontos[num_pontos-2,0])
            b = pontos[0,1] - a*pontos[0,0]
            

        return (a,b)
    def calcula_quadrante(self,pontos):
        
        '''
            
                Metodo que calcula o quadrante que a reta que passa pelos dois ultimos 
            pontos pertence.Esse metodo foi criado para sabermos a direcao de cresci-
            mento do segmento analizado ja que a tangente sempre supoe que a curva esta
            no primeiro ou terceiro quadrante.
                Esse metodo retorna o quadrante caso a reta pertenca ao 1,2,3 ou quarto
            quadrante e retorna 0,90,-180,-90 caso esteja na interseccao entre dois qua-
            drantes.
        
        '''
        
        retorno = 0
        num_pontos = pontos.shape[0] 
        xf = pontos[num_pontos-1,0]
        yf = pontos[num_pontos-1,1]
        x0 = pontos[num_pontos-2,0]
        y0 = pontos[num_pontos-2,1]
        
        dx = xf - x0
        dy = yf - y0
        
        
        if dx > 0 and dy > 0:
        
            retorno = 1
       
        elif dx < 0 and dy > 0:
            
            retorno = 2
            
        elif dx < 0 and dy < 0:
            
            retorno = 3
            
        elif dx > 0 and dy < 0:
            
            retorno = 4
            
        elif dx > 0 and dy == 0:
            
            retorno = 0
            
        elif dx == 0 and dy > 0:
            
            retorno = 90
            
        elif dx < 0 and dy == 0:
            
            retorno = -180
            
        elif dx == 0 and dy < 0:
            
            retorno = -90
        
        return retorno
    
    def reta_perpendicular(self,pontos):
        
        '''     
        
        ALERTA: ESSE METODO NAO ESTA PRONTO PORQUE NAO ESTA SENDO MAIS UTILIZADO,
        REQUER UMA ATUALIZACAO.
        
                Metodo para calcular a reta perpendicular a reta que passa pelos dois 
            ultimos pontos dos pontos dados.
            
        '''
        
        a = self.equacao_da_reta(pontos)[0]
        
        if a == 'inf':
            
            a2=0
            b2 = pontos[self.num_pontos - 1,1]
        
        else:
            
            angulo = np.arctan(a)
            
            if a == 0:
                
                a2 = 'inf'
                b2 = 'nan'
            
            else:
                
                a2 = np.tan(angulo + np.pi/2)
                b2 = self.origem[1] - a2*self.origem[0]
        
        return (a2,b2)    

    def mud_coord_polar_para_cartesiano(self,origem_inercial,origem_movel,ponto):
        
        '''
        
                Metodo utilizado para realizar a mudanca de coordenadas de um sistema
            radial movel para um sistema carteziano fixo.
                
                *** origem_inercial: Define o ponto onde o sistema inercial foi colocado.
                *** origem_movel: Define o ponto onde o sistema movel foi colocado.
                *** pontos: E o ponto que tera ser sistema de coordenadas mudado do refe-
            rencial movel para o referencial inercial.
        
        '''
        
        ponto_coordenadas_movel = np.array([[ponto[0]],[ponto[1]]])
        a = (origem_movel[1] - origem_inercial[1])/(origem_movel[0] - origem_inercial[0])
        pontos = np.array([[origem_inercial[0],origem_inercial[1]],[origem_movel[0],origem_movel[1]]])
        quadrante = self.calcula_quadrante(pontos)
        angulo = np.arctan(a)
        
        if quadrante == 1 or quadrante == 0:
            
            angulo = angulo
        
        elif quadrante == 2 or quadrante == 90:
            
            angulo = (np.pi/2 + angulo) + np.pi/2
            
        elif quadrante == 3 or quadrante == -180:
            
            angulo = angulo + np.pi
            
        elif quadrante == 4 or quadrante == -90:
            
            angulo = (np.pi/2 + angulo)+ 3*2*np.pi/4
            
        
        Matriz = np.array([[np.cos(angulo),-np.sin(angulo)],[np.sin(angulo),np.cos(angulo)]])
        ponto_coordenadas_inercial = np.dot(Matriz,ponto_coordenadas_movel)

        return ponto_coordenadas_inercial
    
    def mud_coord_cartesiano_para_polar(self,origem_inercial,origem_movel,ponto):

        '''
        
                Metodo utilizado para realizar a mudanca de coordenadas de um sistema
            carteziano movel para um sistema radial fixo.
                
                *** origem_inercial: Define o ponto onde o sistema inercial foi colocado.
                *** origem_movel: Define o ponto onde o sistema movel foi colocado.
                *** pontos: E o ponto que tera ser sistema de coordenadas mudado do refe-
            rencial movel para o referencial inercial.
        
        '''
                
        ponto_coordenadas_movel = np.array([[ponto[0]],[ponto[1]]])
        a = (origem_movel[1] - origem_inercial[1])/(origem_movel[0] - origem_inercial[0])
        pontos = np.array([[origem_inercial[0],origem_inercial[1]],[origem_movel[0],origem_movel[1]]])
        quadrante = self.calcula_quadrante(pontos)
        angulo = np.arctan(a)
        
        if quadrante == 1 or quadrante == 0:
            
            angulo = angulo
        
        elif quadrante == 2 or quadrante == 90:
            
            angulo = (np.pi/2 + angulo) + np.pi/2
            
        elif quadrante == 3 or quadrante == -180:
            
            angulo = angulo + np.pi
            
        elif quadrante == 4 or quadrante == -90:
            
            angulo = (np.pi/2 + angulo)+ 3*2*np.pi/4
            
        Matriz = np.array([[np.cos(angulo),np.sin(angulo)],[-np.sin(angulo),np.cos(angulo)]])
        ponto_coordenadas_inercial = np.dot(Matriz,ponto_coordenadas_movel)

        return ponto_coordenadas_inercial

class Reta(Segmento):
    
    '''
    
            Cria um segmento de reta apartir do segmento anterior, dando continuidade
        no segmento anterior atraves da reta que passa pelos dois ultimos pontos do 
        segmento anterior.
            Caso a reta seja o primeiro segmento da trajetoria criada tambem sera
        necessario a entrada da inclinacao.
    
    '''
    
    def __init__(self,segmento_anterior,origem,comprimento,num_pontos,inclinacao):
        
        super().__init__(segmento_anterior,origem,comprimento,num_pontos)
        self.inclinacao = inclinacao
        self.pontos_reta(origem,comprimento,num_pontos,inclinacao)
    
    def pontos_reta(self,origem,comprimento,num_pontos,inclinacao):
        
        x0=self.origem[0]
        y0=self.origem[1]
        dl=self.comprimento/self.num_pontos
        self.pontos[0,0] =  x0
        self.pontos[0,1] =  y0

        for i in range(1,self.num_pontos):
            
            x = x0 + dl*np.cos((self.inclinacao/360)*2*np.pi)
            y = y0 + dl*np.sin((self.inclinacao/360)*2*np.pi)
            
            self.pontos[i,0] =  x
            self.pontos[i,1] =  y
            x0=x
            y0=y
        
  
class Curva(Segmento):
    
    def __init__(self,segmento_anterior,origem,comprimento,num_pontos,arco,lado):
    
        Segmento.__init__(self,segmento_anterior,origem,comprimento,num_pontos)
        self.arco = arco
        self.lado = lado
        self.pontos_curva(segmento_anterior,origem,comprimento,num_pontos,arco,lado)
        
    def pontos_curva(self,segmento_anterior,origem,comprimento,num_pontos,arco,lado):
        
        raio = self.comprimento/(self.arco*2*np.pi)
        der_ang_cir = arco*2*np.pi/num_pontos
        
        reta_anterior = self.equacao_da_reta(segmento_anterior)
        angulo_anterior = np.arctan(reta_anterior[0])
        
        der_angulo_reta = der_ang_cir/2
        
        x1=self.origem[0]
        y1=self.origem[1]
        quadrante = self.calcula_quadrante(segmento_anterior)
      
  
      
        for i in range(num_pontos):
            
                 
                    ang_circulo = i*der_ang_cir

                    if lado =='d':
                                    
                        if ang_circulo <= np.pi:
                        
                            angulo_l = ang_circulo/2
                            l= 2*raio*np.sin(angulo_l)
                            xm = l*np.cos(angulo_l)
                            ym = l*np.sin(angulo_l)
                        
                        else:
                            
                            angulo_l = (2*np.pi - ang_circulo)/2
                            l= 2*raio*np.sin(angulo_l)
                            xm = -l*np.cos(angulo_l)
                            ym = l*np.sin(angulo_l)
                    
                    elif lado =='e':
                        
                        if ang_circulo <= np.pi:
                        
                            angulo_l = ang_circulo/2
                            l= 2*raio*np.sin(angulo_l)
                            xm = l*np.cos(angulo_l)
                            ym = -l*np.sin(angulo_l)
                        
                        else:
                            
                            angulo_l = (2*np.pi - ang_circulo)/2
                            l= 2*raio*np.sin(angulo_l)
                            xm = -l*np.cos(angulo_l)
                            ym = -l*np.sin(angulo_l)
                    
                    
                    x,y = self.mud_coord_polar_para_cartesiano([segmento_anterior[0,0],segmento_anterior[0,1]],origem,[xm,ym])
                    
                        
                    self.pontos[i,0] = x1 + x 
                    self.pontos[i,1] = y1 + y
                
   



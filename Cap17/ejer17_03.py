# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
class Planta:
    """ Clase Planta, con atributos básicos """
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.altura = 0
        self.agua = 0
                
    def regar(self):
        self.agua += 1
        
    def crecer(self):
        """ Crecimiento en una semana """
        pass
        
    def recolectar(self):
        """ Lista de frutos que produce """
        pass
        
    def __str__(self):
        return f"{self.nombre} ({self.altura} cm.)"

class Tomatera(Planta):
    
    def __init__(self):
        super().__init__('Tomatera')
        
    def crecer(self):
        self.altura += self.agua*3
        self.agua = 0
        
    def recolectar(self):
        if self.altura > 20:
            return ['tomate'] * int(self.altura/10)
        return []
    
class Habas(Planta):
    
    def __init__(self):
        super().__init__('Habas')

    def crecer(self):
        self.altura += self.agua*5
        self.agua = 0
        
    def recolectar(self):
        if self.altura > 10:
            return ['habas'] * int(self.altura/3)
        return []

class Huerto:
    """ Clase Huerto, contiene plantas """
    
    __max_plantas = 10
    
    def __init__(self):
        self.__plantas = []
        
    def plantar(self, planta):
        if len(self.__plantas) >= self.__max_plantas:
            print("No queda suelo disponible")
        else:
            self.__plantas.append(planta)
            
    def regar(self):
        for m in self.__plantas:
            m.regar()
            
    def crecer(self):
        for m in self.__plantas:
            m.crecer()

    def recolectar(self):
        cosecha = []
        for m in self.__plantas:
            cosecha += m.recolectar()
        return cosecha
            
    def __str__(self):
        msj = f"Hay {len(self.__plantas)} en el huerto:\n"
        for p in self.__plantas:
            msj += str(p) + "\n"
        return msj
    
    def resumen(cosecha):
        """ Solución ejercicio 17.3e """
        d = {}  # mantenemos un diccionario
        for x in cosecha:
            d[x] = d.get(x, 0) + 1
        for k in d:
             print(d[k], "de", k)   

if __name__ == "__main__":
    tomatera1 = Tomatera()
    tomatera2 = Tomatera()
    tomatera3 = Tomatera()
    habas1 = Habas()
    habas2 = Habas()
    
    huerto = Huerto()
    huerto.plantar(tomatera1)
    huerto.plantar(tomatera2)
    huerto.plantar(tomatera3)
    huerto.plantar(habas1)
    huerto.plantar(habas2)
    
    for i in range(15):
        huerto.regar()
        huerto.crecer()
        cosecha = huerto.recolectar()
        print(cosecha)
        Huerto.resumen(cosecha)
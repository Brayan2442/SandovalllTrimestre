class Pais:
    def __init__(self,pais,fertil,dens,eda_ema):
        self.__pais = pais
        self.__fertil =fertil
        self.__dens = dens
        self.__eda_ema =eda_ema
    def info(self):
        return f"{self.__pais} {self.__fertil} {self.__dens} {self.__eda_ema}"
    
    def getPais(self):
        return self.__pais
    
    def getFertil(self):
        return self.__fertil
    
    def getDens(self):
        return self.__dens
    
    def getEda_ema(self):
        return self.__eda_ema
class clima:
    def __init__(self, ano, mes, temperatura, precipitacao):

        self.ano = ano
        self.mes = mes
        self.temperatura = temperatura
        self.precipitacao = precipitacao


    def __str__(self):
        return f"Dados climaticos (Ano:{self.ano}. Mes:{self.mes}. Temperatura:{self.temperatura}. Precipitacao:{self.precipitacao})"
    
    def __eq__(self, object):
        
        if not isinstance(object, self.__class__):
            return NotImplemented

        return self.ano == object.ano and self.mes == object.mes

from abc import ABC, abstractmethod

class Exportador(ABC):
    @abstractmethod
    def exportar(self, dados):
        pass

class ExportadorCSV(Exportador):
    def exportar(self, dados):
        print("Exportando para CSV...")

class ExportadorExcel(Exportador):
    def exportar(self, dados):
        print("Exportando para Excel...")

def salvar_dados(exportador: Exportador, dados):
    exportador.exportar(dados)

salvar_dados(ExportadorCSV(), {"nome": "Maicon"})
salvar_dados(ExportadorExcel(), {"nome": "Maicon"})


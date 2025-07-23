class ConectarBancoDeDados:
    def __init__ (self) -> None:
        self.connection = None

    def conecta_ao_banco(self) -> None:
        self.connection = True

class RepositorioBanco:
    def __init__(self, conexao: ConectarBancoDeDados) -> None:
        self.__conexao = conexao

    def buscar_dados(self) -> str:
        if self.__conexao.connection:
            return [1, 2, 3, 4, 5 ]
        else:
            return "Conexão não estabelecida"
        
class RegraDeNegocio:
    def __init__(self, repositorio: RepositorioBanco) -> None:
        self.__repositorio = repositorio

    def calcular_resultados(self) -> str:
        dados = self.__repositorio.buscar_dados()
        if isinstance(dados, list):
            return f"Dados recebidos: {dados}"
        else:
            return dados
        
conn = ConectarBancoDeDados()
conn.conecta_ao_banco()
repositorio = RepositorioBanco(conn)
regra_negocio = RegraDeNegocio(repositorio)
resultado = regra_negocio.calcular_resultados()
print(resultado)  # Exibe os dados recebidos ou mensagem de erro
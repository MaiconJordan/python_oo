class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def connect(self):
        print(f"Conectando ao banco de dados: {self.connection_string}")

    def execute(self, query, params=None):
        print(f"Executando query: {query}")
        if params:
            print(f"Com parâmetros: {params}")
        # Simulação de retorno de dados
        if query.strip().lower().startswith("select"):
            return [{"id": 1, "nome": "Exemplo"}]
        return None

class DatabaseManager:
    def __init__(self, connection_string):
        self.connection = DatabaseConnection(connection_string)

    def insert(self, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.connection.connect()
        self.connection.execute(query, tuple(data.values()))

    def select(self, table, where=None):
        query = f"SELECT * FROM {table}"
        params = None
        if where:
            conditions = ' AND '.join([f"{k}=%s" for k in where.keys()])
            query += f" WHERE {conditions}"
            params = tuple(where.values())
        self.connection.connect()
        return self.connection.execute(query, params)

# Exemplo de uso
if __name__ == "__main__":
    db = DatabaseManager("sqlite://meubanco.db")
    db.insert("usuarios", {"nome": "Maicon", "idade": 30})
    resultado = db.select("usuarios", {"nome": "Maicon"})
    print("Resultado do select:", resultado)
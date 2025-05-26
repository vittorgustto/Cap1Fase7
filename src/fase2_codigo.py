
import sqlite3

# Conectar (ou criar) banco de dados
conn = sqlite3.connect('banco_agricola.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS sensores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    local TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id INTEGER,
    data_hora TEXT,
    valor REAL,
    FOREIGN KEY(sensor_id) REFERENCES sensores(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS recomendacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_acao TEXT,
    descricao TEXT,
    origem_fase TEXT
)
""")

# Inserir dados de exemplo
cursor.execute("INSERT INTO sensores (tipo, local) VALUES (?, ?)", ("umidade", "setor norte"))
cursor.execute("INSERT INTO sensores (tipo, local) VALUES (?, ?)", ("pH", "setor leste"))

cursor.execute("INSERT INTO leituras (sensor_id, data_hora, valor) VALUES (1, datetime('now'), 43.2)")
cursor.execute("INSERT INTO leituras (sensor_id, data_hora, valor) VALUES (2, datetime('now'), 6.5)")

cursor.execute("INSERT INTO recomendacoes (tipo_acao, descricao, origem_fase) VALUES (?, ?, ?)",
               ("irrigar", "Umidade abaixo do ideal", "Fase 1"))
cursor.execute("INSERT INTO recomendacoes (tipo_acao, descricao, origem_fase) VALUES (?, ?, ?)",
               ("corrigir pH", "pH fora da faixa ideal", "Fase 3"))

conn.commit()
conn.close()
print("Banco criado com sucesso.")

import sys

# Verifica se o número correto de argumentos foi fornecido
if len(sys.argv) != 2:
  print("Usage: python script.py <file_path>")
  sys.exit(1)

# Obtém o caminho do arquivo a partir dos argumentos da linha de comando
file_path = sys.argv[1]

# Tenta abrir e ler o conteúdo do arquivo
try:
  with open(file_path, 'r') as file:
    content = file.read()
  print("Hello, World! " + content)
except FileNotFoundError:
  print(f"Arquivo '{file_path}' não encontrado.")
except Exception as e:
  print("Ocorreu um erro ao ler o arquivo:", e)

# Limpa o buffer de saída
sys.stdout.flush()

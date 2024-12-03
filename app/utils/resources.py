import os

def get_icon_path(icon_name):
    # BASE_DIR é o diretório onde o script main.py está localizado
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Vai um nível acima da pasta utils
    icon_path = os.path.join(BASE_DIR, "icons", icon_name)  # A pasta icons está diretamente na raiz

    # Verificar se o caminho está correto
    print(f"Procurando ícone em: {icon_path}")

    if not os.path.exists(icon_path):
        raise FileNotFoundError(f"Ícone não encontrado: {icon_path}")
    return icon_path

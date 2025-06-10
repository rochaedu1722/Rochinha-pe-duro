# main.py - Entrada principal do bot Rochinha Pé Duro

from app.modes import ultra, omega, modo_rio_v12

def executar_modos():
    print("🔁 Iniciando execução dos modos ativos...")
    ultra.executar()
    omega.executar()
    modo_rio_v12.executar()

if __name__ == "__main__":
    executar_modos()

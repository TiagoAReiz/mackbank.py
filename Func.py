

def anykey():
    import sys
    import termios
    import tty
    # Exibe uma mensagem para o usuário
    print("Pressione qualquer tecla para continuar...")

    # Obtém o descritor de arquivo do stdin
    fd = sys.stdin.fileno()

    # Salva as configurações originais do terminal
    old_settings = termios.tcgetattr(fd)
    try:
        # Altera o modo do terminal para raw, permitindo a leitura de entrada de uma única tecla
        tty.setraw(sys.stdin.fileno())

        # Lê um único caractere do stdin
        sys.stdin.read(1)
    finally:
        # Restaura as configurações originais do terminal
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
def option():
    print('(1) CADASTRAR CONTA CORRENTE(já cadastrada)')
    print('(2) DEPOSITAR')
    print('(3) SACAR')
    print('(4) CONSULTAR SALDO')
    print('(5) CONSULTAR EXTRATO')
    print('(6) FINALIZAR')

    

def verificar_email(email):
    import re
        # Expressão regular para verificar o formato do email
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        # Verificar se o email corresponde ao padrão
    if re.match(padrao, email):
        return True
    else:
        return False
    
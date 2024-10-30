from main import ContaCorrente, CartaoCredito

# Programa
conta_lira = ContaCorrente("lira", "111.222.333-45", "0007-001", "0912509")
conta_lira.consultar_saldo()

# depositar um dinheirinho na conta:
conta_lira.depositar_dinheiro(10000)
conta_lira.consultar_saldo()

# sacar um dinheirinho na conta:
conta_lira.sacar_dinheiro(1000)
conta_lira.consultar_saldo()

conta_lira.consultar_historico_transacoes()

conta_maeLira = ContaCorrente("Beth", "222.333.444-55", "5555", "656565")

conta_maeLira.consultar_saldo()
conta_lira.transferir(1000, conta_maeLira)
conta_maeLira.consultar_saldo()

conta_maeLira.consultar_historico_transacoes()

# Cria uma nova instância da Classe ContaCorrente (conta_lira)
conta_lira = ContaCorrente("lira", "111.222.333-45", "1234", "430662")

# Cria uma nova instância da Classe CartaoCredito (cartao_lira)
cartao_lira = CartaoCredito("lira", conta_lira)

print(cartao_lira.__dict__)
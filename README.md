
# Sistema Bancário em Python

Este projeto simula um sistema bancário com funcionalidades básicas para gerenciar contas correntes, agências e cartões de crédito.

## Estrutura do Projeto

1. **Agenciabancaria.py**: Define as agências bancárias com três tipos de agência (`AgenciaVirtual`, `AgenciaComum`, `AgenciaPremium`), incluindo funcionalidades como verificação de caixa e concessão de empréstimos.
2. **main.py**: Contém as classes principais do sistema:
   - `ContaCorrente`: Classe para gerenciar saldo, depósitos, saques e histórico de transações.
   - `CartaoCredito`: Classe para criação de cartões de crédito associados a contas correntes.
3. **dadosdacontabancaria.py**: Exemplo de uso com operações de depósito, saque e transferência entre contas.

## Funcionalidades

- **Agências**: Três tipos de agências com caixa inicial e regras de empréstimo próprias.
- **Contas Correntes**: Operações de saldo, depósito, saque e histórico de transações.
- **Cartões de Crédito**: Emissão de cartões de crédito para as contas.

## Requisitos

- Python 3.x
- Biblioteca `pytz` para manipulação de fuso horário

## Como Executar

Para visualizar exemplos de uso, execute `dadosdacontabancaria.py` para operações em contas e `Agenciabancaria.py` para operações de agência.

## Licença

Este projeto é apenas para fins educativos e práticos.
## Feito por João vitor luçolli baartz 
"""

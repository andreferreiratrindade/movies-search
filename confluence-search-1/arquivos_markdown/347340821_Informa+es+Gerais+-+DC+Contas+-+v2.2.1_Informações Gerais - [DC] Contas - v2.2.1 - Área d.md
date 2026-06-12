---
                            title: "Informações Gerais - [DC] Contas - v2.2.1 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "347340821_Informa+es+Gerais+-+DC+Contas+-+v2.2.1"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/347340821/Informa+es+Gerais+-+DC+Contas+-+v2.2.1"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Informações Gerais - [DC] Contas - v2.2.1 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Visão Geral
2
Lista de contas
: (
GET
/accounts/v2/accounts)
3
Identificação da conta
: (
GET
/accounts/v2/accounts/{accountId})
4
Saldos da conta
: (GET /accounts/v2/accounts/{accountId}/balances)
5
Transações da conta
: (
GET
/accounts/v2/accounts/{accountId}/transactions)
6
Transações da conta
: (
GET
/accounts/v2/accounts/{accountId}/transactions-current)
7
Limites da conta
: (GET /accounts/v2/accounts/{accountId}/overdraft-limits)
Visão Geral
A API Accounts viabiliza o compartilhamento das informações de contas de depósito à vista, contas de poupança e contas de pagamento pré-paga tais como limites, transações e saldos.
Lista de contas
: (
GET
/accounts/v2/accounts)
Obtém a lista de contas consentidas pelo cliente.
Método para obter a lista de contas depósito à vista, poupança e pagamento pré-pagas mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.
Visão de alto nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos
Identificação da conta
: (
GET
/accounts/v2/accounts/{accountId})
Obtém os dados de identificação da conta mantidos na instituição transmissora.
Essa especificação inclui todos os artefatos relevantes para a Especificação de API sobre a Identificação de uma conta de: depósito à vista, poupança ou de pagamento pré-paga referente às informações transacionais de cliente.
Visão de alto nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos
Saldos da conta
: (GET /accounts/v2/accounts/{accountId}/balances)
Obtém os saldos da conta mantidos na instituição transmissora.
Essa especificação inclui todos os artefatos relevantes para a Especificação de API sobre os saldos de uma conta de: depósito à vista, poupança ou de pagamento pré-paga referente às informações transacionais de cliente.
Visão de alto nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos
Transações da conta
: (
GET
/accounts/v2/accounts/{accountId}/transactions)
Obtém a lista de transações da conta mantidos na instituição transmissora.
Essa especificação inclui todos os artefatos relevantes para a Especificação de API sobre as transações efetivadas e os pagamentos autorizados de uma conta de: depósito à vista, poupança ou de pagamento pré-paga referente às informações transacionais de cliente.
Visão de alto nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos
Transações da conta
: (
GET
/accounts/v2/accounts/{accountId}/transactions-current)
Obtém a lista de transações da conta mantidos na instituição transmissora.
Essa especificação inclui todos os artefatos relevantes para a Especificação de API sobre as transações efetivadas e os pagamentos autorizados de uma conta de: depósito à vista, poupança ou de pagamento pré-paga referente às informações transacionais de cliente.
Visão de alto nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos
Limites da conta
: (GET /accounts/v2/accounts/{accountId}/overdraft-limits)
Obtém os dados de limite de cheque especial e de adiantamento a depositante da conta mantidos na instituição transmissora.
Essa especificação inclui todos os artefatos relevantes para a Especificação de API sobre os valores utilizado e disponível do limite do Cheque Especial e o valor em excesso (Adiantamento a depositante) de uma conta de depósito à vista, referente às informações transacionais de cliente.
Visão de alto nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos

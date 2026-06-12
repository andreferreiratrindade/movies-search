---
                            title: "Informações Gerais - Cartão de Crédito - v2.1.0-rc.3 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "193691666_Informa+es+Gerais+-+Cart+o+de+Cr+dito+-+v2.1.0-rc.3"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/193691666/Informa+es+Gerais+-+Cart+o+de+Cr+dito+-+v2.1.0-rc.3"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Informações Gerais - Cartão de Crédito - v2.1.0-rc.3 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Lista de cartões de crédito:
(GET /credit-cards-accounts/v2/accounts)
2
Identificação de cartão de crédito
: (GET /credit-cards-accounts/v2/accounts/{creditCardAccountId})
3
Limites de cartão de crédito
: ( GET /credit-cards-accounts/v2/accounts/{creditCardAccountId}/limits)
4
Transações de cartão de crédito
: (GET /credit-cards-accounts/v2/accounts/{creditCardAccountId}/transactions)
5
Transações de cartão de crédito
: (GET /credit-cards-accounts/v2/accounts/{creditCardAccountId}/transactions-current)
6
Fatura de Cartão de Crédito
: (GET /credit-cards-accounts/v2/accounts/{creditCardAccountId}/bills)
7
Transações de cartão de crédito por fatura
: (GET /credit-cards-accounts/v2/accounts/{creditCardAccountId}/bills/{billId}/transactions)
Visão Geral
A API Credit-cards-accounts viabiliza o compartilhamento dos dados de conta pós-paga(cartão de crédito), tais como limites, transações e faturas.
Lista de cartões de crédito:
(GET /credit-cards-accounts/v2/accounts)
Visão Geral
Método para obter a lista de contas de pagamento pós-paga mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento
Tags:
Bandeira (Credit Card Network)
,
Cartão Múltiplo (Multiple CreditCard)
,
CNPJ (CNPJ Number)
e
Conta de pagamento pós-paga (Credit Card)
.
Visão de alto de nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos
Identificação de cartão de crédito
: (GET /credit-cards-accounts/v2/accounts/{creditCardAccountId})
Visão Geral
Obtém dados relativos ao conjunto de informações referentes à identificação da conta de pagamento pós-paga
Tags:
Bandeira (Credit Card Network)
,
Cartão Múltiplo (Multiple CreditCard)
,
CNPJ (CNPJ Number)
e
Conta de pagamento pós-paga (Credit Card)
.
Visão de alto de nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos
Limites de cartão de crédito
: ( GET /credit-cards-accounts/v2/accounts/{creditCardAccountId}/limits)
Visão Geral
Obtém dados dos limites: de Crédito Total e por Modalidade de Crédito relativos à conta de pagamento pós-paga.
Tags:
CNPJ (CNPJ Number)
e
Conta de pagamento pós-paga (Credit Card)
,
Empréstimo Cartão Consignado (Payroll Loan)
e
Limite Flexível (Flexible Limit)
.
Visão de alto de nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos
Transações de cartão de crédito
: (GET /credit-cards-accounts/v2/accounts/{creditCardAccountId}/transactions)
Visão Geral
Obtém dados das transações relativas à conta de pagamento pós-paga.
Tags:
CNPJ (CNPJ Number)
e
Conta de pagamento pós-paga (Credit Card)
,
Crédito Rotativo (Overdraft)
e
MCC (Merchant Category Code)
.
Visão de alto de nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos
Transações de cartão de crédito
: (GET /credit-cards-accounts/v2/accounts/{creditCardAccountId}/transactions-current)
Visão Geral
Obtém dados das transações relativas à conta de pagamento pós-paga.
Tags:
CNPJ (CNPJ Number)
e
Conta de pagamento pós-paga (Credit Card)
,
Crédito Rotativo (Overdraft)
e
MCC (Merchant Category Code)
.
Visão de alto de nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos
Fatura de Cartão de Crédito
: (GET /credit-cards-accounts/v2/accounts/{creditCardAccountId}/bills)
Visão Geral
Obtém dados referentes à fatura da conta de pagamento pós-paga.
Tags:
CNPJ (CNPJ Number)
e
Conta de pagamento pós-paga (Credit Card)
,
Crédito Rotativo (Overdraft)
e
Fatura (Bill)
.
Visão de alto de nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos
Transações de cartão de crédito por fatura
: (GET /credit-cards-accounts/v2/accounts/{creditCardAccountId}/bills/{billId}/transactions)
Visão Geral
Obtém a lista de transações da conta identificada por creditCardAccountId e billId.
Tags:
CNPJ (CNPJ Number)
e
Conta de pagamento pós-paga (Credit Card)
,
Crédito Rotativo (Overdraft)
e
MCC (Merchant Category Code)
.
Visão de alto de nível das estruturas de dados
Open
DER - Diagramas de Entidade e Relacionamento
DER Conceitual
Open
DER Lógico
Open
Dicionário de dados
Fazer download do dicionário de dados
Fazer download dos exemplos

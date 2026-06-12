---
                            title: "Orientações - [DC] Cartão de Crédito - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1739292685_Orienta+es+-+DC+Cart+o+de+Cr+dito"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1739292685/Orienta+es+-+DC+Cart+o+de+Cr+dito"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Orientações - [DC] Cartão de Crédito - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Recomendações do uso de
polling
2
Diagrama representacional do status da API Recursos
3
Comportamento da API de Cartão de Crédito com relação a API de Recursos
4
Regras para o retorno das API Cartão de Crédito de acordo com o status do Recurso (PENDING_AUTHORISATION, AVAILABLE, UNAVAILABLE e TEMPORARILY_UNAVAILABLE) e a transição entre status
5
Casos de uso de contas cartões e o respectivo status a ser informado pela API Recursos
6
Tabela descritiva das possibilidades de interação entre API Recursos e as API Cartão de Crédito:
7
Regras quanto a interpretação pelas receptoras do status da API Recursos para os recursos de cartões
8
Regras de busca na API Recursos em relação aos recursos da API Cartão de Crédito:
9
Quanto ao erro 422:
10
Orientações para listagem do paymentMethod:
11
Orientações para envio e compartilhamento de dados:
12
Casos de uso e preenchimento de campos por cenário de transação
Consentimento
​
Consentimento
​
Modelo:
​
Compartilha todos os recursos
selecionados pelo cliente
​
Recursos passíveis de confirmação pelo cliente
​
Conta Cartão ativa em um período de até 12 meses anterior ao início da vigência do consentimento;​
Conta cartão cancelada/encerrada em um período de até 12 meses anterior ao início da vigência do consentimento;​
Recursos que não devem ser escopo de confirmação pelo cliente
​
Conta cartão que não está efetivamente ativa e visível nos canais eletrônicos​
Conta cartão cancelada/encerrada em um período maior que 12 meses anterior ao início da vigência do consentimento;​
Conta cartão que pertence a clientes que estão sob algum tipo de bloqueio que implique em indisponibilidade do produto no canal eletrônico conforme políticas internas das instituições​
Recomendações do uso de
polling
É recomendado que a instituição receptora implemente um retry exponencial (o tempo de espera entre a última chamada e a próxima chamada da API deve crescer exponencialmente), de forma a não sobrecarregar a API Recursos.
Diagrama representacional do status da API Recursos
Consentimento (ex. 4 meses)
Consentimento (ex. 4 meses)
Cenários
DIA D
D+1M
D+2M
D+3M
D+4M
D+5M
Produto cancelado/encerrado em D -13M
Não é escopo de compartilhamento
Produto cancelado/encerrado em D -11M
AVAILABLE
AVAILABLE
UNAVAILABLE
UNAVAILABLE
UNAVAILABLE
Acesso a API não autorizado
Produto cancelado/encerrado em D +2M
AVAILABLE
AVAILABLE
AVAILABLE
AVAILABLE
AVAILABLE
Acesso a API não autorizado
Glossário:
Dia D
– dia do consentimento.
Eixo X
- representa o tempo em meses.
Eixo em Y
– representa o cenários que são produtos e suas vigências. Ex.: conta cartão cancelada/encerrada a 13 meses • O encontro dos eixos representa o status da API Recursos naquele tempo para aquele produto.
Comportamento da API de Cartão de Crédito com relação a API de Recursos
Visão da API de Recursos (Resources) para o Tipo de Cartão de Crédito (Credit-Cards-Accounts)
O identificador único
resourceId
de cada recurso do tipo
CREDIT_CARD_ACCOUNT
presente na lista devolvida pela API, corresponde ao identificador único
creditCardAccountId
utilizado pela API de Cartão de Crédito (Credit-Cards-Accounts). Por exemplo:
{
“data”: [
{
“resourceId”: “12345678990”,
“type”: “ CREDIT_CARD_ACCOUNT “,
“status”: “AVAILABLE”
}
]
}
Exemplo de utilização do
resourceId
em uma chamada a API de Cartão de Crédito (Credit-Cards-Accounts):
credit-cards-accounts/v1/accounts/12345678990
Cartões (ex. virtual / adicional / físico) bloqueados temporariamente não impactam o status da conta cartão associada ao consentimento.
Regras para o retorno das API Cartão de Crédito de acordo com o status do Recurso (PENDING_AUTHORISATION, AVAILABLE, UNAVAILABLE e TEMPORARILY_UNAVAILABLE) e a transição entre status
PENDING_AUTHORISATION
: indica a existência de pendências para o compartilhamento do recurso, em caso de múltiplas alçadas, quando é necessário o consentimento de mais de um titular. Neste caso a Transmissora deve retornar um erro HTTP Status Code 403 - Forbidden com o conteúdo abaixo:
{
“code”: “STATUS_RESOURCE_PENDING_AUTHORISATION”,
“title”: “Aguardando autorização de múltiplas alçadas”,
“detail”: “(uso a critério do transmissor)”
}
AVAILABLE
: indica que o recurso do produto conta cartão escolhido encontra-se disponível para consulta nas API Cartão de Crédito através do identificador creditCardAccountId compartilhado. A Transmissora retorna os dados com status HTTP 200
UNAVAILABLE
: indica que o recurso (conta cartão) se encontra indisponível para consulta na API Cartão de Crédito. Neste caso a Transmissora deve retornar um erro HTTP Status Code 403 - Forbidden com o conteúdo abaixo:
{
“code”: “STATUS_RESOURCE_UNAVAILABLE”,
“title”: “Recurso indisponível”,
“detail”: “(uso a critério do transmissor)”
}
TEMPORARILY_UNAVAILABLE
: indica que o recurso (conta cartão) se encontra temporariamente indisponível para consulta na API Cartão de Crédito do produto em questão. Neste caso a Transmissora deve retornar um erro HTTP Status Code 403 - Forbidden com o conteúdo abaixo:
{
“code”: “STATUS_RESOURCE_TEMPORARILY_UNAVAILABLE”,
“title”: “Recurso temporariamente indisponível”,
“detail”: “(uso a critério do transmissor)”
}
Casos de uso de contas cartões e o respectivo status a ser informado pela API Recursos
Contas Cartão que se encontram em plena utilização e disponível nos canais de atendimento eletrônico devem ter seu status como AVAILABLE.
Conta cartão cancelada/encerrada nos últimos 12 meses anteriores a data consulta – considerando o consentimento vigente - devem ter seus status como AVAILABLE.
Conta Cartão cancelada/encerrada a mais que 12 meses anteriores a data consulta –considerando o consentimento vigente - devem ter seus status como UNAVAILABLE.
Conta cartão cancelada/encerrada, em situações nas quais o cliente não mais possua acesso aos canais de atendimento eletrônico da instituição, devem retornar o status UNAVAILABLE.
Conta cartão que se encontra em bloqueio temporário, onde o cliente não possui acesso aos detalhes por meio dos canais de atendimento eletrônico, devem retornar o status TEMPORARILY_UNAVAILABLE.
Conta cartão que se encontra em bloqueio definitivo onde o cliente não possui acesso por meio dos canais de atendimento eletrônico, devem retornar o status UNAVAILABLE.
Conta cartão ativa com plásticos bloqueados (ex. virtual, adicional ou físico), visualizada pelo cliente nos canais eletrônicos da instituição, deve ter seu status como AVAILABLE.
Conta cartão ativa para a qual ainda não houve desbloqueio de nenhum plástico - visualizada pelo cliente nos canais eletrônicos da instituição -deve ter seu status como AVAILABLE.
Conta cartão que não está ativa e não pode ser visualizada pelo cliente no canal, como por exemplo as que são criadas “dormentes”, e dependem de ação do cliente para que se tornem ativas não devem ser compartilhadas.
Casos de uso que um cliente final efetue um consentimento para conta cartão para o qual um dos recursos (respeitando a RN001) exija a aprovação de múltiplas alçadas (PENDING_AUTHORISATION) e outro recurso esteja disponível para consulta (AVAILABLE), o comportamento esperado é que cada recurso tenha seu status representado de forma independente, disponibilizando imediatamente os recursos já aprovados.
Tabela descritiva das possibilidades de interação entre API Recursos e as API Cartão de Crédito:
Cenário
Status do recurso na transmissora
API Recursos (.../resources/v1/resources)
API de listagem de Produto (/accounts)¹
APIs de Identificação da Conta (/accounts/{creditCardAccountId}²
Code
Cenário
Status do recurso na transmissora
API Recursos (.../resources/v1/resources)
API de listagem de Produto (/accounts)¹
APIs de Identificação da Conta (/accounts/{creditCardAccountId}²
Code
Sem consentimento
-
401 unauthorized
401 unauthorized
401 unauthorized
Com consentimento não autorizado
-
401 unauthorized
401 unauthorized
401 unauthorized
Com consentimento autorizado (pendente múltipla alçada)
-
200 - Retorna recurso com status PENDING_ AUTHORISATION
200 Não retorna
403 forbidden
Com consentimento autorizado (aprovado múltipla alçada)
OK
200 - Retorna o recurso com status AVAILABLE
200 retorna o recurso na lista
200 retorna dados para o recurso
Com consentimento autorizado (aprovado múltipla alçada)
Bloqueio Temporário
200 - Retorna o recurso com status TEMPORARY_ UNAVAILABLE
200 Não retorna na lista o recurso “bloqueado”
403 forbidden
Com consentimento autorizado (aprovado múltipla alçada)
Cancelado/Encerrado
200 - Retorna o recurso como status AVAILABLE
200 retorna o recurso na lista
200 retorna o recurso na lista
Com consentimento autorizado (aprovado múltipla alçada)
Cancelado/Encerrado a mais de 12 meses (recurso nunca compartilhado na vigência do consentimento)
200 – Não retorna o recurso
200 – Não retorna o recurso
403 forbidden
Com consentimento autorizado (aprovado múltipla alçada)
Cancelado/Encerrado a mais de 12 meses (recurso já compartilhado na vigência do consentimento)
200 - Retorna o recurso como status UNAVAILABLE
200 – Não retorna o recurso
403 forbidden
Com consentimento autorizado (recusado múltipla alçada)
-
200 - Retorna recurso com status UNAVAILABLE
200 - Não retorna recurso recusado na lista
403 forbidden
Com consentimento autorizado (conta inexistente)
-
200 – Não retorna o recurso
200 – Não retorna o recurso
403 forbidden
RESOURCE_FORBIDDEN
Com consentimento revogado ou expirado¹
-
401 unauthorized
401 unauthorized
401 unauthorized
Regras quanto a interpretação pelas receptoras do status da API Recursos para os recursos de cartões
PENDING_AUTHORISATION
: neste caso a recomendação é que a Receptora aguarde a alteração desse status para um dos demais status executando polling na API Recursos (vide recomendações de polling).
AVAILABLE
: indica que o recurso encontra-se disponível para consulta na API Cartão de Crédito através do identificador creditCardAccountId compartilhado.
UNAVAILABLE
: neste status a recomendação é que a Receptora não consulte a API Cartão de Crédito em função do dado não estar disponível para esse creditCardAccountId.
TEMPORARILY_UNAVAILABLE
: neste status a recomendação é que a Receptora aguarde a alteração desse status para um dos demais status executando polling na API Recursos (vide recomendações de polling).
Regras de busca na API Recursos em relação aos recursos da API Cartão de Crédito:
Recomenda-se que a Receptora consulte a API Recursos logo após identificar que o consentimento se encontra autorizado de modo a obter as contas cartão consentida pelo cliente e seus respectivos identificadores.
Recomenda-se que a Receptora, caso obtenha um erro HTTP Status Code 403 - Forbidden na API Cartão de Crédito avalie o JSON retornado no body da requisição para identificar as informações adicionais referentes ao erro, como o status específico da API Recursos que impede o consumo da informação.
Recomenda-se que a Receptora consulte a API Recursos caso obtenha um erro na API Cartão de Crédito, de modo a identificar uma possível alteração de status do recurso.
Quanto ao erro 422:
Na especificação técnica existe a possibilidade de retornar o código HTTP Status Code 422 - accepted. Este código de retorno deve ser utilizado quando algum parâmetro da consulta for enviado semanticamente incorreto, ou seja, desrespeitando uma regra de negócio, para os seguintes
endpoints
:
/accounts/{creditCardAccountId}/bills;
/accounts/{creditCardAccountId}/{billId}/transactions;
/accounts/{creditCardAccountId}/transactions;
/accounts/{creditCardAccountId}/transactions-current.
Orientações para listagem do paymentMethod:
Para o retorno listagem dos cartões (campo paymentMethod) do endpoint de Identificação de Cartão (GET /accounts/{creditCardAccountId}), os cartões físicos e virtuais ativos (de titular, dependentes ou adicionais) são de compartilhamento obrigatório através desta listagem. Caso o cartão já tenha sido excluído, o seu envio torna-se opcional.
Obs:
Ainda que o cartão não conste nesta listagem, as transações relacionadas devem ser listadas com o número de identificação do cartão (campo identificationNumber) correspondente.
Orientações para envio e compartilhamento de dados:
Pagamentos efetuados a partir do momento que uma nova fatura é fechada e exposta, devem estar atrelados a essa fatura através da lista
/data/payments
do endopoint
GET /accounts/{creditCardAccountId}/bills
, até que haja um novo fechamento de fatura. Exceto para pagamentos de faturas realizados para liberação de limite ou pagamentos adiantados, estes devem ser reportados na próxima fatura subsequente quando for efetivamente fechada. Enquanto não ocorre o fechamento, ele deve ser reportado só nos
GET /accounts/{creditCardAccountId}/transactions e transactions-current
Como exemplo de preenchimento da lista
/data/payments
, temos o cenário a seguir:
Dado que o cliente tenha duas faturas fechadas, uma no dia 15/05/2025 e a outra no dia 15/06/2025, e tenha realizado os três pagamentos abaixo:
30/04/25: pagamento avulso (Ex.: para liberação de limite)
20/05/25: pagamento valor total fatura
28/05/25: pagamento avulso (Ex.: para liberação de limite)
20/06/25: pagamento valor mínimo
Os pagamentos ficam atrelados às faturas da seguinte forma:
Data de fechamento da Fatura
Pagamentos atrelados a fatura
Data de fechamento da Fatura
Pagamentos atrelados a fatura
15/05/2025
30/04/2025: pagamento avulso (para liberação de limite)
20/05/2025: pagamento do valor total da fatura
15/06/2025
28/05/25: pagamento avulso (para liberação de limite)
20/06/25: pagamento valor mínimo
Os endpoints de
GET accounts/{creditCardAccountId}/transactions
e
transactions-current
devem compartilhar transações conciliadas
O endpoint
GET /accounts/{creditCardAccountId}/bills/{billId}/transactions
deve compartilhar transações conciliadas e faturadas
Os filtros
fromTransactionDate
e
toTransactionDate
devem levar em conta o campo
transactionDateTime
para realização da consulta nos
endpoints
de
transactions
Casos de uso e preenchimento de campos por cenário de transação
Preenchimento por campo:
Situação
billId
billPostDate
billForecastDate
Observações
Situação
billId
billPostDate
billForecastDate
Observações
Transação já faturada (fatura fechada)
Sim
Sim, Data real da inserção
Sim, mês/ano da fatura (ex.: '2021-01')
billForecastDate indica o mês/ano da fatura já fechada.
Transação em fatura aberta
Sim (quando atribuído)
Sim, Data real
Sim, mês/ano da fatura atual (ex.: '2021 01')
billForecastDate indica o mês/ano da fatura atual. billId pode estar presente mesmo em fatura aberta.
Transação futura (parcelada / próxima fatura)
Não
0001-01-01
Sim, mês/ano da fatura futura (ex.: '2021 02')
billForecastDate projeta o mês/ano de faturamento futuro.
Transação não elegível a fatura (ex. agendada)
Não
0001-01-01
Sim, mês/ano previsto de inserção futura
billForecastDate projeta o mês/ano de faturamento futuro.
Casos de uso por temporalidade por tipo de evento (regras de data e vínculo):
Caso de uso
Regras temporais principais
Campos temporais esperados
Caso de uso
Regras temporais principais
Campos temporais esperados
Compra à vista (A_VISTA)
Entra na fatura em formação e consolida no fechamento do ciclo. billForecastDate sempre presente indicando o mês/ano de faturamento.
Se ainda sem fatura: billPostDate=0001-01-01. Quando houver fatura: preencher billId e billPostDate real. Obrigatório enviar billForecastDate (formato 'AAAA-MM').
Compra parcelada – parcela do mês
Cada parcela lança no mês correspondente (competência daquele ciclo). billForecastDate indica o mês atual de faturamento.
Para a parcela lançada: billId + billPostDate real. Obrigatório billForecastDate (formato 'AAAA-MM').
Compra parcelada – parcelas futuras
Competência em faturas futuras (ainda não lançadas). billForecastDate indica o mês/ano futuro de cada parcela.
Sem billId; billPostDate=0001-01-01. Obrigatório billForecastDate (formato 'AAAA-MM', indicando abertura prevista da fatura futura).
Saque
Postagem normalmente próxima ao evento; consolida no fechamento. billForecastDate indica quando será faturado.
Se sem fatura: billPostDate=0001-01-01. Com fatura: billId + billPostDate real. Obrigatório billForecastDate (formato 'AAAA-MM').
Tarifa
Lançada por política (mensal/uso); consolida no fechamento. billForecastDate indica o mês/ano de cobrança.
Se sem fatura: billPostDate=0001-01-01. Com fatura: billId + billPostDate real. Obrigatório billForecastDate (formato 'AAAA-MM').
Estorno (chargeback/ajuste)
Pode ocorrer no mesmo ciclo da compra ou em ciclo posterior; consolida quando lançado. billForecastDate indica quando será aplicado na fatura.
Quando lançado: billId + billPostDate real. Se ainda não lançado: billPostDate=0001-01-01. Obrigatório billForecastDate (formato 'AAAA-MM').
Pagamento de fatura
Não altera billPostDate de transações; pertence sempre a uma fatura e aparece somente em /bills (payments[]).
Não usa billPostDate/billForecastDate; sempre associado a billId; listado em /bills com payments[]; billClosingDate fecha a competência.

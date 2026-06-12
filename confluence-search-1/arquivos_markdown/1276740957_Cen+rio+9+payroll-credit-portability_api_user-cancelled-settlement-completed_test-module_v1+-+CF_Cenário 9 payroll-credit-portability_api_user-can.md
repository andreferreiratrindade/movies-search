---
                            title: "Cenário 9: payroll-credit-portability_api_user-cancelled-settlement-completed_test-module_v1 - CF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1276740957_Cen+rio+9+payroll-credit-portability_api_user-cancelled-settlement-completed_test-module_v1+-+CF"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1276740957/Cen+rio+9+payroll-credit-portability_api_user-cancelled-settlement-completed_test-module_v1+-+CF"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Cenário 9: payroll-credit-portability_api_user-cancelled-settlement-completed_test-module_v1 - CF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Tipo do teste
Teste de exceção
Descrição
Validação de mensagens e comportamentos do sistema em situações de erro no processo de verificação de respostas.
Objetivo
Garante que a cliente não possa cancelar um pedido de solicitação portabilidade após liquidação ter sido realizada.
Requisito de massa
Um contrato com a categoria CONSIGNADO_SIAPE e com o campo status como 'DISPONIVEL' e o campo isEligible como 'TRUE'
Script
Os passos abaixo são todas as requisições que serão feitas para a jornada do teste acima. Além das requisições temos as respostas esperada para cada requisição a ser realizada para respeitar o teste especifico.
Este cenário se encontra no arquivo disponibilizado em uma página de
WIKI
no Gitlab disponibilizado pela Raidiam.
Foi feita a tradução para português e criado um diagrama de sequência para auxilio no entendimento do cenário de teste.
Steps
Requisições
Respostas esperadas
Etapa da Jornada
Steps
Requisições
Respostas esperadas
Etapa da Jornada
1
Chamada de endpoint POST /consents com o grupo de permissão 'Credit Operations'
Status 201 - Garantindo de status como AWAITING_AUTHORISATION
Etapa de consentimento
2
Redirecionamento para usuário autorizar o consentimento
3
Chamada de endpoint GET /consents/{consentId}
Status 200 - Garantindo de status como AUTHORISED
4
Chamada de endpoint GET Loans Contracts
Status 200 - Recuperando todos os contractIds com data.productSubTypeCategory = "CONSIGNADO_SIAPE" and companyCnpj
Etapa de busca e validação de contrato
5
Chamada de endpoint GET /credit-operations/{contractId}/portability-eligibility para cada contractId até encontrar ao menos um com status como "DISPONIVEL" e isEligible como "TRUE"
6
Chamada de endpoint GET Loans Contracts/{contractId}
Status 200 - Recuperando instalmentPeriodicity
7
Chamada de endpoint GET Loans Contracts/{contractId}/scheduled-installments
Status 200 - Recuperando dueInstalments
8
Chamada de endpoint GET Loans Contracts/{contractId}/payments
Status 200 - Recuperando contractOutstandingBalance
9
Chamada do endpoint POST /portabilities enviando os seguintes valores:
data.institution.creditor.companyCnpj = original companyCnpj
instalmentPeriodicity = original instalmentPeriodicity
proposedContract.totalNumberOfInstalments = original dueInstalments
contractAmount = original contractOutstandingBalance
Status 202 - Resposta de sucesso
Etapa de criação de solicitação de portabilidade
10
Serão feitas a chamadas de endpoint GET /portabilities/{portabilityId} a cada 10 minutos enquanto status estiver em "RECEIVED" ou "PENDING"
Status 200 - Validação de resposta de acordo com a especificação e data.status igual “ACCEPTED_SETTLEMENT_IN_PROGRESS”
Etapa de contraproposta e Etapa de liquidação
11
Chamada de endpoint GET /portabilities/{portabilityId}/account-data
Status 200 - Resposta de sucesso
Etapa de liquidação
12
Chamada de endpoint POST /portabilities/{portabilityId}/payment, incluindo detalhes de pagamento:
paymentAmount = original contractOutstandingBalance
Status 202 - Validação de resposta de acordo com a especificação
13
Serão feitas a chamadas de endpoint GET /portabilities/{portabilityId} a cada 10 minutos enquanto status estiver em "ACCEPTED_SETTLEMENT_IN_PROGRESS"
Status 200 - Validação de resposta de acordo com a especificação e data.status igual “ACCEPTED_SETTLEMENT_COMPLETED”
Etapa de validação da liquidação
14
Chamada de endpoint PATCH /portabilities/{portabilityId}/cancel enviando rejectedBy como "USUARIO" e reason.type como "CANCELADO_PELO_CLIENTE"
Status 422 - Esperando código de erro como "CANCELAMENTO_NAO_EFETUADO"
Etapa de cancelamento de solicitação de portabilidade de crédito
15
Fim do teste
Diagrama de sequência
Open

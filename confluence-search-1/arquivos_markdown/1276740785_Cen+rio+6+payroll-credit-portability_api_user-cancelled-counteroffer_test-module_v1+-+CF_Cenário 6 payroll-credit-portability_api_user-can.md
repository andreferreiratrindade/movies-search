---
                            title: "Cenário 6: payroll-credit-portability_api_user-cancelled-counteroffer_test-module_v1 - CF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1276740785_Cen+rio+6+payroll-credit-portability_api_user-cancelled-counteroffer_test-module_v1+-+CF"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1276740785/Cen+rio+6+payroll-credit-portability_api_user-cancelled-counteroffer_test-module_v1+-+CF"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Cenário 6: payroll-credit-portability_api_user-cancelled-counteroffer_test-module_v1 - CF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Tipo do teste
Teste funcional
Descrição
Criação e cancelamento de solicitação de portabilidade
Objetivo
Garante que o cliente cancele um pedido de solicitação portabilidade enquanto credora analisa proposta
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
Serão feitas a chamadas de endpoint GET /portabilities/{portabilityId} a cada 10 minutos enquanto status estiver em "RECEIVED"
Status 200 - Validação de resposta de acordo com a especificação e data.status igual "PENDING"
Etapa de contraproposta
11
Chamada de endpoint PATCH /portabilities/{portabilityId}/cancel enviando rejectedBy como 'USUARIO' e reason.type como 'CANCELADO_PELO_CLIENTE'
Status 200 - Validação de resposta de acordo com a especificação
Etapa de cancelamento da solicitação de portabilidade
12
Chamada de endpoint GET /portabilities/{portabilityId}
Status 200 - Campo status igual a "CANCELLED" e statusReason.reasonType como "CANCELADO_PELO_CLIENTE"
13
Fim do teste
Diagrama de sequência
Open

---
                            title: "Cenário 16: credit-portability_api_portability-patch-unhappy_test-module_v1 - CPC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1329299944_Cen+rio+16+credit-portability_api_portability-patch-unhappy_test-module_v1+-+CPC"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1329299944/Cen+rio+16+credit-portability_api_portability-patch-unhappy_test-module_v1+-+CPC"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Cenário 16: credit-portability_api_portability-patch-unhappy_test-module_v1 - CPC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Tipo do teste
Teste de exceção
Descrição
Validação de mensagens e comportamentos do sistema em situações de inconsistências na credencial de verificação de respostas.
Objetivo
Garantir que há impossibilidade de se cancelar uma solicitação de portabilidade ao chegar ao estado “Accepted_Settlement_Completed”
Requisito de massa
Um contrato do tipo CREDITO_PESSOAL_CLEAN com o campo status como 'DISPONIVEL' e o campo isEligible como 'TRUE'
This test also requires action from the tester. It will poll for 10 minutes, waiting for the portability status transition to "ACCEPTED_SETTLEMENT_COMPLETED".
Script
Os passos abaixo são todas as requisições que serão feitas para a jornada do teste acima. Além das requisições temos as respostas esperada para cada requisição a ser realizada para respeitar o teste especifico.
Este cenário se encontra no arquivo disponibilizado em uma página de
WIKI
no Gitlab disponibilizado pela Raidiam.
Foi feita a tradução para português e criado um diagrama de sequência para auxilio no entendimento do cenário de teste.
Steps
Requisições
Respostas esperadas
Steps
Requisições
Respostas esperadas
1
Chamada de endpoint POST /consents com o grupo de permissão 'Credit Operations'
Status 201 - Garantindo de status como AWAITING_AUTHORISATION
2
Redirecionamento para usuário autorizar o consentimento
3
Chamada de endpoint GET /consents/{consentId}
Status 200 - Garantindo de status como AUTHORISED
4
Chamada de endpoint GET Loans Contracts
Status 200 - Recuperando todos os contractIds com productSubType = “CREDITO_PESSOAL_CLEAN” e companyCnpj
5
Chamada de endpoint GET /credit-operations/{contractId}/portability-eligibility, para cada contractId até encontrar ao menos um com status como "DISPONIVEL" e isEligible como "TRUE"
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
Chamada de endpoint POST /portabilities utilizando os seguintes valores:
data.institution.creditor.companyCnpj = original companyCnpj
instalmentPeriodicity = original instalmentPeriodicity
proposedContract.totalNumberOfInstalments = original dueInstalments
contractAmount = original contractOutstandingBalance
Status 202 - Validação de resposta de acordo com especificação
10
Rotina de tempo com a chamada de endpoint GET /portabilities/{portabilityId} por 10 minutos enquanto encontrar status igual a “RECEIVED” ou “PENDING”
Status 200 - Validação de resposta e garantia que o status seja igual "ACCEPTED_SETTLEMENT_IN_PROGRESS"
11
Chamada de endpoint GET /account-data
Status 200 - Validação de resposta de acordo com especificação
12
Chamada de endpoint POST /portabilities/{portabilityId}/payment, incluindo detalhes de pagamentos:
paymentAmount = original contractOutstandingBalance
Status 202 - Validação de resposta de acordo com especificação
13
Rotina de tempo com a chamada de endpoint GET /portabilities/{portabilityId} por 10 minutos enquanto encontrar status igual a “ACCEPTED_SETTLEMENT_IN_PROGRESS”
Status 200 - Validação de resposta e garantia que o status seja igual "ACCEPTED_SETTLEMENT_COMPLETED"
14
Chamada de endpoint PATCH /portabilities/{portabilityId}/cancel
Status 422 - Validação de resposta de acordo com a especificação
15
Chamada de endpoint GET /portabilities/{portabilityId}/account-data
Status 200 - Validação de resposta de acordo com especificação
16
Chamada de endpoint POST /portabilities/{portabilityId}/payment, incluindo detalhes de pagamento:
paymentAmount = original contractOutstandingBalance
Status 202 - Validação de resposta de acordo com especificação
17
Chamada de endpoint PATCH /portabilities/{portabilityId}/cancel
Status 422 - Validação de resposta de acordo com a especificação
18
Fim do teste
Diagrama de sequência
Open

---
                            title: "Cenário 6: credit-portability_api_accepted_settlement_test-module_v1 - CPC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1329299654_Cen+rio+6+credit-portability_api_accepted_settlement_test-module_v1+-+CPC"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1329299654/Cen+rio+6+credit-portability_api_accepted_settlement_test-module_v1+-+CPC"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Cenário 6: credit-portability_api_accepted_settlement_test-module_v1 - CPC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Tipo do teste
Teste funcional
Descrição
Validação de mensagens e comportamentos do sistema em situações de erro no processo de verificação de respostas.
Objetivo
Garante que o pedido de portabilidade seja rejeitado quando não há assinatura no contrato
Requisito de massa
Um contrato do tipo CREDITO_PESSOAL_CLEAN com o campo status como 'DISPONIVEL' e o campo isEligible como 'TRUE'
Deverá haver uma interação humana para que realize um pool para validar o estado 'ACCEPTED_SETTLEMENT_IN_PROGRESS'
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
Status 200 - Recuperando todos os contractIds com productSubType = “CREDITO_PESSOAL_CLEAN” e companyCnpj
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
Status 202 - Validação de resposta de acordo com especificação
Etapa de criação de solicitação de portabilidade
10
Rotina de tempo com a chamada de endpoint GET /portabilities/{portabilityId} por 10 minutos enquanto encontrar status igual a “RECEIVED” ou “PENDING”
Status 200 - Validação de resposta e garantia que o status seja igual "ACCEPTED_SETTLEMENT_IN_PROGRESS"
Etapa de criação de contra proposta e Liquidação do contrato
11
Fim do teste
Diagrama de sequência
Open

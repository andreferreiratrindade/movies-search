---
                            title: "Cenário 12: credit-portability_api_invalid-token_test-module_v1 - CPC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1329299828_Cen+rio+12+credit-portability_api_invalid-token_test-module_v1+-+CPC"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1329299828/Cen+rio+12+credit-portability_api_invalid-token_test-module_v1+-+CPC"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Cenário 12: credit-portability_api_invalid-token_test-module_v1 - CPC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Tipo do teste
Teste de exceção
Descrição
Validação de mensagens e comportamentos do sistema em situações de inconsistências na credencial de verificação de respostas.
Objetivo
Garantir que não há chamadas de endpoints quando token grant está inválido
Requisito de massa
Um contrato do tipo CREDITO_PESSOAL_CLEAN com o campo status como 'DISPONIVEL' e o campo isEligible como 'TRUE'
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
Chamada de endpoint GET /credit-operations/{contractId}/portability-eligibility enviando Authorization como token com client_credentials grant
Status 401 ou 403 - Validando mensagem de erro
6
Chamada de endpoint GET /credit-operations/{contractId}/portability-eligibility com x-fapi-interaction-id válido, para cada contractId até encontrar ao menos um com status como "DISPONIVEL" e isEligible como "TRUE"
7
Chamada de endpoint GET Loans Contracts/{contractId}
Status 200 - Recuperando instalmentPeriodicity
8
Chamada de endpoint GET Loans Contracts/{contractId}/scheduled-installments
Status 200 - Recuperando dueInstalments
9
Chamada de endpoint GET Loans Contracts/{contractId}/payments
Status 200 - Recuperando contractOutstandingBalance
10
Chamada do endpoint POST /portabilities enviando os seguintes valores:
data.institution.creditor.companyCnpj = original companyCnpj
instalmentPeriodicity = original instalmentPeriodicity
proposedContract.totalNumberOfInstalments = original dueInstalments
contractAmount = original contractOutstandingBalance
Authorization = token com client_credentials grant
Status 401 ou 403 - Validando mensagem de erro
11
Chamada do endpoint POST /portabilities enviando os seguintes valores:
instalmentPeriodicity = original instalmentPeriodicity
proposedContract.totalNumberOfInstalments = original dueInstalments
contractAmount = original contractOutstandingBalance
Authorization = token com authorization_code grant
Status 202 - Validação de resposta de acordo com a especificação
12
Chamada de endpoint Get /portabilities/{portabilityId} enviando Authorization como token com authorization_code grant
Status 401 ou 403 - Validando mensagem de erro
13
Chamada de endpoint PATCH /portabilities/{portabilityId}/cancel enviando Authorization como token com authorization_code grant
Status 401 ou 403 - Validando mensagem de erro
14
Chamada de endpoint GET portabilities/{portabilityId}/account-data enviando Authorization como token com authorization_code grant
Status 401 ou 403 - Validando mensagem de erro
15
Chamada de endpoint POST /portabilities/{portabilityId}/payment enviando Authorization como token com authorization_code grant
Status 401 ou 403 - Validando mensagem de erro
16
Fim do teste
Diagrama de sequência
Open

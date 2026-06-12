---
                            title: "Cenário 13: credit-portability_api_invalid-consent_test-module_v1 - CPC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1329299857_Cen+rio+13+credit-portability_api_invalid-consent_test-module_v1+-+CPC"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1329299857/Cen+rio+13+credit-portability_api_invalid-consent_test-module_v1+-+CPC"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Cenário 13: credit-portability_api_invalid-consent_test-module_v1 - CPC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Tipo do teste
Teste de exceção
Descrição
Validação de mensagens e comportamentos do sistema em situações de inconsistências na credencial de verificação de respostas.
Objetivo
Garantir que há validações que o x-fapi seja informado nas requisições de todos os endpoints
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
Chamada de endpoint POST /portabilities com x-fapi-interaction-id válido, utilizando os seguintes valores:
data.institution.creditor.companyCnpj = original companyCnpj
instalmentPeriodicity = original instalmentPeriodicity
proposedContract.totalNumberOfInstalments = original dueInstalments
contractAmount = original contractOutstandingBalance
11
Chamada de endpoint GET Loans Contracts/{contractId}/payments
Status 200 - Recuperando contractOutstandingBalance
12
Criar consentimento com todas as permissões necessárias para acesso ao Customer Personal ou a Customer Business API: ("CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ", "CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ", "RESOURCES_READ")ou (“CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ”,” "CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ”, "RESOURCES_READ")
Status 201 - Garantindo de status como AWAITING_AUTHORISATION
13
Redirecionamento para usuário autorizar o consentimento
14
Chamada de endpoint GET /consents/{consentId}
Status 200 - Garantindo de status como AUTHORISED
15
Chamada de endpoint GET /credit-operations/{contractId}/portability-eligibility enviando:
Authorization = token vinculado a consentimento com as permissões de usuário
Status 403 - Validando mensagem de erro
16
Chamada de endpoint POST /portabilities utilizando token vinculado um consentimento com permissões de usuários e enviando:
data.institution.creditor.companyCnpj = original companyCnpj
instalmentPeriodicity = original instalmentPeriodicity
proposedContract.totalNumberOfInstalments = original dueInstalments
contractAmount = original contractOutstandingBalance
Authorization = token vinculado a um consentimento com as permissões de usuário
Status 403 - Validando mensagem de erro
17
Chamada de endpoint Get /portabilities/{portabilityId} enviando:
Authorization = token vinculado a um consentimento com permissões de usuário.
Status 403 - Validando mensagem de erro
18
Chamada de endpoint PATCH /portabilities/{portabilityId}/cancel enviando:
Authorization = token vinculado a um consentimento com permissões de usuário
Status 403 - Validando mensagem de erro
19
Chamada de endpoint GET portabilities/{portabilityId}/account-data enviando:
Authorization = token vinculado a um consentimento com consentimento com permissões de usuário
Status 403 - Validando mensagem de erro
20
Chamada de endpoint POST /portabilities/{portabilityId}/payment enviando:
Authorization = token vinculado a um consentimento com permissões de usuário
Status 403 - Validando mensagem de erro
21
Fim do teste
Diagrama de sequência
Open

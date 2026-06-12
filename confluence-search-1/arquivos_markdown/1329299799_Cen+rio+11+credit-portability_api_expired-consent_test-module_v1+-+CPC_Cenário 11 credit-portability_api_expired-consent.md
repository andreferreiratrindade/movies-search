---
                            title: "Cenário 11: credit-portability_api_expired-consent_test-module_v1 - CPC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1329299799_Cen+rio+11+credit-portability_api_expired-consent_test-module_v1+-+CPC"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1329299799/Cen+rio+11+credit-portability_api_expired-consent_test-module_v1+-+CPC"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Cenário 11: credit-portability_api_expired-consent_test-module_v1 - CPC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Tipo do teste
Teste de exceção
Descrição
Validação de mensagens e comportamentos do sistema em situações de inconsistências na credencial de verificação de respostas.
Objetivo
Garantir que a solicitação portabilidade não é criada devido a expiração do consentimento.
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
Chamada de endpoint POST /consents com o grupo de permissão 'Credit Operations' e configurar o campo expirationDateTime para 5 minutos no futuro
Status 201 - Garantindo de status como AWAITING_AUTHORISATION
2
Redirecionamento para usuário autorizar o consentimento
3
Chamada de endpoint GET /consents/{consentId}
Status 200 - Garantindo de status como AUTHORISED
4
Chamada de endpoint GET Loans Contracts
Status 200 - Recuperando todos os contractIds com data.productSubTypeCategory = CREDITO_PESSOAL_SEM_CONSIGNACAO e companyCnpj
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
Rotina de tempo para chamada de endpoint GET consents para 5 minutos, uma chamada a cada 30 segundos
10
Continuação de rotina de tempo até o consentimento encontre o status "REJECTED"
11
Chamada de endpoint POST /portabilities enviando os seguintes valores:
data.institution.creditor.companyCnpj = original companyCnpj
instalmentPeriodicity = original instalmentPeriodicity
proposedContract.totalNumberOfInstalments = original dueInstalments
contractAmount = original contractOutstandingBalance
Authorization = token associated to the expired consent
Status 401 - Validação de resposta conforme especificação garantindo que o consentimento está expirado
12
Fim do teste
Diagrama de sequência
Open

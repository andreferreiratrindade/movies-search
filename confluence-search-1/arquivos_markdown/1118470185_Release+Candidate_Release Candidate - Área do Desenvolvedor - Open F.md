---
                            title: "Release Candidate - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1118470185_Release+Candidate"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1118470185/Release+Candidate"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Release Candidate - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Objetivo desta página
Acompanhar, em caráter preliminar, a lista e status das iniciativas previstas para cada novo ciclo de desenvolvimento da PCM
Release 2026B
Contexto
Detalhes
Status atual
Contexto
Detalhes
Status atual
Itens associados à versão 5 da API de Pagamentos
Pagamentos
Inclusão de novo endpoint /open-banking/payments/v5/consents/{consentId}/pix/payments. O endpoint /open-banking/payments/v4/pix/payments/consents/{consentId}) continua válido durante o período de convivência entre as versões 4 e 5 da API de Pagamentos. O cronograma pode ser acompanhado conforme calendário,  acessado através do link
https://us5.campaign-archive.com/?u=49f5ff8910ce85bdb1d9a7864&id=e1c812dbf5
Concluído
Obrigatoriedade de additionalInfo para Pagamentos
Inclusão de novos enums nos seguintes additionalInfo:
localInstrument
APDN
APES
rejectionReasonCode
AUTENTICACAO_DIVERGENTE​
CHAVE_PIX_DIVERGENTE_AGENDAMENTO_LIQUIDACAO
CONTA_NAO_PERMITE_PAGAMENTO
QRCODE_INVALIDO
PERMISSAO_INSUFICIENTE
errorCodes
PROPOSITO_INVALIDO
páymentType
WITHDRAW
CHANGE
Estes enums serão validados nos tickets de Qualidade de Dados de Pagamentos
Concluído
Obrigatoriedade de additionalInfo para Pagamentos
Alteração do additionalInfo paymentSchedule: remoção do item additionalInformation do paymentSchedule de dentro da estrutura de custom e tornar um item no mesmo nível do tipo de agendamento (válido para todos os tipos de agendamento).
Exemplos:
De
{custom:{dates:['2026-01-01','2026-02-01','2026-03-01'],additionalInformation:'qwerty'}}
Para
{custom:{dates:['2026-01-01','2026-02-01','2026-03-01']},additionalInformation:'qwerty'}
De
{monthly:{dayOfMonth:1,startDate:'2026-01-01',quantity:12}}
Para
{monthly:{dayOfMonth:1,startDate:'2026-01-01',quantity:12},additionalInformation:'qwerty'}
Concluído
Estoque de Consentimentos
Alteração na regra de validação da quantidade de paymentId únicos por consentId:
A quantidade máxima de pagamentos que podem transitar do iniciador para o detentor é de 60 pagamentos, independentemente do modelo de recorrência definido no consentimento. A data do último pagamento agendado não pode ultrapassar o correspondente dia e mês do segundo ano subsequente à data de criação do consentimento (prazo máximo de dois anos).
Ex.: consentimento criado em 15/03/2026 admite agendamentos até 15/03/2028
Concluído
Itens referentes somente à versão 2026B da PCM
Portabilidade de Crédito
Novo produto Crédito Consignado Federal
Inclusão de novos endpoints a serem monitorados na PCM
/open-banking/payroll-credit-portability/vx/portabilities
/open-banking/payroll-credit-portability/vx/portabilities/{portabilityId}
/open-banking/payroll-credit-portability/vx/portabilities/{portabilityId}/account-data
/open-banking/payroll-credit-portability/vx/portabilities/{portabilityId}/cancel
/open-banking/payroll-credit-portability/vx/portabilities/{portabilityId}/payment
/open-banking/payroll-credit-portability/vx/credit-operations/{contractId}/registering-entity
/open-banking/payroll-credit-portability/vx/credit-operations/{contractId}/portability-eligibility
/open-banking/payroll-credit-portability/vx/portabilities/{portabilityId}/request-discharge
Novo campo hasFinancialAgent, com as seguintes regras de validação:
role = SERVER
Todos statusCode exceto 4xx e 5xx
httpMethod = GET
endpoint = /open-banking/payroll-credit-portability/vx/portabilities/{portabilityId}/account-data
Inclusão de uma página no Confluence com as regra de validação dos campos para este novo produto
Inclusão da validação dos novos endpoints e do novo campo nos tickets de Portabilidade de Crédito (Qualidade, Descartados e Pareamento)
Retirado da release conforme Informa #901
additionalInfo dropReason em Pagamentos e Clientes
Novos enum no additionalInfo dropReason:
CREDENTIAL_UNAVAILABLE
TECHNICAL_FAILURE
Alteração na regra de preenchimento para:
O campo dropReason deve ser adicionado nas informações do campo additionalInfo que deverá ser enviado no reporte do provedor do serviço consumido (papel SERVER). O campo deverá ser preenchido com um dos seguintes valores:​
NONE
: CPF/CNPJ possui credencial autenticadora e o servidor já verificou que possui poderes suficientes para completar a ação solicitada, ou o usuário abandonou a jornada após essa verificação bem-sucedida.​
NO_CREDENTIAL
: Quando o CPF/CNPJ não possui credencial autenticadora cadastrada na instituição, por inexistência de relacionamento ou por nunca ter habilitado credencial, alinhado à definição de cliente da IN 706, §2.6.2.​
CREDENTIAL_UNAVAILABLE
: Quando o CPF/CNPJ possui credencial autenticadora cadastrada, mas a credencial está temporariamente indisponível para uso (bloqueio por tentativas, expiração, inativação por inatividade, 2FA indisponível, bloqueio cautelar, KYC pendente). Para fins regulatórios, permanece considerado cliente.​
NO_AUTHORITY
: Quando o CPF/CNPJ possui credencial autenticadora e consegue se autenticar, mas não dispõe de poderes ou alçadas suficientes para prosseguir no fluxo de compartilhamento de dados e serviços.​
NO_AUTHORITY_PERSON_MISMATCH
: Quando o CPF não possui relação com a credencial utilizada na etapa de autenticação do Hybrid Flow.​
TECHNICAL_FAILURE
: Quando uma falha técnica impede a verificação do estado do CPF/CNPJ, incluindo, mas não se limitando a, erros HTTP 4xx por validação prévia ao lookup, 5xx, timeout e indisponibilidade de sistemas dependentes. Reservado a falhas ocorridas antes ou durante a verificação da credencial
Adiado para a release 2026C
Obrigatoriedade de additionalInfo para Pagamentos
Alteração na regra de preenchimento do additionalInfo paymentType
Se /data/payment/details/purpose = IMMEDIATE, paymentType = IMMEDIATE
Se /data/payment/details/purpose = SINGLE_SCHEDULED, paymentType = SCHEDULED
Se /data/payment/details/purpose = RECURRENT_SCHEDULED, paymentType = RECURRENT
Se /data/payment/details/purpose = WITHDRAW, paymentType = WITHDRAW
Se /data/payment/details/purpose = CHANGE, paymentType = CHANGE
Obs.: esta é uma regra associada à v5 de Pagamentos
Em andamento
Campos opcionais e obrigatórios / obrigatoriedade de additionalInfo
Refinamento na documentação dos campos opcionais/obrigatórios e additionalInfo:
Todos os produtos
Reorganização das tabelas de campos opcionais e obrigatórios, identificando os campos necessários para o POST, o campos de response e os retornos do GET
Em andamento
Campos opcionais e obrigatórios / obrigatoriedade de additionalInfo
Pagamentos
Todos os tipos de pagamento
status: definição e domínio ajustados para conter somente os valores existentes para esta API
Pagamentos
rejectionReasonCode: Inclusão na regra de preenchimento -
Obrigatório somente quando o status for RJCT ou REJECTED
rejectionReasonDetail: Inclusão na regra de preenchimento -
Obrigatório somente quando o status for RJCT ou REJECTED
paymentList: explicitar regra de obrigatoriedade de envio para paymentType IMMEDIATE, RECURRENT e SCHEDULED, mesmo possuindo apenas um paymentId na lista.
Jornada Sem Redirecionamento
Remoção da versão v1 da API nos endpoints válidos
platform: incluído o domínio do campo -
ANDROID, BROWSER, CROSS_PLATFORM, IOS
rejectionReasonCode: alteração da obrigatoriedade de statusCode
para Todos menos 4xx e 5xx
revocationReasonCode: incluída a regra de preenchimento -
Deve ser preenchido com a mesma string obtida no ".data.cancellation.reason.revocationReason". Caso a informação esteja em formato de lista, enviar apenas o valor do primeiro item da lista.
Dever ser enviado quando o status for REVOKED
tokenId: inclusão do endpoint
/open-banking/enrollments/v2/recurring-consents/{recurringConsentId}/authorise
journeyIsLinked: alteração da regra de preenchimento para
Deve ser preenchido com a string obtida no campo journey.isLinked, após a chamada inicial na API “POST /consents” se o parâmetro isLinked estiver preenchido na requisição no contexto de Jornada Otimizada. Em casos em que a informação não está disponível espera-se o envio do valor FALSE.
journeyLinkId: complemento da regra de preenchimento -
Deve ser enviado se journeyIsLinked for TRUE
Pagamentos Automáticos
authorisationFlow: ajuste na descrição do campo -
Identifica o fluxo de autorização em que um pagamento ou operação foi solicitado. Descreve como o autenticador (por exemplo, um dispositivo FIDO) está anexado ao cliente que realiza a autenticação (ex: platform para autenticadores integrados como Face ID ou cross-platform para chaves de segurança USB).
errorCodes: correção do campo, estava duplicado. Foi dividido em regras para statusCode 422 e statusCode 4xx / 5xx exceto 422, a exemplo de Iniciação de Pagamentos
interval: incluído domínio do campo -
SEMANAL, MENSAL, TRIMESTRAL, SEMESTRAL, ANUAL
isRetryAccepted: incluído domínio do campo -
TRUE, FALSE
originalRecurringPaymentId: inclusão do endpoint /open-banking/automatic-payments/vx/pix​/recurring-payments​/{originalRecurringPaymentId}​/retry
paymentReference: complementada a regra de preehchimento -
Campo de preenchimento obrigatório caso seja um pagamento de Pix automático e deve ser enviado para critérios de coleta de métricas do ecossistema. Caso essa regra não seja respeitada, a instituição detentora da conta deve retornar um erro HTTP 422 com o código DETALHE_PAGAMENTO_INVALIDO.
paymentType: complemento da regra de preenchimento -
WITHDRAW:
PIX Saque e
CHANGE:
PIX Troco
recurringConsentId: ajustada a descrição, incluída a regra de preenchimento e o endpoint  /open-banking/automatic-payments/vx/pix​/recurring-payments​/{originalRecurringPaymentId}​/retry
recurringPaymentDate: complementada a descrição -
Data em que o pagamento será realizado no formato timezone UTC-3 (UTC time format)
recurringPaymentId: ajustadas a descrição e a regra de preenchimento, incluído padrão do campo e o endpoint endpoint /open-banking/automatic-payments/vx/pix​/recurring-payments​/{originalRecurringPaymentId}​/retry
referenceStartDate: ajustada a descrição -
Data prevista para o início do ciclo de cobrança dos pagamentos associados à recorrência. Trata-se de uma string com data conforme especificação RFC-3339, seguindo o horário de Brasília (UTC-3). O pagamento inicial avulso, declarado no objeto firstPayment do consentimento, não está sujeito a essa data
rejectedBy: incluída a regra de preenchimento -
Deve ser preenchido com a mesma string obtida no ".data.rejection.rejectedBy". Obrigatório somente quando o status for RJCT ou REJECTED
rejectedFrom: incluída a regra de preenchimento -
Deve ser preenchido com a mesma string obtida no ".data.rejection.rejectedFrom". Obrigatório somente quando o status for RJCT ou REJECTED
rejectionReasonCode: complementada a regra de preenchimento -
Obrigatório somente quando o status for RJCT ou REJECTED,
alteração da obrigatoriedade de statusCode
para Todos menos 4xx e 5xx
rejectionReasonDetail: Inclusão na regra de preenchimento -
Deve ser preenchido com a mesma string obtida no ".data.rejectionReason.detail". Caso a informação esteja em formato de lista, enviar apenas o valor do primeiro item da lista. Obrigatório somente quando o status for RJCT ou REJECTED,
alteração da obrigatoriedade de statusCode
para Todos menos 4xx e 5xx
revocationReasonCode: complemento à regra de preenchimento -
Obrigatório somente quando o status for REVOKED
revocationReasonDetail: incluída a regra de preenchimento -
Deve ser preenchido com a string obtida no campo ".data.revocation.reason.detail". Caso a informação esteja em formato de lista, enviar apenas o valor do primeiro item da lista. Obrigatório somente quando o status for REVOKED
status: inclusão do endpoint
/open-banking/automatic-payments/vx/pix​/recurring-payments​/{originalRecurringPaymentId}​/retry
tokenId: inclusão do endpoint
/open-banking/automatic-payments/vx/pix/recurring-payments/{originalRecurringPaymentId}/retry
Em andamento
Campos opcionais e obrigatórios / obrigatoriedade de additionalInfo
Dados de Clientes
Reestruturação da página, dando clareza dos campos que devem ser enviados no método POST da Private API, quais campos são retornados no response e quais são adicionais ao método GET.
Remoção da coluna “Métodos” para evitar conflito com a reestruturação da página
clientSSIDd: correção nas roles obrigatórias, o correto é somente CLIENT
processTimespan: correção do exemplo para refletir de forma correta o valor esperado
statusCode: maior esclarecimento na regra de preenchimento -
No contexto operacional do Open Finance, de acordo com a definição de governança, a instituição consumidora (Client) deve aguardar até 15 segundos pela resposta da instituição provedora (Server).
Caso esse período seja atingido ou excedido (≥ 15 segundos) sem resposta, a instituição consumidora pode, por decisão própria e para preservar a experiência do usuário, encerrar a conexão. Nessa situação, o evento deve ser reportado com status code 408, caracterizando timeout na interação, ainda que a interrupção tenha sido iniciada pelo lado consumidor.
Por sua vez, quando a instituição estiver atuando como provedora (Server) e encerrar a conexão por não ter recebido a requisição completa dentro do tempo esperado, também deverá reportar status code 408, em conformidade com a RFC 7231.
Consentimentos
journeyIsLinked - ajustada a regra de preenchimento -
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.isLinked”, retornado após a chamada inicial na API “POST /consent” (Pagamentos Automáticos) ou “POST /enrollments” (Jornada Sem Redirecionamento) em caso de Jornada Otimizada. Em casos em que a informação não está disponível espera-se o envio do valor FALSE.
tokenId: inclusão dos endpoints
/open-banking/consents/v3/consents/{consentId}/extends
e
/open-banking/consents/v3/consents/{consentId}/extensions
Em andamento
Campos opcionais e obrigatórios / obrigatoriedade de additionalInfo
Dados Abertos
Reestruturação da página, dando clareza dos campos que devem ser enviados no método POST da Opendata API e quais campos são retornados no response
Remoção da coluna “Métodos” para evitar conflito com a reestruturação da página
Inclusão da coluna “Regras de Preenchimento”
processTimespan: correção do exemplo para refletir de forma correta o valor esperado
statusCode: inclusão de regra de preenchimento -
No contexto operacional do Open Finance, de acordo com a definição de governança, a instituição consumidora (Client) deve aguardar até 15 segundos pela resposta da instituição provedora (Server).
Caso esse período seja atingido ou excedido (≥ 15 segundos) sem resposta, a instituição consumidora pode, por decisão própria e para preservar a experiência do usuário, encerrar a conexão. Nessa situação, o evento deve ser reportado com status code 408, caracterizando timeout na interação, ainda que a interrupção tenha sido iniciada pelo lado consumidor.
Por sua vez, quando a instituição estiver atuando como provedora (Server) e encerrar a conexão por não ter recebido a requisição completa dentro do tempo esperado, também deverá reportar status code 408, em conformidade com a RFC 7231.
endpoint: inclusão de regra de preenchimento -
Identificação do Endpoint: Deve ser preenchido com o identificador padronizado do endpoint, conforme uma lista (ENUM) predefinida.Não usar o caminho real: É fundamental NÃO utilizar o caminho completo da   requisição original, que inclui dados variáveis (ex: IDs).
Exemplo: Se a requisição foi para /open-banking/credit-cards-accounts/v1/accounts/123456789/transactions, o valor a ser enviado no endpoint deve ser /open-banking/credit-cards-accounts/v1/accounts/{creditCardAccountId}/transactions. O dado real 123456789 não deve ser enviado no campo endpoint
processTimespan: alteração da definição -
Tempo em milissegundos inteiros decorrido desde o recebimento do request até o momento imediatamente anterior ao envio do primeiro byte da resposta.
Remoção do campo tokenId, pois o mesmo não existe dentro do contexto de Dados Abertos
Atualização das versões de API
Atendimento: v2
Previdência: v2
Seguros: v2
Títulos de Capitalização: v2
Remoção do grupo Produtos e Serviços, que foi desmembrado em grupos menores
Inclusão de novos grupos:
Contas
Cartão de Crédito
Direitos Creditórios Descontados
Empréstimos
Financiamentos
Adiantamento a Depositantes
Em andamento
Campos opcionais e obrigatórios / obrigatoriedade de additionalInfo
Segurança
Inclusão de página com os campos obrigatórios e opcionais de reportes de Segurança
status: definição e domínio ajustados para conter somente os valores existentes para esta API
consentId: complemento da regra de preenchimento  -
Deve ser preenchido com a mesma string obtida no campo .data.consentId retornado após a chamada inicial na API "POST /consent”. *Ao reportar o uso de um endpoint /token, o identificador único de consentimento só será reportado nos casos em que "grant_type" é do tipo "authorization_code" ou do tipo "refresh_token"
grantType: complemento da regra de preenchimento -
Deve ser preenchido com a mesma string enviada no campo ".grant_type "​
AUTHORIZATION_CODE:
Utilizado na autorização de acesso a um recurso por meio de login de usuário
REFRESH_TOKEN:
Utilizado para obter um novo token de acesso quando o token anterior expira
CLIENT_CREDENTIALS:
Utilizado na autorização de acesso entre aplicações onde não há a figura do usuário
webhookEnable: correção na regra de preenchimento; não deve ser enviado um valor booleano TRUE ou FALSE, mas sim uma string contendo ou TRUE ou FALSE.
Em andamento
Campos opcionais e obrigatórios / obrigatoriedade de additionalInfo
Estados de Pagamento
status: definição e domínio ajustados para conter somente os valores existentes para esta API
Em andamento
Swagger da PCM
Ajuste no swagger para refletir os ajustes realizados nos campos obrigatórios/opcionais e additionalInfo
Em andamento
Regras de Validação - todos os produtos
Ajustes nas regras de validação de acordo com o refinamento realizado nos campos obrigatórios/opcionais e additionalInfo
Em andamento
Regras de descarte - todos os produtos
Atualização dos motivos de descarte na documentação e mensagens nas evidências dos tickets
Em andamento
Estados de Pagamento
Envio dos tickets de validação - refinamento das regras de validação entre os reportes de Pagamentos e Estados de Pagamento, de acordo com o documentado neste link:
Comportamento e Qualidade Estados de Pagamentos - Regras de validação
Em andamento
Estoque de Consentimentos
Revisão das definições dos campos do reporte, ajustando conceitos e padrões
Em andamento
Estados de Pagamento
Revisão das definições dos campos do reporte, ajustando conceitos e padrões
Em andamento
Release 2026A
Contexto
Detalhes
Status atual
Contexto
Detalhes
Status atual
Portabilidade de Crédito
Novo endpoint /credit-operations/{contractId}/portability-eligibility
Finalizado
Todos os produtos
Tempo de expiração do token - obtenção de token adicionais para que o participante possa ter sempre sessões em aberto antes do token expirar.
Finalizado
Estados de Pagamento
Envio dos tickets de validação - comportamento e qualidade de Estados de Pagamento, onde é feita a verificação entre a parametrização dos pagamentos realizada através da API Private, nos reportes de Pagamentos, e seus respectivos estados enviados através da API Payment Status. As regras de validação podem ser encontradas em:
Comportamento e Qualidade Estados de Pagamentos - Regras de validação
Finalizado
Obrigatoriedade de additionalInfo de Pagamantos Automáticos
Explicitação da obrigatoriedade de envio do campo recurringConsentId em pagamentos automáticos, em substituição ao consentId.
Finalizado
Criação de novo fluxo de obtenção de token
Criação do fluxo fresh (/token-fresh), que sempre gera um token novo, ignorando qualquer token em cache para leitura.
Finalizado
Release 2025D
Data prevista da release:
17/11/2025
Contexto
Detalhes
Status atual
Contexto
Detalhes
Status atual
Jornada Sem Redirecionamento
Novo código de rejeição (rejectionReasonCode): ORIGEM_FIDO_INVALID) no POST /consents/{consentId}/authorise
Finalizado
Jornada Sem Redirecionamento
Novo código de rejeição (rejectionReasonCode): MAXIMO_CHALLENGES_ATINGIDO no POST /enrollments/{enrollmentId}/fido-registration-options
Finalizado
Jornada Sem Redirecionamento
Novo código de rejeição (rejectionReasonCode): REJEITADO_TITULARIDADE_DIVERGENTE no GET /enrollments/enrollmentId
Finalizado
Jornada Sem Redirecionamento
Novo endpoint para autorização de consentimentos recorrentes de Pix Automático
Finalizado
Jornada Sem Redirecionamento
Ajuste do endpoint que obtém os parâmetros de autenticação para incluir consentimentos de longa duração (recurringConsentId) no POST /enrollments/{enrollmentId}/fido-sign-options
Finalizado
Jornada Sem Redirecionamento
Ajuste da descrição do endpoint POST /enrollments/{enrollmentId}/risk-signals
Sem impacto para a PCM, retirado da release
Jornada Otimizada
Jornada Otimizada - Inclusão de campos para monitoramento de consentimentos em Jornada Otimizada
Finalizado
Jornada Sem Redirecionamento
Novo código de erro (errorCode): PERMISSAO_INVALIDA_VINCULO_CONSENTIMENTO em /enrollments/{enrollmentId}/fido-sign-options
Finalizado
Pagamentos Automáticos
inclusão de localInstrument AUTO em GET /pix/payments/{recurringPaymentId} e PATCH /pix/payments/{recurringPaymentId}
Finalizado
Pagamentos Automáticos
Alteração da descrição do endpoint PATCH /recurring-consents/{recurringConsentId}
Finalizado
Pagamentos Automáticos
Alteração na regra do campo localInstrument para o tipo AUTO em POST /pix/recurring-payments, GET /pix/recurring-payments/{recurringPaymentId} e PATCH /pix/recurringpayments/{recurringPaymentId}
Finalizado
Pagamentos Automáticos
Remoção do código de erro (errorCodes) DETALHE_TENTATIVA_INVALIDA em  POST /pix/recurring-payments
Finalizado
Pagamentos Automáticos
Remoção da mensagem de cancelamento do pagamento em POST /pix/recurring-payments
Finalizado
Pagamentos Automáticos
Remoção dos códigos de erro (errorCodes): DETALHE_TENTATIVA_INVALIDO e LIMITE_TENTATIVAS_EXCEDIDO em POST /pix/recurring-payments
Finalizado
Pagamentos Automáticos
Novo código de rejeição (rejectionReasonCode):FLUXO_NAO_SUPORTADO_PRODUTO em POST /recurring-consents, GET /recurring-consents/{recurringConsentId} e PATCH /recurring-consents/{recurringConsentId}
Finalizado
Pagamentos Automáticos
Alteração das regras de preenchimento para o campo paymentReference em POST /pix/recurring-payments, GET /pix/recurring-payments/{recurringPaymentId}, GET /pix/recurring-payments e PATCH /pix/recurringpayments/{recurringPaymentId}
Sem impacto para a PCM, retirado da release
Pagamentos Automáticos
Altração do código de erro (errorCodes): LIMITE_TENTATIVAS_EXCEDIDO)
Sem impacto para a PCM, retirado da release
Portabilidade de Crédito
Ingestão de consentId para Portabilidade de Crédito
Finalizado
Segurança
Tratamento do tempo de expiração do token
Finalizado
Dados Cadastrais e Transacionais / Pagamentos
IQD PJ
Retirado da release
Dados Cadastrais e Transacionais / Pagamentos / Hybridflow / Segurança / Dados Abertos
Introdução do additionalInfo tokenId para vinculação e rastreabilidade das jornadas de tokens
Finalizado
Iniciação de Pagamentos / Pagamentos Automáticos
Desambiguação de jornadas de pagamentos via campo autorisationFlowIntent
Finalizado

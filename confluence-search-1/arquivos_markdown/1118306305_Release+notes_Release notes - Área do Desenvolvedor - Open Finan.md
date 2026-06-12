---
                            title: "Release notes - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1118306305_Release+notes"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1118306305/Release+notes"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Release notes - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.00
Objetivo desta página
Relacionar a lista de iniciativas implementadas em cada uma das Releases da PCM
2026B
Data da release:
11/06/2026
Data do Informa:
Número do Informa:
Contexto
Tipo de alteração
O que foi alterado?
Detalhes
Antes
Depois
Contexto
Tipo de alteração
O que foi alterado?
Detalhes
Antes
Depois
Novos endpoints aceitos pela PCM
Inclusão
Inclusão de novos endpoints da API de Pagamentos
Endpoints incluídos:
/open-banking/payments/v5/consents
/open-banking/payments/v5/consents/{consentId}
/open-banking/payments/v5/consents/{consentId}/pix/payments
/open-banking/payments/v5/pix/payments
/open-banking/payments/v5/pix/payments/{paymentId}
Somente endpoints da v4 da API de Pagamentos
Endpoints das v4 e v5 da API de Pagamentos
Dados Abertos - Campos Obrigatórios e Opcionais
Alteração
Reestruturação da página
Reestruturação da página, dando clareza dos campos que devem ser enviados no método POST da Opendata API e quais campos são retornados no response
Remoção da coluna “Métodos” para evitar conflito com a reestruturação da página
Inclusão da coluna “Regras de Preenchimento”
Tabela com campos misturados entre campos de POST e RESPONSE da PCM, falta da regra de preenchimento
Tabelas separadas para campos que devem ser enviados via POST, com regra de preenchimento e campos retornados em RESPONSE, dando clareza do contexto de cada campo
Alteração
processTimespan
Alteração do exemplo para refletir de forma correta o valor esperado
Alteração da definição
120
Tempo em milissegundos inteiros decorrido desde o registro do timestamp até a chegada do primeiro byte da resposta do server.
120.000000
Tempo em milissegundos inteiros decorrido desde o recebimento do request até o momento imediatamente anterior ao envio do primeiro byte da resposta.
Inclusão
statusCode
Inclusão de regra de preenchimento
Sem regra de preenchimento
No contexto operacional do Open Finance, de acordo com a definição de governança, a instituição consumidora (Client) deve aguardar até 15 segundos pela resposta da instituição provedora (Server).
Caso esse período seja atingido ou excedido (≥ 15 segundos) sem resposta, a instituição consumidora pode, por decisão própria e para preservar a experiência do usuário, encerrar a conexão. Nessa situação, o evento deve ser reportado com status code 408, caracterizando timeout na interação, ainda que a interrupção tenha sido iniciada pelo lado consumidor.
Por sua vez, quando a instituição estiver atuando como provedora (Server) e encerrar a conexão por não ter recebido a requisição completa dentro do tempo esperado, também deverá reportar status code 408, em conformidade com a RFC 7231.
Inclusão
endpoint
Inclusão da regra de preenchimento
Sem regra de preenchimento
Identificação do Endpoint: Deve ser preenchido com o identificador padronizado do endpoint, conforme uma lista (ENUM) predefinida.Não usar o caminho real: É fundamental NÃO utilizar o caminho completo da   requisição original, que inclui dados variáveis (ex: IDs).
Exemplo: Se a requisição foi para /open-banking/credit-cards-accounts/v1/accounts/123456789/transactions, o valor a ser enviado no endpoint deve ser /open-banking/credit-cards-accounts/v1/accounts/{creditCardAccountId}/transactions. O dado real 123456789 não deve ser enviado no campo endpoint
Dados Abertos - Obrigatoriedade de additionalInfo
Exclusão
tokenId
Remoção do campo tokenId, pois o mesmo não existe dentro do contexto de Dados Abertos
tokenId declarado como um campo obrigatório para Dados Abertos
tokenId removido da tabela
Alteração
Versões das APIs
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
Atendimento: v1
Previdência: v1
Seguros: v1
Títulos de Capitalização: v1
Produtos e Serviços v1
Atendimento: v2
Previdência: v2
Seguros: v2
Títulos de Capitalização: v2
Contas: v1
Cartão de Crédito: v1
Direitos Creditórios Descontados: v1
Empréstimos: v1
Financiamentos: v1
Adiantamento a Depositantes: v1
Dados Cadastrais e Transacionais - Campos Obrigatórios e Opcionais
Alteração
Reestruturação da página
Reestruturação da página, dando clareza dos campos que devem ser enviados no método POST da Private API, quais campos são retornados no response e quais são adicionais ao método GET
Remoção da coluna “Métodos” para evitar conflito com a reestruturação da página
Tabela com campos misturados entre campos de POST, GET e RESPONSE da PCM
Tabelas separadas para campos que devem ser enviados via POST, campos retornados em RESPONSE e em GET, dando clareza do contexto de cada campo
Alteração
clientSSId
Correção nas roles obrigatórias, o correto é somente CLIENT
CLIENT / SERVER
CLIENT
Alteração
processTimespan
Alteração do exemplo para refletir de forma correta o valor esperado
120
120.000000
Alteração
statusCode
Maior esclarecimento na regra de preenchimento
Para informações adicionais, por favor consulte
Reporte - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor
No contexto operacional do Open Finance, de acordo com a definição de governança, a instituição consumidora (Client) deve aguardar até 15 segundos pela resposta da instituição provedora (Server).
Caso esse período seja atingido ou excedido (≥ 15 segundos) sem resposta, a instituição consumidora pode, por decisão própria e para preservar a experiência do usuário, encerrar a conexão. Nessa situação, o evento deve ser reportado com status code 408, caracterizando timeout na interação, ainda que a interrupção tenha sido iniciada pelo lado consumidor.
Por sua vez, quando a instituição estiver atuando como provedora (Server) e encerrar a conexão por não ter recebido a requisição completa dentro do tempo esperado, também deverá reportar status code 408, em conformidade com a RFC 7231.
Dados Cadastrais e Transacionais - Obrigatoriedade de additionalInfo
Alteração
Consentimento - journeyIsLinked
Alteração na regra de preenchimento
Deve ser preenchido com a string obtida no campo journey.isLinked, após a chamada inicial na API “POST /consents” se o parâmetro isLinked estiver preenchido na requisição no contexto de Jornada Otimizada
Não deve ser reportado o campo journeyIsLinked ou journeyLinkId quando:
O consentimento for criado fora do contexto de Jornada Otimizada, ou seja, quando não houver indicação de journey.isLinked=true no payload da criação do consentimento
O consentimento for do tipo convencional (ex.: consents isolados, enrollments isolados, recurring-consents isolados), sem vínculo com outro consentimento
Nestes casos, a transmissora/detentora deve omitir os campos journeyIsLinked e journeyLinkId no reporte à PCM
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.isLinked”, retornado após a chamada inicial na API “POST /consent” (Pagamentos Automáticos) ou “POST /enrollments” (Jornada Sem Redirecionamento) em caso de Jornada Otimizada. Em casos em que a informação não está disponível espera-se o envio do valor FALSE.
Alteração
Recursos - statusSummary
Alteração na regra de preenchimento
Sumarização da quantidade por ENUM observado em
data.status
Sumarização da quantidade por ENUM observado em data.status
Obrigatório para PF e PJ
Pagamentos - Estados de Pagamento
Alteração
paymentList
Correção da descrição do campo paymentList, dando maior clareza quanto ao seu escopo
Lista de dados de pagamentos com agendamento recorrentes.
Lista de dados de pagamentos com agendamento imediatos, agendados ou recorrentes.
Alteração
eventDateTime
Complemento da descrição do campo eventDateTime, incluindo o escopo de agendamento aos demais estados
Data e hora associada a mudança de estados finais reportados abaixo, como liquidação, rejeição ou cancelamento. Formato AAAA-MM-DD hh:mm:ss reportado em UTC 0
Data e hora associada à mudança de estados reportados abaixo, como agendamento, liquidação, rejeição ou cancelamento. Formato AAAA-MM-DD hh:mm:ss reportado em UTC 0
Alteração
Regra de Validação – paymentId
Complemento da regra de validação da quantidade de paymentIds distintos para um mesmo consentId, passando a validar também a data do último pagamento
Para
paymentType
RECURRENT, validar que não há mais de 60
paymentIds
por
consentId.
Se houverem mais de 60, ingerir e criticar
Para
paymentType
RECURRENT, validar que não há mais de 60
paymentIds
por
consentId
s, independentemente do modelo de recorrência definido no consentimento. A data do último pagamento agendado não pode ultrapassar o correspondente dia e mês do segundo ano subsequente à data de criação do consentimento (Ex.: consentimento criado em 15/03/2026 admite agendamentos até 15/03/2028)
.
Se houverem mais de 60 ou a data do último pagamento não estiver de acordo com a regra, ingerir e criticar.
Pagamentos - Campos Obrigatórios e Opcionais
Alteração
Reestruturação da página
Reestruturação da página, dando clareza dos campos que devem ser enviados no método POST da Private API, quais campos são retornados no response e quais são adicionais ao método GET
Remoção da coluna “Métodos” para evitar conflito com a reestruturação da página
Tabela com campos misturados entre campos de POST, GET e REPONSE da PCM
Tabelas separadas para campos que devem ser enviados via POST, campos retornados em RESPONSE e em GET, dando clareza do contexto de cada campo
Alteração
clientSSId
Correção nas roles obrigatórias, o correto é somente CLIENT
CLIENT / SERVER
CLIENT
Alteração
processTimespan
Alteração do exemplo para refletir de forma correta o valor esperado
120
120.000000
Alteração
statusCode
Maior esclarecimento na regra de preenchimento
Para informações adicionais, por favor consulte
Reporte - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor
No contexto operacional do Open Finance, de acordo com a definição de governança, a instituição consumidora (Client) deve aguardar até 15 segundos pela resposta da instituição provedora (Server).
Caso esse período seja atingido ou excedido (≥ 15 segundos) sem resposta, a instituição consumidora pode, por decisão própria e para preservar a experiência do usuário, encerrar a conexão. Nessa situação, o evento deve ser reportado com status code 408, caracterizando timeout na interação, ainda que a interrupção tenha sido iniciada pelo lado consumidor.
Por sua vez, quando a instituição estiver atuando como provedora (Server) e encerrar a conexão por não ter recebido a requisição completa dentro do tempo esperado, também deverá reportar status code 408, em conformidade com a RFC 7231.
Pagamentos - Obrigatoriedade de additionalInfo
Inclusão
Iniciação de Pagamentos - paymentList
Inclusão de regra de preenchimento para dar maior clareza da regra do campo
Sem regra de preenchimento
Deve ser enviado obrigatoriamente para os tipos de pagamento (paymentType) IMMEDIATE, SCHEDULED e RECURRENT, mesmo que a lista contenha apenas um item. Para o mesmo consentId não podem ser reportados nesta lista mais do que 60 paymentId.
Inclusão
Iniciação de Pagamentos - paymentType
Inclusão de regra de preenchimento específica para a v5 de pagamentos
Sem regra de preenchimento para v5
Se /data/payment/details/purpose = IMMEDIATE, paymentType = IMMEDIATE
Se /data/payment/details/purpose = SINGLE_SCHEDULED, paymentType = SCHEDULED
Se /data/payment/details/purpose = RECURRENT_SCHEDULED, paymentType = RECURRENT
Se /data/payment/details/purpose = WITHDRAW, paymentType = WITHDRAW
Se /data/payment/details/purpose = CHANGE, paymentType = CHANGE
Inclusão
Iniciação de Pagamentos - localInstrument
Inclusão de domínio
DICT, INIC, MANU, QRDN, QRES, AUTO
DICT, INIC, MANU, QRDN, QRES, AUTO, APDN, APES
Inclusão
Iniciação de Pagamentos - rejectionReasonCode
Inclusão de domínio
Lista de rejectionReasonCode antes da v5 de Pagamentos
Lista de rejectionReasonCode com os novos motivos de rejeição:
AUTENTICACAO_DIVERGENTE​
CHAVE_PIX_DIVERGENTE_AGENDAMENTO_LIQUIDACAO
CONTA_NAO_PERMITE_PAGAMENTO
QRCODE_INVALIDO
PERMISSAO_INSUFICIENTE
Inclusão
Iniciação de Pagamentos - errorCodes
Inclusão de domínio
Lista de errorCodes antes da v5 de Pagamentos
Lista de errorCodes com o novo erro:
PROPOSITO_INVALIDO
Exclusão
Jornada Sem Redirecionamento
Remoção da versão v1 da API nos endpoints válidos
Endpoints da v1 da API sendo apresentados como válidos
Somente endpoints da v2 são válidos
Inclusão
Jornada Sem Redirecionamento - authenticatorAttachment
Incluído o domínio do campo
Sem domínio declarado
platform, cross-platform
Inclusão
Jornada Sem Redirecionamento - platform
Incluído o domínio do campo
Sem domínio declarado
ANDROID, BROWSER, CROSS_PLATFORM, IOS
Inclusão
Jornada Sem Redirecionamento - revocationReasonCode
Incluída a regra de preenchimento
Sem regra de preenchimento
Deve ser preenchido com a mesma string obtida no ".data.cancellation.reason.revocationReason". Caso a informação esteja em formato de lista, enviar apenas o valor do primeiro item da lista. Dever ser enviado quando o status for REVOKED
Inclusão
Jornada Sem Redirecionamento - tokenId
Incluído o endpoint /open-banking/enrollments/v2/recurring-consents/{recurringConsentId}/authorise
/open-banking/enrollments/v
x
/enrollments
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-registration-options
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-registration
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-sign-options
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/risk-signals
/open-banking/enrollments/v
x
/consents/{consentId}/authorise
/open-banking/enrollments/v
x
/recurring-consents/{recurringConsentId}/authorise
/open-banking/automatic-payments/v
x
/pix/recurring-payments/{originalRecurringPaymentId}/retry
/open-banking/enrollments/v
x
/enrollments
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-registration-options
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-registration
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-sign-options
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/risk-signals
/open-banking/enrollments/v
x
/consents/{consentId}/authorise
/open-banking/enrollments/v
x
/recurring-consents/{recurringConsentId}/authorise
/open-banking/automatic-payments/v
x
/pix/recurring-payments/{originalRecurringPaymentId}/retry
/open-banking/enrollments/v2/recurring-consents/{recurringConsentId}/authorise
Alteração
Jornada Sem Redirecionamento - journeyIsLinked
Alteração da regra de preenchimento
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.isLinked”, retornado após a chamada inicial na API “POST /enrollments” em caso de Jornada Otimizada
Deve ser preenchido com a string obtida no campo journey.isLinked, após a chamada inicial na API “POST /consents” se o parâmetro isLinked estiver preenchido na requisição no contexto de Jornada Otimizada.  Em casos em que a informação não está disponível espera-se o envio do valor FALSE.
Alteração
Jornada Sem Redirecionamento - journeyLinkId
Complemento da regra de preenchimento
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.linkId”, retornado após a chamada inicial na API “POST /enrollments” em caso de Jornada Otimizada.
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.linkId”, retornado após a chamada inicial na API “POST /enrollments” em caso de Jornada Otimizada.
Deve ser enviado se journeyIsLinked for TRUE
Alteração
Pagamentos Automáticos - authorisationFlow
Ajuste na descrição do campo
Identifica o fluxo de autorização em que um pagamento ou operação foi solicitado
Identifica o fluxo de autorização em que um pagamento ou operação foi solicitado. Descreve como o autenticador (por exemplo, um dispositivo FIDO) está anexado ao cliente que realiza a autenticação (ex: platform para autenticadores integrados como Face ID ou cross-platform para chaves de segurança USB).
Alteração
Pagamentos Automáticos - errorCodes
Correção do campo, estava duplicado. Foi dividido em regras para statusCode 422 e statusCode 4xx / 5xx exceto 422, a exemplo de Iniciação de Pagamentos
Linhas duplicadas para errorCodes
Linhas separadas em 422 e demais erros, a exemplo da Iniciação de Pagamentos
Inclusão
Pagamentos Automáticos - interval
Incluído domínio do campo
Sem domínio delcarado
SEMANAL, MENSAL, TRIMESTRAL, SEMESTRAL, ANUAL
Inclusão
Pagamentos Automáticos - isRetryAccepted
Incluído domínio do campo
Sem domínio delcarado
TRUE, FALSE
Inclusão
Pagamentos Automáticos - originalRecurringPaymentId
Inclusão do endpoint /open-banking/automatic-payments/vx/pix​/recurring-payments​/{originalRecurringPaymentId}​/retry
/open-banking/automatic-payments/v
x
/pix/recurring-payments
/open-banking/automatic-payments/v
x
/pix/recurring-payments/{recurringPaymentId}
/open-banking/automatic-payments/v
x
/pix/recurring-payments
/open-banking/automatic-payments/v
x
/pix/recurring-payments/{recurringPaymentId}
/open-banking/automatic-payments/vx/pix​/recurring-payments​/{originalRecurringPaymentId}​/retry
Alteração
Pagamentos Automáticos - paymentReference
Complementada a regra de preehchimento
Preencher com o valor do campo ".data.paymentReference"
Deve ser preenchido quando paymentType for AUTOMATIC
Preencher com o valor do campo "paymentReference"
Campo de preenchimento obrigatório caso seja um pagamento de Pix automático e deve ser enviado para critérios de coleta de métricas do ecossistema. Caso essa regra não seja respeitada, a instituição detentora da conta deve retornar um erro HTTP 422 com o código DETALHE_PAGAMENTO_INVALIDO.
Deve ser preenchido quando paymentType for AUTOMATIC
Alteração
Pagamentos Automáticos - paymentType
Complementada a regra de preehchimento
Identifica o modo de pagamento acionado no consentimento e deve ser preenchido de acordo com o campo ".data.recurringConfiguration/oneOf"
IMMEDIATE
: Pix sem configuração de agendamento
SCHEDULED
: Pix com configuração de agendamento
RECURRENT
: Pix com agendamento e recorrência
SWEEPING
: Chamadas de pagamentos inteligentes
AUTOMATIC
: Pagamentos automáticos
Identifica o modo de pagamento acionado no consentimento e deve ser preenchido de acordo com o campo ".data.recurringConfiguration/oneOf"
IMMEDIATE
: Pix sem configuração de agendamento
SCHEDULED
: Pix com configuração de agendamento
RECURRENT
: Pix com agendamento e recorrência
SWEEPING
: Chamadas de pagamentos inteligentes
AUTOMATIC
: Pagamentos automáticos
WITHDRAW:
PIX Saque
CHANGE:
PIX Troco

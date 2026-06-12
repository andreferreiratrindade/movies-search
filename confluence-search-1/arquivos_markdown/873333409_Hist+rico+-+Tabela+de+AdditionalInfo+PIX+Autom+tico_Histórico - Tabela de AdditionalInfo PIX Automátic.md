---
                            title: "Histórico - Tabela de AdditionalInfo PIX Automático - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "873333409_Hist+rico+-+Tabela+de+AdditionalInfo+PIX+Autom+tico"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/873333409/Hist+rico+-+Tabela+de+AdditionalInfo+PIX+Autom+tico"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Histórico - Tabela de AdditionalInfo PIX Automático - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Esta é a documentação legada, e deve ser consultada apenas para fins de histórico. A página atualizada pode ser encontrada aqui:
Regras de Obrigatoriedade (additionalInfo) - SV
Abaixo a tabela com os campos especiais additionalinfo.
Nome
Jornada
Regra de preenchimento
Role
Http code
Método
Endpoints
amountType
Consentimento
Valida se o serviço contratado possui maior conversão em relação ao tipo do valor definido, sendo ele fixo ou variável​
ENUM com duas possibilidades: ​
Se não enviando nem ".data.recurringConfiguration.automatic.fixedAmount" e nem ".data.recurringConfiguration.automatic.maximumVariableAmount", “VARIAVEL”; ou
​* Se enviado fixedAmount, “FIXO”; ou
Se enviado maximumVariableAmount, “VARIAVEL”
Deve ser preenchido quando paymentType for AUTOMATIC
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
authorisationFlow​
Pagamento
Identifica o fluxo de autorização em que o pagamento foi solicitado​
Deve ser preenchido com a mesma string obtida no ".data.authorisationFlow". Caso a informação esteja em formato de lista, enviar apenas o valor do primeiro item da lista
CLIENT
Todos
POST/PATCH/​GET
/open-banking/automatic-payments/v2/pix/recurring-payments
/open-banking/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}
cancellationReason​
Pagamento
Identifica o estado que o pagamento estava quando foi  cancelado​
Preencher com o valor do campo ".cancellation.reason"
Deve ser enviado quando em um GET ou POST /payment e o campo status é "CANC" ou em um PATCH /payment (que é a API de cancelamento).
CLIENT
2xx
POST/PATCH/​GET
/open-banking/automatic-payments/v2/pix/recurring-payments
/open-banking/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}
cancelledFrom​
Pagamento
Informa o meio pelo qual foi realizado o cancelamento​
Preencher com o valor do campo ".cancellation.cancelledFrom"
Status do pagamento deve ser "CANC"
Valores possíveis: INICIADORA, DETENTORA
CLIENT
2xx
POST/PATCH/​GET
/open-banking/automatic-payments/v2/pix/recurring-payments
/open-banking/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}
consentId​
Consentimento Pagamento
Deve ser preenchido com a mesma string obtida no campo ".data.recurringConsentId" ou ".data.recurringconsentId" retornado após a chamada inicial na API "POST /consent". *Ao reportar o uso de um endpoint /token, o identificador único de consentimento só será reportado nos casos em que "grant_type" é do tipo "authorization_code" ou do tipo "refresh_token", uma vez que esta informação de consentId é inexistente quando "grant_type" é do tipo "client_credentials".
CLIENT
Todos exceto 4xx e 5xx no método POST
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
/open-banking/automatic-payments/v2/pix/recurring-payments
/open-banking/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}
consentId​
Consentimento
Deve ser preenchido com a mesma string obtida no campo ".data.recurringConsentId" ou ".data.recurringconsentId" retornado após a chamada inicial na API "POST /consent". *Ao reportar o uso de um endpoint /token, o identificador único de consentimento só será reportado nos casos em que "grant_type" é do tipo "authorization_code" ou do tipo "refresh_token", uma vez que esta informação de consentId é inexistente quando "grant_type" é do tipo "client_credentials".
CLIENT
Todos exceto 4xx e 5xx no método POST
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents
dropReason
Consentimento
Identifica a razão pela qual o usuário não pode prosseguir na jornada.​
Regras:
O campo dropReason deve ser adicionado nas informações do campo additionalInfo que deverá ser enviado no reporte do provedor do serviço consumido (papel SERVER)
O reporte deverá ser feito por todos os transmissores de dados e detentoras de conta. Para os casos em que ocorram falhas técnicas que impossibilitem a verificação do CPF/CNPJ (incluindo, mas não se limitando, a erros HTTP 4xx, 500 ou timeout na resposta), o reporte deve ser realizado com o valor NO_CREDENTIAL, Em jornadas de múltipla alçada de pessoas jurídicas, quando a autenticação é bem-sucedida mas os poderes constituídos são insuficientes para finalização do Hybrid Flow, deve-se usar NO_AUTHORITY.
Diretrizes:
NONE:
quando o CPF (loggedUser) / CNPJ (businessEntity) possui credencial autenticadora e poderes suficientes para prosseguir o fluxo monitorado - exemplo: PF, cliente, que possui credencial ativa, mas não se autenticou; cliente que se autenticou utilizando a credencial correta.
NO_CREDENTIAL:
quando o CPF (loggedUser) / CNPJ (businessEntity) não for cliente ou não possuir credencial válida/ativa para prosseguir no fluxo monitorado.
NO_AUTHORITY:
quando o CPF (loggedUser) / CNPJ (businessEntity) consegue se autenticar, mas não dispõe de poderes ou alçadas para prosseguir no fluxo de compartilhamento de dados e serviços.
NO_AUTHORITY_PERSON_MISMATCH:
quando o CPF (loggedUser) não possui relação com a credencial utilizada na etapa de autenticação do Hybrid Flow - exemplo: consentimento criado para um CPF e autenticado por outro; criado para um CNPJ e autenticado por CPF sem relação com o CNPJ.
SERVER
Todos
POST
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
hasMinimumAmount​
Consentimento
Valida se possui o valor mínimo definido pelo usuário recebedor​
Se preenchido o campo “.data/recurringConfiguration.automatic.minimumVariableAmount”, enviar "TRUE"; ou
Se não preenchido o campo “.data.recurringConfiguration.automatic.minimumVariableAmount” enviar "FALSE"
Deve ser preenchido quando paymentType for AUTOMATIC
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
interval​
Consentimento
Periodicidade que a recorrência foi definida (semanal, trimestral, anual...)​
Preencher com o valor do campo ".data.recurringConfiguration.interval"
Deve ser preenchido quando paymentType for AUTOMATIC
Valores possíveis: SEMANAL, MENSAL, ANUAL, SEMESTRAL, TRIMESTRAL
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
isFirstPayment​
Consentimento
Valida se o serviço possui um pagamento associado na adesão​
Se preenchido o campo ".data.recurringConfiguration.automatic.firstPayment", enviar "TRUE"; ou
Se não preenchido o campo ".data.recurringConfiguration.automatic.firstPayment", enviar "FALSE"
Deve ser preenchido quando paymentType for AUTOMATIC
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
isRetryAccepted​
Consentimento
Identifica se foi autorizado a tentativas de pagamento em dias subsequentes na situação de falha do pagamento da recorrência​
Preencher com o valor do campo ".data.recurringConfiguration.automatic.isRetryAccepted"
Deve ser preenchido quando paymentType for AUTOMATIC
CLIENT
Todos (POST/PATCH)
Todos menos 4xx e 5xx (GET)
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
localInstrument​
Pagamento
Especifica a forma de iniciação do pagamento​
Deve ser preenchido com a mesma string informada no payload ".data.localInstrument"
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST/PATCH/GET
/open-banking/automatic-payments/v2/pix/recurring-payments
/open-banking/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}
originalRecurringPaymentId​
Pagamento
Identifica o primeiro pagamento da recorrência em relação as retentativas​
Preencher com o valor do campo ".data.originalRecurringPaymentId"
Deve ser preenchido quando paymentType for AUTOMATIC
CLIENT
Todos (POST/PATCH)
Todos menos 4xx e 5xx (GET)
POST/PATCH/GET
/open-banking/automatic-payments/v2/pix/recurring-payments
/open-banking/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}
paymentReference​
Pagamento
Identifica a referência do pagamento no tempo (semanal, mensal, trimestral...)​
Preencher com o valor do campo ".data.paymentReference"
Deve ser preenchido quando paymentType for AUTOMATIC
CLIENT
Todos (POST/PATCH)
Todos menos 4xx e 5xx (GET)
POST/PATCH/GET
/open-banking/automatic-payments/v2/pix/recurring-payments
/open-banking/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}
paymentType
Consentimento Pagamento
Identifica o modo de pagamento acionado no consentimento e deve ser preenchido de acordo com o campo ".data.recurringConfiguration/oneOf"
Valores possíveis: SWEEPING, AUTOMATIC
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
/open-banking/automatic-payments/v2/pix/recurring-payments
/open-banking/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}
personType​
Consentimento
Identifica a natureza do solicitante (PESSOA_NATURAL/PESSOA_JURIDICA)​
Deve ser preenchida baseado no tipo de pessoa responsável pelo consentimento. Deverá ser observado se '/data/businessEntity' estiver preenchido no payload, se estiver então preencher com "PESSOA_JURIDICA", se não estiver então preencher com "PESSOA_NATURAL"
CLIENT
2xx
POST/PATCH/​GET
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
recurringPaymentId​
Pagamento
Contagem de acionamentos feitos no pagamento​
Para Pagamentos v4: Preencher com o valor do campo ".data.paymentId"​
Para Pagamentos Automáticos v2: Preencher com o valor do campo ".data.recurringPaymentId"
CLIENT
Todos menos 4xx e 5xx
POST/PATCH/GET
/open-banking/automatic-payments/v2/pix/recurring-payments
/open-banking/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}
rejectionReasonCode​
Consentimento Pagamento
Código de rejeição referente ao consentimento​
Preencher com o valor do campo ".data.rejection.reason.code"
Deve ser preenchido se o campo ".data.status" for igual a REJECTED para APIs de consentimento e RJCT para APIs de pagamento
CLIENT
Todos (POST/GET)
Todos menos 4xx e 5xx (PATCH)
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
/open-banking/automatic-payments/v2/pix/recurring-payments
/open-banking/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}
rejectionReasonDetail​
Consentimento Pagamento
Detalhe sobre a rejeição referente ao consentimento​
Preencher com o valor do campo ".data.rejection.reason.detail"
Deve ser preenchido se o campo ".data.status" for igual a REJECTED para APIs de consentimento e RJCT para APIs de pagamento
CLIENT
Todos (POST/GET)
Todos menos 4xx e 5xx (PATCH)
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
/open-banking/automatic-payments/v2/pix/recurring-payments
/open-banking/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}
revocationReasonCode​
Consentimento
Código de revogação referente ao consentimento​
Preencher com o valor do campo ".data.revocation.reason.code"
Deve ser preenchido se o campo ".data.status" for igual a "REVOKED"
CLIENT
Todos (POST/GET)
Todos menos 4xx e 5xx (PATCH)
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
revocationReasonDetail​
Consentimento
Detalhe sobre a revogação referente ao consentimento​
Preencher com o valor do campo ".data.revocation.reason.detail"
Deve ser preenchido se o campo ".data.status" for igual a "REVOKED"
CLIENT
Todos (POST/GET)
Todos menos 4xx e 5xx (PATCH)
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
status​
Consentimento Pagamento
Status que se encontra o recurso  do pagamento
Deve ser preenchido com a mesma string obtida no ".data.status"
Valores possíveis para consentimento: AWAITING_AUTHORISATION, PARTIALLY_ACCEPTED, AUTHORISED, REJECTED, REVOKED, CONSUMED
Valores possíveis para pagamento: RCVD, CANC, ACCP, ACPD, RJCT, ACSC, PDNG, SCHD
CLIENT
2xx
POST/PATCH/GET
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
/open-banking/automatic-payments/v2/pix/recurring-payments
/open-banking/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}

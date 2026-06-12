---
                            title: "Histórico - Tabela de AdditionalInfo para Jornada Sem Redirecionamento (JSR) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "657981441_Hist+rico+-+Tabela+de+AdditionalInfo+para+Jornada+Sem+Redirecionamento+JSR"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/657981441/Hist+rico+-+Tabela+de+AdditionalInfo+para+Jornada+Sem+Redirecionamento+JSR"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Histórico - Tabela de AdditionalInfo para Jornada Sem Redirecionamento (JSR) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Esta é a documentação legada, e deve ser consultada apenas para fins de histórico. A página atualizada pode ser encontrada aqui:
https://openfinancebrasil.atlassian.net/wiki/pages/createpage.action?spaceKey=of&title=Tabela%20de%20Obrigatoriedade%20de%20additionalInfo&linkCreation=true&fromPageId=657981441
Abaixo a tabela com os campos especiais additionalinfo.
Nome
Descrição
Role
Http Code
Método
Enrollments
Nome
Descrição
Role
Http Code
Método
Enrollments
consentId
Deve ser preenchido com a mesma string obtida no campo `.data.consentId` retornado após a chamada inicial na API "POST /consent". *Ao reportar o uso de um endpoint /token, o identificador único de consentimento só será reportado nos casos em que "grant_type" é do tipo "authorization_code" ou do tipo "refresh_token", uma vez que esta informação de consentId é inexistente quando "grant_type" é do tipo "client_credentials".
CLIENT
Todos
Todos
/open-banking/enrollments/v1/consents/{consentId}/authorise
/open-banking/enrollments/v2/consents/{consentId}/authorise
personType
Deve ser preenchida baseado no tipo de pessoa responsável pelo consentimento. Deverá ser obserdado se `.data.businessEntity` estiver preenchido no payload, se estiver então preencher com "PJ", se não estiver então preencher com "PF"
CLIENT
2xx
GET e POST
/open-banking/enrollments/v1/enrollments
/open-banking/enrollments/v1/enrollments/{enrollmentId}
/open-banking/enrollments/v2/enrollments
/open-banking/enrollments/v2/enrollments/{enrollmentId}
localInstrument
Deve ser preenchido com a mesma string informada no payload ".data.localInstrument"
CLIENT
N/A
N/A
N/A
status
Deve ser preenchido com a mesma string obtida no ".data.status"
CLIENT
2xx
GET e POST
/open-banking/enrollments/v1/enrollments
/open-banking/enrollments/v1/enrollments/{enrollmentId}
/open-banking/enrollments/v2/enrollments
/open-banking/enrollments/v2/enrollments/{enrollmentId}
clientIp
Deve ser preenchido com o Endereço IPv4 ou IPv6 do client que fez a requisição
CLIENT
Todos
Todos
/open-banking/enrollments/v1/consents/{consentId}/authorise
/open-banking/enrollments/v1/enrollments
/open-banking/enrollments/v1/enrollments/{enrollmentId}
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-registration
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-registration-options
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-sign-options
/open-banking/enrollments/v1/enrollments/{enrollmentId}/risk-signals
/open-banking/enrollments/v2/consents/{consentId}/authorise
/open-banking/enrollments/v2/enrollments
/open-banking/enrollments/v2/enrollments/{enrollmentId}
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-registration
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-registration-options
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-sign-options
/open-banking/enrollments/v2/enrollments/{enrollmentId}/risk-signals
errorCodes
Caso o HTTP Code seja 4XX ou 5XX, esse campo deve ser preenchido com a lista das strings obtidas em ".errors[].code" . Não havendo string, deve ser enviada uma lista vazia.
CLIENT
4xx ou 5xx
Todos
/open-banking/enrollments/v1/consents/{consentId}/authorise
/open-banking/enrollments/v1/enrollments
/open-banking/enrollments/v1/enrollments/{enrollmentId}
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-registration
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-registration-options
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-sign-options
/open-banking/enrollments/v1/enrollments/{enrollmentId}/risk-signals
/open-banking/enrollments/v2/consents/{consentId}/authorise
/open-banking/enrollments/v2/enrollments
/open-banking/enrollments/v2/enrollments/{enrollmentId}
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-registration
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-registration-options
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-sign-options
/open-banking/enrollments/v2/enrollments/{enrollmentId}/risk-signals
webhookEnable
Deve ser preenchido com o valor booleano TRUE caso haja pelo menos um item indicado na lista do campo ".webhook_uris" no payload, caso contrário deverá ser preenchido com o valor booleano FALSE
CLIENT
N/A
N/A
N/A
webhookInteractionId
Caso o GET esteja sendo feito após o estímulo do webhook, o x-webhook-interaction-id deverá ser indicado
CLIENT
N/A
N/A
N/A
enrollmentId​
Deve ser preenchido com a mesma string obtida no campo `.data.enrollmentId` retornado após a chamada inicial na API "POST /enrollments". *Ao reportar o uso de um endpoint /token, o identificador único de consentimento só será reportado nos casos em que "grant_type" é do tipo "authorization_code" ou do tipo "refresh_token", uma vez que esta informação de enrollmentId é inexistente quando "grant_type" é do tipo "client_credentials".​
CLIENT​
Todos​
Todos​
/open-banking/enrollments/v1/consents/{consentId}/authorise
​
/open-banking/enrollments/v1/enrollments/{enrollmentId}
​
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-registration
​
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-registration-options
​
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-sign-options
​
/open-banking/enrollments/v1/enrollments/{enrollmentId}/risk-signals
​
/open-banking/enrollments/v2/consents/{consentId}/authorise
​
/open-banking/enrollments/v2/enrollments/{enrollmentId}
​
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-registration
​
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-registration-options
​
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-sign-options
​
/open-banking/enrollments/v2/enrollments/{enrollmentId}/risk-signals​
enrollmentId​
Deve ser preenchido com a mesma string obtida no campo `.data.enrollmentId` retornado após a chamada inicial na API "POST /enrollments". *Ao reportar o uso de um endpoint /token, o identificador único de consentimento só será reportado nos casos em que "grant_type" é do tipo "authorization_code" ou do tipo "refresh_token", uma vez que esta informação de enrollmentId é inexistente quando "grant_type" é do tipo "client_credentials".​
CLIENT​
201​
POST​
/open-banking/enrollments/v1/enrollments
​
/open-banking/enrollments/v2/enrollments​
authenticatorAttachment​
Deve ser preenchido com a mesma string definida em ".data.authenticatorAttachment". Não havendo string, deve ser explicitamente enviada esse additionalInfo como sendo uma string vazia.​
CLIENT​
Todos​
Todos​
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-registration
​
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-registration​
platform​
Deve ser preenchido com a mesma string definida em ".data.platform"​
CLIENT​
Todos​
Todos​
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-registration-options
​
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-registration-options
​
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-sign-options
​
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-sign-options​
rp​
Deve ser preenchido com a mesma string definida em ".data.rp"​
CLIENT​
Todos​
POST​
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-registration-options
​
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-registration-options
​
/open-banking/enrollments/v1/enrollments/{enrollmentId}/fido-sign-options
​
/open-banking/enrollments/v2/enrollments/{enrollmentId}/fido-sign-options​
rejectionReasonCode​
Deve ser preenchido com a mesma string obtida no ".data.rejectionReason.code" ou ".data.rejection.reason.code" ou ".data.cancellation.rejectionReason"​
CLIENT​
Todos (PATCH)
​
200 (GET)​
GET ou PATCH​
/open-banking/enrollments/v1/enrollments/{enrollmentId}
​
/open-banking/enrollments/v2/enrollments/{enrollmentId}​
rejectionReasonDetail​
Deve ser preenchido com a mesma string obtida no ".data.rejectionReason.detail" ou ".data.rejection. reason.detail"​
CLIENT​
N/A​
N/A​
N/A​
authorisationFlow​
Deve ser preenchido com a mesma string obtida no ".data.authorisationFlow"​
CLIENT​
N/A​
N/A​
N/A​
dropReason​
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
​/open-banking/enrollments/v1/enrollments
​
/open-banking/enrollments/v2/enrollments​
paymentType​
Identifica o modo de pagamento acionado no consentimento e deve ser preenchido de acordo com a tabela especificada no swagger da API​
CLIENT​
N/A​
N/A​
N/A​
revocationReasonCode​
Deve ser preenchido com a mesma string definida em ".data.revocation.reason.code" ou ".data.cancellation.revocationReason"​
CLIENT​
Todos (PATCH)
​
200 (GET)​
GET ou PATCH​
/open-banking/enrollments/v1/enrollments/{enrollmentId}
​
/open-banking/enrollments/v2/enrollments/{enrollmentId}​
revocationReasonDetail​
Deve ser preenchido com a mesma string definida em ".data.revocation.reason.detail"​
CLIENT​
N/A​
N/A​
N/A​
revokedBy​
Deve ser preenchido com a mesma string definida em ".data.revocation.revokedBy"​
CLIENT​
N/A​
N/A​
N/A​
revokedFrom​
Deve ser preenchido com a mesma string definida em ".data.revocation.revokedFrom"​
CLIENT​
N/A​
N/A​
N/A​
rejectedBy ​
Deve ser preenchido com a mesma string definida em ".data.rejection. rejectedBy"​
CLIENT​
N/A​
N/A​
N/A​
rejectedFrom​
Deve ser preenchido com a mesma string definida em ".data.rejection. rejectedFrom"​
CLIENT​
N/A​
N/A​
N/A​
grantType​
Deve ser preenchido com a mesma string enviada no campo ".grant_type "​
CLIENT​
N/A​
N/A​
N/A​
riskSignalsQuantity​
Calculado pelo iniciador. Cada parâmetro enviado no request body no objeto data.riskSignals durante a operação deve-se ser contabilizado, seja ele opcional ou obrigatório, gerando a quantidade total de parâmetros que foram enviados pelo iniciador na operação. É um numero inteiro​
CLIENT​
Todos​
POST​
/open-banking/enrollments/v2/consents/{consentId}/authorize​
riskSignalsEnumList​
Lista das propriedades de RiskSignals enviadas no request body (Schema RiskSignals.data )​
CLIENT​
Todos​
POST​
/open-banking/enrollments/v2/enrollments/{enrollmentId}/risk-signals​
cancelledFrom​
Deve ser preenchido com a mesma string definida em ".data.cancelledFrom "​
CLIENT​
200​
GET​
/open-banking/enrollments/v2/enrollments/{enrollmentId}​
nfcPayment
Identifica se o pagamento foi realizado através de NFC
Valores aceitos: TRUE,, FALSE
CLIENT
Todos
POST
/open-banking/consents/{consentId}/authorise

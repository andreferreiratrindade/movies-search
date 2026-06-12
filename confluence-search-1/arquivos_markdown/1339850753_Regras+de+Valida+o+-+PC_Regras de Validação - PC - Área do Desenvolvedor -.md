---
                            title: "Regras de Validação - PC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1339850753_Regras+de+Valida+o+-+PC"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1339850753/Regras+de+Valida+o+-+PC"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Regras de Validação - PC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.03
Objetivo desta página
Demonstrar funcionalmente as regras de validação de qualidade de campos básicos e additionalInfos realizados na PCM. Estas validações são utilizadas para aberturas de tickets e monitoramento através do dashboard de Monitoramento Operacional.
Guia de leitura
Nos endpoints, a referência “v
x
” deve ser substituída pela versão da API que está sendo enviada. Por exemplo, para a versão 4 (v4) dos endpoints de pagamento, enviar “open-banking/automatic-payments/
v
4
/recurring-consents/{recurringConsentId}”.
Nos endpoints, a referência % significa que vale para qualquer conteúdo antes ou depois, de acordo com o endpoint em questão. Por exemplo, “%/automatic-payments/v
x
/recurring-consents%” significa que vale para os endpoints “/open-banking/automatic-payments/v2/recurring-consents” e “/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}”.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Portabilidade de Crédito
Campo
Regra
Campo
Regra
clientSSId
SE
Role = CLIENT
E
método = POST, GET ou PATCH
E
endpoint = %/credit-portability/v
x
/portabilities%
ENTÃO
Se o clientSSId for nulo, retorna
Nulo
Se o clientSSId for vazio, retorna
Vazio
Se o REGEX do clientSSId não for ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$, retorna
Invalido
consentId
SE
Método = POST
E
endpoint = %/credit-portability/v
x
/portabilities ou %/credit-portability/v
x
/portabilities/{portabilityId}
E
statusCode não é 4xx ou 5xx
ENTÃO
Se o consentId for nulo, retorna
Nulo
Se o consentId for vazio, retorna
Vazio
Se o REGEX do consentId não for ^urn:[a-zA-Z0-9][a-zA-Z0-9\-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*''%\/?#]+$, retorna
Invalido
creationDateTime
SE
Role = CLIENT
E
método = POST ou GET
E
statusCode não é 4xx ou 5xx
E
endpoint = %/credit-portability/v
x
/portabilities ou %/credit-portability/v
x
/portabilities
ENTÃO
Se o creationDateTime for nulo, retorna
Nulo
Se o creationDateTime for vazio, retorna
Vazio
creditPortabilityStatus
SE
Método = GET
E
statusCode não é 4xx ou 5xx
E
endpoint = %/credit-portability/v
x
/portabilities/{portabilityId}
ENTÃO
Se o creditPortabilityStatus for nulo, retorna
Nulo
Se o creditPortabilityStatus for vazio, retorna
Vazio
Se o creditPortabilityStatus não for ACCEPTED_SETTLEMENT_COMPLETED, ACCEPTED_SETTLEMENT_IN_PROGRESS, CANCELLED, PENDING, PAYMENT_ISSUE, PORTABILITY_COMPLETED, RECEIVED ou REJECTED, retorna
Invalido
endpoint
SE
endpoint for nulo, retorna
Nulo
endpoint for vazio, retorna
Vazio
endpoint não for um endpoint válido para Portabilidade de Crédito, retorna
Invalido
endpointUriPrefix
SE
Role = CLIENT
E
método = POST, GET ou PATCH
ENTÃO
Se o endpointUriPrefix for nulo, retorna
Nulo
Se o endpointUriPrefix for vazio, retorna
Vazio
Se o REGEX do endpointUriPrefix não for ^[- /:_.,0-9a-zA-Z]{0,200}$, retorna
Invalido
errorCode
SE
Role = CLIENT
E
endpoint = %/credit-portability/v
x
/portabilities%
E
método = POST, GET ou PATCH
E
statusCode for 4xx ou 5xx
ENTÃO
Se o errorCode for nulo, retorna
Nulo
Se o errorCode for vazio, retorna
Vazio
portabilityId
SE
Método = POST ou GET
E
statusCode não for 4xx ou 5xx
E
endpoint = %/credit-portability/v
x
/portabilities ou %/credit-portability/v
x
/portabilities/{portabilityId
ENTÃO
Se o portabilityId for nulo, retorna
Nulo
Se o portabilityId for vazio, retorna
Vazio
Se o REGEX do portabilityId não for ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$, retorna
Invalido
rejectedBy
SE
Método = GET ou PATCH
E
statusCode não é 4xx ou 5xx
E
endpoint = %/credit-portability/v
x
/portabilities/{portabilityId} ou %/credit-portability/v
x
/portabilities/{portabilityId}/cancel
E
creditPortabilityStatus = REJECTED, CANCELLED ou PAYMENT_ISSUE
ENTÃO
Se o rejectedBy for nulo, retorna
Nulo
Se o rejectedBy for vazio, retorna
Vazio
Se o rejectedBy não for CREDORA, PROPONENTE ou USUARIO, retorna
Invalido
rejectionReason
SE
Método = GET ou PATCH
E
statusCode não é 4xx ou 5xx
E
endpoint = %/credit-portability/v
x
/portabilities/{portabilityId} ou %/credit-portability/v
x
/portabilities/{portabilityId}/cancel
E
creditPortabilityStatus = REJECTED, CANCELLED ou PAYMENT_ISSUE
ENTÃO
Se o rejectionReason for nulo, retorna
Nulo
Se o rejectionReason for vazio, retorna
Vazio
Se o rejectedBy for PROPONENTE, creditPortabilityStatus for REJECTED e rejectionReason não for OUTROS, POLITICA_DE_CREDITO,  SALDO_DEVEDOR_ATUALIZADO_SUBSTANCIALMENTE_DIVERGENTE, retorna
Invalido
Se o rejectedBy for CREDORA, creditPortabilityStatus for REJECTED e rejectionReason não for CLIENTE_COM_ACAO_JUDICIAL, CONTRATO_JA_LIQUIDADO, DECURSO_DO_PRAZO_PARA_PAGAMENTO, MODALIDADE_DA_OPERACAO_INCOMPATIVEL, PORTABILIDADE_CANCELADA_POR_FALTA_DE_LIQUIDACAO,
PORTABILIDADE_EM_ANDAMENTO ou RETENCAO_DO_CLIENTE, retorna
Invalido
Se o rejectedBy for USUARIO, creditPortabilityStatus for CANCELLED e rejectionReason não for CANCELADO_PELO_CLIENTE, retorna
Invalido
Se o rejectedBy for CREDORA, creditPortabilityStatus for PAYMENT_ISSUE e rejectionReason não for DIVERGENCIA_DE_PAGAMENTO_EFETUADO ou OUTROS, retorna
Invalido
statusUpdateDateTime
SE
Método = GET
E
statusCode não for 4xx ou 5xx
E
endpoint = %/credit-portability/v
x
/portabilities/{portabilityId}
ENTÃO
Se o statusUpdateDateTime for nulo, retorna
Nulo
Se o statusUpdateDateTime for vazio, retorna
Vazio

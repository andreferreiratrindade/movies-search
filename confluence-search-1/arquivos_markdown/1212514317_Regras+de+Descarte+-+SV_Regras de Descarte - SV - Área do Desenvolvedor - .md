---
                            title: "Regras de Descarte - SV - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1212514317_Regras+de+Descarte+-+SV"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1212514317/Regras+de+Descarte+-+SV"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Regras de Descarte - SV - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.02
Objetivo desta página
Demonstrar funcionalmente as regras de descartes de reportes realizados na PCM. Estas regras são utilizadas para aberturas de tickets e monitoramento através do dashboard de Monitoramento Operacional.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Private API - Pagamentos
Campo
Regra
Campo
Regra
additionalInfo
Informação não enviada
Invalid type: additionalInfo: Required:
additonalInfo não enviado; na ausência de additonalInfo, deve ser informada uma matriz vazia
Conteúdo inválido
additionalInfo should not be empty:
additonalInfo vazio; na ausência de additonalInfo, deve ser informada uma matriz vazia
Invalid type: additionalInfo: Expected object, received ‘xxxx’:
tipo do campo additionalInfo inválido; esperado objeto
Campos additionalInfo
Conteúdo inválido
Invalid type: Expected string, received ‘xxxx’:
tipo do campo inválido; esperado string
clientOrgId
Informação não enviada
Invalid type: clientOrgId: Required:
campo ClientOrgId ausente
Missing property: clientOrgId or serverOrgId:
campo clientOrgid ausente
Conteúdo inválido
clientOrgId 'xxxx' is invalid to role 'CLIENT':
clientOrgId informado é inválido para o role CLIENT
Invalid field type, clientOrgId must be a valid UUID:
clientOrgId não está no formato UUID
Invalid type: clientOrgId: Expected string, received null:
conteúdo do campo clientOrgId inválido; esperado string, recebido nulo
Requester id mismatch with clientOrgId:
clientOrgId informado no role CLIENT não é a mesma organização reportadora (PAR-100)
Validation error: clientOrgId:
conteúdo do campo clientOrgId inválido
invalid value: Client organization ID not found:
clientOrgId informado não foi localizado no Diretório Central
clientSSId
Informação não enviada
Invalid type: clientSSId: Required:
campo clientSSId ausente
Missing property: clientSSId:
campo clientSSId ausente
Conteúdo inválido
Invalid field type, clientSSId should not be empty:
campo clientSSId não pode estar vazio
Invalid format: clientSSId: Invalid uuid:
formato do clientSSId inválido, deve estar no formato UUID
Invalid format: Unrecognized key(s) in object: 'clientSSId':
conteúdo do campo clientSSId inválido
Invalid type: clientSSId: Expected string, received null:
conteúdo do campo clientSSId inválido; esperado string, recebido nulo
Invalid value: Client SSID not found in combined org IDs:
campo clientSSId inválido, não encontrado na combinação de org IDs
correlationId
Conteúdo inválido
Invalid format: correlationId: Invalid correlationId format:
formato do correlationId inválido (não pode ter mais de 100 caracteres)
endpoint
Informação não enviada
Invalid type: endpoint: Required; validation error: undefined:
campo endpoint ausente
Conteúdo inválido
Missing property, endpoint can't be empty:
campo endpoint não pode estar vazio
Unlisted endpoint:
endpoint enviado não é válido (consultar a tabela de endpoints aceitos pela PCM)
endpointUriPrefix
Informação não enviada
Invalid type: endpointUriPrefix: Required:
campo endpointUriPrefix ausente
Conteúdo inválido
Invalid format: : Unrecognized key(s) in object: 'endpointUriPrefix':
conteúdo do campo endpointUriPrefix inválido
fapiInteractionId
Informação não enviada
Invalid field value fapiInteractionId can't be empty for status 408 or 500:
fapiInteractionId deve ser informado para status 408 ou 500
Missing property: fapiInteractionId is required:
campo fapiInteractionId ausente
Missing property, fapiInteractionId is not provided:
campo fapiInteractionId ausente
Conteúdo inválido
Invalid format: fapiInteractionId must match format "uuid”:
campo fapiInteractionId com formato inválido (UUID) ou com menos de 36 caracteres
Invalid format: : Unrecognized key(s) in object: 'fapiinteractionid':
conteúdo do campo fapiInteractionId inválido
Invalid type: fapiInteractionId mismatch. Ensure the ID is not "00000000-0000-0000-0000-000000000000.":
formato do campo fapiInteractionId inválido
Invalid type: fapiInteractionId: Expected string, received ‘xxxx’:
tipo do campo fapiInteractionId inválido; esperado string
httpMethod
Informação não enviada
Invalid type: httpMethod: Required:
campo httpMethod ausente
Conteúdo inválido
Invalid format: : Unrecognized key(s) in object: 'httpmethod':
conteúdo do campo httpMethod inválido
Invalid value: httpMethod: Invalid enum value. Expected ‘GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE', received 'HEAD’:
conteúdo do campo httpMethod inválido, recebido conteúdo não determinado no enum do campo
processTimespan
Informação não enviada
Invalid type: processTimespan: Required:
campo processTimespan ausente
Conteúdo inválido
Invalid type: processTimespan: Expected number, received ‘xxxx’:
conteúdo do campo processTimespan inválido; esperado número
Invalid value: processTimespan must be greater than zero:
campo processTimespan deve ter valor maior do que zero
role
Informação não enviada
Invalid type: role: Required
campo role ausente
Conteúdo inválido
Invalid value: role: Invalid enum value. Expected 'SERVER' | 'CLIENT', received 'xxxx':
conteúdo do campo role inválido, recebido conteúdo não determinado no enum do campo
rp (additilonalInfo)
Conteúdo inválido
Invalid type: additionalInfo.rp: Expected string, received ‘xxxx’:
tipo do campo rp inválido; esperado string
serverOrgId
Informação não enviada
Invalid type: serverOrgId: Required; missing property: serverOrgId:
campo serverOrgId ausente
Missing property: clientOrgId or serverOrgId
: serverOrgId ausente
Missing property: serverOrgId:
campo serverOrgId ausente
Conteúdo inválido
Invalid field type, serverOrgId must be a valid UUID:
serverOrgId não está no formato UUID
Requester id mismatch with serverOrgId:
serverOrgId informado no role SERVER não é a mesma organização reportadora
Requester mismatch: serverOrgId:
serverOrgId informado no role SERVER não é a mesma organização reportadora
serverOrgId 'xxxx' is invalid to role 'SERVER':
serverIrgId informado é inválido para o role SERVER
invalid value: Server organization ID not found:
serverOrgId informado não foi localizado no Diretório Central
statusCode
Informação não enviada
Invalid type: statusCode: Required:
campo statusCode ausente
Conteúdo inválido
Invalid type: statusCode: Expected number, received ‘xxxx’:
conteúdo do campo statusCode inválido; esperado número
Invalid value: statusCode must be between 200 and 599:
campo statusCode com valor menor do que 200 ou maior do que 599
Missing property, statusCode can't be empty:
campo statusCode não pode estar vazio
timestamp
Conteúdo inválido
Error not mapped or not expected by validations: Report is too old:
campo timestamp com data passada de 7 dias
Invalid format: timestamp: Invalid date:
conteúdo do campo timestamp inválidlo
Missing property, timestamp can't be empty:
campo timestamp não pode estar vazio
Timestamp is older than 7 days:
campo timestamp com data passada de 7 dias
Timestamp of report is too old:
campo timestamp com data passada de 7 dias
Validation error: Report is too old:
campo timestamp com data passada de 7 dias
API Estados de Pagamento
Campo
Regra
Campo
Regra
clientOrgId
Deve ser enviado no payload (não deve estar ausente)
clientOrgId must be a UUID:
campo clientOrgId deve estar no formato UUID
clientOrgId should not be empty:
campo vazio
consentId
Deve ser enviado no payload (não deve estar ausente)
Deve estar no padrão especificado na documentação funcional para ser considerado válido
consentId should not be empty:
campo vazio
consentId must be a string:
tipo do campo consentId inválido; esperado string
eventDateTime
Não pode estar vazio
Deve ser enviado no payload (não deve estar ausente)
Deve estar no padrão especificado na documentação funcional para ser considerado válido
EventDateTime must not be older than 7 days:
campo eventDateTime com data passada de 7 dias
paymentId
Deve ser enviado no payload (não deve estar ausente)
Deve estar no padrão especificado na documentação funcional para ser considerado válido
paymentId should not be empty:
campo vazio
paymentId must be a string:
tipo do campo paymentId inválido; esperado string
paymentStatus
Deve ser enviado no payload (não deve estar ausente)
paymentStatus should not be empty:
campo vazio
paymentStatus must be a string:
tipo do campo paymentStatus inválido; esperado string
paymentStatus must be one of the following values: ACSC, RJCT, CANC, SCHD:
conteúdo do campo paymentStatus inválido, recebido conteúdo não determinado no enum do campo
paymentType
Deve ser enviado no payload (não deve estar ausente)
paymentType should not be empty:
campo vazio
paymentType must be one of the following values: IMMEDIATE, RECURRENT, SWEEPING, AUTOMATIC, SCHEDULED:
conteúdo do campo paymentType inválido, recebido conteúdo não determinado no enum do campo
statusReasonCode
statusReasonCode should not be empty:
campo vazio

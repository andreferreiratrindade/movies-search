---
                            title: "Regras de Descarte - SG - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1212383257_Regras+de+Descarte+-+SG"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1212383257/Regras+de+Descarte+-+SG"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Regras de Descarte - SG - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.01
Objetivo desta página
Demonstrar funcionalmente as regras de descartes de reportes realizados na PCM. Estas regras são utilizadas para aberturas de tickets e monitoramento através do dashboard de Monitoramento Operacional.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Private API - Segurança
Campo
Regra
Campo
Regra
additionalInfo
Informação não enviada
Invalid type: additionalInfo: Required:
additonalInfo não enviado; na ausência de additonalInfo, deve ser informada uma matriz vazia
Conteúdo inválido
AdditionalInfo should not be empty:
additonalInfo vazio; na ausência de additonalInfo, deve ser informada uma matriz vazia
Invalid type: additionalInfo: Expected object, received ‘xxxx’:
conteúdo do campo additionalInfo inválido, deveria ser object
clientOrgId
Informação não enviada
Invalid type: clientOrgId: Required:
campo ClientOrgId ausente
Missing property: clientOrgId:
campo clientOrgid ausente
Conteúdo inválido
clientOrgId 'xxxx' is invalid to role 'CLIENT':
clientOrgId informado é inválido para o role CLIENT
clientOrgId must be a valid UUID:
clientOrgId não está no formato UUID
invalid format: clientOrgId: Invalid uuid:
clientOrgId não está no formato UUID
Invalid type: clientOrgId: Expected string, received ‘xxxx’:
conteúdo do campo clientOrgId inválido; esperado string
Requester id mismatch with clientOrgId:
clientOrgId informado no role CLIENT não é a mesma organização reportadora
invalid value: Client organization ID not in directory:
clientOrgId não cadastrado no Diretório Central
clientSSId
Informação não enviada
Invalid type: clientSSId: Required:
campo clientSSId ausente
Missing property: clientSSId:
campo clientSSId ausente
Conteúdo inválido
clientSSId should not be empty:
campo clientSSId não pode estar vazio
Invalid format: clientSSId: Invalid uuid:
formato do clientSSId inválido, deve estar no formato UUID
Invalid format: Unrecognized key(s) in object: 'clientSSId':
conteúdo do campo clientSSId inválido
Invalid type: clientSSId: Expected string, received null:
conteúdo do campo clientSSId inválido; esperado string, recebido nulo
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
invalid type: endpointUriPrefix: Required:
campo endpointUriPrefix ausente
Conteúdo inválido
endpointUriPrefix should not be empty:
campo endpointUriPrefix não pode estar vazio
Invalid format: : Unrecognized key(s) in object: 'endpointUriPrefix':
conteúdo do campo endpointUriPrefix inválido
errorCodes
Conteúdo inválido
Invalid type: additionalInfo.errorCodes.0: Expected string,  received 'xxxx':
conteúdo do campo inválido, deveria ser string
fapiInteractionId
Informação não enviada
fapiInteractionId is not provided:
campo fapiInteractionId não enviado
Invalid field value fapiInteractionId can't be empty for status 408 or 500:
fapiInteractionId deve ser enviado para status 408 e 500
Conteúdo inválido
fapiInteractionId must be a valid UUID:
formato do fapiInteractionId inválido, deve estar no formato UUID
Invalid type: fapiInteractionId mismatch. Ensure the ID is not "00000000-0000-0000-0000-000000000000.":
conteúdo do fapiInteractionId inválido
Invalid type: fapiInteractionId: Expected string, received null:
conteúdo do campo fapiInteractionId inválido
grantType (additionalInfo)
Conteúdo inválido
Invalid value: additionalInfo.grantType: Invalid enum value. Expected 'AUTHORIZATION_CODE' | 'CLIENT_CREDENTIALS' | 'REFRESH_TOKEN', received 'xxxx':
conteúdo do campo grantType inválido, recebido conteúdo não determinado no enum do campo
Unsupported grant_type:
campo grantType inválido, vazio ou ausente
invalid type: additionalInfo.grantType: Expected string, received ‘xxxx’:
campo grantTypr deve ser do tipo string
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
Conteúdo inválido
Invalid type: role: Required:
campo role ausente
Invalid value: role: Invalid enum value. Expected 'SERVER' | 'CLIENT':
conteúdo do campo role inválido, recebido conteúdo não determinado no enum do campo
serverOrgId
Informação não enviada
Invalid type: serverOrgId: Required:
campo serverOrgId ausente
Missing property: serverOrgId:
campo serverOrgId ausente
Conteúdo inválido
Invalid field type, serverOrgId must be a valid UUID:
serverOrgId não está no formato UUID
invalid format: serverOrgId: Invalid uuid:
serverOrgId não está no formato UUID
Invalid type: serverOrgId: Expected string, received ‘xxxx’:
conteúdo do campo serverOrgid inválido
Requester id mismatch with serverOrgId:
serverOrgId informado no role SERVER não é a mesma organização reportadora
Requester mismatch: serverOrgId:
serverOrgId informado no role SERVER não é a mesma organização reportadora
serverOrgId 'xxxx' is invalid to role 'SERVER':
serverIrgId informado é inválido para o role SERVER
invalid value: Server organization ID not found:
serverOrgId não cadastrado no Diretório Central
statusCode
Informação não enviada
Invalid type: statusCode: Required:
campo statusCode ausente
Conteúdo inválido
Invalid type: statusCode: Expected number, received string:
conteúdo do campo statusCode inválido; esperado número, recebido string
Invalid value: statusCode must be between 100 and 599:
campo statusCode com valor menor do que 100 ou maior do que 599
Missing property, statusCode can't be empty:
campo statusCode não pode estar vazio
timestamp
Conteúdo inválido
Error not mapped or not expected by validations: Report is too old:
campo timestamp com data passada de 7 dias
Invalid format: timestamp: Invalid date:
conteúdo do campo timestamp inválidlo
Timestamp is older than 7 days:
campo timestamp com data passada de 7 dias
Timestamp of report is too old:
campo timestamp com data passada de 7 dias
webhookEnable
Conteúdo inválido
Invalid type: additionalInfo.webhookEnable: Expected string, receivded 'xxxx':
conteúdo do campo webhookEnable inválido, deveria ser string, recebido boolean
webhookEnable must be a string:
conteúdo do campo webhookEnable inválido, deveria ser string

---
                            title: "Regras de Descarte - DC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1212383245_Regras+de+Descarte+-+DC"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1212383245/Regras+de+Descarte+-+DC"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Regras de Descarte - DC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.01
Objetivo desta página
Demonstrar funcionalmente as regras de descartes de reportes realizados na PCM. Estas regras são utilizadas para aberturas de tickets e monitoramento através do dashboard de Monitoramento Operacional.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Private API - Dados Cadastrais e Transacionais
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
Campos additionalInfo
Conteúdo inválido
Valida se o campo é do tipo string
clientOrgId
Informação não enviada
Invalid type: clientOrgId: Required:
campo ClientOrgId ausente
Missing property: clientOrgId:
campo clientOrgid ausente
Conteúdo inválido
clientOrgId 'xxxx' is invalid to role 'CLIENT':
clientOrgId informado é inválido para o role CLIENT
invalid format: clientOrgId: Invalid uuid:
clientOrgId não está no formato UUID
Invalid field type, clientOrgId must be a valid UUID:
clientOrgId não está no formato UUID
Requester id mismatch with clientOrgId:
clientOrgId informado no role CLIENT não é a mesma organização reportadora
invalid value: Client organization ID not in directory:
clientOrgId não cadastrado no diretório
clientSSId
Informação não enviada
Invalid type: clientSSId: Required:
campo clientSSId ausente
Missing property: clientSSId:
campo clientSSId ausente
Conteúdo inválido
invalid format: : Unrecognized key(s) in object: 'clientSSId':
conteúdo do campo clientSSId inválido
Invalid field type, clientSSId should not be empty:
campo clientSSId não pode estar vazio
Invalid format: clientSSId: Invalid uuid:
formato do clientSSId inválido, deve estar no formato UUID
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
endpointUriPrefix
Informação não enviada
Invalid type: endpointUriPrefix: Required:
campo endpointUriPrefix ausente
Conteúdo inválido
Invalid format: : Unrecognized key(s) in object: 'endpointUriPrefix':
conteúdo do campo endpointUriPrefix inválido
fapiInteractionId
Informação não enviada
Missing property: fapiInteractionId is required:
campo fapiInteractionId ausente
Conteúdo inválido
Invalid format: fapiInteractionId must match format "uuid”:
campo fapiInteractionId com formato inválido (UUID) ou com menos de 36 caracteres
Invalid format: : Unrecognized key(s) in object: 'fapiinteractionid':
conteúdo do campo fapiInteractionId inválido
Invalid type: fapiInteractionId mismatch. Ensure the ID is not "00000000-0000-0000-0000-000000000000.":
formato do campo fapiInteractionId inválido
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
Invalid value: processTimespan must be greater than zero:
campo processTimespan deve ter valor maior do que zero
role
Informação não enviada
Invalid type: role: Required
campo role ausente
Conteúdo inválido
Invalid value: role: Invalid enum value. Expected 'SERVER' | 'CLIENT', received 'xxxx':
conteúdo do campo role inválido, recebido conteúdo não determinado no enum do campo
serverOrgId
Informação não enviada
Invalid type: serverOrgId: Required; missing property: serverOrgId:
campo serverOrgId ausente
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
statusCode
Informação não enviada
Invalid type: statusCode: Required:
campo statusCode ausente
Conteúdo inválido
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

---
                            title: "Regras de Descarte - HF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1212350477_Regras+de+Descarte+-+HF"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1212350477/Regras+de+Descarte+-+HF"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Regras de Descarte - HF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.00
Objetivo desta página
Demonstrar funcionalmente as regras de descartes de reportes realizados na PCM. Estas regras são utilizadas para aberturas de tickets e monitoramento através do dashboard de Monitoramento Operacional.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Hybridflow API
Campo
Regra
Campo
Regra
clientOrgId
Informação não enviada
Invalid type: clientOrgId: Required:
campo clientOrgId ausente
Conteúdo inválido
Invalid format: clientOrgId: Invalid uuid:
campo clientOrgId vazio, inválido ou com mais de 36 caracteres
Invalid field type, clientOrgId must be a valid uuid:
campo clientOrgId deve obedecer ao formato UUID
consentId
Informação não enviada
Invalid type: consentId: Required:
campo consentId ausente
Conteúdo inválido
Invalid field type, consentId need match with regex:
conteúdo do campo consentId inválido, não está dentro do padrão especificado
Invalid field value, consentId can't be empty:
campo consentId não pode estar vazio
Invalid format: consentId: Invalid:
conteúdo do campo consentId inválido
Invalid format: consentId: String must contain at least 1 character(s):
conteúdo do campo consentId inválido, deve possuir pelo menos um caractere
error
Informação não enviada
Invalid type: error: Required:
campo error ausente
Missing property, error can't be empty:
campo error não pode estar vazio
Conteúdo inválido
error must be a string:
conteúdo do campo error inválido, deve ser uma string
Invalid type: error: Expected string, received array:
conteúdo do campo error inválido; esperado string, recebido array
Invalid format: error: String must contain at least 1 character(s):
conteúdo do campo error inválido, deve possuir pelo menos um caractere
os
Informação não enviada
Invalid type: os: Required:
campo os ausente
Missing property, os can't be empty:
campo os não pode estar vazio
Conteúdo inválido
Invalid field value, os must be a valid enum:
conteúdo do campo os inválido, deve ser um enum válido
Invalid value: os: Invalid enum value. Expected ‘LINUX' | ‘MACOS' | 'UNIX' | 'WINDOWS' | 'IOS' | 'ANDROID' | 'OTHER', received 'XXX’:
conteúdo do campo os inválido, recebido conteúdo não determinado no enum do campo
osVersion
Conteúdo inválido
Invalid field value, osVersion can't be empty:
campo osVersion não pode estar vazio
Invalid format: osVersion: Invalid:
conteúdo do campo osVersion inválido
Invalid format: osVersion: String must contain at least 1 character(s):
conteúdo do campo osVersion inválido, deve possuir pelo menos um caracter
Invalid type: osVersion: Expected string, received ‘xxxx’:
conteúdo do campo osVersion inválido, deve ser string
Invalid field type, os version must be a string:
conteúdo do campo osVersion inválido, deve ser string
platform
Informação não enviada
Invalid type: platform: Required:
campo platform ausente
Missing property, platform can't be empty:
campo platform não pode estar vazio
Conteúdo inválido
Invalid field value, platform must be a valid enum:
conteúdo do campo platform inválido, recebido conteúdo não determinado no enum do campo
Invalid value: platform: Invalid enum value. Expected 'BROWSER' | 'APP', received 'xxxx':
conteúdo do campo platform inválido, recebido conteúdo não determinado no enum do campo
serverOrgId
Informação não enviada
Invalid type: serverOrgId: Required:
campo serverOrgId ausente
Conteúdo inválido
Invalid field type, serverOrgId must be a valid uuid:
conteúdo do campo serverOrgId inválido, deve estar no formato UUID
Invalid format: serverOrgId: Invalid uuid:
conteúdo do campo serverOrgId inválido, deve estar no formato UUID
timestamp
Conteúdo inválido
Invalid format: timestamp: Invalid date:
conteúdo do campo timestamp inválido, não é uma data válida
Validation error: Report is too old:
campo timestamp com data passada de 7 dias
Invalid field type, timestamp must be a valid date:
conteúdo do campo timestamp inválido, não é uma data válida
Timestamp is in the future, timestamp of report is in the future:
conteúdo do campo timestamp futuro em relação à data de recebimento do reporte
type
Informação não enviada
Invalid type: type: Required:
campo type ausente
Missing property, type can't be empty:
campo type não pode estar vazio
Conteúdo inválido
Invalid field value, type must be a valid enum:
conteúdo do campo type inválido
Invalid value: type: Invalid enum value. Expected ‘AWAITING_HANDOFF' | 'AWAITING_USER_AUTH' | 'AWAITING_REDIRECT_TO_APP' | 'AUTHORISED' | 'REJECTED', received 'xxxx’:
conteúdo do campo type inválido, recebido conteúdo não determinado no enum do campo
uriAuthorizationEndpoint
Informação não enviada
Invalid type: uriAuthorizationEndpoint: Required:
campo uriAuthorizationEndpoint ausente
Missing property, uriAuthorizationEndpoint can't be empty:
campo uriAuthorizationEndpoint não pode estar vazio
Conteúdo inválido
Invalid field type, uriAuthorizationEndpoint need match with regex:
conteúdo do campo uriAuthorizationEndpoint inválido, não está dentro do padrão especificado
Invalid field value, uriAuthorizationEndpoint must be less than 11 characters:
conteúdo do campo uriAuthorizationEndpoint não pode ter menos do que 11 caracteres
Invalid field value, uriAuthorizationEndpoint must be more than 200 characters:
conteúdo do campo uriAuthorizationEndpoint não pode ter mais do que 200 caracteres
Invalid format: uriAuthorizationEndpoint: Invalid:
conteúdo do campo uriAuthorizationEndpoint inválido
Invalid format: uriAuthorizationEndpoint: String must contain at least 1 character(s):
campo uriAuthorizationEndpoint deve possuir pelo menos 1 caractere
Invalid field type, uriAuthorizationEndpoint must be a string:
campo uriAuthorizationEndpoint deve ser uma string
uri_callback
Informação não enviada
Invalid type: uri_callback: Required:
campo uriAuthorizationEndpoint ausente
Missing property, uri_callback can't be empty:
campo uri_callback não pode estar vazio
Conteúdo inválido
Invalid field type, uri_callback need match with regex:
conteúdo do campo uri_callback inválido, não está dentro do padrão especificado
Invalid field value, uri_callback must be less than 11 characters:
conteúdo do campo uri_callback não pode ter menos do que 11 caracteres
Invalid field value, uri_callback must be more than 200 characters:
conteúdo do campo uri_callback não pode ter mais do que 200 caracteres

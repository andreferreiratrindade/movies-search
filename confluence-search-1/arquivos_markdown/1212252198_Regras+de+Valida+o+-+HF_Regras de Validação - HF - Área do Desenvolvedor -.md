---
                            title: "Regras de Validação - HF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1212252198_Regras+de+Valida+o+-+HF"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1212252198/Regras+de+Valida+o+-+HF"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Regras de Validação - HF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.01
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
Hybridflow
Campo
Regra
Campo
Regra
clientOrgId
SE
Endpoint = %/client/redirect-to-server, %/client/redirect-target-with-errors ou %/client/redirect-target-without-errors
ENTÃO
Se o clientOrgId for nulo, retorna
Nulo
Se o clientOrgId for vazio, retorna
Vazio
consentId
SE
Endpoint = %/client/redirect-to-server, %/client/redirect-target-with-errors, %/client/redirect-target-without-errors,  %/server/redirect-target, %/server/authenticated ou %/server/redirect-to-client
ENTÃO
Se o consentId for nulo, retorna
Nulo
Se o consentId for vazio, retorna
Vazio
Se o REGEX do consentId não for ^urn:[a-zA-Z0-9][a-zA-Z0-9\-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*''%/?#]+, retorna
Invalido
error
SE
Endpoint = %/client/redirect-target-with-errors
ENTÃO
Se o error for nulo, retorna
Nulo
Se o error for vazio, retorna
Vazio
os
SE
Endpoint = %/client/redirect-to-server, %/client/redirect-target-with-errors, %/client/redirect-target-without-errors, %/server/redirect-target, %/server/authenticated ou %/server/redirect-to-client
ENTÃO
Se o os for nulo, retorna
Nulo
Se o os for vazio, retorna
Vazio
Se o os não for ANDROID, IOS, LINUX, MACOS, OTHER, UNIX ou WINDOWS, retorna
Invalido
osVersion
SE
Endpoint = %/client/redirect-to-server, %/client/redirect-target-with-errors, %/client/redirect-target-without-errors, %/server/redirect-target, %/server/authenticated ou %/server/redirect-to-client
ENTÃO
Se o osVersion for nulo, retorna
Nulo
Se o osVersion for vazio, retorna
Vazio
platform
SE
Endpoint = %/client/redirect-to-server, %/client/redirect-target-with-errors, %/client/redirect-target-without-errors, %/server/authenticated ou %/server/redirect-to-client
ENTÃO
Se o platform for nulo, retorna
Nulo
Se o platform for vazio, retorna
Vazio
Se o platform não for APP ou BROWSER, retorna
Invalido
serverOrgId
SE
Endpoint = %/server/redirect-target, %/server/authenticated ou %/server/redirect-to-client
ENTÃO
Se o serverOrgId for nulo, retorna
Nulo
Se o serverOrgId for vazio, retorna
Vazio
timestamp
SE
Endpoint = %/client/redirect-to-server, %/client/redirect-target-with-errors, %/client/redirect-target-without-errors, %/server/redirect-target, %/server/authenticated ou %/server/redirect-to-client
ENTÃO
Se o timestamp for nulo, retorna
Nulo
Se o timestamp for vazio, retorna
Vazio
type
SE
Endpoint = %/server/redirect-target ou %/server/redirect-to-client
ENTÃO
Se o type for nulo, retorna
Nulo
Se o type for vazio, retorna
Vazio
Se o type não for AUTHORISED ou REJECTED, retorna
Invalido

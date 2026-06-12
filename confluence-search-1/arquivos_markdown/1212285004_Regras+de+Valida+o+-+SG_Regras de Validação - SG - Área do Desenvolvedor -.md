---
                            title: "Regras de Validação - SG - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1212285004_Regras+de+Valida+o+-+SG"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1212285004/Regras+de+Valida+o+-+SG"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Regras de Validação - SG - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.02
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
Segurança
Campo
Regra
Campo
Regra
consentId
SE
Role = CLIENT
E
endpoint = %/token
E
método = POST
E
statusCode não é 4xx ou 5xx
E
grantType = AUTHORIZATION_CODE ou REFRESH_TOKEN
ENTÃO
Se o consentId e enrollmentId forem ambos vazios ou nulos, retorna
Obrigatorio o preenchimento ou do consentId ou do enrollmentId
Se o REGEX do consentId não bater com ^urn:[a-zA-Z0-9][a-zA-Z0-9\-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*''%/?#]+, retorna
Invalido
enrollmentId
SE
Role = CLIENT
E
endpoint = %/token
E
método = POST
E
statusCode não é 4xx ou 5xx
E
grantType = AUTHORIZATION_CODE ou REFRESH_TOKEN
ENTÃO
Se o consentId e enrollmentId forem ambos vazios ou nulos, retorna
Obrigatorio o preenchimento ou do consentId ou do enrollmentId
grantType
SE
Role = CLIENT
E
endpoint = %/token
E
método = POST
ENTÃO
Se o grantType for nulo, retorna
Nulo
Se o grantType for vazio, retorna
Vazio
Se o grantType não for AUTHORIZATION_CODE, REFRESH_TOKEN ou CLIENT_CREDENTIALS, retorna
Invalido
tokenId
SE
Role = CLIENT
E
endpoint = %/token, %/register ou %/register/{clientId}
E
método = POST
E
statusCode = 200
ENTÃO
Se o tokenId for nulo, retorna
Nulo
Se o tokenId for vazio, retorna
Vazio
webhookEnable
SE
Role = CLIENT
E
endpoint = %/register
E
método = POST ou PUT
OU
endpoint = %/register/{clientId}
E método = PUT
ENTÃO
Se o webhookEnable for nulo, retorna
Nulo
Se o webhookEnable for vazio, retorna
Vazio
Se o webhookEnable não for TRUE ou FALSE, retorna
Invalido

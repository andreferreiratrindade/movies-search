---
                            title: "Contas - Regras de Validação - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1622573065_Contas+-+Regras+de+Valida+o"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1622573065/Contas+-+Regras+de+Valida+o"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Contas - Regras de Validação - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

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
Dados Cadastrais e Transacionais
Contas
Campo
Regra
Campo
Regra
consentId
SE
Role = CLIENT
E
endpoint = %/accounts/%
E
método = GET
ENTÃO
Se o consentId for nulo, retorna
Nulo
Se o consentId for vazio, retorna
Vazio
Se o REGEX do consentId não for ^urn:[a-zA-Z0-9][a-zA-Z0-9\-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*''%/?#]+, retorna
Invalido
tokenId
SE
Role = CLIENT
E
endpoint = %/accounts/%
ENTÃO
Se o tokenId for nulo, retorna
Nulo
Se o tokenId for vazio, retorna
Vazio

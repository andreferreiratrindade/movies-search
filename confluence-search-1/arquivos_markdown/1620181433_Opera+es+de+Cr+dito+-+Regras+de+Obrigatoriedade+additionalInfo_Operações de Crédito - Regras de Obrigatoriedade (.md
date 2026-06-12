---
                            title: "Operações de Crédito - Regras de Obrigatoriedade (additionalInfo) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1620181433_Opera+es+de+Cr+dito+-+Regras+de+Obrigatoriedade+additionalInfo"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1620181433/Opera+es+de+Cr+dito+-+Regras+de+Obrigatoriedade+additionalInfo"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Operações de Crédito - Regras de Obrigatoriedade (additionalInfo) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.05
Guia de leitura
Se o campo não está listado, é porque não existe a obrigatoriedade de enviá-lo.
Nos endpoints, a referência “v
x
” indica que se aplicam às versões listadas na coluna “Versões”. Por exemplo, Endpoint “open-banking/automatic-payments/v
x
/recurring-consents/{recurringConsentId}” e Versões “v1 v2” significa que o endpoint é válido para as versões 1 e 2.
Dica: para rolar a tabela horizontalmente, segure SHIFT e utilize o botão de rolagem do mouse.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Dados Cadastrais e Transacionais
Operações de Crédito
Campo
Grupo
Definição
Regra de preenchimento
Tipo
Roles
Http code
Métodos
Endpoints
Versões
Tamanho máximo
Padrão
Exemplo
Campo
Grupo
Definição
Regra de preenchimento
Tipo
Roles
Http code
Métodos
Endpoints
Versões
Tamanho máximo
Padrão
Exemplo
consentId
Adiantamento a Depositantes
O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.
Deve ser preenchido com a mesma string obtida no campo .data.consentId retornado após a chamada inicial na API "POST /consent”
string
CLIENT
Todos
GET
/open-banking/unarranged-accounts-overdraft/v
x
/contracts
/open-banking/unarranged-accounts-overdraft/v
x
/contracts/{contractId}
/open-banking/unarranged-accounts-overdraft/v
x
/contracts/{contractId}/warranties
/open-banking/unarranged-accounts-overdraft/v
x
/contracts/{contractId}/payments
/open-banking/unarranged-accounts-overdraft/v
x
/contracts/{contractId}/scheduled-instalments
v2
100
^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD33123
consentId
Direitos Creditórios Descontados
O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.
Deve ser preenchido com a mesma string obtida no campo .data.consentId retornado após a chamada inicial na API "POST /consent”
string
CLIENT
Todos
GET
/open-banking/invoice-financings/v
x
/contracts
/open-banking/invoice-financings/v
x
/contracts/{contractId}
/open-banking/invoice-financings/v
x
/contracts/{contractId}/warranties
/open-banking/invoice-financings/v
x
/contracts/{contractId}/payments
/open-banking/invoice-financings/v
x
/contracts/{contractId}/scheduled-instalments
v2
100
^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD33123
consentId
Empréstimos
O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.
Deve ser preenchido com a mesma string obtida no campo .data.consentId retornado após a chamada inicial na API "POST /consent”
string
CLIENT
Todos
GET
/open-banking/loans/v
x
/contracts
/open-banking/loans/v
x
/contracts/{contractId}
/open-banking/loans/v
x
/contracts/{contractId}/warranties
/open-banking/loans/v
x
/contracts/{contractId}/payments
/open-banking/loans/v
x
/contracts/{contractId}/scheduled-instalments
v2
100
^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD33123
consentId
Financiamentos
O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.
Deve ser preenchido com a mesma string obtida no campo .data.consentId retornado após a chamada inicial na API "POST /consent”
string
CLIENT
Todos
GET
/open-banking/financings/v
x
/contracts
/open-banking/financings/v
x
/contracts/{contractId}
/open-banking/financings/v
x
/contracts/{contractId}/warranties
/open-banking/financings/v
x
/contracts/{contractId}/payments
/open-banking/financings/v
x
/contracts/{contractId}/scheduled-instalments
v2
100
^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD33123
tokenId
Todos
Identificador único e criptograficamente seguro do token utilizado no consumo da API.
A implementação do tokenId preencherá a lacuna de rastreabilidade, permitindo vincular a emissão de cada token (incluindo os de CLIENT_CREDENTIALS) às suas respectivas jornadas, mesmo quando múltiplos consentimentos forem iniciados por um único token. Isso resultará em uma visão mais completa da jornada do token, aprimorando a capacidade de rastreabilidade e análise operacional para as instituições e do ecossistema
O tokenId será gerado pelo cliente (role CLIENT) no momento do reporte para a PCM, aplicado um hash SHA256 sobre o token recebido e um Pepper (segredo) gerenciado internamente pela instituição. Este tokenId deve ser reportado na PCM, complementando as informações já existentes de grant_type e consentId (onde aplicável). Para garantir a robustez criptográfica do hash, o Pepper utilizado deverá ser um valor aleatório e criptograficamente forte, gerenciado internamente pela instituição. Recomenda-se um tamanho de 128 a 256 bits para o Pepper, aplicado no cálculo do tokenId, como por exemplo, SHA256 (token + Pepper). O tokenId será composto pelos 72 bits iniciais do hash Base64URL-safe encoded.
Importante:
O tokenId será gerado apenas quando o token for recebido com sucesso na resposta do POST /token. Em casos nos quais a requisição ao POST /token resultar em erros 4xx ou 5xx, o token não será obtido e, consequentemente, o tokenId não poderá ser gerado. Nessas situações, o campo tokenId deve ser omitido do reporte à PCM.
string
CLIENT
Todos
Todos
Todos
v2
Dados de entrada
Token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' (JWT completo)
Pepper: '[valor secreto da instituição]'
Processo
Concatenar: token + pepper
Hash SHA256: da string concatenada
Truncar: primeiros 72 bits (9 bytes)
Codificar: Base64URL-safe
Resultado
{
"additionalInfo": {
"tokenId": "c9ng8aKzxNXm"
}
}

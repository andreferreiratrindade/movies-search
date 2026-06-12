---
                            title: "Regras de Obrigatoriedade (additionalInfo) - SG - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1212153857_Regras+de+Obrigatoriedade+additionalInfo+-+SG"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1212153857/Regras+de+Obrigatoriedade+additionalInfo+-+SG"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Regras de Obrigatoriedade (additionalInfo) - SG - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.02
Guia de leitura
Se o campo não está listado, é porque não existe a obrigatoriedade de enviá-lo.
Nos endpoints, a referência “v
x
” indica que se aplicam às versões listadas na coluna “Versões”. Por exemplo, Endpoint “open-banking/automatic-payments/v
x
/recurring-consents/{recurringConsentId}” e Versões “v1 v2” significa que o endpoint é válido para as versões 1 e 2.
Dica: para rolar a tabela horizontalmente, segure SHIFT e utilize o botão de rolagem do mouse.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Segurança
Campo
Grupo
Definição
Regra de preenchimento
Roles
Roles
Http code
Métodos
Domínio
Endpoints
Tamanho máximo
Padrão
Exemplo
Campo
Grupo
Definição
Regra de preenchimento
Roles
Roles
Http code
Métodos
Domínio
Endpoints
Tamanho máximo
Padrão
Exemplo
consentId
Token
O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.
Deve ser preenchido com a mesma string obtida no campo .data.consentId retornado após a chamada inicial na API "POST /consent”
*Ao reportar o uso de um endpoint /token, o identificador único de consentimento só será reportado nos casos em que "grant_type" é do tipo "authorization_code" ou do tipo "refresh_token"
string
CLIENT
Todos menos 4xx e 5xx
POST
/token
100
^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:[a-zA-Z0-9()+,-.:=@;$_!*''%/?#]+
urn:bancoex:C1DD33123
enrollmentId
Token
Identificador usado para registrar uma jornada ou um vínculo inicial
Deve ser preenchido com a mesma string obtida no campo .data.enrollmentId retornado após a chamada inicial na API "POST /enrollments". Ao reportar o uso de um endpoint /token, o identificador único de consentimento só será reportado nos casos em que "grant_type" é do tipo "authorization_code" ou do tipo "refresh_token"
string
CLIENT
Todos menos 4xx e 5xx
POST
/token
100
^urn:[a-zA-Z0-9][a-zA-Z0-9\-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD33123
grantType
Token
Informa o tipo de concessão (grant type) utilizado em uma solicitação
Deve ser preenchido com a mesma string enviada no campo ".grant_type "​
AUTHORIZATION_CODE:
Utilizado na autorização de acesso a um recurso por meio de login de usuário
REFRESH_TOKEN:
Utilizado para obter um novo token de acesso quando o token anterior expira
CLIENT_CREDENTIALS:
Utilizado na autorização de acesso entre aplicações onde não há a figura do usuário
string
CLIENT
Todos
POST
AUTHORIZATION_CODE, REFRESH_TOKEN, CLIENT_CREDENTIALS
/token
AUTHORIZATION_CODE
tokenId
Todos
Identificador único e criptograficamente seguro do token utilizado no consumo da API.
A implementação do tokenId preencherá a lacuna de rastreabilidade, permitindo vincular a emissão de cada token (incluindo os de CLIENT_CREDENTIALS) às suas respectivas jornadas, mesmo quando múltiplos consentimentos forem iniciados por um único token. Isso resultará em uma visão mais completa da jornada do token, aprimorando a capacidade de rastreabilidade e análise operacional para as instituições e do ecossistema
O tokenId será gerado pelo cliente (role CLIENT) no momento do reporte para a PCM, aplicado um hash SHA256 sobre o token recebido e um Pepper (segredo) gerenciado internamente pela instituição. Este tokenId deve ser reportado na PCM, complementando as informações já existentes de grant_type e consentId (onde aplicável). Para garantir a robustez criptográfica do hash, o Pepper utilizado deverá ser um valor aleatório e criptograficamente forte, gerenciado internamente pela instituição. Recomenda-se um tamanho de 128 a 256 bits para o Pepper, aplicado no cálculo do tokenId, como por exemplo, SHA256 (token + Pepper). O tokenId será composto pelos 72 bits iniciais do hash Base64URL-safe encoded.
Importante:
O tokenId será gerado apenas quando o token for recebido com sucesso na resposta do POST /token. Em casos nos quais a requisição ao POST /token resultar em erros 4xx ou 5xx, o token não será obtido e, consequentemente, o tokenId não poderá ser gerado. Nessas situações, o campo tokenId deve ser omitido do reporte à PCM.
string
CLIENT
200
POST
/token
/register
/register/{clientId}
Dados de entrada
*
Token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' (JWT completo)
* Pepper: '[valor secreto da instituição]'
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
webhookEnable
DCR/DCM
Indica se há URLs de webhook configuradas em uma requisição.
Deve ser preenchido com o valor booleano TRUE caso haja pelo menos um item indicado na lista do campo ".webhook_uris" no payload, caso contrário deverá ser preenchido com a string FALSE
string
CLIENT
Todos
PUT
TRUE, FALSE
/register/{clientId}
TRUE
webhookEnable
DCR/DCM
Indica se há URLs de webhook configuradas em uma requisição.
Deve ser preenchido com o valor booleano TRUE caso haja pelo menos um item indicado na lista do campo ".webhook_uris" no payload, caso contrário deverá ser preenchido com a string FALSE
string
CLIENT
Todos
POST
PUT
TRUE, FALSE
/register
TRUE

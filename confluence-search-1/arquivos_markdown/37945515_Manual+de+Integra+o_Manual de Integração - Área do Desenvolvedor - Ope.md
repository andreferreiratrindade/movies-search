---
                            title: "Manual de Integração - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "37945515_Manual+de+Integra+o"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/37945515/Manual+de+Integra+o"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Manual de Integração - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            O presente documento demonstra o uso das APIs da Plataforma de Coleta de Métricas.
Referências
Documentação da API
A documentação oficial da API se encontra em
Documentação da API - PCM
Documentação funcional
A documentação funcional pode ser encontrada em
Plataforma de Coleta de Métricas
Procedimento de integração
Visão geral
O diagrama abaixo ilustra os principais componentes da plataforma
Open
Para que reportes sejam enviados para a PCM é necessário que o participante obtenha um token de acesso, o que é feito através de um endpoint de autenticação que é acessível através de uma conexão mTLS. De posse do token, o participante pode efetuar os envios para os endpoints da API descritas na documentação. É necessário o uso de certificados válidos para a recuperação do token, em contrapartida os envios de reportes são feitos sem a necessidade de uma conexão mTLS.
Endereços base
Os endereços base em cada ambiente, bem como suas respectivas datas de validade são os abaixo:
Ambiente
Endereço
Tipo
Validade
Ambiente
Endereço
Tipo
Validade
Sandbox
https://api.pcm.sandbox.openfinancebrasil.org.br
API
Indeterminada
https://auth.pcm.sandbox.openfinancebrasil.org.br
Autenticação
Piloto
https://api.pcm.piloto.openfinancebrasil.org.br
API
Disponível até 31/01/2023
https://auth.pcm.piloto.openfinancebrasil.org.br
Autenticação
Produção
https://api.pcm.openfinancebrasil.org.br
API
Disponível a partir de 01/02/2023
https://auth.pcm.openfinancebrasil.org.br
Autenticação
Autenticação
O procedimento segue o fluxo de
client_credentials
da especificação oauth2, sendo que o acesso ao endpoint precisa ser feito usando uma conexão mTLS. As credenciais, bem como os certificados aceitos em cada um dos ambientes estão descritos abaixo:
Ambiente
Credenciais
Certificados
Ambiente
Credenciais
Certificados
Sandbox/Piloto
client_id do Software Statement do diretório de sandbox
Certificado emitido pelo diretório central de sandbox
Produção
client_id do Software Statement do diretório de produção
Certificado emitido por autoridade certificadora aceita pelo ecossistema
[1]
O endpoint de recuperação de token é:
<endereço de autenticação conforme ambiente>/token/
Importante
: manter a última barra ("/") depois de
token
.
Para se recuperar um token, é necessário estabelecer uma comunicação mTLS entre o cliente que está fazendo a chamada e o authorization server, utilizando um certificado de cliente. Os passos para configuração de certificados cliente no Postman podem ser encontrados em
Add and manage CA and client certificates in Postman | Postman Docs
.
Os tokens gerados estão configurados com duração de 21600 segundos (6 horas). Não há limitação para a quantidade de tokens gerados muito embora seja importante que eles sejam reaproveitados no período de validade. É possível fazer a introspecção do token para se determinar até quando ele é válido, uma vez que ele não é criptografado.
Para recuperar um token é necessário fazer uma chamada POST usando um payload com os seguintes campos:
client_id
client_id
do software statement ligado ao certificado usado no acesso
grant_type
Fixo:
client_credentials
Não há a necessidade do envio do
client_secret
, uma vez que a camada de transporte via certificado cliente já assegura a autenticidade do chamador.
Os campos relevantes devolvidos por esse endpoint são:
access_token
Token no padrão jwt para acesso às APIs
expires_in
Número de segundos em que o token é válido
token_type
O tipo do token fornecido (nesse caso, Bearer)
Exemplo
Envio de um request para o endereço de autenticação em sandbox:
POST https://auth.pcm.sandbox.openfinancebrasil.org.br/token/
Content-Type: application/json
{
"client_id": "1234",
"grant_type": "client_credentials"
}
Resposta:
200 Ok
{
"access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFiT",
"expires_in": 21600,
"token_type": "Bearer"
}
Alternativamente, é possível utilizar o fluxo fresh, ficando a cargo das instituições o comportamento mais adequado a cada situação.
<endereço de autenticação conforme ambiente>/token-fresh/
O fluxo fresh sempre gera um token novo, ignorando qualquer token em cache para leitura. Após a leitura, salva esse token em cache.
O comportamento desse endpoint é:
Ao chamar o endpoint fresh, o sistema
não reutiliza
token de cache existente.
O sistema chama o provedor de autenticação e obtém
um token novo
.
Em seguida, esse token novo
também é gravado no cache
.
Depois disso, uma chamada ao endpoint
/token
pode retornar esse token recém-gerado, desde que ele ainda esteja válido.
Em resumo:
fresh ignora cache na entrada, mas alimenta cache na saída
.
Para a maioria das requisições, o uso de
token em cache continua sendo o comportamento padrão
, trazendo:
menor latência
menos chamadas externas
melhor escalabilidade do sistema
Isso mantém o sistema
rápido e eficiente para uso cotidiano
.
Cenário
Endpoint recomendado
Cenário
Endpoint recomendado
Uso geral
/token
Garantir token novo na chamada atual
/token-fresh
Reutilizar token válido para performance
/token
Interação com a API
Para realizar chamadas localmente, realize a importação da documentação OpenAPI no seu cliente HTTP (Postman:
Integrate Postman with OpenAPI | Postman Docs
, Insomnia:
How to: Import an API specification as a design document in Insomnia | Kong Docs
). Esse procedimento irá criar as collections nos formatos descritos pela documentação.
O token gerado deverá ser enviado nas chamadas da API do PCM dentro do header Authorization, identificando o tipo do token conforme abaixo:
Authorization: <token type> <token>
Onde
<token type>
pode ser Bearer, Basic, etc (no caso das APIs da PCM, será aceito apenas tokens do tipo Bearer), e o token recuperado no processo de autenticação.
Usando o exemplo da chamada da sessão anterior, o header deverá ser mandado com o seguinte conteúdo:
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFiT
Exemplo
Para o envio de um reporte como server, o request tem que ser como o exemplo abaixo:
POST https://api.pcm.sandbox.openfinancebrasil.org.br/report-api/v1/private/report
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFiT
[
{
"timestamp": "2022-08-31T17:43:13.622Z",
"fapiInteractionId": "e67824fa-6b4d-448c-8101-304407259552",
"endpoint": "/open-banking/customers/v2/personal/financial-relations",
"statusCode": 200,
"httpMethod": "GET",
"processTimespan": 120,
"clientOrgId": "c160a6f5-e5df-5067-9e97-ec6fba62fd87",
"serverOrgId": "2a01e202-e8f0-5f5a-9651-ebc257371e6e",
}
]
Resposta
200 Ok
Content-Type: application/json
{
"reportId": "9737cc7f-9854-4f57-aec6-7f1778c642d4",
"status": "ACCEPTED"
}
Exemplos de chamadas
Os exemplos abaixo utilizam as instituições que participaram do Piloto da PCM. São elas (em ordem alfabética): Banrisul, BV, Caixa e Gerencianet.
Os cenários de teste foram montados a fim de demonstrar o uso da API. A escolha de qual instituição faz qual chamada foi aleatória, e tem o único objetivo de exemplificar os tipos de chamadas em seus cenários.
Cenário 1: PAIRED
BV faz chamada para Caixa, ambos enviam reportes sem erros. O status esperado para os dois reportes finais é
PAIRED
.
BV:
{
“role”: “CLIENT”,
"timestamp": "2022-08-31T17:43:13.622Z",
"fapiInteractionId": "cd9a2e6b-0c33-403b-a8dd-544e95c63cd8",
"endpoint": "/open-banking/unarranged-accounts-overdraft/v1/contracts/{contractId}/scheduled-instalments",
“additionalInfo”: {
“consentId”: “uri:bv:6096c7f6-53a0-4c53-bc95-9c8d48b9a6cf“,
“personType”: “PF“
}
"statusCode": 200,
"httpMethod": "GET",
"clientOrgId": "062c5edb-4e83-5002-9981-e2a96c5ad41e",
"serverOrgId": "c160a6f5-e5df-5067-9e97-ec6fba62fd87",
"processTimespan": 120,
"clientSSId": "clientSSId",
"endpointUriPrefix": "https://openbanking.instituicao.com.br/namespace"
}
Caixa:
{
“role”: “SERVER”,
"timestamp": "2022-08-31T17:44:42.812Z",
"fapiInteractionId": "cd9a2e6b-0c33-403b-a8dd-544e95c63cd8",
"endpoint": "/open-banking/unarranged-accounts-overdraft/v1/contracts/{contractId}/scheduled-instalments",
"statusCode": 200,
"httpMethod": "GET",
"clientOrgId": "062c5edb-4e83-5002-9981-e2a96c5ad41e",
"serverOrgId": "c160a6f5-e5df-5067-9e97-ec6fba62fd87",
"processTimespan": 90
}
Cenário 2: PAIRED_INCONSISTENT
Caixa reporta transação feita com Banrisul, mas os dados de consistência não estão iguais. O status esperado para os dois reportes finais é
PAIRED_INCONSISTENT.
Caixa:
{
“role”: “CLIENT”,
"timestamp": "2022-08-31T17:43:13.622Z",
"fapiInteractionId": "cd9a2e6b-0c33-403b-a8dd-544e95c63cd8",
"endpoint": "/open-banking/unarranged-accounts-overdraft/v1/contracts/{contractId}/scheduled-instalments",
“additionalInfo”: {
“consentId”: “uri:caixa:6096c7f6-53a0-4c53-bc95-9c8d48b9a6cf“
}
"statusCode": 200,
"httpMethod": "GET",
"clientOrgId": "c160a6f5-e5df-5067-9e97-ec6fba62fd87",
"serverOrgId": "2a01e202-e8f0-5f5a-9651-ebc257371e6e",
"processTimespan": 120,
"clientSSId": "clientSSId",
"endpointUriPrefix": "https://openbanking.instituicao.com.br/namespace"
}
Banrisul:
{
“role”: “SERVER”,
"timestamp": "2022-08-31T17:44:42.812Z",
"fapiInteractionId": "cd9a2e6b-0c33-403b-a8dd-544e95c63cd8",
"endpoint": "/open-banking/unarranged-accounts-overdraft/v1/contracts/{contractId}/scheduled-instalments",
"statusCode": 201,
"httpMethod": "GET",
"clientOrgId": "c160a6f5-e5df-5067-9e97-ec6fba62fd87",
"serverOrgId": "2a01e202-e8f0-5f5a-9651-ebc257371e6e",
"processTimespan": 90
}
Cenário 3: SINGLE
Banrisul reporta timeout em uma transação com BV, sendo que a geração do fapiInteractionId seria feita pelo server. O status desse reporte será
SINGLE
.
{
“role”: “CLIENT”,
"timestamp": "2022-08-31T17:43:13.622Z",
"fapiInteractionId": "cd9a2e6b-0c33-403b-a8dd-544e95c63cd8",
"endpoint": "/open-banking/unarranged-accounts-overdraft/v1/contracts/{contractId}/scheduled-instalments",
“additionalInfo”: {
“consentId”: “uri:banrisul:6096c7f6-53a0-4c53-bc95-9c8d48b9a6cf“,
“personType”: “PF“
}
"statusCode": 408,
"httpMethod": "GET",
"clientOrgId": "2a01e202-e8f0-5f5a-9651-ebc257371e6e",
"serverOrgId": "062c5edb-4e83-5002-9981-e2a96c5ad41e",
"processTimespan": 120,
"clientSSId": "clientSSId",
"endpointUriPrefix": "https://openbanking.instituicao.com.br/namespace"
}
Cenário 4: DISCARDED
Gerencianet envia um reporte sem o campo httpMethod, que é um campo obrigatório. O status do reporte será registrado como DISCARDED, e o status retorno da chamada será 400.
{
“role”: “CLIENT”,
"timestamp": "2022-08-31T17:43:13.622Z",
"fapiInteractionId": "cd9a2e6b-0c33-403b-a8dd-544e95c63cd8",
"endpoint": "/open-banking/unarranged-accounts-overdraft/v1/contracts/{contractId}/scheduled-instalments",
“additionalInfo”: {
“consentId”: “uri:gerencianet:6096c7f6-53a0-4c53-bc95-9c8d48b9a6cf“,
“personType”: “PF“
}
"statusCode": 200,
"httpMethod": "GET",
"clientOrgId": "b43131be-6a7f-5bfb-b436-c3ac5c5c2dac",
"serverOrgId": "062c5edb-4e83-5002-9981-e2a96c5ad41e",
"processTimespan": 120,
"clientSSId": "clientSSId",
"endpointUriPrefix": "https://openbanking.instituicao.com.br/namespace"
}
Resposta
400 BadRequest
Content-Type: application/json
{
"reportId": "9737cc7f-9854-4f57-aec6-7f1778c642d4",
"status": "DISCARDED",
"message": "Missing fields: httpMethod
}
Cenário 5: DISCARDED
Caixa envia reporte com dado inconsistente no campo endpoint (veja lista dos endpoints válidos na
Documentação da API - PCM
e na
documentação funcional
). Status do reporte tem que ser DISCARDED com a devida justificativa, e o status da resposta 400.
{
“role”: “CLIENT”,
"timestamp": "2022-08-31T17:43:13.622Z",
"fapiInteractionId": "cd9a2e6b-0c33-403b-a8dd-544e95c63cd8",
"endpoint": "/invalid_endpoint",
“additionalInfo”: {
“consentId”: “uri:caixa:6096c7f6-53a0-4c53-bc95-9c8d48b9a6cf“,
“personType”: “PF“
}
"statusCode": 200,
"httpMethod": "GET",
"clientOrgId": "c160a6f5-e5df-5067-9e97-ec6fba62fd87",
"serverOrgId": "062c5edb-4e83-5002-9981-e2a96c5ad41e",
"processTimespan": 120,
"clientSSId": "clientSSId",
"endpointUriPrefix": "https://openbanking.instituicao.com.br/namespace"
}
Resposta
400 BadRequest
Content-Type: application/json
{
"reportId": "9737cc7f-9854-4f57-aec6-7f1778c642d4",
"status": "DISCARDED",
"message": "Unlisted endpoint: /invalid_enpoint
}
Cenário 6: DISCARDED
Banrisul envia reporte sem os identificadores de receptor e transmissor. Status do reporte deverá ser DISCARDED com a devida justificativa e o status de retorno, 400. No entanto, apenas o Banrisul poderá consultar esse reporte.
{
“role”: “CLIENT”,
"timestamp": "2022-08-31T17:43:13.622Z",
"fapiInteractionId": "cd9a2e6b-0c33-403b-a8dd-544e95c63cd8",
"endpoint": "/invalid_endpoint",
“additionalInfo”: {
“consentId”: “uri:banrisul:6096c7f6-53a0-4c53-bc95-9c8d48b9a6cf“,
“personType”: “PF“
}
"statusCode": 200,
"httpMethod": "GET",
"processTimespan": 120,
"clientSSId": "clientSSId",
"endpointUriPrefix": "https://openbanking.instituicao.com.br/namespace"
}
[1]
Padrão de certificação do Open Finance Brasil v2.1

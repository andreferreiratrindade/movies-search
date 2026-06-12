---
                            title: "Campos Obrigatórios e Opcionais - SG - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1798537221_Campos+Obrigat+rios+e+Opcionais+-+SG"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1798537221/Campos+Obrigat+rios+e+Opcionais+-+SG"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Campos Obrigatórios e Opcionais - SG - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.00
Dica: para rolar a tabela horizontalmente, segure SHIFT e utilize o botão de rolagem do mouse.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Private API
Campos que devem ser informados à PCM via POST
Campo
Definição
Obrigatório
Tipo
Regra de preenchimento
Roles
Domínio
Tamanho máximo
Valor mínimo
Valor máximo
Padrão
Exemplo
Campo
Definição
Obrigatório
Tipo
Regra de preenchimento
Roles
Domínio
Tamanho máximo
Valor mínimo
Valor máximo
Padrão
Exemplo
additionalInfo
Informações adicionais sobre o reporte deste endpoint/método. Possui característica variável. As regras de preenchimento estão na documentação funcional em
Regras de Obrigatoriedade (additionalInfo) - SG
Sim
object
Caso não exista o campo enviar como um objeto vazio: {}
CLIENT
clientOrgId
Identificador da organização de onde a chamada foi disparada
Sim
string <uuid>
CLIENT
36
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
56411f7e-d58b-44a8-8a2b-ff326d3f2955
clientSSId
Identificador do software statement de onde a chamada foi disparada. A PCM garante que foi esta orgId que obteve o token de acesso utilizado neste reporte.
Sim
string <uuid>
CLIENT
36
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
84570da9-567b-4201-9b77-c715bc5bffde
correlationId
ID de correlação que identifica uma sequência de chamadas inter-relacionadas no ecossistema. Diferente do fapiInteractionId que serve para identificar cada par request-response (interação), o identificador de correlação serve para ligar diferentes reportes quando estes representam uma jornada ou uma sequência de chamadas. Este valor é de livre provimento pelo reportador.
Não
string
CLIENT
100
^[- /:_.',0-9a-zA-Z]{0,100}$
uGQHwNupARo7I9E2PLJZph18a0M9y7DcUe7ITt3DqUOJd9NVjnskxf2
endpoint
Identificação do endpoint que foi utilizado na transação reportada. A identificação do endpoint deve estar presente na lista de endpoints aceitos pela PCM para ser considerado válido. Nesse campo não deve ser utilizado o path da requisição original, uma vez que ao comparar com os valores dessa enum, ele não será considerado válido.
Sim
string <uri>
Não usar o caminho real: é fundamental NÃO utilizar o caminho completo da requisição original, que inclui dados variáveis (ex: IDs).
Exemplo: Se a requisição foi para /open-banking/credit-cards-accounts/v1/accounts/123456789/transactions, o valor a ser enviado no endpoint deve ser /open-banking/credit-cards-accounts/v1/accounts/{creditCardAccountId}/transactions. O dado real 123456789 não deve ser enviado no campo endpoint.
CLIENT
Endpoints aceitos pela PCM
/open-banking/consents/v2/consents
endpointUriPrefix
Endereço do servidor de destino da chamada, incluindo o prefixo quando houver. O formato do campo deverá ser o seguinte:
https://{host}/{prefixo}, sendo:
host: endereço FQDN do servidor de destino
prefixo: toda a parte do path que vem antes da string /open-banking
Sim
string
Exemplos:
Para uma requisição em
https://openbanking.instituicao-1.com.br/opbk/open-banking/products-services/v1/business-accounts
, o dado a ser enviado é
https://openbanking.instituicao-1.com.br/opbk
.
Para uma requisição em
https://openbanking.instituicao-2.com.br/open-banking/products-services/v1/business-accounts
, o dado a ser enviado é
https://openbanking.instituicao-1.com.br/
.
Nos reportes relativos aos endpoints /token e /register este campo deverá conter a URL inteira do request.
Exemplos:
https://oauth2.cartaodummy.opf.instituicao/as/token.oauth2
https://instituicao.com.br/orgs/instituicao/reg
CLIENT
200
^[- /:_.',0-9a-zA-Z]{0,200}$
https://openbanking.instituicao-1.com.br/opbk
fapiInteractionId
UUID RFC4122 que identifica uma transação específica entre dois participantes no ecossistema Open Finance. Este identificador é derivado do header HTTP x-fapi-interaction-id, conforme especificação RFC4122 para geração de identificadores únicos universais. Serve como chave de correlação fundamental para rastreabilidade, auditoria e conciliação de transações entre instituições participantes. Mais informações em Cabeçalhos HTTP na documentação de produtos do Open Finance Brasil
Não
string <uuid>
CLIENT
36
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
d78fc4e5-37ca-4da3-adf2-9b082bf92280
httpMethod
Método HTTP da solicitação.
Sim
enum<string>
CLIENT
DELETE, GET, PATCH, POST, PUT
GET
processTimespan
Tempo em milissegundos inteiros decorrido desde o registro do timestamp até a chegada do primeiro byte da resposta do server.
Sim
integer <int16>
CLIENT
120.000000
role
Indica se o reporte que está sendo enviado apresenta a visão do server ou do client.
Sim
enum<string>
CLIENT
CLIENT, SERVER
CLIENT
serverOrgId
Identificador da organização para onde a chamada foi feita
Sim
string <uuid>
CLIENT
36
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
c1ca8e62-9d6f-4ea3-84f2-d66bc0a8f7dc
statusCode
Status de retorno HTTP da solicitação.
Sim
integer <int32>
No contexto operacional do Open Finance, de acordo com a definição de governança, a instituição consumidora (Client) deve aguardar até 15 segundos pela resposta da instituição provedora (Server).
Caso esse período seja atingido ou excedido (≥ 15 segundos) sem resposta, a instituição consumidora pode, por decisão própria e para preservar a experiência do usuário, encerrar a conexão. Nessa situação, o evento deve ser reportado com status code 408, caracterizando timeout na interação, ainda que a interrupção tenha sido iniciada pelo lado consumidor.
Por sua vez, quando a instituição estiver atuando como provedora (Server) e encerrar a conexão por não ter recebido a requisição completa dentro do tempo esperado, também deverá reportar status code 408, em conformidade com a RFC 7231.
CLIENT
200
599
200
timestamp
Data/Hora UTC no formato ISO8601 com milissegundos (YYYY-MM-DDTHH:mm:ss.sssZ) do momento em que a chamada foi disparada, imediatamente antes do primeiro byte enviado na requisição.
Sim
string <date-time>
CLIENT
28
^\d{4}-\d{2}-\d{2}T(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d(?:\.\d+)?(?:Z|[+-][01]\d:[0-5]\d)$
2021-11-11T18:08:08.278Z
Campos retornados em response
Campo
Definição
Tipo
Domínio
Tamanho máximo
Padrão
Exemplo
Campo
Definição
Tipo
Domínio
Tamanho máximo
Padrão
Exemplo
reportId
Identificador único interno do reporte no formato UUID v4.
string <uuid>
36
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
9a97c2df-b261-4fc2-aa66-d1b5168397da
status
Informa o status do registro de reporte.
ACCEPTED
: O status ACCEPTED indica que a validação de formato do reporte não tem erros e este será enviado para processamento.
DISCARDED
: O status DISCARDED indica que o reporte enviado pelo participante foi rejeitado pela PCM. O motivo do descarte será enviado com a resposta, podendo ser por conta de um reporte inválido ou por um erro no processamento. Não é possível modificar um reporte DISCARDED, portanto o reportador deverá corrigir o registro que apresentou erro e reenviar via POST.
SINGLE
: O status SINGLE indica que o reporte em questão não tem uma contraparte. Ele é utilizado em casos onde a conciliação entre dois reportes não é possível.
enum<string>
ACCEPTED, DISCARDED, SINGLE
SINGLE
Campos adicionais retornados no GET
O GET retorna todos os campos do POST e do response, além dos adicionais abaixo
Campo
Definição
Tipo
Tamanho máximo
Exemplo
Campo
Definição
Tipo
Tamanho máximo
Exemplo
createdAt
Carimbo do tempo do momento da criação do registro
string <date-time>
28
2026-01-14 13:08:25.319000 UTC
updatedAt
Carimbo do tempo do momento da última atualização do registro
string <date-time>
28
2026-01-14 15:53:50.978000 UTC

---
                            title: "Campos Obrigatórios e Opcionais - DA - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1211334657_Campos+Obrigat+rios+e+Opcionais+-+DA"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1211334657/Campos+Obrigat+rios+e+Opcionais+-+DA"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Campos Obrigatórios e Opcionais - DA - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.01
Dica: para rolar a tabela horizontalmente, segure SHIFT e utilize o botão de rolagem do mouse.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Opendata API
Campos que devem ser informados à PCM via POST
Campo
Definição
Obrigatório
Tipo
Regra de Preenchimento
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
Regra de Preenchimento
Domínio
Tamanho máximo
Valor mínimo
Valor máximo
Padrão
Exemplo
additionalInfo
Informações adicionais sobre o reporte deste endpoint/método. Possui característica variável. As regras de preenchimento estão na documentação funcional em
Regras de Obrigatoriedade (additionalInfo) - DA
Caso não exista o campo enviar como um objeto vazio: {}
Sim
object
endpoint
Identificação do endpoint que foi utilizado na transação reportada. A identificação do endpoint deve estar presente na lista de endpoints aceitos pela PCM para ser considerado válido. Nesse campo não deve ser utilizado o path da requisição original.
Sim
string
Identificação do Endpoint: Deve ser preenchido com o identificador padronizado do endpoint, conforme uma lista (ENUM) predefinida.
Não usar o caminho real: É fundamental NÃO utilizar o caminho completo da   requisição original, que inclui dados variáveis (ex: IDs).
Exemplo: Se a requisição foi para /open-banking/credit-cards-accounts/v1/accounts/123456789/transactions, o valor a ser enviado no endpoint deve ser /open-banking/credit-cards-accounts/v1/accounts/{creditCardAccountId}/transactions. O dado real 123456789 não deve ser enviado no campo endpoint
Endpoints aceitos pela PCM
/open-banking/opendata-acquiring-services/v1/businesses
httpMethod
Método HTTP da solicitação.
Sim
string
DELETE, GET, PATCH, POST, PUT
GET
processTimespan
Tempo em milissegundos inteiros decorrido desde o registro do timestamp até a chegada do primeiro byte da resposta do server.
Sim
integer <int16>
120.000000
statusCode
Status de retorno HTTP da solicitação.
Sim
integer <int32>
No contexto operacional do Open Finance, de acordo com a definição de governança, a instituição consumidora (Client) deve aguardar até 15 segundos pela resposta da instituição provedora (Server).
Caso esse período seja atingido ou excedido (≥ 15 segundos) sem resposta, a instituição consumidora pode, por decisão própria e para preservar a experiência do usuário, encerrar a conexão. Nessa situação, o evento deve ser reportado com status code 408, caracterizando timeout na interação, ainda que a interrupção tenha sido iniciada pelo lado consumidor.
Por sua vez, quando a instituição estiver atuando como provedora (Server) e encerrar a conexão por não ter recebido a requisição completa dentro do tempo esperado, também deverá reportar status code 408, em conformidade com a RFC 7231.
200
599
200
timestamp
Data/Hora UTC no formato ISO8601 com milissegundos (YYYY-MM-DDTHH:mm:ss.sssZ) do momento em que a chamada foi disparada, imediatamente antes do primeiro byte enviado na requisição.
Sim
string <date-time>
28
^\d{4}-\d{2}-\d{2}T(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d(?:\.\d+)?(?:Z|[+-][01]\d:[0-5]\d)$
2021-11-11T18:08:08.278Z
Campos retornados em response
Campo
Definição
Obrigatório
Tipo
Domínio
Tamanho máximo
Padrão
Exemplo
Campo
Definição
Obrigatório
Tipo
Domínio
Tamanho máximo
Padrão
Exemplo
correlationId
Retorna o valor do atributo correlationId informado na solicitação de inclusão de reporte sem alteração.
Sim
string
100
^[- /:_.',0-9a-zA-Z]{0,100}$
uGQHwNupARo7I9E2PLJZph18a0M9y7DcUe7ITt3DqUOJd9NVjnskxf2
reportId
Identificador único interno do reporte no formato UUID v4.
Sim
string <uuid>
36
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
9a97c2df-b261-4fc2-aa66-d1b5168397da
status
Informa o status do registro de reporte.
ACCEPTED:
O status ACCEPTED indica que a validação de formato do reporte não tem erros e este será enviado para processamento.
DISCARDED:
O status DISCARDED indica que o reporte enviado pelo participante foi rejeitado pela PCM. O motivo do descarte será enviado com a resposta, podendo ser por conta de um reporte inválido ou por um erro no processamento. Não é possível modificar um reporte DISCARDED, portanto o reportador deverá corrigir o registro que apresentou erro e reenviar via POST.
Sim
enum <string>
ACCEPTED, DISCARDED
ACCEPTED

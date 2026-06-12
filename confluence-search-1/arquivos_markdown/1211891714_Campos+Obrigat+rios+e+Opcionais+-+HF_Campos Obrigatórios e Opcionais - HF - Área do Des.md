---
                            title: "Campos Obrigatórios e Opcionais - HF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1211891714_Campos+Obrigat+rios+e+Opcionais+-+HF"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1211891714/Campos+Obrigat+rios+e+Opcionais+-+HF"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Campos Obrigatórios e Opcionais - HF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.01
Dica: para rolar a tabela horizontalmente, segure SHIFT e utilize o botão de rolagem do mouse.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Hybridflow API
Campos que devem ser informados à PCM via POST
Campo
Definição
Obrigatório
Tipo
Roles
Domínio
Endpoints
Versões
Tamanho máximo
Valor mínimo
Valor máximo
Padrão
Exemplo
Campo
Definição
Obrigatório
Tipo
Roles
Domínio
Endpoints
Versões
Tamanho máximo
Valor mínimo
Valor máximo
Padrão
Exemplo
clientOrgId
A ser enviado vazio caso o report seja da mesma instituição que obteve o token para uso da PCM e, caso contrário, deve ser preenchido com o organisationId da instituição filha para o qual a instituição mãe está fazendo o report.
Sim
string <uuid>
CLIENT
/report-api/v
x
/hybrid-flow/client/redirect-to-server
/report-api/v
x
/hybrid-flow/client/redirect-target-with-errors
/report-api/v
x
/hybrid-flow/client/redirect-target-without-errors
v2
36
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
56411f7e-d58b-44a8-8a2b-ff326d3f2955
consentId
O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.
Sim
string
CLIENT
SERVER
/report-api/v
x
/hybrid-flow/client/redirect-to-server
/report-api/v
x
/hybrid-flow/client/redirect-target-with-errors
/report-api/v
x
/hybrid-flow/client/redirect-target-without-errors
/report-api/v
x
/hybrid-flow/server/redirect-target
/report-api/v
x
/hybrid-flow/server/authenticated
/report-api/v
x
/hybrid-flow/server/redirect-to-client
v2
256
^urn:[a-zA-Z0-9][a-zA-Z0-9\-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*''%\/?#]+$
urn:bancoex:C1DD33123
error
Código de erro retornado no payload do Hybrid Flow
Sim
string
CLIENT
/report-api/v
x
/hybrid-flow/client/redirect-target-with-errors
v2
access_denied
os
Sistema Operacional utilizado
Sim
enum<string>
CLIENT
SERVER
ANDROID, IOS, LINUX, MACOS, OTHER, UNIX, WINDOWS
/report-api/v
x
/hybrid-flow/client/redirect-to-server
/report-api/v
x
/hybrid-flow/client/redirect-target-with-errors
/report-api/v
x
/hybrid-flow/client/redirect-target-without-errors
/report-api/v
x
/hybrid-flow/server/redirect-target
/report-api/v
x
/hybrid-flow/server/authenticated
/report-api/v
x
/hybrid-flow/server/redirect-to-client
v2
LINUX
osVersion
Versão do Sistema Operacional utilizado
Sim
string
CLIENT
SERVER
/report-api/v
x
/hybrid-flow/client/redirect-to-server
/report-api/v
x
/hybrid-flow/client/redirect-target-with-errors
/report-api/v
x
/hybrid-flow/client/redirect-target-without-errors
/report-api/v
x
/hybrid-flow/server/redirect-target
/report-api/v
x
/hybrid-flow/server/authenticated
/report-api/v
x
/hybrid-flow/server/redirect-to-client
v2
20.04
platform
Identifica a plataforma utilizada
Sim
enum<string>
CLIENT
APP, BROWSER
/report-api/v
x
/hybrid-flow/client/redirect-to-server
/report-api/v
x
/hybrid-flow/client/redirect-target-with-errors
/report-api/v
x
/hybrid-flow/client/redirect-target-without-errors
/report-api/v
x
/hybrid-flow/server/authenticated
/report-api/v
x
/hybrid-flow/server/redirect-to-client
v2
BROWSER
serverOrgId
A ser enviado vazio caso o report seja da mesma instituição que obteve o token para uso da PCM e, caso contrário, deve ser preenchido com o organasationId da instituição filha para o qual a instituição mãe está fazendo o report
Sim
string <uuid>
SERVER
/report-api/v
x
/hybrid-flow/server/redirect-target
/report-api/v
x
/hybrid-flow/server/authenticated
/report-api/v
x
/hybrid-flow/server/redirect-to-client
v2
36
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
c1ca8e62-9d6f-4ea3-84f2-d66bc0a8f7dc
timestamp
Data/Hora UTC no formato ISO8601 com milissegundos (YYYY-MM-DDTHH:mm:ss.sssZ) do momento em que a chamada foi disparada, imediatamente antes do primeiro byte enviado na requisição.
Sim
string <date-time>
CLIENT
SERVER
/report-api/v
x
/hybrid-flow/client/redirect-to-server
/report-api/v
x
/hybrid-flow/client/redirect-target-with-errors
/report-api/v
x
/hybrid-flow/client/redirect-target-without-errors
/report-api/v
x
/hybrid-flow/server/redirect-target
/report-api/v
x
/hybrid-flow/server/authenticated
/report-api/v
x
/hybrid-flow/server/redirect-to-client
v2
28
^\d{4}-\d{2}-\d{2}T(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d(?:\.\d+)?(?:Z|[+-][01]\d:[0-5]\d)$
2021-11-11T18:08:08.278Z
type
Tipo do fluxo de Hybridflow
Sim
enum<string>
SERVER
AWAITING_HANDOFF, AWAITING_USER_AUTH, AWAITING_REDIRECT_TO_APP
/report-api/v
x
/hybrid-flow/server/redirect-target
v2
AWAITING_REDIRECT_TO_APP
type
Tipo do fluxo de Hybridflow
Sim
enum<string>
SERVER
AUTHORISED, REJECTED
/report-api/v
x
/hybrid-flow/server/redirect-to-client
v2
AUTHORISED
uri_callback
URI específico fornecido como endpoint de retorno de chamada. Preencher com a uri_callback registrada pelo sistema consumidor durante o DCR/DCM. Caso a URI tenha mais de 200 caracteres de extensão, truncar.
Sim
string <uri>
SERVER
/report-api/v
x
/hybrid-flow/server/redirect-to-client
v2
200
^[- /:_.',0-9a-zA-Z]{0,200}$
https://receptora.com.br/open-banking/landing-page
uriAuthorizationEndpoint
Endpoint utilizado para o redirecionamento do usuário conforme cadastrado pela transmissora/detentora no arquivo .well-known/openid-configuration sem qualquer parâmetro introduzido pelo sistema da receptora/iniciadora. Caso a URI tenha mais de 200 caracteres de extensão, truncar.
Não
string
CLIENT
SERVER
/report-api/v
x
/hybrid-flow/client/redirect-to-server
/report-api/v
x
/hybrid-flow/server/redirect-target
v2
200
^[- /:_.',0-9a-zA-Z]{0,200}$
https://auth.banco.com.br/open-banking/Auth
Campos retornados em response
Campo
Definição
Tipo
Domínio
Padrão
Exemplo
Campo
Definição
Tipo
Domínio
Padrão
Exemplo
correlationId
Retorna o valor do atributo
correlationId
informado na solicitação de inclusão de reporte sem alteração.
string
^[- /:_.',0-9a-zA-Z]{0,100}$
uGQHwNupARo7I9E2PLJZph18a0M9y7DcUe7ITt3DqUOJd9NVjnskxf2
reportId
Identificador único interno do reporte no formato UUID v4.
string <uuid>
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
uGQHwNupARo7I9E2PLJZph18a0M9y7DcUe7ITt3DqUOJd9NVjnskxf2
status
Informa o status do registro de reporte.
ACCEPTED:
O status ACCEPTED indica que a validação de formato do reporte não tem erros e este será enviado para processamento.
DISCARDED:
O status DISCARDED indica que o reporte enviado pelo participante foi rejeitado pela PCM. O motivo do descarte será enviado com a resposta, podendo ser por conta de um reporte inválido ou por um erro no processamento. Não é possível modificar um reporte DISCARDED, portanto o reportador deverá corrigir o registro que apresentou erro e reenviar via POST.
enum <string>
ACCEPTED, DISCARDED
ACCEPTED

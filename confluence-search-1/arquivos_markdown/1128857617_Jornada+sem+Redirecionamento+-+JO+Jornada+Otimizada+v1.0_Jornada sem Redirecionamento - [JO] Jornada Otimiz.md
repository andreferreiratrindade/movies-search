---
                            title: "Jornada sem Redirecionamento - [JO] Jornada Otimizada v1.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1128857617_Jornada+sem+Redirecionamento+-+JO+Jornada+Otimizada+v1.0"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1128857617/Jornada+sem+Redirecionamento+-+JO+Jornada+Otimizada+v1.0"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Jornada sem Redirecionamento - [JO] Jornada Otimizada v1.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            A
Jornada Otimizada de Jornada Sem Redirecionamento com Consentimento de Dados para Saldo e Limites
simplifica a experiência do cliente ao integrar, em um único fluxo, a autorização para o compartilhamento de dados (saldo e/ou limites) e a execução do serviço de jornada sem redirecionamento.
O consentimento de dados é utilizado exclusivamente para compartilhar informações essenciais da conta, permitindo que o iniciador compreenda a situação financeira do cliente e otimize a execução das transferências de forma mais eficiente, segura e alinhada ao serviço prestado.
Esta página descreve em detalhes as regras particulares dessa jornada, servindo como guia para a implementação do fluxo específico de
Jornada Sem Redirecionamento com Consentimento de Dados para Saldo e Limites
.
Fluxo Base
Open
O
Software Cliente (client)
gera um
access_token
utilizando o
grant_type=client_credentials
para possibilitar a criação dos consentimentos primário e secundário.
O client cria um
consentimento secundário de dados
, solicitando permissões referentes aos agrupamentos de saldo e/ou limites. Esse consentimento deve ser criado o parâmetro
isLinked
com o valor
true
, indicando que faz parte de uma Jornada Otimizada.
O client cria um
consentimento primário de Vínculo de Dispositivo (JSR)
, vinculando-o ao consentimento de dados. O objeto
journey
deve ter
isLinked=true
e
linkId=<consentId do consentimento de dados>
.
O client chama o
endpoint PAR
, informando os escopos de ambos os consentimentos, e redireciona o usuário para autenticação e autorização. O Authorization Server identifica a jornada como otimizada a partir dos parâmetros recebidos.
O
usuário revisa
os consentimentos no fluxo otimizado e realiza a aprovação
O client solicita um novo
access_token
que inclua os escopos referentes a
contas
e
Jornada sem Redirecionamento (JSR)
.
O client consulta a
API Resources
para identificar os recursos compartilhados
O client verifica a lista de contas e o saldo disponível para confirmar a possibilidade de execução do pagamento.
O client inicia o
processo de pagamento via Jornada sem Redirecionamento
.
Criação do Consentimento de Dados
O consentimento de dados deve ser criado
antes
do consentimento de vínculo de dispositivo, assumindo caráter secundário. Deverá ser enviado um parâmetro opcional com as seguintes regras:
isLinked
: obrigatório, indica que o consentimento faz parte de uma jornada otimizada.
true
: aplica regras da Jornada Otimizada.
false
: segue fluxo convencional.
A resposta da criação e a consulta do consentimento irão trazer os dados do consentimento vinculado através do objeto
journey.
O objeto opcional
journey
identifica que o consentimento faz parte de uma jornada otimizada e só é retornado quando o consentimento fizer parte de uma jornada otimizada. Atributos:
isLinked
:
boolean
– indica que o consentimento é vinculado a outro em uma Jornada Otimizada. É de preenchimento obrigatório se o objeto
journey
estiver presente.
linkId
:
string
- identifica o consentimento de dados vinculado. É de preenchimento obrigatório se o objeto
journey
estiver presente e o atributo
isLinked
é igual a
true
. No momento da criação do consentimento de dados, este atributo não é preenchido, pois o consentimento de jornada sem redirecionamento só será criado posteriormente. No entanto, durante a jornada de aprovação de consentimento, o valor do campo
linkedId
deverá ser atualizado.
Regras de preenchimento do atributo linkId
Todo consentimento de dados pertencente a uma jornada otimizada deve ter o atributo
linkedId
preenchido quando o cliente aprovar o consentimento (mudando seu estado para
APPROVED
) ou quando o cliente ativamente rejeitar o consentimento (mudando o seu estado para
REJECTED
). O momento do preenchimento do atributo
linkId
é de escolha do detentor, podendo ocorrer durante o redirecionamento, fluxo de telas ou na aprovação/rejeição, desde que a condição descrita seja atendida.
Consentimentos de dados que não passarem pela jornada de aprovação ou tiverem a jornada abandonada pelo cliente podem ter o atributo
linkId
não preenchido. Nesse caso, tanto o iniciador quanto o receptor podem utilizar o atributo
isLinked
para entender que houve uma intenção de vínculo deste consentimento.
Permissions
A lista de
permissions
deve estar restrita a
saldos e limites:
ACCOUNTS_READ
,
ACCOUNTS_BALANCES_READ
,
ACCOUNTS_OVERDRAFT_LIMITS_READ
e
RESOURCES_READ
.
Caso outras permissões sejam solicitadas, a transmissora deve retornar erro HTTP
422
com
code=COMBINACAO_PERMISSOES_INCORRETA
.
Criação do Consentimento de Jornada sem Redirecionamento (JSR)
O consentimento de Jornada sem Redirecionamento atua como
primário
e deve ser criado
após o consentimento de dados
, obedecendo as mesmas regras da jornada convencional com a adição do objeto opcional
journey
no corpo da requisição, conforme especificação abaixo:
Objeto
journey
: identifica que o consentimento faz parte de uma Jornada Otimizada. Se não for enviado, o consentimento seguirá o fluxo convencionado de aprovação.
Atributos:
isLinked
:
boolean
– indica que o consentimento é vinculado a outro em uma Jornada Otimizada. É de preenchimento obrigatório se o objeto
journey
estiver presente. Se o valor for
true
, as regras da Jornada Otimizada serão aplicadas ao consentimento, senão, seguirá o fluxo convencional.
linkId
:
string
- identifica o consentimento de dados vinculado. É de preenchimento obrigatório se o objeto
journey
estiver presente e o atributo
isLinked
é igual a
true
. Deve ser preenchido com o
consentId
recebido na criação do consentimento de dados.
Seleção de Recursos
Durante o fluxo de telas, o cliente deve:
Selecionar a conta de origem para as transferências.
Definir o prazo de validade do consentimento.
A mesma
conta
e a mesma
data de validade
devem ser aplicadas tanto ao consentimento de dados quanto ao de Jornada sem Redirecionamento.
Identificação da Jornada
A jornada otimizada pode ser identificada quando, no
endpoint PAR
, forem enviados conjuntamente:
Consentimento de dados (
/consents
).
Consentimento de Jornada sem Redirecionamento (
/enrollments
).
Jornada
Descrição
Escopos
Jornada
Descrição
Escopos
Jornada Otimizada de Vínculo de Dispositivo (JSR) com compartilhamento de dados de Saldo e/ou Limites
Cliente deseja habilitar o uso de Jornada sem Redirecionamento da sua conta e ao mesmo tempo compartilhar os dados de saldo para facilitar o gerenciamento.
Obrigatório
: openid consent:consentId consents resources accounts enrollment:enrollmentId  payments nrp-consents
Aprovação do Consentimento
Na jornada otimizada de JSR:
O cliente define na iniciadora se deseja compartilhar dados.
Essa escolha
não pode ser alterada
durante o fluxo de aprovação.
Cenários possíveis:
Aprovação simultânea dos dois consentimentos (Dados e JSR).
Rejeição simultânea de ambos.
Criação do access-token
Após a aprovação, deve ser gerado um
access_token
único, vinculado a ambos os consentimentos.
Esse token deve conter todos os escopos referentes a
dados
e
jornada sem redirecionamento
.
Renovação do access-token
Durante o processo de renovação do access-token, o servidor de autorização deve verificar se os consentimentos vinculados permanecem válidos. Se pelo menos um dos consentimentos ainda for válido, o token deve ser renovado, conforme diagrama a seguir:
Open
Software Cliente realiza uma chamada ao endpoint POST /token do servidor de autorização para realizar a renovação do access-token através do refresh-token;
Servidor de autorização verifica se o consentimento de jornada sem redirecionamento permanece em um estado válido
Servidor de autorização verifica se o consentimento de dados permanece em um estado válido
Se pelo menos um dos consentimentos estiver em um estado válido, servidor de autorização emite um novo access-token
Gerenciamento dos Consentimentos
Na
Jornada Otimizada de JSR com compartilhamento de dados de Saldo e/ou Limites
, o
consentimento de JSR
é considerado
primário
, enquanto o
consentimento de dados
é considerado
secundário
.
Dessa forma, aplicam-se as seguintes regras de gerenciamento:
Consentimento de Dados (Secundário)
Pode ser revogado de forma independente, mantendo o consentimento de Jornada sem Redirecionamento ativo.
Não pode ter a sua data de expiração (expirationDateTime) estendida diretamente. Tentativas de alteração devem retornar erro HTTP
422
com
code=ALTERACAO_NAO_PERMITIDA
.
É possível estender a data de expiração (expirationDateTime) através da edição do consentimento primário.
Consentimento de Jornada sem Redirecionamento (Primário)
Se revogado ou rejeitado, deve
revogar automaticamente
o consentimento de dados vinculado.
Se editado o prazo de validade, deve estender o consentimento secundário, atualizando para a mesma data de validade (expirationDateTime).
Diagrama de Sequência
Open
1. Autenticação Técnica
O
Software Client (C)
solicita ao
Authorization Server (AS)
um
access_token
técnico via
POST /oauth/token
com
grant_type=client_credentials
.
Esse token será usado para autenticar a criação de consentimentos.
2. Criação do Consentimento de Dados (Secundário)
O Cliente envia
POST /consents
para a
API Consents (D)
com:
permissions
limitadas a saldos e limites (
ACCOUNTS_READ
,
ACCOUNTS_BALANCES_READ
,
ACCOUNTS_OVERDRAFT_LIMITS_READ
,
RESOURCES_READ
).
parâmetro
isLinked=true
.
Regras:
O consentimento de Dados é
SECUNDÁRIO
na jornada JSR.
Deve estar restrito à
mesma debtorAccount
vinculada ao consentimento de dispositivo.
Se contiver permissions fora do escopo → retornar
422 -
COMBINACAO_PERMISSOES_INCORRETA
.
Retorno:
consentId
.
3. Criação do Consentimento JSR (Primário – Vínculo de Dispositivo)
O Cliente envia
POST /enrollments
para a
API JSR (TI)
com:
journey.isLinked=true
journey.linkId=<consentId de Dados>
Regras:
O consentimento de
JSR é PRIMÁRIO
.
O vínculo é estabelecido pelo campo
linkId
.
Retorno:
enrollmentId
.
4. PAR (Pushed Authorization Request)
O Cliente envia
POST /par
ao
AS
, incluindo no JWT os escopos necessários (
openid
,
consents
,
resources
,
accounts
,
enrollment:{enrollmentId}
,
payments
,
nrp-consents
,
consent:{consentId}
).
O AS retorna um
request_uri
.
O Cliente redireciona o Usuário (U) para o AS usando o
request_uri
.
5. Autenticação e Aprovação Unificada
O Usuário (U) autentica no
AS
e aprova
simultaneamente
:
O Consentimento de Dados.
O Consentimento de Vínculo JSR.
Durante a aprovação, o usuário escolhe a
conta (debtorAccount)
, que deve refletir em ambos consentimentos.
6. Troca do Authorization Code por Tokens
Se aprovados:
O AS retorna um
authorization_code
.
O Cliente envia
POST /oauth/token
(
grant_type=authorization_code
) solicitando os escopos combinados.
O AS retorna
access_token
(escopos de Dados + JSR) e
refresh_token
.
7. Descoberta de Recursos e Consulta de Saldos
Com o
access_token
do usuário, o Cliente:
Chama
GET /resources
→ recebe lista de recursos autorizados.
Chama
GET /accounts
→ lista de contas vinculadas.
Chama
GET /accounts/{accountId}/balances
→ saldo e limites.
8. Iniciação de Pagamentos (via JSR)
O Cliente inicia um pagamento via
POST /payments
, usando o
Authorization: Bearer <access_token>
.
O pagamento ocorre sem redirecionamento (vinculado ao dispositivo autorizado).
Retorno:
paymentId
e status
Initiated
.
9. Renovação do Access Token
O Cliente pode renovar via
POST /oauth/token
com
grant_type=refresh_token
.
O AS valida os consentimentos vinculados (JSR e Dados).
Se
ao menos um
estiver válido → retorna novo
access_token
.
Se
ambos expirados/revogados
→ retorna erro
invalid_grant
.
10. Revogação
Revogação do Consentimento de Dados (Secundário):
Usuário envia
DELETE /consents/{consentId}
.
Apenas o consentimento de Dados é revogado; o JSR permanece válido.
Consequência: deixa de haver compartilhamento de saldo; novo consentimento de Dados deve ser criado se necessário.
Revogação do Consentimento JSR (Primário):
Usuário envia
PATCH /enrollments/{enrollmentId}
.
Ao ser revogado, o JSR revoga
automaticamente
o consentimento de Dados vinculado.

---
                            title: "Iniciação de Pagamentos - Regras de Obrigatoriedade (additionalInfo) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1621622796_Inicia+o+de+Pagamentos+-+Regras+de+Obrigatoriedade+additionalInfo"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1621622796/Inicia+o+de+Pagamentos+-+Regras+de+Obrigatoriedade+additionalInfo"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Iniciação de Pagamentos - Regras de Obrigatoriedade (additionalInfo) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.09
Guia de leitura
Se o campo não está listado, é porque não existe a obrigatoriedade de enviá-lo.
Nos endpoints, a referência “v
x
” indica que se aplicam às versões listadas na coluna “Versões”. Por exemplo, Endpoint “open-banking/automatic-payments/v
x
/recurring-consents/{recurringConsentId}” e Versões “v1 v2” significa que o endpoint é válido para as versões 1 e 2.
Dica: para rolar a tabela horizontalmente, segure SHIFT e utilize o botão de rolagem do mouse.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Pagamentos
Iniciação de Pagamentos
Campo
Definição
Regra de preenchimento
Tipo
Roles
Http code
Métodos
Domínio
Endpoints
Versões
Tamanho máximo
Padrão
Exemplo
Campo
Definição
Regra de preenchimento
Tipo
Roles
Http code
Métodos
Domínio
Endpoints
Versões
Tamanho máximo
Padrão
Exemplo
authorisationFlow
Identifica o fluxo de autorização em que um pagamento ou operação foi solicitado
O campo deve ser preenchido com a string obtida em ".data.authorisationFlow". Se a informação for uma lista, utilize apenas o primeiro item. Caso a string de ".data.authorisationFlow" seja nula, preencha obrigatoriamente com HYBRID_FLOW. É fundamental que sempre seja reportado um dos valores do enum (como HYBRID_FLOW, CIBA ou FIDO), e nunca um valor nulo, pois para fins de telemetria é necessário identificar explicitamente qual fluxo de autorização foi utilizado, independentemente da permissão de valor nulo nas especificações das APIs do Open Finance.
string
CLIENT
Todos
POST
GET
PATCH
CIBA_FLOW, FIDO_FLOW, HYBRID_FLOW
/open-banking/payments/vx/pix/payments
/open-banking/payments/v
x
/pix/payments/{paymentId}​
v4
v5
HYBRID_FLOW
authorisationFlowIntent
Permite a desambiguação e clara distinção entre as jornadas de pagamento que demandam ou não redirecionamento do usuário, já na etapa de provisionamento do consentimento
O campo deve ser preenchido obrigatoriamente com um dos valores do enum: HYBRID_FLOW, CIBA_FLOW ou FIDO_FLOW. A instituição iniciadora deve comunicar a intenção de fluxo de autorização que será utilizado na jornada de pagamento. Esta informação é essencial para a desambiguação das jornadas de pagamento na etapa de consentimento.
Nota técnica:
Esta informação não existe tecnicamente nesta etapa da API de Consents; cabe à instituição iniciadora, por seu conhecimento prévio, reportar sua intenção de fluxo que será efetivamente utilizado na transação.
string
CLIENT
Todos
POST
GET
PATCH
CIBA_FLOW, FIDO_FLOW, HYBRID_FLOW
/open-banking/payments/v
x
/consents
v4
v5
HYBRID_FLOW
companyProfileInfo
Objeto JSON que representa o perfil da Pessoa Jurídica (PJ) do cliente, contendo informações como a natureza jurídica e o porte da empresa, conforme a classificação oficial da Receita Federal do Brasil.
Os itens indentados abaixo pertencem ao objeto companyProfileInfo e seguem as mesmas regras de obrigatoriedade.
Obrigatório para clientes PJ.
O objeto deve conter um objeto de perfil da empresa. As informações de natureza jurídica e porte devem ser obtidas prioritariamente da
API oficial Consulta CNPJ (RFB/SERPRO) ou dos Dados Abertos do CNPJ (RFB)
, conforme o Dicionário de Dados do CNPJ da Receita Federal. Este objeto deve ser enviado como parte do additionalInfo ao consumir as APIs de criação de consentimento para dados e serviços.
Consulta CNPJ — Catálogo de APIs governamentais
(API/Swagger)
Portal de Dados Abertos
(arquivo de dados)
object
CLIENT
Todos
POST
/open-banking/payments/v
x
/consents
v4
v5
Objeto JSON
{ "naturezaJuridica": "2135", "porteEmpresa": "01" }
naturezaJuridica
Código que identifica a constituição jurídico-institucional da entidade, conforme a Tabela de Natureza Jurídica do IBGE, categorizando-a em: Administração pública; Entidades empresariais; Entidades sem fins lucrativos; Pessoas físicas e organizações internacionais; e Outras instituições extraterritoriais.
Obrigatório para clientes PJ.
O cliente (receptor/iniciador) deve obter essa informação a partir de fontes oficiais (ex., Governo Federal/Dados Abertos/Base CNPJs ou API do SERPRO), com base no CNPJ do usuário, e reportá-la como parte do additionalInfo quando houver consumo as APIs de criação de consentimento para compartilhamento de dados e serviços.
string
CLIENT
Todos
POST
/open-banking/payments/v
x
/consents
v4
v5
4
^\d{4}$
2135
porteEmpresa
Código numérico que identifica o porte da empresa do cliente Pessoa Jurídica (PJ), conforme a classificação oficial da Receita Federal do Brasil.
Obrigatório para clientes PJ.
O receptor/iniciador, que detém o CNPJ do usuário, é responsável por obter o código do porte da empresa. Esta informação deve ser consultada e validada a partir de fontes oficiais, como a base de Dados Abertos do CNPJ ou a API do SERPRO, ambas mantidas pelo Governo Federal, e conforme o Dicionário de Dados do CNPJ da Receita Federal. O valor deve ser enviado como parte do additionalInfo quando houver consumo as APIs de criação de consentimento para compartilhamento de dados e serviços.
string
CLIENT
Todos
POST
/open-banking/payments/v
x
/consents
v4
v5
2
^\d{2}$
01
consentId
O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.
Deve ser preenchido com a mesma string obtida no campo .data.consentId retornado após a chamada inicial na API "POST /consents”
string
CLIENT
Todos menos 4xx e 5xx para o método POST
POST
GET
PATCH
/open-banking/payments/v
x
/consents
/open-banking/payments/v
x
/consents/{consentId}
v4
v5
256
^urn:[a-zA-Z0-9][a-zA-Z0-9\-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD33123
consentId
O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.
Deve ser preenchido com a mesma string obtida no campo .data.consentId retornado após a chamada inicial na API "POST /consents”
string
CLIENT
Todos
POST
GET
PATCH
/open-banking/payments/v
x
/pix/payments
/open-banking/payments/v
x
/pix/payments/{paymentId}​
/open-banking/payments/v
x
/pix/payments/consents/{consentId}
v4
256
^urn:[a-zA-Z0-9][a-zA-Z0-9\-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD33123
consentId
O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.
Deve ser preenchido com a mesma string obtida no campo .data.consentId retornado após a chamada inicial na API "POST /consents”
string
CLIENT
Todos
POST
GET
PATCH
/open-banking/payments/v
x
/pix/payments
/open-banking/payments/v
x
/pix/payments/{paymentId}​
/open-banking/payments/v
x
/consents/{consentId}/pix/payments/
v5
256
^urn:[a-zA-Z0-9][a-zA-Z0-9\-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD33123
dropReason
Razão pela qual um usuário não conseguiu prosseguir em uma jornada, especificamente no contexto de consentimentos
O campo dropReason deve ser adicionado nas informações do campo additionalInfo que deverá ser enviado no reporte do provedor do serviço consumido (papel SERVER)
O reporte deverá ser feito por todos os transmissores de dados e detentoras de conta. Para os casos em que ocorram falhas técnicas que impossibilitem a verificação do CPF/CNPJ (incluindo, mas não se limitando, a erros HTTP 4xx, 500 ou timeout na resposta), o reporte deve ser realizado com o valor NO_CREDENTIAL, Em jornadas de múltipla alçada de pessoas jurídicas, quando a autenticação é bem-sucedida mas os poderes constituídos são insuficientes para finalização do Hybrid Flow, deve-se usar NO_AUTHORITY.
NONE
: quando o CPF (loggedUser) / CNPJ (businessEntity) possui credencial autenticadora e poderes suficientes para prosseguir o fluxo monitorado - exemplo: PF, cliente, que possui credencial ativa, mas não se autenticou; cliente que se autenticou utilizando a credencial correta.
NO_CREDENTIAL
: quando o CPF (loggedUser) / CNPJ (businessEntity) não for cliente ou não possuir credencial válida/ativa para prosseguir no fluxo monitorado ou quando o HTTP response code for diferente de 201.
NO_AUTHORITY
: quando o CPF (loggedUser) / CNPJ (businessEntity) consegue se autenticar, mas não dispõe de poderes ou alçadas para prosseguir no fluxo de compartilhamento de dados e serviços.
NO_AUTHORITY_PERSON_MISMATCH
: quando o CPF (loggedUser) não possui relação com a credencial utilizada na etapa de autenticação do Hybrid Flow - exemplo: consentimento criado para um CPF e autenticado por outro; criado para um CNPJ e autenticado por CPF sem relação com o CNPJ.
string
SERVER
Todos
POST
NO_AUTHORITY, NO_AUTHORITY_PERSON_MISMATCH, NO_CREDENTIAL, NONE
/open-banking/payments/v
x
/consents
v4
v5
NO_CREDENTIAL
errorCodes
Registrar os códigos de erro detalhados de uma requisição que resultou em um erro HTTP (série 4xx ou 5xx).
Caso o HTTP Code seja 4XX ou 5XX, esse campo deve ser preenchido com a lista das strings obtidas em ".errors[].code", devendo constar apenas um código de erro. Não havendo string, deve ser enviada uma lista vazia.
string
CLIENT
422
POST
GET
PATCH
422ReponseError Create Consent
DATA_PAGAMENTO_INVALIDA, DETALHE_PAGAMENTO_INVALIDO, ERRO_IDEMPOTENCIA, FORMA_PAGAMENTO_INVALIDA, NAO_INFORMADO, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO, PROPOSITO_INVALIDO
CreateError PIX Payments
COBRANCA_INVALIDA, CONSENTIMENTO_INVALIDO, CONSENTIMENTO_PENDENTE_AUTORIZACAO, DETALHE_PAGAMENTO_INVALIDO, ERRO_IDEMPOTENCIA, NAO_INFORMADO, PAGAMENTO_DIVERGENTE_CONSENTIMENTO, PAGAMENTO_NAO_PERMITE_CANCELAMENTO, PAGAMENTO_RECUSADO_DETENTORA, PAGAMENTO_RECUSADO_SPI, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO, SALDO_INSUFICIENTE, VALOR_ACIMA_LIMITE, VALOR_INVALIDO
/open-banking/payments/v
x
/consents
/open-banking/payments/v
x
/consents/{consentId}
/open-banking/payments/v
x
/pix/payments
/open-banking/payments/v
x
/pix/payments/{paymentId}​
/open-banking/payments/v
x
/pix/payments/consents/{consentId}
v4
NAO_INFORMADO
errorCodes
Registrar os códigos de erro detalhados de uma requisição que resultou em um erro HTTP (série 4xx ou 5xx).
Caso o HTTP Code seja 4XX ou 5XX, esse campo deve ser preenchido com a lista das strings obtidas em ".errors[].code", devendo constar apenas um código de erro. Não havendo string, deve ser enviada uma lista vazia.
string
CLIENT
422
POST
GET
PATCH
422ReponseError Create Consent
DATA_PAGAMENTO_INVALIDA, DETALHE_PAGAMENTO_INVALIDO, ERRO_IDEMPOTENCIA, FORMA_PAGAMENTO_INVALIDA, NAO_INFORMADO, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO, PROPOSITO_INVALIDO
CreateError PIX Payments
COBRANCA_INVALIDA, CONSENTIMENTO_INVALIDO, CONSENTIMENTO_PENDENTE_AUTORIZACAO, DETALHE_PAGAMENTO_INVALIDO, ERRO_IDEMPOTENCIA, NAO_INFORMADO, PAGAMENTO_DIVERGENTE_CONSENTIMENTO, PAGAMENTO_NAO_PERMITE_CANCELAMENTO, PAGAMENTO_RECUSADO_DETENTORA, PAGAMENTO_RECUSADO_SPI, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO, SALDO_INSUFICIENTE, VALOR_ACIMA_LIMITE, VALOR_INVALIDO
/open-banking/payments/v
x
/consents
/open-banking/payments/v
x
/consents/{consentId}
/open-banking/payments/v
x
/pix/payments
/open-banking/payments/v
x
/pix/payments/{paymentId}​
/open-banking/payments/v
x
/consents/{consentId}/pix/payments
v5
NAO_INFORMADO
errorCodes
Registrar os códigos de erro detalhados de uma requisição que resultou em um erro HTTP (série 4xx ou 5xx).
Caso o HTTP Code seja 4XX ou 5XX, esse campo deve ser preenchido com a lista das strings obtidas em ".errors[].code", devendo constar apenas um código de erro. Não havendo string, deve ser enviada uma lista vazia.
string
CLIENT
4xx ou 5xx exceto 422
POST
GET
PATCH
/open-banking/payments/v
x
/consents
/open-banking/payments/v
x
/consents/{consentId}
/open-banking/payments/v
x
/pix/payments
/open-banking/payments/v
x
/pix/payments/{paymentId}​
/open-banking/payments/v
x
/pix/payments/consents/{consentId}
v4
errorCodes
Registrar os códigos de erro detalhados de uma requisição que resultou em um erro HTTP (série 4xx ou 5xx).
Caso o HTTP Code seja 4XX ou 5XX, esse campo deve ser preenchido com a lista das strings obtidas em ".errors[].code", devendo constar apenas um código de erro. Não havendo string, deve ser enviada uma lista vazia.
string
CLIENT
4xx ou 5xx exceto 422
POST
GET
PATCH
/open-banking/payments/v
x
/consents
/open-banking/payments/v
x
/consents/{consentId}
/open-banking/payments/v
x
/pix/payments
/open-banking/payments/v
x
/pix/payments/{paymentId}​
/open-banking/payments/v
x
/consents/{consentId}/pix/payments
v5
localInstrument
Especifica a forma de iniciação do pagamento​
Deve ser preenchido com a mesma string informada no payload ".data.localInstrument"
Se /data/payment/schedule enviado com valor diferente de single durante a criação do consentimento, apenas os métodos MANU, DICT ou QRES são permitidos.
string
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST
GET
PATCH
DICT, INIC, MANU, QRDN, QRES, AUTO, APDN, APES
/open-banking/payments/v
x
/consents
/open-banking/payments/v
x
/pix/payments/{paymentId}
v4
v5
MANU
paymentDate
Data em que o pagamento será realizado
Deve ser enviado obrigatoriamente para os tipos de pagamento (paymentType) SWEEPING e AUTOMATIC
Deve ser preenchido com o conteúdo de
data.payment.date
Mutualmente excludente com o campo
paymentSchedule
string
CLIENT
201
POST
/open-banking/payments/v
x
/consents
v4
v5
2021-01-01
paymentList
Lista de dados de pagamentos com pagamentos imediatos e agendamentos únicos ou recorrentes.
Os itens indentados abaixo pertencem ao objeto paymentList e seguem as mesmas regras de obrigatoriedade
Deve ser enviado obrigatoriamente para os tipos de pagamento (paymentType) IMMEDIATE, SCHEDULED e RECURRENT, mesmo que a lista contenha apenas um item. Para o mesmo consentId não podem ser reportados nesta lista mais do que 60 paymentId.
object
CLIENT
201
POST
/open-banking/payments/v
x
/pix/payments
v4
v5
[{"paymentId":"4d4dec4b-5960-4041-8099-1340b8c8a4bb","consentId":"urn:bancoex:C1DD33123","statusUpdateDateTime":"2026-02-08T19:53:53Z","status":"ACSC"}]'2021-01-01
paymentId
Código ou identificador único informado pela instituição detentora da conta para representar a iniciação de pagamento​
string
CLIENT
201
POST
/open-banking/payments/v
x
/pix/payments
v4
v5
4d4dec4b-5960-4041-8099-1340b8c8a4bb
consentId
Identificador único do consentimento criado para a iniciação de pagamento solicitada​
string
CLIENT
201
POST
/open-banking/payments/v
x
/pix/payments
v4
v5
urn:bancoex:C1DD33123
statusUpdateDateTime
Data e hora da última atualização da iniciação de pagamento

---
                            title: "Pagamentos Automáticos - Regras de Obrigatoriedade (additionalInfo) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1622081540_Pagamentos+Autom+ticos+-+Regras+de+Obrigatoriedade+additionalInfo"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1622081540/Pagamentos+Autom+ticos+-+Regras+de+Obrigatoriedade+additionalInfo"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Pagamentos Automáticos - Regras de Obrigatoriedade (additionalInfo) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

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
Pagamentos Automáticos
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
Padrão
Exemplo
amountType
Valida se o serviço contratado possui maior conversão em relação ao tipo do valor definido, sendo ele fixo ou variável​
Se não enviando nem ".data.recurringConfiguration.automatic.fixedAmount" e nem ".data.recurringConfiguration.automatic.maximumVariableAmount", “VARIAVEL”; ou
Se enviado fixedAmount, “FIXO”; ou
Se enviado maximumVariableAmount, “VARIAVEL”
Deve ser preenchido quando paymentType for AUTOMATIC
string
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST
GET
PATCH
FIXO, VARIAVEL
/open-banking/automatic-payments/v
x
/recurring-consents
/open-banking/automatic-payments/v
x
/recurring-consents/{recurringConsentId}
v2
FIXO
authorisationFlow
Identifica o fluxo de autorização em que um pagamento ou operação foi solicitado. Descreve como o autenticador (por exemplo, um dispositivo FIDO) está anexado ao cliente que realiza a autenticação (ex: platform para autenticadores integrados como Face ID ou cross-platform para chaves de segurança USB).
O campo deve ser preenchido com a string obtida em ".data.authorisationFlow". Se a informação for uma lista, utilize apenas o primeiro item. Caso a string de ".data.authorisationFlow" seja nula, preencha obrigatoriamente com HYBRID_FLOW. É fundamental que sempre seja reportado um dos valores do enum (como HYBRID_FLOW, CIBA ou FIDO), e nunca um valor nulo, pois para fins de telemetria é necessário identificar explicitamente qual fluxo de autorização foi utilizado, independentemente da permissão de valor nulo nas especificações das APIs do Open Finance.
string
CLIENT
Todos
POST
GET
PATCH
CIBA_FLOW, FIDO_FLOW, HYBRID_FLOW
/open-banking/automatic-payments/v
x
/pix/recurring-payments
/open-banking/automatic-payments/v
x
/pix/recurring-payments/{recurringPaymentId}
v2
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
/open-banking/automatic-payments/v
x
/recurring-consents
v2
HYBRID_FLOW
cancellationReason
Identifica o estado que o pagamento estava quando foi cancelado​
Preencher com o valor do campo ".cancellation.reason"
Deve ser enviado quando em um GET ou POST /payment e o campo status é "CANC" ou em um PATCH /payment (que é a API de cancelamento).
string
CLIENT
2xx
POST
GET
PATCH
CANCELADO_AGENDAMENTO, CANCELADO_PENDENCIA
/open-banking/automatic-payments/v
x
/pix/recurring-payments
/open-banking/automatic-payments/v
x
/pix/recurring-payments/{recurringPaymentId}
v2
CANCELADO_PENDENCIA
cancelledFrom
Informa o meio pelo qual foi realizado o cancelamento
Preencher com o valor do campo ".cancellation.cancelledFrom"
Status do pagamento deve ser "CANC"
string
CLIENT
2xx
POST
GET
PATCH
DETENTORA, INICIADORA
/open-banking/automatic-payments/v
x
/pix/recurring-payments
/open-banking/automatic-payments/v
x
/pix/recurring-payments/{recurringPaymentId}
v2
INICIADORA
companyProfileInfo
Objeto JSON que representa o perfil da Pessoa Jurídica (PJ) do cliente, contendo informações como a natureza jurídica e o porte da empresa, conforme a classificação oficial da Receita Federal do Brasil.
Os itens indentados abaixo pertencem ao objeto companyProfileInfo e seguem as mesmas regras de obrigatoriedade.
Obrigatório para clientes PJ
. O objeto deve conter um objeto de perfil da empresa. As informações de natureza jurídica e porte devem ser obtidas prioritariamente da
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
/open-banking/automatic-payments/v
x
/recurring-consents
v2
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
/open-banking/automatic-payments/v
x
/recurring-consents
v2
^\d{4}$
2135
porteEmpresa
Código numérico que identifica o porte da empresa do cliente Pessoa Jurídica (PJ), conforme a classificação oficial da Receita Federal do Brasil.
Obrigatório para clientes PJ
. O receptor/iniciador, que detém o CNPJ do usuário, é responsável por obter o código do porte da empresa. Esta informação deve ser consultada e validada a partir de fontes oficiais, como a base de Dados Abertos do CNPJ ou a API do SERPRO, ambas mantidas pelo Governo Federal, e conforme o Dicionário de Dados do CNPJ da Receita Federal. O valor deve ser enviado como parte do additionalInfo quando houver consumo as APIs de criação de consentimento para compartilhamento de dados e serviços.
string
CLIENT
Todos
POST
/open-banking/automatic-payments/v
x
/recurring-consents
v2
^\d{2}$
01
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
/open-banking/automatic-payments/v
x
/recurring-consents
v2
NO_CREDENTIAL
errorCodes
Registra os códigos de erro detalhados de uma requisição que resultou em um erro HTTP (série 4xx ou 5xx).
Caso o HTTP Code seja 4XX ou 5XX, esse campo deve ser preenchido com a lista das strings obtidas em ".errors[].code", devendo constar apenas um código de erro. Não havendo string, deve ser enviada uma lista vazia.
string
CLIENT
422
POST
ReponseError Create Consent
DATA_PAGAMENTO_INVALIDA, DETALHE_PAGAMENTO_INVALIDO, ERRO_IDEMPOTENCIA, FUNCIONALIDADE_NAO_HABILITADA, NAO_INFORMADO, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO
422ReponseError Recurring Consent
CAMPO_NAO_PERMITIDO, CONSENTIMENTO_NAO_PERMITE_CANCELAMENTO, DETALHE_EDICAO_INVALIDO, FALTAM_SINAIS_OBRIGATORIOS_PLATAFORMA, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO,  PERMISSAO_INSUFICIENTE
422ResponseError PIX Recurring  Payment
CONSENTIMENTO_INVALIDO, CONSENTIMENTO_PENDENTE_AUTORIZACAO, DETALHE_PAGAMENTO_INVALIDO, ERRO_IDEMPOTENCIA, FORA_PRAZO_PERMITIDO, LIMITE_PERIODO_QUANTIDADE_EXCEDIDO, LIMITE_PERIODO_VALOR_EXCEDIDO, LIMITE_VALOR_TOTAL_CONSENTIMENTO_EXCEDIDO, LIMITE_VALOR_TRANSACAO_CONSENTIMENTO_EXCEDIDO, NAO_INFORMADO, PAGAMENTO_DIVERGENTE_CONSENTIMENTO, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO, PAGAMENTO_RECUSADO_DETENTORA, PAGAMENTO_RECUSADO_SPI, SALDO_INSUFICIENTE, VALOR_ACIMA_LIMITE, VALOR_INVALIDO
422ReponseErrorCreate Recurring Payment PaymentId
CANCELAMENTO_FORA_PERIODO_PERMITIDO, PAGAMENTO_NAO_PERMITE_CANCELAMENTO, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO
/open-banking/automatic-payments/v
x
/recurring-consents
/open-banking/automatic-payments/v
x
/pix/recurring-payments
/open-banking/automatic-payments/v
x
/recurring-consents/{recurringConsentId}
/open-banking/automatic-payments/v
x
/pix/recurring-payments
/open-banking/automatic-payments/v
x
/pix/recurring-payments/{recurringPaymentId}
v2
NAO_INFORMADO
errorCodes
Registra os códigos de erro detalhados de uma requisição que resultou em um erro HTTP (série 4xx ou 5xx).
Caso o HTTP Code seja 4XX ou 5XX, esse campo deve ser preenchido com a lista das strings obtidas em ".errors[].code", devendo constar apenas um código de erro. Não havendo string, deve ser enviada uma lista vazia.
string
CLIENT
4xx ou 5xx exceto 422
POST
GET
/open-banking/automatic-payments/v
x
/recurring-consents
/open-banking/automatic-payments/v
x
/pix/recurring-payments
/open-banking/automatic-payments/v
x
/recurring-consents/{recurringConsentId}
/open-banking/automatic-payments/v
x
/pix/recurring-payments
/open-banking/automatic-payments/v
x
/pix/recurring-payments/{recurringPaymentId}
v2
hasMinimumAmount
Valida se possui o valor mínimo definido pelo usuário recebedor​
Se preenchido o campo “.data/recurringConfiguration.automatic.minimumVariableAmount”, enviar "TRUE"; ou
Se não preenchido o campo “.data.recurringConfiguration.automatic.minimumVariableAmount” enviar "FALSE"
Deve ser preenchido quando paymentType for AUTOMATIC
string
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST
GET
PATCH
TRUE, FALSE
/open-banking/automatic-payments/v
x
/recurring-consents
/open-banking/automatic-payments/v
x
/recurring-consents/{recurringConsentId}
v2
TRUE
interval
Periodicidade que a recorrência foi definida (semanal, trimestral, anual...)​
Preencher com o valor do campo ".data.recurringConfiguration.interval"
Deve ser preenchido quando paymentType for AUTOMATIC
string
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST
GET
PATCH
SEMANAL, MENSAL, TRIMESTRAL, SEMESTRAL, ANUAL
/open-banking/automatic-payments/v
x
/recurring-consents
/open-banking/automatic-payments/v
x
/recurring-consents/{recurringConsentId}
v2
ANUAL
isFirstPayment
Valida se o serviço possui um pagamento associado na adesão
Se preenchido o campo ".data.recurringConfiguration.automatic.firstPayment", enviar "TRUE"; ou
Se não preenchido o campo ".data.recurringConfiguration.automatic.firstPayment", enviar "FALSE"
Deve ser preenchido quando paymentType for AUTOMATIC
string
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST
GET
PATCH
TRUE, FALSE
/open-banking/automatic-payments/v
x
/recurring-consents
/open-banking/automatic-payments/v
x
/recurring-consents/{recurringConsentId}
v2
TRUE
isRetryAccepted
Identifica se foi autorizado a tentativas de pagamento em dias subsequentes na situação de falha do pagamento da recorrência​
Preencher com o valor do campo ".data.recurringConfiguration.automatic.isRetryAccepted"
Deve ser preenchido quando paymentType for AUTOMATIC
string
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST
GET
PATCH
TRUE, FALSE
/open-banking/automatic-payments/v
x
/recurring-consents
/open-banking/automatic-payments/v
x
/recurring-consents/{recurringConsentId}
v2
TRUE
journeyIsLinked
Indica que o consentimento faz parte de uma jornada otimizada.
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.isLinked”, retornado após a chamada inicial na API “POST /consent” em caso de Jornada Otimizada.
Em casos em que a informação não está disponível espera-se o envio do valor FALSE.
string
CLIENT
Todos
POST
GET
TRUE, FALSE
/open-banking/automatic-payments/v
x
/recurring-consents
/open-banking/automatic-payments/v
x
/recurring-consents/{recurringConsentId}
v2
FALSE
journeyLinkId
Identifica o consentimento de dados vinculado a uma Jornada Otimizada.
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.linkId”, retornado após a chamada inicial na API “POST /consent” em caso de Jornada Otimizada.
Deve ser enviado se journeyIsLinked for TRUE.
string
CLIENT
Todos
POST
GET
/open-banking/automatic-payments/v
x
/recurring-consents
/open-banking/automatic-payments/v
x
/recurring-consents/{recurringConsentId}
v2
^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD331237
localInstrument
Especifica a forma de iniciação do pagamento​
Deve ser preenchido com a mesma string informada no payload ".data.localInstrument"
Caso consentimento associado a tentativa de pagamento seja para Pix automático (objeto “automatic” selecionado no oneOf do campo "/data/recurringConfiguration") e a referência do pagamento indicar uma recorrência (valor do campo "/data/paymentReference" diferente de "zero"), apenas o método AUTO é permitido, ou; Caso consentimento associado a tentativa de pagamento seja para Pix automático (objeto “automatic” selecionado no oneOf do campo "/data/recurringConfiguration") e a referência do pagamento indicar o pagamento inicial avulso (valor do campo "/data/paymentReference" igual a "zero"), apenas o método MANU é permitido. Para consentimentos de Transferências Inteligentes (objeto “sweeping” selecionado no “oneOf” do campo “/data/recurringConfiguration/”), apenas os métodos MANU, DICT e INIC são permitidos
string
CLIENT
Todos (POST)
Todos menos 4xx e 5xx (GET/PATCH)
POST
GET
PATCH
DICT, INIC, MANU, QRDN, QRES, AUTO, APDN, APES
/open-banking/automatic-payments/v
x
/pix/recurring-payments
/open-banking/automatic-payments/v
x
/pix/recurring-payments/{recurringPaymentId}
v2
DICT
originalRecurringPaymentId
Identifica o primeiro pagamento da recorrência em relação as retentativas​
Preencher com o valor do campo ".data.originalRecurringPaymentId"
Deve ser preenchido quando paymentType for AUTOMATIC
string
CLIENT
Todos (POST/PATCH)
Todos menos 4xx e 5xx (GET)
POST
GET
PATCH
/open-banking/automatic-payments/v
x
/pix/recurring-payments
/open-banking/automatic-payments/v
x
/pix/recurring-payments/{recurringPaymentId}
/open-banking/automatic-payments/vx/pix​/recurring-payments​/{originalRecurringPaymentId}​/retry

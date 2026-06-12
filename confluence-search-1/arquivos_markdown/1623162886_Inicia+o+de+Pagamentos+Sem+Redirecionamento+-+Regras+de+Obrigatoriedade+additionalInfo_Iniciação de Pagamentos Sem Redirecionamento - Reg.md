---
                            title: "Iniciação de Pagamentos Sem Redirecionamento - Regras de Obrigatoriedade (additionalInfo) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1623162886_Inicia+o+de+Pagamentos+Sem+Redirecionamento+-+Regras+de+Obrigatoriedade+additionalInfo"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1623162886/Inicia+o+de+Pagamentos+Sem+Redirecionamento+-+Regras+de+Obrigatoriedade+additionalInfo"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Iniciação de Pagamentos Sem Redirecionamento - Regras de Obrigatoriedade (additionalInfo) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

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
Iniciação de Pagamentos Sem Redirecionamento
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
authenticatorAttachment​
Descreve como o autenticador (por exemplo, um dispositivo FIDO) está anexado ao cliente que realiza a autenticação (ex: platform para autenticadores integrados como Face ID ou cross-platform para chaves de segurança USB).
Deve ser preenchido com a mesma string definida em ".data.authenticatorAttachment". Não havendo string, deve ser explicitamente enviada esse additionalInfo como sendo uma string vazia.​
string
CLIENT
Todos
POST
platform, cross-platform
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-registration​
v2
cross-platform
cancelledFrom
Informa o meio pelo qual foi realizado o cancelamento
Preencher com o valor do campo ".cancellation.cancelledFrom"
Status do pagamento deve ser "REVOKED"
string
CLIENT
2xx
GET
INICIADORA, DETENTORA
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}​
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
/open-banking/enrollments/v
x
/enrollments
v2
{ "naturezaJuridica": "2135", "porteEmpresa": "01" }
naturezaJuridica
Código que identifica a constituição jurídico-institucional da entidade, conforme a Tabela de Natureza Jurídica do IBGE, categorizando-a em: Administração pública; Entidades empresariais; Entidades sem fins lucrativos; Pessoas físicas e organizações internacionais; e Outras instituições extraterritoriais.
Obrigatório para clientes PJ.
O cliente (receptor/iniciador) deve obter essa informação a partir de fontes oficiais (ex., Governo Federal/Dados Abertos/Base CNPJs ou API do SERPRO), com base no CNPJ do usuário, e reportá-la como parte do additionalInfo quando houver consumo as APIs de criação de consentimento para compartilhamento de dados e serviços.
string
CLIENT
Todos
POST
/open-banking/enrollments/v
x
/enrollments
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
/open-banking/enrollments/v
x
/enrollments
v2
^\d{2}$
01
consentId​
O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.
Deve ser preenchido com a mesma string obtida no campo .data.consentId retornado após a chamada inicial na API "POST /consents”
string
CLIENT
Todos menos 4xx e 5xx para o método POST
POST
/open-banking/enrollments/v
x
/consents/{consentId}/authorise
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-sign-options
v2
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
/open-banking/enrollments/v
x
/enrollments
v2
NO_CREDENTIAL
enrollmentId
Identificador usado para registrar uma jornada ou um vínculo inicial
Deve ser preenchido com a mesma string obtida no campo .data.enrollmentId retornado após a chamada inicial na API "POST /enrollments".
string
CLIENT
2XX
POST
/open-banking/enrollments/v
x
/enrollments
/open-banking/enrollments/v
x
/recurring-consents/{recurringConsentId}/authorise
v2
^urn:[a-zA-Z0-9][a-zA-Z0-9\-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD33123
enrollmentId
Identificador usado para registrar uma jornada ou um vínculo inicial
Deve ser preenchido com a mesma string obtida no campo .data.enrollmentId retornado após a chamada inicial na API "POST /enrollments".
string
CLIENT
Todos
POST
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-registration
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-sign-options
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/risk-signals
/open-banking/enrollments/v
x
/consents/{consentId}/authorise
v2
^urn:[a-zA-Z0-9][a-zA-Z0-9\-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD33123
errorCodes
Registrar os códigos de erro detalhados de uma requisição que resultou em um erro HTTP (série 4xx ou 5xx).
Caso o HTTP Code seja 4XX ou 5XX, esse campo deve ser preenchido com a lista das strings obtidas em ".errors[].code", devendo constar apenas um código de erro. Não havendo string, deve ser enviada uma lista vazia.
string
CLIENT
422
POST
GET
PATCH
422ReponseError Create Enrollment
CONTA_INVALIDA, ERRO_IDEMPOTENCIA, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO, PERMISSOES_INVALIDAS
422ReponseError Cancel Enrollment
ERRO_IDEMPOTENCIA, MOTIVO_REJEICAO, MOTIVO_REVOGACAO, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO, REJEITADO_OUTRO_SEM_DETALHES, REVOGADO_OUTRO_SEM_DETALHES, STATUS_INVALIDO
422ResponseError Fido Registration
CHALLENGE_INVALIDO, ERRO_IDEMPOTENCIA, EXTENSION_INVALIDA, ORIGEM_FIDO_INVALIDA, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO, PUBLIC_KEY_INVALIDA, RP_INVALIDA, STATUS_VINCULO_INVALIDO
422ResponseError Fido Registration-Options
ERRO_IDEMPOTENCIA, MAXIMO_CHALLENGES_ATINGIDO, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO, RP_INVALIDA, STATUS_VINCULO_INVALIDO
422ResponseError Risk Signals
ERRO_IDEMPOTENCIA, FALTAM_SINAIS_OBRIGATORIOS_DA_PLATAFORMA, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO, STATUS_VINCULO_INVALIDO
422ResponseError Fido Sign Options
ERRO_IDEMPOTENCIA, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO, PERMISSAO_INVALIDA_VINCULO_CONSENTIMENTO, RP_INVALIDA, STATUS_CONSENTIMENTO_INVALIDO, STATUS_VINCULO_INVALIDO
422ResponseError Consents Authorization
CONTA_DEBITO_DIVERGENTE_CONSENTIMENTO_VINCULO, ERRO_IDEMPOTENCIA, FALTAM_SINAIS_OBRIGATORIOS_DA_PLATAFORMA, ORIGEM_FIDO_INVALIDA, PARAMETRO_INVALIDO, PARAMETRO_NAO_INFORMADO, RISCO, STATUS_CONSENTIMENTO_INVALIDO, STATUS_VINCULO_INVALIDO
422ResponseError Create Consent
COMBINACAO_PERMISSOES_INCORRETA, DATA_EXPIRACAO_INVALIDA, DEPENDE_MULTIPLA_ALCADA, ERRO_NAO_MAPEADO, ESTADO_CONSENTIMENTO_INVALIDO, INFORMACOES_PJ_NAO_INFORMADAS, PERMISSAO_PF_PJ_EM_CONJUNTO, PERMISSOES_PJ_INCORRETAS, SEM_PERMISSOES_FUNCIONAIS_RESTANTES
/open-banking/enrollments/v
x
/enrollments
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-registration-options
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-registration
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-sign-options
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/risk-signals
/open-banking/enrollments/v
x
/consents/{consentId}/authorise
v2
PARAMETRO_INVALIDO
errorCodes
Registrar os códigos de erro detalhados de uma requisição que resultou em um erro HTTP (série 4xx ou 5xx).
Caso o HTTP Code seja 4XX ou 5XX, esse campo deve ser preenchido com a lista das strings obtidas em ".errors[].code", devendo constar apenas um código de erro. Não havendo string, deve ser enviada uma lista vazia.
string
CLIENT
4xx e 5xx exceto 422
POST
GET
PATCH
/open-banking/enrollments/v
x
/enrollments
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-registration-options
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-registration
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-sign-options
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/risk-signals
/open-banking/enrollments/v
x
/consents/{consentId}/authorise
/open-banking/enrollments/v
x
/recurring-consents/{recurringConsentId}/authorise
v2
journeyIsLinked
Indica que o consentimento faz parte de uma jornada otimizada
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.isLinked”, retornado após a chamada inicial na API “POST /enrollments” em caso de Jornada Otimizada.
Em casos em que a informação não está disponível espera-se o envio do valor FALSE.
string
CLIENT
Todos
POST
GET
TRUE, FALSE
/open-banking/enrollments/v
x
/enrollments
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}
v2
FALSE
journeyLinkId
Identifica o consentimento de dados vinculado a uma Jornada Otimizada.
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.linkId”, retornado após a chamada inicial na API “POST /enrollments” em caso de Jornada Otimizada.
Deve ser enviado se journeyIsLinked for TRUE.
string
CLIENT
Todos
POST
GET
/open-banking/enrollments/v
x/
enrollments
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}
v2
^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD331237
nfcPayment
Identifica se o pagamento foi realizado através de NFC
Enviar o valor do campo "x-bcb-nfc", presente no de request header do endpoint de autorização de consentimentos via JSR (POST /consents/{consentId}/authorise)
string
CLIENT
Todos
POST
TRUE, FALSE
/open-banking/enrollments/v
x
/consents/{consentId}/authorise
v2
FALSE
personType
Identifica a natureza do solicitante em uma transação ou consentimento.
Se .data.businessEntity estiver preenchido no payload, se estiver então preencher com "PJ", se não estiver então preencher com "PF"
string
CLIENT
2xx
POST
GET
PF, PJ,PESSOA_NATURAL, PESSOA_JURIDICA
/open-banking/enrollments/v
x
/enrollments
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}
v2
PJ
platform
Identifica a plataforma utilizada
Deve ser preenchido com a mesma string definida em ".data.platform"
string
CLIENT
Todos
POST
ANDROID, BROWSER, CROSS_PLATFORM, IOS
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-registration-options
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-sign-options
v2
ANDROID
recurringConsentId​
Identificador único do consentimento de longa duração criado para a iniciação de pagamento solicitada
Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na
RFC8141
é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme "urn" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para
recurringConsentId
temos:
o namespace(urn)
o identificador associado ao namespace da instituição transmissora (bancoex)
o identificador específico dentro do namespace (C1DD33123).
Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na
RFC8141
.
string
CLIENT
Todos menos 4xx e 5xx para o método POST
POST
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}/fido-sign-options
/open-banking/enrollments/v
x
/recurring-consents/{recurringConsentId}/authorise
v2
^urn:[a-zA-Z0-9][a-zA-Z0-9\-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
urn:bancoex:C1DD331237
rejectionReasonCode
Código da razão pela qual um consentimento ou pagamento foi rejeitado
Deve ser preenchido com a mesma string obtida no ".data.rejectionReason.code, “data.rejection.reason.code” ou “data.cancellation.reason.rejectionReason". Caso a informação esteja em formato de lista, enviar apenas o valor do primeiro item da lista.
Dever ser enviado quando o status for REJECTED
string
CLIENT
Todos menos 4xx e 5xx
GET
PATCH
REJEITADO_DISPOSITIVO_INCOMPATIVEL, REJEITADO_FALHA_FIDO, REJEITADO_FALHA_HYBRID_FLOW, REJEITADO_FALHA_INFRAESTRUTURA, REJEITADO_MANUALMENTE, REJEITADO_MAXIMO_CHALLENGES_ATINGIDO, REJEITADO_OUTRO, REJEITADO_SEGURANCA_INTERNA, REJEITADO_TEMPO_EXPIRADO_ACCOUNT_HOLDER_VALIDATION, REJEITADO_TEMPO_EXPIRADO_RISK_SIGNALS, REJEITADO_TEMPO_EXPIRADO_ENROLLMENT, REJEITADO_TITULARIDADE_DIVERGENTE
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}
v2
REJEITADO_OUTRO
revocationReasonCode
Código indicador do motivo da revogação
Deve ser preenchido com a mesma string obtida no ".data.cancellation.reason.revocationReason". Caso a informação esteja em formato de lista, enviar apenas o valor do primeiro item da lista.
Dever ser enviado quando o status for REVOKED
string
CLIENT
Todos (PATCH)
200 (GET)
GET
PATCH
REVOGADO_FALHA_INFRAESTRUTURA, REVOGADO_MANUALMENTE, REVOGADO_OUTRO, REVOGADO_SEGURANCA_INTERNA, REVOGADO_VALIDADE_EXPIRADA
/open-banking/enrollments/v
x
/enrollments/{enrollmentId}
v2
REVOGADO_OUTRO
rp
"Relying Party" (RP) onde reside originalmente na requisição FIDO
Deve ser preenchido com a mesma string definida em ".data.rp"
string
CLIENT
Todos

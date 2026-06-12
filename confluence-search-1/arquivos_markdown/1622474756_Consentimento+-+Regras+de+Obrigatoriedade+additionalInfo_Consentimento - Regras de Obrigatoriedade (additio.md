---
                            title: "Consentimento - Regras de Obrigatoriedade (additionalInfo) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1622474756_Consentimento+-+Regras+de+Obrigatoriedade+additionalInfo"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1622474756/Consentimento+-+Regras+de+Obrigatoriedade+additionalInfo"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Consentimento - Regras de Obrigatoriedade (additionalInfo) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

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
Consentimento
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
companyProfileInfo
Objeto JSON que representa o perfil da Pessoa Jurídica (PJ) do cliente, contendo informações como a natureza jurídica e o porte da empresa, conforme a classificação oficial da Receita Federal do Brasil.
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
/open-banking/consents/v
x
/consents
v3
N/A
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
/open-banking/consents/v
x
/consents
v3
4
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
/open-banking/consents/v
x
/consents
v3
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
DELETE
/open-banking/consents/v
x
/consents
/open-banking/consents/v
x
/consents/{consentId}
/open-banking/consents/v
x
/consents/{consentId}/extensions
/open-banking/consents/v
x
/consents/{consentId}/extends
v3
100
^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:[a-zA-Z0-9()+,\-.:=@;$_!*'%\/?#]+$
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
/open-banking/consents/v
x
/consents
v3
NO_CREDENTIAL
journeyIsLinked
Indica que o consentimento é vinculado a outro em uma Jornada Otimizada
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.isLinked”, retornado após a chamada inicial na API “POST /consent” (Pagamentos Automáticos) ou “POST /enrollments” (Jornada Sem Redirecionamento) em caso de Jornada Otimizada
Em casos em que a informação não está disponível espera-se o envio do valor FALSE.
string
CLIENT
Todos
POST
GET
TRUE, FALSE
/open-banking/consents/v
x
/consents
/open-banking/consents/v
x
/consents/{consentId}
v3
FALSE
personType
Identifica a natureza do solicitante em uma transação ou consentimento.
Se .data.businessEntity estiver preenchido no payload, se estiver então preencher com "PJ", se não estiver então preencher com "PF"
string
CLIENT
Todos
POST
PESSOA_JURIDICA, PESSOA_NATURAL, PF, PJ
/open-banking/consents/v
x
/consents
v3
PJ
status
Identifica o status atual do recurso (como um consentimento ou um pagamento) que está sendo reportado.
Deve ser preenchido com a mesma string obtida no ".data.status". Caso a informação esteja em formato de lista, enviar apenas o valor do primeiro item da lista
string
CLIENT
Todos menos 4xx e 5xx
GET
AUTHORISED, AWAITING_AUTHORISATION, REJECTED
/open-banking/consents/v
x
/consents/{consentId}
v3
AUTHORISED
tokenId
Identificador único e criptograficamente seguro do token utilizado no consumo da API.
A implementação do tokenId preencherá a lacuna de rastreabilidade, permitindo vincular a emissão de cada token (incluindo os de CLIENT_CREDENTIALS) às suas respectivas jornadas, mesmo quando múltiplos consentimentos forem iniciados por um único token. Isso resultará em uma visão mais completa da jornada do token, aprimorando a capacidade de rastreabilidade e análise operacional para as instituições e do ecossistema
O tokenId será gerado pelo cliente (role CLIENT) no momento do reporte para a PCM, aplicado um hash SHA256 sobre o token recebido e um Pepper (segredo) gerenciado internamente pela instituição. Este tokenId deve ser reportado na PCM, complementando as informações já existentes de grant_type e consentId (onde aplicável). Para garantir a robustez criptográfica do hash, o Pepper utilizado deverá ser um valor aleatório e criptograficamente forte, gerenciado internamente pela instituição. Recomenda-se um tamanho de 128 a 256 bits para o Pepper, aplicado no cálculo do tokenId, como por exemplo, SHA256 (token + Pepper). O tokenId será composto pelos 72 bits iniciais do hash Base64URL-safe encoded.
Importante:
O tokenId será gerado apenas quando o token for recebido com sucesso na resposta do POST /token. Em casos nos quais a requisição ao POST /token resultar em erros 4xx ou 5xx, o token não será obtido e, consequentemente, o tokenId não poderá ser gerado. Nessas situações, o campo tokenId deve ser omitido do reporte à PCM.
string
CLIENT
Todos
Todos
/open-banking/consents/v
x
/consents
/open-banking/consents/v
x
/consents/{consentId}
/open-banking/consents/v
x
/consents/{consentId}/extends
/open-banking/consents/v
x
/consents/{consentId}/extensions
v3
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

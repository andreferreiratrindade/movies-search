---
                            title: "Adaptações para consultas de recursos entre as versões 1.0.0 e 2.2.0 ou superiores da API Pagamentos Automáticos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1178042602_Adapta+es+para+consultas+de+recursos+entre+as+vers+es+1.0.0+e+2.2.0+ou+superiores+da+API+Pagamentos+Autom+ticos"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1178042602/Adapta+es+para+consultas+de+recursos+entre+as+vers+es+1.0.0+e+2.2.0+ou+superiores+da+API+Pagamentos+Autom+ticos"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Adaptações para consultas de recursos entre as versões 1.0.0 e 2.2.0 ou superiores da API Pagamentos Automáticos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Introdução e objetivo
A introdução do produto Pix Automático resultou no versionamento da API Pagamentos Automáticos para contemplar a operação desse novo produto. Foram implementadas diversas alterações (disponíveis para consulta nas páginas de changelog de cada versão), porém, devido a características inerentes do consentimento dessa API, certos aspectos requerem observação durante a operação de recursos pertencentes a versões anteriores. Estes pontos são abordados nas seções subsequentes.
Este documento complementa o changelog da API e define quais operações podem ser realizadas entre as versões e quais não podem. Além disso, detalha o tratamento a ser aplicado a cada um dos campos que apresentam alguma mudança em suas regras de negócio ou técnicas significativas para a execução das consultas de recursos no Open Finance.
Ressalta-se que a versão 1.0.0 da API Pagamentos Automáticos permitia a operação apenas do produto Transferências Inteligentes, portanto, as adequações especificadas neste documento aplicam-se predominantemente às consultas de operações deste produto.
Orientações Gerais
Será permitido que uma transação de pagamento seja iniciada usando o
endpoint
POST /recurring-consents da versão 1.0.0 e finalizada com o
endpoint
POST /pix/recurring-payments da versão 2.1.0;
Adicionalmente, consentimentos existentes antes da versão 2.1.0 podem continuar a ser utilizados (observação: consentimentos da v1 são aplicáveis apenas a Transferências Inteligentes)
Não será permitido que uma transação de pagamento seja iniciada usando o
endpoint
POST /recurring-consents da versão 2.0.0 e finalizada com o
endpoint
POST /pix/recurring-payments da versão 1.0.0;
Neste cenário, deve-se retornar o código de erro HTTP 422 com os seguintes detalhes:
code
: PAGAMENTO_RECUSADO_DETENTORA;
detail
: Divergência entre versões de consentimento e pagamentos.
Não será permitido que um pagamento que foi agendado utilizando os
endpoints
da versão 2.1.0 seja consultado usando os
endpoint
GET /pix/recurring-payments/{recurringPaymentId} ou GET /pix/recurring-payments/ da versão 1.0.0;
Neste cenário, deve-se retornar o código de erro HTTP 400.
Obs: A funcionalidade de agendamento é única do Pix Automático, não sendo escopo da versão 1.0.0.
Não será permitido que um pagamento  criado utilizando os
endpoints
da versão 2.1.0 seja consultado usando os
endpoint
GET /pix/recurring-payments/{recurringPaymentId} ou GET /pix/recurring-payments/ da versão 1.0.0;
Neste cenário, deve-se retornar o código de erro HTTP 400.
Não será permitido que o consentimento de um pagamento criado utilizando os
endpoints
da versão 2.0.0 seja consultado usando o
endpoint
GET/recurring-consents/{recurringConsentId} da versão 1.0.0;
Neste cenário, deve-se retornar o código de erro HTTP 400.
Será permitido a revogação de consentimentos criados na versão 1.0.0 utilizando o endpoint PATCH /recurring-consents/{recurringConsentId} da versão 2.1.0.
Pagamentos e consentimentos criados em versões anteriores poderão ser consultados nos
endpoints
GET /recurring-consents/{recurringConsentId}, GET /pix/recurring-payments/ e GET /pix/recurring-payments/{recurringPaymentId} da versão 2.1.0;
Orientações Específicas
1. Análise Comparativa do corpo de resposta do GET /recurring-consents/{recurringConsentId} entre as Versões 1.0.0 e 2.1.0 (Ignorando formatação e riskSignals)
1.1
Campos Adicionados na Versão 2.0.0:
Campo (XPath)
Obrigatoriedade
Tipo de Dado
Descrição
Ação
Campo (XPath)
Obrigatoriedade
Tipo de Dado
Descrição
Ação
data>authorisedAtDateTime
Opcional
date-time
Obrigatório quando o consentimento transita para
AUTHORISED
.
Não enviar o campo no retorno.
data>updatedAtDateTime
Opcional
date-time
Data/hora de atualização pelo usuário pagador (aplicável apenas para edições no Pix Automático).
Não enviar o campo no retorno.
data>approvalDueDate
Opcional
date
Data máxima para aprovação de consentimentos em
PARTIALLY_ACCEPTED
.
Não enviar o campo no retorno.
data>recurringConfiguration>sweeping>useOverdraftLimit
Obrigatório
boolean
Indica se o usuário autorizou uso de limite pré-aprovado (cheque especial).
Se a instituição possui o cheque especial e o cliente dono do consentimento possui o produto cheque especial, o valor retornado deve ser
true
, caso contrário,
false
. Recomendamos que os cliente sejam avisados da modificação sobre seu consentimento passar a utilizar cheque especial.
data>recurringConfiguration>sweeping>startDateTime
Obrigatório
date-time
Se não enviado, assume o valor de
creationDateTime
.
Consentimentos da versão 1 consultados na versão 2, que não possuem o campo
data>recurringConfiguration>sweeping>startDateTime
definido, devem retornar no campo
data>recurringConfiguration>sweeping>startDateTime
o valor presente no campo
data>recurringConfiguration>sweeping>creationDateTime
. Isso representa um consentimento criado com validade a partir da data de criação.  <br>Caso já exista valor no campo, este deve ser retornado.
1.2
Campos Modificados (Mudanças de Conteúdo):
Campo (XPath)
Versão 1.0.0
Versão 2.0.0
Ação
Campo (XPath)
Versão 1.0.0
Versão 2.0.0
Ação
data>expirationDateTime
Sem restrição específica.
Nova regra:
Para Pix Automático, horário deve ser
23:59:59 UTC
.
Sem ação. Devolver valor atual caso exista.
data>creditors[0]
Sem regras de validação específicas.
Novas regras:
CPF do credor deve ser igual ao do
loggedUser
(pessoa física).
CNPJ deve ter a mesma raiz do
businessEntity
(pessoa jurídica).
Sem ação. Devolver valor atual.
data>debtorAccount>ibgeTownCode
Obrigatório apenas para
recurringConfiguration
"automatic".
Ampliação:
Obrigatório também quando o consentimento passar por
AUTHORISED
.
Sem ação. Devolver valor atual.
data>rejection>reason>code
Valores do enum sem
AUTENTICACAO_DIVERGENTE
.
Novo valor:
AUTENTICACAO_DIVERGENTE
(autenticação divergente).
Sem ação. Devolver valor atual.
data>status
Descrição sem menção a transições de estado.
Adição de contexto sobre máquina de estados (ex:
PARTIALLY_ACCEPTED
).
Sem ação. Devolver valor atual.
1.3
Campos Modificados (Mudanças de obrigatoriedade):
Campo (XPath)
Versão 1.0.0
Versão 2.0.0
Ação
Campo (XPath)
Versão 1.0.0
Versão 2.0.0
Ação
data>recurringConfiguration>sweeping>startDateTime
(antigo  <br>
data>startDateTime)
Opcional
Obrigatório
Sem ação. Devolver valor atual.
2. Análise Comparativa do corpo de resposta do GET /pix/recurring-payments/{recurringPaymentId} entre as Versões 1.0.0 e 2.1.0
2.1. Campos Adicionados na Versão 2.0.0
Campo (XPath)
Obrigatoriedade
Tipo de Dado
Descrição (Regras Novas)
Ação
Campo (XPath)
Obrigatoriedade
Tipo de Dado
Descrição (Regras Novas)
Ação
data>proxy
opcional
string
Chave Pix do recebedor (CPF, CNPJ, e-mail, etc.). Obrigatório se
localInstrument=DICT
.
Se a transação exigiu o envio do proxy pelo ITP para ocorrer a liquidação na v1, o campo deverá ser retornado durante a consulta à v2.
data>localInstrument
obrigatório
enum
Define a forma de iniciação do pagamento (
MANU
,
DICT
,
INIC
).
O campo deverá ser retornado durante a consulta à v2 com o valor original informado na sua criação.
data>originalRecurringPaymentId
opcional
string
Identificador da tentativa original de pagamento que falhou (obrigatório para retentativas).
Sem ação
data>paymentReference
opcional
string
Referência da recorrência (ex:
W50-2024
para pagamentos semanais).
Sem ação
2.2 Campos Removidos na Versão 2.0.0
Campo (XPath)
Motivo/Observação
Ação
Campo (XPath)
Motivo/Observação
Ação
data>ibgeTownCode
Não está presente na versão 2.0.0 (removido em detrimento de sua presença já existir no consentimento).
Sem ação
2.3. Campos Modificados (Regras/Descrições)
Campo (XPath)
Versão 1.0.0
Versão 2.0.0
Ação
Campo (XPath)
Versão 1.0.0
Versão 2.0.0
Ação
data>endToEndId
Sem menção a Pix Automático.
Nova regra:
Para Pix Automático, deve usar data agendada e horário fixo
15:00 UTC
.
Sem ação
data>status
PDNG
aplicável a qualquer cenário.
PDNG
não se aplica a
Transferências Inteligentes
.
Sem ação
data>rejectionReason>code
14 opções de códigos de rejeição.
Novos códigos adicionados:
LIMITE_VALOR_TOTAL_CONSENTIMENTO_EXCEDIDO
,
LIMITE_VALOR_TRANSACAO_CONSENTIMENTO_EXCEDIDO
,
CONSENTIMENTO_REVOGADO
,
FORA_PRAZO_PERMITIDO
,
DETALHE_TENTATIVA_INVALIDO
,
DETALHE_PAGAMENTO_INVALIDO
.
Sem ação
data>cancellation>reason
Incluía
CANCELADO_MULTIPLAS_ALCADAS
.
Remoção de valor:
CANCELADO_MULTIPLAS_ALCADAS
não está mais disponível.
Sem ação. Era um bug de especificação que não deveria ocorrer desde o nascimento do produto, uma vez que nunca foi possível ter múltipla alçada no pagamento em si, apenas no consentimento.
data>transactionIdentification
Sem restrições específicas.
Nova restrição:
Campo condicional baseado em
localInstrument
(ex: obrigatório para
INIC
).
Se a transação exigiu o envio do transactionIdentification pelo ITP para ocorrer a liquidação na v1, o campo deverá ser retornado durante a consulta à v2.
data>document>rel
Sem enumeração explícita.
Enum adicionado:
[ CPF, CNPJ ]
.
Sem ação
data>date
Descrição genérica sobre data do pagamento.
Formato explícito:
Timezone
UTC-3
e formatação RFC-3339.
Sem ação
2.4. Campos Modificados (Obrigatoriedade)
Campo (XPath)
Versão 1.0.0
Versão 2.0.0
Ação
data>creditorAccount
Opcional
Obrigatório
Ensejou o versionamento para versão 2.1.0, lançada em 25/04, tornando o campo opcional nos retornos de consulta de pagamento.
data>localInstument
Inexistente na consulta
Obrigatório
O campo deverá ser retornado durante a consulta à v2 com o valor original informado na sua criação.
Conclusão:
Adotando as ações necessárias, as consultas de recursos entre as versões (anterior e recente) devem ocorrer de forma suave pelas ITPs e Detentoras que sigam as especificações e realizem as adequações de retrocompatibilidade.

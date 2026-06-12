---
                            title: "Orientações - [DC] Contas - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1739096252_Orienta+es+-+DC+Contas"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1739096252/Orienta+es+-+DC+Contas"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Orientações - [DC] Contas - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Obrigatoriedade de informações de contraparte
2
Orientações sobre o transactionId
3
Identificador de transações
4
QUANTO AO ERRO 422
5
Tabela descritiva das possibilidades de interação entre API de Recursos (Resources) e API Contas (Accounts)
6
Exemplos de casos de uso de contas e o respectivo status a ser informado pela API Resources
7
Orientações sobre Dados do Empregador
8
Orientações para campo type nos
endpoints
de transações
9
Orientações sobre Reservas de saldo
10
Orientações para compartilhamento de contas e suas transações
Obrigatoriedade de informações de contraparte
Com a IN BCB nº 371, a partir de 02/05/23, o envio das informações de identificação de contraparte (CPF ou CNPJ) tornou-se obrigatória para transações de pagamento conforme os tipos de transações da tabela abaixo.
#
Tipo de transação
Envio da informação da contraparte pagador (S/N) -creditDebitType= CRÉDITO
Envio da informação da contraparte recebedor (S/N) -creditDebitType= DÉBITO
Observação
#
Tipo de transação
Envio da informação da contraparte pagador (S/N) -creditDebitType= CRÉDITO
Envio da informação da contraparte recebedor (S/N) -creditDebitType= DÉBITO
Observação
1-
TED
S
S
Existem transações em lote* onde as informações únicas de contraparte não são identificadas para o cliente
2-
DOC
N
N
3-
PIX
S
S
No caso de transações em lote*, as informações únicas de contraparte não são identificadas para o cliente.
4-
TRANSFERÊNCIA MESMA INSTITUIÇÃO
S
S
5-
BOLETO
R
S
No caso de transações em lote*, as informações únicas de contraparte não são identificadas para o cliente
6-
CONVÊNIO ARRECADAÇÃO
R
S
No caso de transações em lote*, as informações únicas de contraparte não são identificadas para o cliente. Caso a instituição possuam a contraparte recebedor, poderá ser enviado
7-
PACOTE TARIFA SERVIÇOS
N
N
O beneficiário é a própria instituição financeira onde o cliente detém a conta
8-
TARIFA SERVIÇOS AVULSOS
N
N
O beneficiário é a própria instituição financeira onde o cliente detém a conta
9-
FOLHA DE PAGAMENTO
S
R
No caso de transações em lote*, as informações únicas de contraparte não são identificadas para o cliente
10-
DEPOSITO
S
N
Pagador existe informação de contraparte apenas em transações acima de R$2.000 (Circular 3978 de 2020)
11-
SAQUE
N
N
Estas operações não entram na classificação de transação de pagamento
12-
CARTÃO
S e N*
N
*Para pagamento de fatura: há informação da contraparte. Para cartão de débito e pré-pago: não há informação de contraparte por parte da bandeira (protocolo das bandeiras)
13-
ENCARGOS JUROS CHEQUE ESPECIAL
N
N
O beneficiário é a própria instituição financeira onde o cliente detém a conta
14-
RENDIMENTO_APLIC_FINANCEIRA
N
N
Estas operações não entram na classificação de transação de pagamento
15-
PORTABILIDADE SALÁRIO
N
N
O beneficiário é o próprio portador. Observar a forma de transferência do recurso
16-
RESGATE APLICAÇÃO FINANCEIRA
N
N
Estas operações não entram na classificação de transação de pagamento
17-
OPERAÇÃO DE CRÉDITO
N
N
Existe uma API dedicada às operações de crédito
18-
TRANSFERÊNCIA SALDOS RESERVADOS
N
N
19-
OUTROS
N
N
Preencher em casos que houver informação de contraparte
Legenda:
N –Envio não obrigatório; S –Envio obrigatório; R –Em avaliação pelo Banco Central
*transações em lote tratam-se da possibilidade de clientes do tipo pessoa jurídica efetuarem pagamentos e transferências de forma agrupadas, ou seja, 1 débito para N créditos.
Abaixo encontramos os casos de exceções à obrigatoriedade de envio da contraparte: ​
Tipo de transação TED quando se tratar de Transferência entre Reservas (STR0004); ​
Recebimento de recursos judiciais (STR0051R2);
Pagamento decorrente de Convênio de Arrecadação na qual a contraparte é um banco correspondente (Neste caso o pagador não necessita enviar a contraparte);
Transferência para depósito judicial (STR0025);
Depósito em cheque, e compra e venda de cheque (Neste caso não é necessário envio de contraparte do pagador e recebedor);
Crédito em conta por motivo de rejeição de Pix, ou seja, uma transação que tem como causa uma tentativa anterior de débito na mesma conta, também realizada via Pix, a qual foi recusada pelo PSP recebedor.
Orientações sobre o transactionId
O identificador de transação pode ser reutilizado e alterado exclusivamente para transações nos status TRANSACAO_PROCESSANDO e LANCAMENTO_FUTURO. Nas situações em que uma transação com status de TRANSACAO_PROCESSANDO e LANCAMENTO_FUTURO não possuir número de identificador próprio, a instituição deve utilizar o identificador 0000000000 para identificar todas as transações que ainda serão confirmadas.
Identificador de transações
O envio do campo transactionId nos
endpoints
de transações é obrigatório no Open Finance Brasil. O identificador de transação é obrigatório em D0 para todos os tipos de transação. Já a imutabilidade se dá de acordo com a tabela abaixo:
Tipo de Transação
Data da Obrigatoriedade
Data da Imutabilidade
Tipo de Transação
Data da Obrigatoriedade
Data da Imutabilidade
TED
D0
D0
PIX
D0
D0
TRANSFERENCIA MESMA INSTITUIÇÃO (TEF)
D0
D0
TARIFA SERVIÇOS AVULSOS
D0
D0
FOLHA DE PAGAMENTO
D0
D0
DOC
D0
D+1
BOLETO
D0
D+1
CONVÊNIO ARRECADAÇÃO
D0
D+1
PACOTE TARIFA SERVIÇOS
D0
D+1
DEPÓSITO
D0
D+1
SAQUE
D0
D+1
CARTÃO
D0
D+1
ENCARGOS JUROS CHEQUE ESPECIAL
D0
D+1
RENDIMENTO APLICAÇÃO FINANCEIRA
D0
D+1
PORTABILIDADE SALÁRIO
D0
D+1
RESGATE APLICAÇÃO FINANCEIRA
D0
D+1
OPERAÇÃO DE CRÉDITO
D0
D+1
OUTROS
D0
D+1
Data de imutabilidade por tipo de transação
Abaixo a descrição dos possíveis status que uma transação pode ter:​
TRANSACAO_EFETIVADA - corresponde a data de processamento/efetivação da transação​
LANCAMENTO_FUTURO - corresponde a data prevista de efetivação da transação​
TRANSACAO_PROCESSANDO – corresponde a data de lançamento da transação
Para as transações que podem ter seu identificador alterado, conforme regras delimitadas, os comportamentos abaixo devem ser seguidos: ​
Quando a documentação menciona “Dias”, exemplo: D+1, ela está se referindo ao dia calendário e não a uma janela de 24 horas. Lembrando que cada instituição pode definir seu horário de processamento diário para transações.
O identificador “provisório” compartilhado em D0 deve ser alterado para o identificador definitivo em D+1
:​
Importante considerar que as instituições financeiras tem diferentes formas de tratar feriados ao processar transações. Umas consideram apenas feriados nacionais e outras consideram feriados regionais. ​
Para transações em D+1 com status TRANSACAO_EFETIVADA entende-se que D+1 diz respeito a dias úteis.
Não devem ser compartilhados ao mesmo tempo o identificador provisório e o identificador definitivo, ou seja, após a alteração do status da transação para TRANSACAO_EFETIVADA, somente a transação com o identificador definitivo deve ser exposta.​
A data e o valor da transação podem ser alterados na mudança do status para TRANSACAO_EFETIVADA, de acordo com os processos internos existentes nas instituições. Por exemplo: Resgates de investimentos sem liquidez, e Compra e Venda de ações. ​
A propriedade de identificador de transação único, estável e  imutável passa a vigorar a partir do momento em que o status da transação passa a ser TRANSACAO_EFETIVADA. Entretanto:​
Não se deve ter o mesmo identificador entre transações em diferentes status. Por exemplo, não é possível se ter ao mesmo tempo o identificador 123 sendo utilizado para transações no status TRANSACAO_PROCESSANDO e TRANSACAO_EFETIVADA, mesmo que os valores e datas sejam distintos.​
Especificamente nos casos de transações no status LANÇAMENTO_FUTURO a data do campo transactionDateTime deve ser enviado com as informações de dia/mês/ano prevista para o processamento da transação e os demais campos de precisão da data/hora podem ser enviados como 0 (00:00:00.000).​
O identificador de transação pode se repetir apenas para transações em status TRANSACAO_PROCESSANDO e LANCAMENTO_FUTURO. Ou seja, uma instituição pode utilizar, por exemplo, o identificador 9999999 para identificar todas as transações que ainda serão confirmadas (status TRANSACAO_PROCESSANDO).
Para as transações que não podem ter seu identificador alterado, conforme regras delimitadas, há exceções mapeadas:  ​
Existem situações, principalmente para clientes Pessoa Jurídica, nas quais as transações são lançadas de forma individual (múltiplas transações) em D0 e em D+1 são consolidadas em um único lançamento. Também podemos ter o cenário oposto, no qual a transação é lançada de forma consolidada em D0 e em D+1 “abertas” em múltiplos lançamentos individuais. É importante que não haja duplicidade de informações na exposição, ou seja, as transações individuais e a transação consolidada não sejam expostas ao mesmo tempo. ​
Por exemplo, para transações de boleto, pix ou folha de pagamento, em D0 são feitos lançamentos individuais com TransactionId individuais, e em D+1 é efetuado lançamento único com um novo transactionID. ​
Existem situação de exceção nas quais um lançamento com identificador estável em D0 pode ser eliminado em D+1. ​
Por exemplo, para situações de cobrança de tarifa avulsa nas quais existe acordo negocial ou insuficiência de saldo.
QUANTO AO ERRO 422
Na especificação técnica existe a possibilidade de retornar o código HTTP Status Code 422 - accepted. Este código de retorno deve ser utilizado quando algum parâmetro da consulta for enviado semanticamente incorreto, ou seja, desrespeitando uma regra de negócio, para os seguintes
endpoints
:
/accounts/{accountId}/transactions;
/accounts/{accountId}/transactions-current.
Tabela descritiva das possibilidades de interação entre API de Recursos (Resources) e API Contas (Accounts)
Cenário
Status Conta
API Recursos
API Listagem Contas
APIs Dados Contas
Code
Cenário
Status Conta
API Recursos
API Listagem Contas
APIs Dados Contas
Code
Sem consentimento
-
401 UNAUTHORIZED
401 UNAUTHORIZED
401 UNAUTHORIZED
Com consentimento não autorizado
-
401 UNAUTHORIZED
401 UNAUTHORIZED
401 UNAUTHORIZED
Com consentimento autorizado (pendente múltipla alçada)
-
200 Retorna recurso com status PENDING_ AUTHORISATION
200 Não retorna conta
403 FORBIDDEN
STATUS_RESOURCE_PENDING_AUTHORISATION
Com consentimento autorizado (aprovado múltipla alçada)
OK
200 Retorna o recurso com status AVAILABLE
200 Retorna a conta
200 Retorna dados
Com consentimento autorizado (aprovado múltipla alçada)
Bloqueio
200 Retorna o recurso com status TEMPORARY_UNAVAILABLE
200 Não retorna conta
403 FORBIDDEN
STATUS_RESOURCE_TEMPORARY_UNAVAILABLE
Com consentimento autorizado (aprovado múltipla alçada)
Encerrada/Migrada
200 Retorna o recurso como status UNAVAILABLE
200 Não retorna conta
403 FORBIDDEN
STATUS_RESOURCE_UNAVAILABLE
Com consentimento autorizado (recusado múltipla alçada)
-
200 Retorna o recurso como status UNAVAILABLE
200 Não retorna conta
403 FORBIDDEN
STATUS_RESOURCE_UNAVAILABLE
Com consentimento autorizado (conta inexistente)
-
200 Não retorna na lista
200 Não retorna conta
403 FORBIDDEN
RESOURCE_FORBIDDEN
Com consentimento revogado ou expirado*
-
401 UNAUTHORIZED
401 UNAUTHORIZED
401 UNAUTHORIZED
*Para os cenários de consentimento revogado ou expirado, conforme determinado na especificação de segurança o access token associado ao mesmo é invalidado impossibilitando a consulta as APIs produtos por parte da Receptora.
Exemplos de casos de uso de contas e o respectivo status a ser informado pela API Resources
Contas que se encontram em plena utilização e disponível nos canais de atendimento eletrônico devem ter seu status como AVAILABLE.
Conta cancelada/encerrada nos últimos 12 meses anteriores da data consulta – considerando o consentimento vigente - devem ter seus status como AVAILABLE.
Conta cancelada/encerrada a mais que 12 meses anteriores da data consulta –considerando o consentimento vigente - devem ter seus status como UNAVAILABLE.
Conta cancelada/encerrada, em situações nas quais o cliente não mais possua acesso aos canais de atendimento eletrônico da instituição, devem retornar o status UNAVAILABLE.
Conta que se encontra em bloqueio temporário, onde o cliente não possui acesso aos detalhes por meio dos canais de atendimento eletrônico, devem retornar o status TEMPORARILY_UNAVAILABLE.
Conta que se encontra em bloqueio definitivo onde o cliente não possui acesso por meio dos canais de atendimento eletrônico, devem retornar o status UNAVAILABLE.
Contas com bloqueios nas quais o cliente tenha acesso aos detalhes da conta por meio dos canais eletrônicos da instituição devem ter seu status como AVAILABLE.
Casos de uso que um cliente final efetue um consentimento para Conta para o qual um dos recursos (respeitando a RN001) exija a aprovação de múltiplas alçadas (PENDING_AUTHORISATION) e outro recurso esteja disponível para consulta (AVAILABLE), o comportamento esperado é que cada recurso tenha seu status representado de forma independente, disponibilizando imediatamente os recursos já aprovados.
Conforme a identificação de cenários pelas instituições a lista de exemplos de casos de uso de Contas e o respectivo status a ser informado pela API Resources pode ser complementada.
Orientações sobre Dados do Empregador
Para os
endpoints
/transactions e /transactions-current, no caso do tipo de transação FOLHA_PAGAMENTO, o conteúdo do campo partieCnpjCpf obrigatoriamente deve ser o CPF ou CNPJ do empregador quando a transmissora for a responsável pelo pagamento de salário (banco-folha).
Não é obrigatório o reprocessamento de histórico para o campo partieCnpjCpf. Já para transações que ocorrerem a partir de 15/08/2024, é esperado que o campo /partieCnpjCpf seja preenchido com informação do empregador, caso o campo type, seja FOLHA_PAGAMENTO.
Orientações para campo type nos
endpoints
de transações
O tipo de transação PORTABILIDADE_SALARIO deverá ser usada apenas quando houver uma transação entre instituições de conglomerados distintos devido à realização da portabilidade de salário entre essas duas instituições.
Recomenda-se o uso do tipo de transação RESGATE_APLIC_FINANCEIRA para transações de resgates/liquidação de investimento.
Orientações sobre Reservas de saldo
Está no escopo de compartilhamento da API Contas: Reservas sem rendimento, como forma se separar dinheiro para gasto futuro, e Reservas com rendimento, mas não atreladas a um investimento associado ao CPF/CNPJ do cliente. Como exemplos de nomenclatura para reserva, temos: caixinhas, cofrinhos, saldo separado. Reservas que estão atreladas a um investimento associado ao CPF/CNPJ do cliente devem ser compartilhadas nas APIs de Investimentos.
Reserva de saldo faz parte do mesmo agrupamento de
permissions
que saldo. Ou seja, quando o cliente concede permissões para acesso de consulta a saldo, ele também estará dando consentimento para consultas a reserva de saldo.
Os dados enviados no
endpoint
GET /accounts/{accountId}/reserved-balances devem seguir as definições abaixo:
Se houver diferentes remunerações atreladas a aportes na mesma reserva de saldo, a listagem availableAmount deve possuir um item para cada faixa de remuneração. Por exemplo, se um cliente possuir R$ 30.000 de saldo reservado, sendo que, deste valor, R$ 10.000 rendem 100% do CDI e R$ 20.000 rendem 110% do CDI, a listagem availableAmount deve vir com dois itens: um com saldo R$ 10.000, informando o rendimento 100% do CDI, e outro com saldo R$ 20.000, informando o rendimento 110% do CDI.
Para reserva de saldo com o saldo zerado, a listagem availableAmount deve conter um item explícito com o saldo R$ 0,00. O objeto remuneration não deve ser enviado nesse caso.
Nos casos em que o produto é ofertado pela transmissora mas o cliente não possui reserva de saldo, a listagem do
endpoint
reserved-balances deve vir vazia, com status code 200.
Para instituições que não possuam o produto reserva de saldo e não exista o cadastro da funcionalidade no diretório, deve ser retornado o HTTP Status Code 404 – Not Found, seguindo os padrões de response para as APIs do ecossistema.
Orientações para compartilhamento de contas e suas transações
Em caso de encerramento de conta, se o cliente ainda tiver acesso ao canal eletrônico e houver transações nos últimos 12 meses, os dados devem continuar sendo compartilhados.
As transações apresentadas precisam ser as mesmas apresentadas nos canais digitais da instituição. Caso a instituição possua mais de um canal digital, a informação compartilhada deve ser a do canal que apresenta as informações mais completas possíveis sobre as transações.
Quando a especificação se refere a 12 meses, ela está se referindo ao ano Civil que em anos comuns tem o total de 365 dias e em anos bissextos 366 dias.
O envio do campo /data/codeISPB deve ser considerado, seguindo a restrição estabelecida na descrição do campo, nas transações que ocorrerem após o go-live da versão 2.5.0, não sendo obrigatório o reprocessamento de histórico de transações para preenchimento da informação, mesmo que a instituição possua a informação para a mesma.
A nova restrição adicionada a descrição do campo /data/partieCompeCode deve ser considerada somente nas transações que ocorrerem após o go-live da versão 2.5.0, não sendo obrigatório o reprocessamento de histórico de transações para preenchimento da informação.

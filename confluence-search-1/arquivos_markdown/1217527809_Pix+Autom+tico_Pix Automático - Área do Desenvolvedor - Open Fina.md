---
                            title: "Pix Automático - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1217527809_Pix+Autom+tico"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1217527809/Pix+Autom+tico"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Pix Automático - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1 - Introdução
1.1 - Sobre o documento
Este guia auxiliará os implementadores a compreenderem as funcionalidades de criação do consentimento com pagamento inicial avulso ou sem no momento da contratação do serviço ou produto. Para o processo de liquidação dos pagamentos, abordaremos o funcionamento da primeira ordem de pagamento de um ciclo de cobrança, das tentativas no mesmo dia e das tentativas em dias subsequentes. Além disso, também temos as regras de negócio que compõe o produto no âmbito do Open Finance.
Não é o objetivo que a leitura deste documento substitua a leitura de outros documentos de igual importância. Recomendamos a leitura de todos os documentos relacionados para permitir o correto entendimento sobre a operação deste produto. Alguns exemplos de documentos importantes:
Normativo/Manual/Documento
Tema
Normativo/Manual/Documento
Tema
Resolução Conjunta Nº 1, Versão vigente compilada (v7)
Dispõe sobre a implementação do Open Finance.
Instrução Normativa BCB Nº 512
Dispõe sobre os limites de valor para as transações no âmbito do Pix.
Instrução Normativa BCB Nº 513
Estabelece os procedimentos operacionais relativos ao Pix Automático.
Diretrizes Técnicas e Operacionais do Open Finance
Dispõe sobre procedimentos técnicos e operacionais aos quais as instituições devem adotar (Inclui orientações para reportes à PCM, o Guia De Experiencia, entre outros).
1.2 - Pix Automático
É uma solução que permite o recebedor solicitar o pagamento de cobranças recorrentes de maneira automatizada. Isso ocorre após o usuário pagador conceder permissão ao recebedor, no contexto do serviço contratado. A funcionalidade possibilita que o recebedor PJ, através de seu Iniciador, envie regularmente os detalhes das cobranças recorrentes ao PSP do Pagador (dentro de uma periodicidade previamente definida). Este, por sua vez, agenda o débito e efetua a liquidação automaticamente na data programada, conforme o contrato de serviços estabelecido entre usuário pagador e recebedor.
A implementação do Pix Automático é obrigatória para as detentoras que atendem clientes PF e PJ, porém, instituições que atendem apenas clientes PJ ou que não desejem ofertar o produto para o público PJ, podem realizar o
optout
junto ao BCB, conforme especificado na IN BCB 581, de 30/12/2024.
Essa funcionalidade está presente na API de pagamentos automáticos, a partir de sua versão 2.0.0. O link para a API pode ser encontrado abaixo.
Pagamentos automáticos
2 - Regras para
Pix Automático
no
OFB
2.1 - Regras de negócio:
No quadro abaixo podemos observar as regras de negócio definidas para o produto Pix Automático no âmbito do Open Finance.
Cenários
Pix Automático
Cenários
Pix Automático
Casos de uso
(Sugestões BC)
Utilities/serviços públicos, assinaturas, escolas, academias, aluguel, seguros, cobranças de pagamento de operação de crédito
Configurações de recorrência
Motor de recorrência
Criação de um consentimento para recorrência com limites de valores e prazos, e definição de periodicidade
Valor
Fixo ou variável
Modelo de recorrência, intervalos de pagamentos
Semanal, mensal, trimestral, semestral e anual
Gestão da Agenda
Compartilhada: Iniciador tem visibilidade completa, PSP pagador tem visibilidade com antecedência de 2 a 10 dias das próximas incidências
Comanda o pagamento
Iniciador
Recebedor
PJ
Pagamento inicial avulso
Imediato ou Agendado
Demais pagamentos
Agendado
Permite pagamentos imediatos
Sim, apenas para pagamento inicial avulso
Definição do final do período da recorrência
Opcional
Prazo máximo de duração para recorrência do consentimento
Opcional
Permite a configurar data de início do consentimento?
Sim
Permite a configurar data de expiração do consentimento?
Sim
Permite limites globais do consentimento?¹
Não
Permite limites periódicos por consentimento?
Sim, uma transação liquidada com sucesso por período de recorrência.
Permite limites por transação?
Sim. Recebedor pode definir valor mínimo. Pagador pode definir um valor máximo. O valor definido pelo Pagador não pode ser menor que o valor definido pelo Recebedor.
Processo de consentimento
Tipo de fluxo
Consentimento FAPI
long-lived tokens
Role
no diretório
CONTA, PAGTO
Será possível editar configurações de recorrência no durante a autorização no Detentor?
Não
Revogação do consentimento
Via Iniciador ou Detentor
Permite múltiplas alçadas?
Sim
Iniciador terá acesso aos status do consentimento via Webhook?
Sim
Consentimento tem id de contrato?
Sim
Gestão do consentimento
Permite edição técnica dos dados do consentimento pós autorização?
Sim, verificar no
link
Revogação do consentimento
Pelo pagador, no ambiente da iniciadora ou detentora. Recebedor pode acionar o Iniciador para o cancelamento. Iniciador ou Detentor poderão revogar o consentimento por motivos de fraude.
Consumação do consentimento?
Responsabilidade do Detentor, quando o consentimento possuir data de expiração definida.
Processo de liquidação
Canal para liquidação
Serão utilizados os canais primário e secundário (obedecendo as regras da trilha Pix). Quem deverá criar o E2EID com a data da liquidação é o Iniciador.
Responsável pela liquidação na data do pagamento
Uma vez agendado pelo Iniciador, responsabilidade é do Detentor.
Onde o cliente cancela o pagamento?
Iniciadora ou Detentora
Erros de saldo insuficiente modificam o status do consentimento?
Erro de liquidação por esse motivo (em qualquer etapa do processo, do pagamento inicial avulso ao pagamento do ciclo) não modifica o estado do consentimento. Diferente da jornada 3 do arranjo Pix Automático, o qual prevê o cancelamento do processo de autorização em caso de falha.
Listagem das informações do pagamento
Busca por id do consentimento e por id de pagamento
Iniciador é responsável pelo envio da ocorrência do pagamento?
Sim, no prazo de 2 a 10 dias anteriores a data de vencimento da cobrança
Quem avisa o pagador sobre pagamento com falha?
Consultar o tópico sobre “Regras de notificações”
Responsável pela geração do endToEndId
Iniciador
Podem ocorrer liquidação em dias não úteis?
Sim
Qual é o localInstrument utilizado na liquidação?
MANU
Pode haver cobrança das recorrências antes da liquidação (com ou sem sucesso) do pagamento inicial avulso?
Só pode haver cobrança de recorrência após a data de liquidação do pagamento inicial avulso.
Como é calculada a janela de liquidação?
Depende da periodicidade e do dia informado como data de início do ciclo. A data de início de um ciclo representa a partir de quando um recebedor estará apto para enviar cobranças ao pagador e, de acordo com a periodicidade, é incrementada para o próximo ciclo.
Qual é a definição dos ciclos?
Um ciclo consiste de um intervalo de tempo onde uma cobrança pode ser realizada como compensação pelos produtos ou serviços que ensejam periodicidade. O primeiro ciclo inicia-se no dia informado no consentimento e deve ser acrescido, de acordo com a periodicidade, até o dia imediatamente anterior a data de início de um novo ciclo, por exemplo:
Periodicidade: Mensal
Data de início da recorrência: 22/09/2025
Primeiro ciclo: 22/09/2025 ~ 21/10/2025
Segundo ciclo: 22/10/2025 ~ 21/11/2025
Terceiro ciclo: 22/11/2025 ~ 21/12/2025
Caso a data do ciclo caia em um dia inexistente, deve-se considerar o primeiro dia anterior existente como data do ciclo, por exemplo:
Periodicidade: Mensal
Data de início da recorrência: 31/10/2025
Primeiro ciclo: 31/10/2025 ~ 29/11/2025
Segundo ciclo: 30/11/2025 ~ 30/12/2025
Terceiro ciclo: 31/12/2026 ~ 30/01/2026
Quarto ciclo: 31/01/2026 ~ 27/02/2026
Observação sobre fevereiro: Para anos bissextos as datas do ciclos de fevereiro, neste cenário, variam, terminando no dia 28 e iniciando no dia 29.
Quinto ciclo: 28/02/2026 ~ 30/03/2026
Outras informações
É possível habilitar crédito?
Seguir a regra do arranjo. Na confirmação do consentimento é necessário um aviso ao cliente que o uso de linha de crédito pré-aprovada na instituição detentora de conta está habilitado e poderá ser alterado na detentora em ambiente de gestão do Pix Automático.
Tentativas para pagamentos que falharam
Detentor realiza primeira tentativa das 0h – 8h. Segunda tentativa entre 18h – 21h. Caso de falha, recebedor pode solicitar ao iniciador envio de novas tentativas (contando que o pagador tenha aceito e o motivo do erro permita). Novas tentativas de liquidação devem ocorrer em até 7 dias corridos após a primeira tentativa. São permitidas no máximo 3 retentativas, totalizando 4 tentativas de liquidação para um mesmo pagamento. Iniciador deve informar ao detentor que o recebedor deseja ativar as retentativas, pagador deve autorizar em momento de consentimento.
Funcionalidade de contestação
Contestação está disponível no arranjo Pix automático, conforme pode ser visto na Página 84, Requisito 4, Requisitos Mínimos para Experiencia do Usuário, versão 7.0
2.2 Regras de notificação:
Notificações ao usuário pagador relacionadas ao consentimento (ou seja à permissão/autorização) devem, obrigatoriamente, ser enviadas pela Iniciadora, não podendo ser desabilitadas pelo usuário.
É opcional para a detentora o envio dessas notificações, exceto nos casos relacionados a alteração de valor máximo e utilização do limite de crédito, quando também deverá obrigatoriamente notificar o cliente em caso de alteração.
Notificações ao usuário pagador relacionadas a agendamento e liquidação de pagamentos deverão estar habilitadas por padrão na detentora de conta, de acordo com o especificado nas regras do arranjo.
Apenas notificações de sucesso de agendamento poderão ser desabilitadas pelos usuários na detentora de conta. As demais permanecerão ativas, também seguindo o definido pelo arranjo.
O envio de notificações ao usuário pagador sobre agendamento e liquidações por parte da Iniciadora é opcional. Se implementadas, deve ser permitido que possam ser desabilitadas pelo usuário.
A detentora de conta deverá comunicar todas as ocorrências de sucesso/não sucesso de agendamentos e pagamentos a Iniciadora, para que esta avalie se deseja ou não notificar também o cliente.
A comunicação será realizada via Webhook e o Iniciador precisará consultar o recurso antes de realizar a avaliação.
É
vedado
ao Iniciador o encaminhamento ao recebedor de mensagens de erro e motivos de rejeição que especifiquem que houve falha no pagamento por insuficiência de saldo ou de limites. Nesses casos, a comunicação ao recebedor sobre o não processamento do pagamento deve ser feita de modo genérico, com a orientação de que o usuário pagador busque informações em sua detentora de conta.
É
vedado
ao Iniciador permitir que o recebedor acesse informações sobre valor máximo por transação definido pelo cliente, bem como suas alterações.
3 - Descrição de fluxos
3.1- Para criação do consentimento:
Diferente dos pagamentos realizados via agendamento recorrente ou pagamentos imediatos, o Pix Automático possui consentimentos de longa duração, os quais poderão ter alguns parâmetros editados ao longo da sua vida útil. Entraremos mais no detalhe do processo de criação do consentimento a seguir.
3.1.1 - Jornada 1 - Fluxo da criação do consentimento sem pagamento inicial avulso
Serviços que não possuem pagamento inicial avulso são aqueles que, geralmente, paga-se pelo consumo, como serviços de energia elétrica, água e gás. Esta jornada trata desde a solicitação de autorização até a sua conclusão.
Open
ID
CAMADA
TIPO
DESCRIÇÃO
ID
CAMADA
TIPO
DESCRIÇÃO
1
Usuário Pagador
Ação
Pagador acessa ambiente do recebedor e manifesta a intenção de contratar um dos serviços ofertados.
2
Usuário Pagador
Ação
Em ambiente do Recebedor: Pagador seleciona Pix Automático via Open Finance como forma de pagamento pelo serviço.
3
Usuário Pagador
Ação
Em ambiente do Recebedor: Pagador informa seus dados de pagamento e, opcionalmente, configura parâmetros de limite para a transação.
4
Usuário Pagador
Comunicação
Em ambiente do Recebedor: Dados são repassados ao Iniciador.
5
Iniciador
Comunicação
Recebe os dados enviados do Recebedor e inicia o processo de criação do consentimento.
6
Iniciador
Ação
Valida as informações recebidas do Recebedor.
7
Iniciador
Ação
Iniciador prepara o payload de envio do consentimento de longa duração atentando-se ao produto para o qual este consentimento está sendo criado.
Antes do envio o iniciador deve realizar a solicitação de token de acesso. Grant-type e scopes podem ser encontrado na especificação da API.
8
Iniciador
Comunicação
Envia solicitação de criação de consentimento de longa duração para o Detentor.
9
PSP Pagador (Detentor)
Comunicação
Recebe a solicitação de criação de consentimento de longa duração enviada pelo Iniciador.
10
PSP Pagador (Detentor)
Ação
Processa a solicitação de consentimento recorrente.
11
PSP Pagador (Detentor)
Comunicação
Retorna sucesso na criação do consentimento de longa duração para o Iniciador junto a URL de redirecionamento.
12
Iniciador
Comunicação
Recebe o sucesso na criação do consentimento de longa duração e URL de redirecionamento.
13
Iniciador
Ação
Processa o retorno da solicitação de criação do consentimento de longa duração.
14
Iniciador
Comunicação
Redireciona o pagador para autenticação no Detentor.
15
Usuário Pagador
Ação
Em ambiente do PSP Pagador: Realiza a autenticação.
16
Usuário Pagador
Ação
Em ambiente do PSP Pagador: Autoriza o consentimento.
17
Usuário Pagador
Ação
Em ambiente do PSP Pagador: PSP Pagador muda o consentimento para o status
AUTHORISED
.
18
Usuário Pagador
Ação
Em ambiente do PSP Pagador: PSP Pagador notifica os demais aprovadores solicitando a aprovação em caso de múltiplas alçadas.
19
Usuário Pagador
Comunicação
Em ambiente do PSP Pagador: PSP Pagador redireciona o usuário pagador para o ambiente do Iniciador.
20
Iniciador
Comunicação
Recebe informações do redirecionamento.
21
Iniciador
Ação
Valida informações recebidas.
22
Iniciador
Ação
Realiza consulta ao PSP do Pagador para verificar o estado do consentimento. AUTHORISED indica que o consentimento foi autorizado pelo cliente. Porém, caso a consulta retorne o valor REJECTED, deve-se abortar o processo de consentimento e pagador e recebedor devem ser comunicados da falha.
23
Iniciador
Comunicação
Notifica o pagador do resultado do processo de consentimento (do pagador ao serviço de cobranças recorrentes).
24
Pagador
Comunicação
Recebe notificação do resultado do processo de consentimento/autorização
25
Iniciador
Comunicação
Aguarda até que o(s) usuário pagador tenha realizado a aprovação do consentimento para notifica-lo do sucesso no consentimento.
26
Recebedor
Comunicação
Notifica o recebedor do resultado do consentimento
3.1.2 - Jornada 2 - Fluxo da criação do consentimento com pagamento inicial avulso
O pagamento inicial avulso ao serviço é considerado como o primeiro pagamento relacionado aquela contratação do serviço, em outras palavras, é o pagamento inicial para utilização de algum serviço contratado. Alguns exemplos de serviços que possuem essa característica são os de streaming, alugueis de bens e matrículas. Esta jornada trata desde a solicitação de autorização até a sua conclusão.
Open
ID
CAMADA
TIPO
DESCRIÇÃO
ID
CAMADA
TIPO
DESCRIÇÃO
1
Usuário Pagador
Ação
Pagador acessa ambiente do recebedor e manifesta a intenção de contratar um dos serviços ofertados.
2
Usuário Pagador
Ação
Em ambiente do Recebedor: Pagador seleciona Pix Automático via Open Finance como forma de pagamento pelo serviço.
3
Usuário Pagador
Ação
Em ambiente do Recebedor: Pagador informa seus dados de pagamento e, opcionalmente, configura parâmetros de limite para a transação.
4
Usuário Pagador
Comunicação
Em ambiente do Recebedor: Dados são repassados ao Iniciador.
5
Iniciador
Comunicação
Recebe os dados enviados do Recebedor e inicia o processo de criação do consentimento.
6
Iniciador
Ação
Valida as informações recebidas do Recebedor.
7
Iniciador
Ação
Iniciador prepara o payload de envio do consentimento de longa duração atentando-se ao produto para o qual este consentimento está sendo criado.
8
Iniciador
Comunicação
Envia solicitação de criação de consentimento de longa duração para o Detentor (
POST
/consents).
Deve possuir o objeto “/data/recurringConfiguration/automatic/firstPayment” preenchido.
Antes do envio o iniciador deve realizar a solicitação de token de acesso. “Grant-type” e “scopes” podem ser encontrado na especificação da API.

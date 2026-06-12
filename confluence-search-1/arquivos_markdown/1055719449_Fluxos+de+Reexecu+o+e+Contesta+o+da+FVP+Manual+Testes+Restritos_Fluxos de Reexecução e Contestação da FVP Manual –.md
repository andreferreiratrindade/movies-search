---
                            title: "Fluxos de Reexecução e Contestação da FVP Manual – Testes Restritos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1055719449_Fluxos+de+Reexecu+o+e+Contesta+o+da+FVP+Manual+Testes+Restritos"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1055719449/Fluxos+de+Reexecu+o+e+Contesta+o+da+FVP+Manual+Testes+Restritos"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Fluxos de Reexecução e Contestação da FVP Manual – Testes Restritos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Introdução
A Ferramenta de Validação em Produção (FVP) Manual – Testes Restritos é utilizada para verificar periodicamente a conformidade das implementações técnicas, em ambiente produtivo das instituições. Quando uma instituição é notificada de uma falha em um teste da FVP Manual – Testes Restritos (ou seja, recebe um ticket de notificação comunicando a falha), existem dois caminhos possíveis a seguir para resolver a situação: o
fluxo de Reexecução
ou o
fluxo de Contestação
. Esta documentação descreve cada fluxo, indicando quando e como utilizar cada um deles.
As instituições devem utilizar o fluxo apropriado de acordo com o motivo da falha identificada no ticket de notificação:
O
Fluxo de Reexecução
deve ser seguido quando a instituição identificar que a falha ocorreu devido a um problema em sua própria implementação ou ambiente, devendo corrigi-lo e, após isso, solicitar uma nova execução pela Associação.
O
Fluxo de Contestação
deve ser utilizado quando a instituição acreditar que a falha reportada não foi causada por falha em sua implementação, mas sim por um erro da ferramenta de teste ou por alguma falha operacional na execução do teste.
Abaixo, são apresentadas as definições de alguns termos e detalhamos cada um dos fluxos, incluindo exemplos práticos de utilização.
Importante:
Sempre selecione a categoria correta ao abrir um chamado no Service Desk do Open Finance. Pedidos de contestação feitos na categoria de reexecução (ou vice-versa)
não serão atendidos
e serão encerrados sem seu devido atendimento. Certifique-se de escolher “Reexecução” apenas quando desejar uma nova execução dos testes após corrigir sua implementação, e “Contestação” somente quando desejar questionar o resultado devido a um possível erro da ferramenta ou do processo de teste.
Para melhor compreensão, seguem as definições de alguns termos utilizados no contexto dos fluxos de reexecução e contestação:
Ticket de notificação:
é o chamado aberto pela própria Associação Open Finance Brasil (via Service Desk) para notificar a instituição participante de que uma execução dos testes da FVP Manual – Testes Restritos resultou em falha. Este ticket de notificação inclui evidências da falha identificada (logs de falha, descrições do erro, capturas de tela etc.) e permanece aberto até que uma execução com sucesso seja realizada pela própria Associação.
Ticket de reexecução:
é o chamado aberto pela instituição
para solicitar uma nova execução (reteste)
do módulo de teste que falhou. A abertura é feita no Service Desk, na categoria apropriada (“Requisição > Reexecução > FVP Manual – Testes Restritos”). No primeiro pedido de reexecução, a instituição deve referenciar o número do ticket de notificação original. Em casos de múltiplas reexecuções (ver Fluxo de Reexecução adiante), se uma reexecução anterior também falhar, um novo ticket de reexecução deverá ser aberto referenciando o
ticket de reexecução anterior
, e não mais o ticket de notificação inicial.
Ticket de contestação:
é o chamado aberto pela instituição
para contestar o resultado
de um teste da FVP Manual – Testes Restritos. A abertura é feita no Service Desk na categoria “Requisição > Contestação > FVP Manual – Testes Restritos”. No ticket de contestação, a instituição deve informar o número do ticket de notificação relacionado e indicar o tipo de falha que está sendo contestada (vide
falha técnica
vs
falha operacional
). Em casos de múltiplas reexecuções, se uma reexecução anterior também falhar, um novo ticket de reexecução deverá ser aberto referenciando o
ticket de reexecução anterior
, e não mais o ticket de notificação inicial. O ticket de contestação será analisado pela Estrutura do Open Finance, que decidirá se a contestação procede ou não. Os tickets de contestação poderão ser classificados pela instituição da seguinte maneira:
Falha técnica (erro técnico):
refere-se a uma falha causada por alguma inconsistência ou bug na própria ferramenta de teste (FVP).
Falha operacional (erro operacional):
refere-se a uma falha decorrente de
problemas no processo de execução ou notificação do teste
. São situações em que a execução não ocorreu como deveria por questões operacionais ou de configuração. Alguns exemplos de falha operacional são: Parâmetros de teste inválidos ou incorretos, ausência de evidências anexadas no ticket de notificação da falha ou saldo insuficiente na conta utilizada para um cenário de pagamento durante o teste, resultando em falha que não está ligada a uma falha na implementação da API da instituição.
Fluxo de Reexecução
O fluxo de reexecução deve ser utilizado quando a instituição, ao analisar a falha reportada no ticket de notificação, conclui que é necessária alguma
correção em sua implementação ou ambiente
para atender aos requisitos do Open Finance. Em resumo, a reexecução é apropriada quando a falha indica uma não conformidade real no sistema da instituição, a qual precisa ser ajustada.
A seguir, detalhamos os passos do fluxo de reexecução dos tickes da FVP Manual - Testes Restritos:
Notificação da falha:
A instituição recebe um
ticket de notificação
informando que sua execução dos testes da FVP Manual – Testes Restritos apresentou falhas. O ticket contém as evidências do problema.
Análise e correção interna:
A equipe da instituição analisa a falha apontada e identifica a causa em sua implementação ou configuração. Em seguida, são feitos os devidos ajustes ou correções no sistema (por exemplo, correção de um bug na API, ajustes de configurações de sistemas etc.).
Solicitação de reexecução:
Após corrigir o problema, a instituição deve abrir um
ticket de reexecução
no Service Desk, seguindo o caminho
Requisição > Reexecução > FVP Manual – Testes Restritos
. Nesse chamado, é preciso informar o número do ticket de notificação original da falha e detalhar, quando necessário, as correções realizadas ou o contexto da solicitação.
Pausa do SLA e nova execução do teste:
Ao receber o pedido de reexecução, o ticket de notificação terá seu
SLA pausado
.
Avaliação do resultado da reexecução:
Se o novo teste passar com sucesso na reexecução, a falha é considerada resolvida. O ticket de notificação original será então
encerrado
.
Importante:
Os testes de longa duração são testes que fazem validações em dias posteriores (como liquidações de pagamentos e novas tentativas de pagamento, como
retrys
). Portanto, um sucesso parcial (por exemplo, sucesso apenas no primeiro teste, realizado manualmente pelo fornecedor) em um pedido de reexecução não garante o encerramento do ticket de notificação, pois é necessário que todos os testes seguintes, que serão realizados automaticamente pela ferramenta, tenham sucesso. (Mais informações sobre os testes de longa duração estão disponíveis na página "FVP Manual")
Se
a falha persistir ou surgirem novas falhas
na reexecução: a Associação atualizará o ticket de notificação original anexando as novas evidências da falha ocorrida na reexecução e retomará o SLA. Nesse caso, a instituição deverá retornar ao passo 2 (analisar e corrigir) considerando as novas falhas evidenciadas.
Fluxo de Contestação
O fluxo de contestação deve ser utilizado quando a instituição entende que a falha reportada
não se deve a um erro de sua implementação
, mas possivelmente a um
equívoco na execução ou problema nos testes
. Em outras palavras, a contestação deverá ser utilizada quando a instituição suspeita de falso negativo na detecção da falha. Contestações de resultado podem ser ocasionados por
erro da ferramenta (falha técnica)
ou por um
erro no processo de execução/notificação (falha operacional)
, conforme definidos anteriormente. O objetivo da contestação é solicitar à Associação do Open Finance uma revisão do resultado do teste ou a correção de algum fator externo.
A seguir, detalhamos os passos do fluxo de contestação dos tickes da FVP Manual - Testes Restritos:
Notificação da falha:
Assim como no caso anterior, tudo começa com a instituição recebendo um
ticket de notificação
de falha nos testes da FVP Manual – Testes Restritos, contendo as evidências do problema.
Análise interna:
A equipe da instituição analisa as evidências e o contexto da falha. Nesta etapa, ao invés de encontrar um defeito no sistema próprio, a instituição identifica que a falha pode ter sido causada por falhas na ferramenta ou na execução. Por exemplo, ao verificar os logs, a instituição nota um comportamento inesperado da ferramenta de teste ou percebe que informações ausentes podem ter sido causadas por parâmetros incorretos fornecidos no teste.
Solicitação de contestação:
Por se tratar de um erro da ferramenta ou do processo, a instituição abre um
ticket de contestação
no Service Desk, seguindo o caminho
Requisição > Contestação > FVP Manual – Testes Restritos
. No chamado de contestação, deve-se:
Referenciar o número do ticket de notificação da falha. Lembre-se: caso já tenha ocorrido uma tentativa de reexecução anterior que também falhou, informe o número do ticket de reexecução anterior, ao invés do ticket de notificação, conforme as orientações acima;
Informar o tipo de falha que está sendo contestada, selecionando
“Erro Técnico”
ou
“Erro Operacional”
conforme a natureza do problema identificado;
Descrever claramente por que a instituição entende que o resultado do teste está equivocado ou o que foi realizado errado no processo. Inclua detalhes da evidência e qualquer dado adicional que sustente a contestação.
Avaliação da contestação pela Estrutura:
Ao receber o pedido de contestação, a Estrutura do Open Finance (e/ou a equipe técnica responsável pela FVP, como o provedor dos testes) irá analisar as evidências e a justificativa apresentadas. O ticket de notificação original terá seu SLA pausado durante essa análise, já que a resolução depende de verificação da Associação. A análise pode resultar em dois cenários: Contestação procedente (aceita) ou Contestação improcedente (negada).
Contestação procedente (aceita):
Se a equipe concluir que de fato houve um erro na ferramenta ou no processo do teste que invalida o resultado:
No caso de contestações de
tickets de notificação
originais, eles serão
cancelados
. Após o  cancelamento do ticket de notificação, a Estrutura do Open Finance realizará uma nova execução do teste. Caso ocorra uma nova falha, um novo ticket de notificação será aberto à instituição;
No caso de contestações de
tickets de reexecução
, o ticket de notificação original não será encerrado ou cancelado, permanecendo em aberto. Para esses casos, será adicionado ao ticket original o tempo compreendido entre o fechamento do ticket de reexecução e a abertura do ticket de contestação.
No caso de
falha técnica
confirmada: o caso é encaminhado para correção da ferramenta de teste. O ticket de notificação permanecerá aberto (em status de aguardando correção) enquanto a falha na ferramenta é corrigida pela Estrutura.
Após a correção do problema técnico ou operacional identificado, a Estrutura realizará uma
nova execução do teste
para verificar se tudo está correto. Essa execução é iniciada pela própria Estrutura como parte da validação da contestação, não exigindo que a instituição abra um pedido de reexecução. Se o teste tiver novas falhas identificadas, um novo ticket de notificação será aberto à instituição.
Contestação improcedente (negada):
Se a análise concluir que
não
houve erro na ferramenta ou no processo, isto é, a falha apontada realmente indica um problema na implementação da instituição:
O ticket de contestação será
recusado
. A Estrutura atualizará o chamado informando os motivos (por exemplo, esclarecendo que os testes funcionaram como esperado, com o devido embasamento técnico, e que a falha demonstra uma não conformidade real da instituição).
O ticket de notificação original terá seu
SLA retomado
e continuará aberto aguardando uma nova solicitação de reexecução. A instituição deve então providenciar as correções necessárias em seu sistema e posteriormente solicitar uma reexecução conforme o fluxo já descrito anteriormente, para tentar obter sucesso nos testes.
Encerramento:
Para contestação procedente (aceita), o ticket de notificação será cancelado. Se a contestação for improcedente (negada), o encerramento ocorrerá somente após a instituição efetuar correções e conseguir uma execução bem-sucedida via fluxo de reexecução.
Nota
: A cada nova solicitação de contestação, utilize sempre o número do último ticket de reexecução falhado como referência, conforme mencionado. Apenas o último ticket de reexecução associado a um ticket de notificação pode ser contestado. Contestações de tickets de reexecuções anteriores não serão aceitas. Não abra um novo pedido referenciando novamente o ticket de notificação após já ter ocorrido uma reexecução, pois isso pode causar confusão no rastreamento do caso.

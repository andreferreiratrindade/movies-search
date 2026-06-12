---
                            title: "Gestão dos tickets de Não Conformidade - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "689045505_Gest+o+dos+tickets+de+N+o+Conformidade"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/689045505/Gest+o+dos+tickets+de+N+o+Conformidade"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Gestão dos tickets de Não Conformidade - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Fluxo dos tickets de Não Conformidade
Open
Parte 1 do Fluxo de Tickets de Monitoramento de UX
Detalhamento do fluxo - Parte 1
O Ticket é aberto pelo time de Monitoramento UX e encaminhado para atendimento do N2 das Instituições Financeiras, com atualização do status para
ENCAMINHADO N2 ATENDIMENTO
.
O N2 da Instituição Financeira atualiza o ticket para
EM ANÁLISE N2
.
O N2 da Instituição Financeira deve verificar os apontamentos, anexos e acesso aos links disponibilizados e:
caso haja problema no acesso aos links ou dúvidas relacionadas aos apontamentos, o ticket pode ser encaminhado para o requisitante, com status
AGUARDANDO REQUISITANTE
. O time de Monitoramento UX deve responder aos questionamentos e encaminhar o ticket de volta à Instituição Financeira, atualizando o status para
ATUALIZADO PELO REQUISITANTE
;
não havendo problemas ou dúvidas, o N2 da Instituição financeira atualiza o ticket para
EM ATENDIMENTO N2
.
Iniciado o atendimento, caso o N2 da Instituição Financeira identifique que um ou mais apontamentos necessitam de desenvolvimento para resolução, o ticket deve ser atualizado para
AGUARDANDO IMPLEMENTAÇÃO N2
.
A Instituição Financeira pode realizar também a contestação do apontamento, quando entender que esse está em conformidade com o Guia de Experiência. Nesse caso, o ticket deve ser atualizado para
EM CONTESTAÇÃO
.
Importante
: Nesse status há parada na contagem de tempo do SLA da Instituição Financeira.
O time de Monitoramento UX irá avaliar a contestação e:
caso seja considerada procedente, o ticket será CANCELADO;
caso seja considerada improcedente, o ticket será devolvido à Instituição Financeira com o status
ENCAMINHADO N2 ATENDIMENTO
.
pode ocorrer também do time de Monitoramento de UX necessitar de análise técnica de outros times da Associação Open Finance para determinar se a contestação é procedente ou não. Nesse caso, o ticket deve ser atualizado para
ENCAMINHADO N3 ANÁLISE TÉCNICA
, mantendo a parada na contagem de tempo do SLA da Instituição Financeira.
Após o atendimento de um ou mais apontamentos, o N2 da Instituição Financeira pode atualizar o ticket para:
IMPLEMENTADA CORREÇÃO PARCIAL
: indica que parte dos apontamentos foi corrigida e atualizada em ambiente produtivo, podendo ser retestada ou ter suas evidências validadas, enquanto outros apontamentos permanecem pendentes de correção.
Importante
: Nesse status
não
há parada na contagem de tempo do SLA da Instituição Financeira
.
Após o atendimento de todos os apontamentos, o N2 da Instituição Financeira deve atualizar o ticket para
CORREÇÃO IMPLEMENTADA
: indica que todos os apontamentos foram corrigidos e atualizados em ambiente produtivo, podendo ser retestados ou ter suas evidências validadas.
Importante
: Nesse status há parada na contagem de tempo do SLA da Instituição Financeira
.
Fluxo de Validação da Correção da Não Conformidade
Open
Parte 2 do Fluxo de Tickets de Monitoramento de UX
Detalhamento do fluxo - Parte 2
Com a correção de todos os apontamentos pela Instituição Financeira, o time de Monitoramento de UX irá verificar se as evidências necessárias foram disponibilizadas no ticket. As evidências devem ser provenientes de ambiente produtivo, e devem demonstrar a jornada corrigida, respeitando o papel, o segmento e o sistema operacional utilizados no Ciclo de Monitoramento.
Caso não tenham sido disponibilizadas, estas serão solicitadas, devolvendo o ticket para a Instituição Financeira, com status
ENCAMINHADO N2 ATENDIMENTO
.
Estando todas as evidências disponíveis, o ticket será atualizado para
EM VALIDAÇÃO DE EVIDÊNCIA
.
Importante
: Nesse status há parada na contagem de tempo do SLA da Instituição Financeira
.
Após a validação, caso seja confirmada a correção da não conformidade, o time de Monitoramento de UX pode encerrar o ticket, atualizando-o para
ATENDIMENTO ENCERRADO
. Caso ainda existam pendências, o ticket será devolvido para a Instituição Financeira, com status
ENCAMINHADO N2 ATENDIMENTO
.
Para os tickets que não possuem evidência, será solicitado um reteste ao fornecedor, e o ticket é atualizado para
AGUARDANDO VALIDAÇÃO DA NÃO CONFORMIDADE
.
Importante
: Nesse status há parada na contagem de tempo do SLA da Instituição Financeira
.
O reteste tem prazo de SLA de 5 dias úteis.
Após a realização do reteste, se ainda existam pendências, o ticket será devolvido para a Instituição Financeira, com status
ENCAMINHADO N2 ATENDIMENTO
. Não havendo pendências, o time de Monitoramento de UX pode encerrar o ticket, atualizando para
ATENDIMENTO ENCERRADO
.
O prazo de SLA para a Instituição Financeira realizar a correção da não conformidade é de 10 dias úteis.
Critérios Mínimos para Geração da Evidência
Para viabilizar a validação da não conformidade por meio de validação de evidência, foram estabelecidos os seguintes critérios mínimos:
Evidência deve ser gerada, prioritariamente, com o mesmo formato da evidência do apontamento:
vídeo gerado em ambiente produtivo;
tratamento adequado aos dados sensíveis do usuário
indicação da minutagem do vídeo em que é apresentada a correção realizada;
repetição dos passos da jornada apresentados no vídeo de evidência do apontamento da não conformidade (disponibilizado no momento da abertura do ticket).
Caso não seja possível gerar a evidência em vídeo, será permitido o envio de:
captura da tela do aplicativo ou do navegador em ambiente produtivo;
tratamento adequado aos dados sensíveis do usuário;
destaque na captura de tela indicando onde a correção foi realizada;
apresentação da jornada completa ou, no mínimo, da tela anterior e posterior à tela onde foi realizada a correção, além da própria tela corrigida.
Ponto de atenção
A mesma evidência pode ser utilizada para demonstrar a correção de mais de um apontamento, desde que seja informada a minutagem correspondente a cada correção ou, no caso de captura de tela, que os destaques indiquem claramente cada correção realizada.
Documentos anexados aos tickets de Não conformidade
Os tickets de não conformidade do Ciclo de Monitoramento são encaminhados às Instituições Financeiras contendo dois arquivos:
Os tickets de não conformidade do Ciclo de Monitoramento são encaminhados às Instituições Financeiras contendo os seguintes arquivos:
arquivo em formato .xlsx com os apontamentos de não conformidades, erros técnicos ou impedimentos;
vídeo de evidência da jornada realizada e da não conformidade identificada.
Em alguns casos, devido ao tamanho do arquivo, não é possível anexar o vídeo ao ticket, ficando este disponível por meio de link do SharePoint informado na descrição do ticket.

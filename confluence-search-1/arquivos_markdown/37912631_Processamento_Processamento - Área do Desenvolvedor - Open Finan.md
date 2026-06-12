---
                            title: "Processamento - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "37912631_Processamento"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/37912631/Processamento"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Processamento - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            A rotina de
Processamento
compreende o trabalho de conciliação dos dados recebidos pelas instituições, bem como o procedimento de fechamento periódico.
O desenho esquemático abaixo mostra como esse processo funciona:
Open
Desenho esquemático do processo de conciliação
Conciliação
O processo de conciliação consiste em encontrar os reportes feitos por duas instituições que representem a requisição e a devida resposta de uma transação de negócio. O processo acontece de maneira assíncrona após a recepção do reporte, e consiste em se buscar um reporte que contenha o mesmo valor no atributo
fapiInteractionId
. Se esse reporte-par não existir, o reporte corrente é considerado
não pareado
(status
UNPAIRED
). Caso esse registro exista, a segunda etapa de validação busca conciliar os campos
clientOrgId
,
serverOrgId
,
statusCode
,
httpMethod
e
endpoint
. Se esses campos estiverem com valores iguais nos dois reportes, ambos serão considerados conciliados (status
PAIRED
). Caso esses dados não sejam iguais, eles são considerados
pareados e inconsistentes
(status
PAIRED_INCONSISTENT
), e portanto divergentes.
Para maiores informações sobre cada status, consulte o tópico Ciclo de vida do reporte mais abaixo. O fluxo da regra de conciliação é descrita no diagrama a seguir:
Open
Diagrama de atividades do processo de conciliação
Importante
Os participantes devem sempre que possível enviar os reportes dos dois lados, seja como server ou como client, mesmo que a chamada não tenha sido bem sucedida, uma vez que elas serão usadas para fins de controle estatístico e de monitoramento do ecossistema (objetivo principal da plataforma), incluindo casos de erros http séries 5xx, 4xx, etc.
Fases do processamento
O processo de conciliação ocorre em três momentos do fluxo de processamento dos reportes: Recepção, Fechamento e na Resolução de Divergências.
Recepção
Quando um report é recebido pela API, ele é validado e enfileirado para que cada reporte seja processado individualmente. É nesse momento que a maioria dos reportes serão conciliados.
Fechamento
No momento do fechamento, a plataforma busca por todos os registros que ainda permanecem como pendentes e aplica a regra da conciliação sobre eles. Esse passo é necessário para evitar eventuais problemas de concorrência no processamento em tempo real. O momento do fechamento e os SLAs a serem cumpridos pelo sparticipantes serão oportunamente definidos pelos GTs responsáveis.
Resolução de Divergências
Registros com os status
UNPAIRED
e
PAIRED_INCONSISTENT
são considerados divergentes e deverão passar pelo processo de resolução. Este processo será oportunamente definido pelos GT responsáveis.
Ciclo de vida do reporte
O diagrama abaixo ilustra as interações entre os status de um reporte:
Open
Interação entre as partes de um reporte
Um reporte deverá sempre estar em um dos seguinte status:
DISCARDED
O status
DISCARDED
indica que o reporte foi enviado pelo participante e será descartado para fins de composição de métricas. Ainda que não utilizado nas métricas, ele será persistido e só será utilizado em relatórios estatísticos, não sendo possível corrigí-lo e nem utilizá-lo em nenhum processo de negócio. Esse status é devolvido para o participante de maneira síncrona no momento da inclusão do reporte. Consulte a
Documentação da API - PCM
para informações sobre o schema a ser enviado.
Transições
: N/A (estado terminal)
ACCEPTED
O status
ACCEPTED
indica que a validação de formato do reporte não apresentou erros e este será enviado para processamento.
Transições
:
[1] Transiciona para
PAIRED
para indicar que outro reporte foi encontrado com o mesmo
fapiInteractionId
e os demais dados foram conciliados
[2] Transiciona para
PAIRED_INCONSISTENT
quando outro reporte foi encontrado com o mesmo
fapiInteractionId
mas os demais dados não foram conciliados
[3] Transiciona para
UNPAIRED
quando não existe outro reporte com o mesmo
fapiInteractionId
.[9] Transiciona para
DISCARDED
quando existe algum tipo de erro semântico no reporte.
SINGLE
O status
SINGLE
indica que o reporte em questão não tem uma contraparte. Ele é atribuído nos casos em que o reporte não contêm
fapiInteractionId
, como por exemplo reportes de dados abertos, em que apenas o SERVER reporta.
Transições
: N/A (estado terminal)
UNPAIRED
O status
UNPAIRED
significa que o reporte atual não possui uma correspondência em outro reporte através do atributo
fapiInteractionId
. Indica um reporte
divergente
.
Transições
:
[4] Transiciona para
PAIRED
para indicar que outro reporte foi encontrado com o mesmo
fapiInteractionId
e os demais dados foram conciliados. Esse processo só vai acontecer quando o reporte par for enviado.
[5] Transiciona para
PAIRED_INCONSISTENT
caso um reporte seja enviado com o mesmo
fapiInteractionId
mas algum dado esteja inconsistênte entre os reportes.
[8] Transiciona para
SINGLE
caso o reporte seja válido, mas não haja a possibilidade de conciliá-lo com outro reporte.
PAIRED_INCONSISTENT
O status
PAIRED_INCONSISTENT
significa que o reporte corrente possui uma contraparte com o mesmo
fapiInteractionId
, mas algum dado esteja inconsistente entre os reportes. Indica um reporte
divergente
.
Transições
:
[6] Transiciona para
PAIRED
caso o processo de resolução de divergência"*" corrija um dos dois reportes. Processo a ser definido.
PAIRED
Indica que o reporte tem uma contraparte com o mesmo
fapiInteractionId
e os demais dados estão conciliados. Representa o estado final desejado em um fluxo correto.
Transições
: N/A (estado terminal)

---
                            title: "Reporte de informações - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "498500110_Reporte+de+informa+es"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/498500110/Reporte+de+informa+es"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Reporte de informações - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            item 2.4
Controle de versão
Versão
Data
Resumo das alterações
1
May 16, 2024
Versão inicial
2
Apr 1, 2025
Revisão geral do documento
Inclusão dos tópicos “Interpretação dos Dados no Painel” e “Período de Apuração dos Dados”
Introdução e Objetivos
Esta métrica tem como foco garantir que as instituições participantes do Open Finance cumpram os requisitos de reporte de informações, conforme definido pela Estrutura Responsável pela Governança do Open Finance. O objetivo é assegurar a disponibilização de dados com qualidade e detalhamento suficientes, dentro dos prazos estabelecidos, permitindo a implementação efetiva das funcionalidades dispostas no manual. A métrica visa monitorar e identificar situações de desconformidade no processo de envio de informações, promovendo a transparência e a integridade dos dados no ecossistema do Open Finance.
Sobre a Métrica
A avaliação da conformidade é feita através da verificação dos reportes das instituições participantes à Plataforma de Coleta de Métricas, que devem enviar pelo menos 70% dos reportes de um determinado dia até 8h do próximo dia e pelo menos 75% dos reportes em até sete dias a partir da data e horário das transações. Diariamente deve ser avaliado também se existem dados reportados para o Motor de Qualidade.
Importante
: conforme disposto na IN 575 de 20/12/2024, no item 2.4, a partir do dia 01 de julho de 2025 entrarão em vigor os novos percentuais de envio dos reportes, sendo:
O atendimento da meta de envio de pelo menos 95% dos reportes até 8h do próximo dia a partir da data e horário das transações (em vez dos 70%)
O atendimento da meta de envio de pelo menos 99% dos reportes em até 7 dias a partir da data e horário das transações (em vez dos 75%).
Metodologia Simplificada
Plataforma de Coleta de Métricas (PCM)
A conformidade é avaliada com base na quantidade, periodicidade, e status dos dados reportados, de acordo com os critérios estabelecidos pela Estrutura de Governança do Open Finance.
Uma instituição participante estará em desconformidade se ocorrerem as seguintes situações, considerando para o universo da análise o total de reportes com os status “PAIRED” , “UNPAIRED” e “PAIRED_INCONSISTENT” :
Percentual de reporte diário para uma API até 8h do próximo dia a partir da data e hora das transações com status UNPAIRED >5%;
Não atendimento, superior a 3 dias do mês de apuração, da meta diária de envio de reportes em até 8h do próximo dia a partir da data e hora das transações, mesmo que atenda à meta de pelo menos 99% dos reportes desses dias em até 7 dias a partir da data e hora das transações para a API monitorada;
Percentual de reportes diários para uma API em até 7 dias a partir da data e hora das transações com status UNPAIRED e PAIRED_INCONSISTENT>1%.
Motor de Qualidade de Dados (MQD)
A conformidade é avaliada com base na quantidade de dias com reporte, no mês de apuração. Um conglomerado estará em desconformidade se para uma ou mais APIs a quantidade de dias sem reporte esperado ao Motor de Qualidade for superior a 3 dias no mês de apuração.
Interpretação dos Resultados
A interpretação dos resultados obtidos através desta métrica permite identificar instituições que não estão cumprindo com os requisitos de reporte de informações estabelecidos.
Se o total de reportes diários para a PCM até às 8h do próximo dia a partir da data e hora das transações, com status "UNPAIRED" excederem 5% do volume de chamadas da instituição para cada API, a instituição estará em desconformidade;
Se o total de reportes diários para a PCM em até sete dias a partir da data e hora das transações com status "UNPAIRED" e "PAIRED INCONSISTENT” excederem 1% do volume de chamadas da instituição para cada API, a instituição estará em desconformidade.
Período de Apuração dos Dados
Para fins do processo de monitoramento, o período de apuração referente a esta métrica é mensal e deve haver controle diário do envio dos reportes. Durante o mês, ainda que a instituição não exceda 1% do volume de chamadas com status "UNPAIRED" e "PAIRED INCONSISTENT” em 7 dias a partir da data e hora das transações, se o número de dias em que a meta diária não for atingida for superior a 3, a instituição estará em desconformidade.
Interpretação dos Dados no Painel
As informações contidas neste item têm como objetivo ajudar o usuário a compreender cada um dos campos exibidos no painel de “Reporte de Informações”. Desta forma, têm-se:
Em “
Controles
”:
Open
Campos
Descrição
Mês análise
informar a data ou período desejado, podendo ser uma data relativa ou intervalo de datas absoluto
Conglomerado
selecionar o conglomerado desejado
Visualizar organização
selecionar a opção “sim” para exibir os detalhes da organização pertencentes ao conglomerado ou a opção “não” para exibir o resultado por conglomerado
Em “
Desconformidade Consolidada
” é apresentado o resultado consolidado da apuração mensal por conglomerado e/ou organização, de acordo com o filtro selecionado em “
Controles
”.
O painel é interativo. Por exemplo, ao clicar na célula “
NÃO CONFORME
” do conglomerado ou da organização, serão exibidos os detalhamentos do mês de apuração. Além disso, é possível maximizar a visualização do painel e exportar os dados para CSV ou Excel.
Open
Em “
Desconformidade Mensal
”, têm-se:
Open
Importante
: O MQD aplica-se para as instituições transmissoras de dados pertencentes ao rol de 99%. Sendo assim, as células em branco indicam que as instituições não pertencem a este grupo.
Campos
Descrição
Mês análise
mês referente a apuração
Organização
organização selecionada
PCM
resultado mensal dos reportes realizados à PCM referente ao mês de apuração
MQD
resultado mensal dos reportes realizados ao MQD referente ao mês de apuração
Em “
Detalhes do mês de apuração da PCM
”, têm-se:
Open
Campos
Descrição
Mês análise
mês/ano referente a apuração
Dias de tolerância mensal (até 3 dias)
quantidade total de dias de tolerância mensal referente ao mês de apuração
Status
não conforme
Para exibir os detalhamentos, deve-se sempre clicar nas células “
NÃO CONFORME
”. Desta forma, têm-se:
Open
Campos
Descrição
Data transação
data em que a transação foi realizada
Método HTTP
método da requisição
Endpoint
endpoint
da requisição
Total reportes diário
quantidade total de reportes realizados em um determinado dia
% até 08h do próximo dia
percentual de reportes de um determinado dia realizados até às 08h do próximo dia
% não pareados
percentual de reportes não pareados de um determinado dia
Total reportes 7 dias
total de reportes realizados dentro do período de 7 dias das transações referentes a um determinado dia
% não pareados e pareados inconsistentes
percentual dos reportes não pareados e pareados inconsistentes de um determinado dia
Status
não conforme
Nos “
Detalhes do mês de apuração do MQD
”, têm-se:
Open
Campos
Descrição
Mês análise
mês referente apuração
Family Type
tipo da família de APIs
Total de dias no período
quantidade total de dias do mês de apuração
Quantidade de dias com reporte
quantidade total de dias do mês de apuração em que houve reporte
Quantidade de dias sem reporte
quantidade total de dias do mês de apuração em que não houve reporte
Status
não conforme
Dados e Fontes
Para o cálculo desta métrica, os dados são obtidos a partir dos dados reportados para a Plataforma de Coleta de Métricas (PCM ) e para o Motor de Qualidade (MQD). Esses dados são posteriormente consolidados na Plataforma Analítica de Dados (PAD), que é um repositório centralizado e serve como base para a análise e avaliação da métrica.
Limitações e Considerações
Caso a instituição não consiga enviar os reportes devido a falhas da PCM, e seja comprovada a ocorrência de instabilidades ou indisponibilidades da ferramenta, a meta de envio dos reportes até 8h do próximo dia não precisa ser atendida, mas a instituição continua obrigada a enviá-los em até 7 dias a partir da data e hora das transações.
Responsável pela Aprovação
GT Arquitetura

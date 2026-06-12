---
                            title: "Disponibilidade de APIs - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "795017220_Disponibilidade+de+APIs"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/795017220/Disponibilidade+de+APIs"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Disponibilidade de APIs - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Controle de versão
Versão
Data
Resumo das alterações
1
May 27, 2024
Versão inicial
2
31 de jan. de 2025
Segregação da métrica de desempenho de APIs da métrica de disponibilidade de APIs.
Maior detalhamento do cálculo da métrica.
3
Mar 24, 2025
Revisão geral do documento
Inclusão do tópico “Interpretação dos Dados no Painel”
Introdução e Objetivos
Esta métrica visa monitorar se os
endpoints
das APIs das instituições participantes estão cumprindo os SLAs de disponibilidade, estabelecidos no Manual de APIs do Open Finance.
Considerando que a disponibilidade dos
endpoints
das APIs do
Open Finance
será calculada empiricamente, baseada na monitoração de requisições válidas.
Sobre a Métrica
A métrica de Disponibilidade das APIs mede a capacidade de uma API estar acessível e funcionando corretamente para os desenvolvedores e usuários finais.
As medições devem ser feitas todos os dias, em todas as faixas de 1 minuto disponíveis, iniciando na primeira faixa (00:00:00-00:00:59) e terminando na última faixa (23:59:00-23:59:59), considerando o horário de Brasília.
As medições devem ser realizadas de maneira independente para cada versão "
major
" dos
endpoints
em produção.
O
status code
a ser considerado para uma requisição é o valor reportado pelo consumidor da API, ou seja, o valor reportado pela instituição iniciadora de pagamentos nas APIs de “Serviços de Iniciação de Pagamentos” e o valor reportado pela receptora de dados no caso de APIs de "Dados Cadastrais e Transacionais".
Na falta de informações dos consumidores, serão utilizadas as informações dos provedores para o cálculo do SLA de disponibilidade, ou seja,  o valor reportado pela instituição detentora de contas nas APIs de "Serviços de Iniciação de Pagamentos", e o valor reportado pela instituição transmissora de dados no caso de APIs de "Dados Cadastrais e Transacionais".
A indisponibilidade programada não exime o cálculo da disponibilidade no período apurado.
A disponibilidade de
endpoints
que não tenham requisições válidas no período apurado será considerada "indefinida", não estando sujeita a um SLA.
Cada um dos
endpoints
das APIs categorizadas como "Dados Abertos", "Dados Cadastrais e Transacionais", "Relatórios e Métricas", por versão, e os
endpoints
das APIs de "Segurança" "/
register
" e "/
token
", deverão satisfazer os requisitos mínimos de disponibilidade abaixo:
I - disponibilidade diária (calendário): 95%; e
II - disponibilidade longa (média móvel de 90 dias), medida diariamente: 99,5%.
As APIs classificadas como "Serviços de Iniciação de Pagamentos" seguem o definido na regulamentação do Pix, ou seja, ou seja os participantes têm metas de índice de disponibilidade diferentes, de acordo com as suas categorias de participação no arranjo:
Categoria
Disponibilidade
Categoria
Disponibilidade
A
99,5%
B
99,0%
C
98,5%
D
95,0%
A conformidade é avaliada mensalmente, verificando se os
endpoints
das APIs das instituições participantes atenderam aos SLAs de disponibilidade. A aferição mensal deve considerar a disponibilidade longa do último dia do mês de referência.
Metodologia Simplificada
Para fins de monitoramento deste item, o período de apuração será mensal, conforme orientado pelo Manual de Monitoramento do Open Finance Brasil. A avaliação envolverá:
Para as APIs de “Dados Abertos", "Dados Cadastrais e Transacionais", "Relatórios e Métricas", por versão, e os
endpoints
das APIs de "Segurança" "/
register
" e "/
token
":
Disponibilidade diária: monitoramento da disponibilidade em todos os dias do mês de referência.
Disponibilidade longa: monitoramento da da disponibilidade longa como média móvel dos últimos 90 dias.
Para as APIs de “Serviços de Iniciação de Transação de Pagamentos” monitoramento mensal de acordo com a regulamentação do Pix, .
Aspectos Técnicos
O monitoramento inclui várias etapas:
AGRUPAR POR MINUTO E CONTAR AS REQUISIÇÕES COM SUCESSO E ERRO
Filtragem
organisationid
=
clientorgid
OU
(
organisationid
= s
erverorgid
E
status
=
'UNPAIRED'
)
statuscode
= 2xx, 5xx, 408 ou 422
status ≠ “PAIRED_INCONSISTENT”
Agrupamento
serverorgid
endpoint
dia
minuto
Contar as requisições por tipo
total_validas → total de chamadas
success
→ total chamadas com
status code
2xx ou 422
error
→ total chamadas com
status code
5xx OU 408
CALCULAR A DISPONIBILIDADE DO MINUTO
Para cada minuto, realiza o cálculo do percentual de disponibilidade:
Open
AGRUPAR POR DIA E CALCULAR O TOTAL DE MINUTOS DISPONÍVEIS
Agrupamento
orgid
do servidor
ponto final
dia
Cálculo
total_validas_dia → total de chamadas no dia
total_minutos_disponiveis → total disponibilidade_no_minuto ≥ 95%
total_minutos → total de minutos do dia
CALCULAR DISPONIBILIDADE E CONFORMIDADE DIÁRIA, MENSAL E LONGA
Disponibilidade diária
Open
Conformidade diária
Porcentagem_disp_dia ≥ 0,95  = CONFORME
Porcentagem_ disp _dia < 0,95  = NÃO CONFORME
Disponibilidade mensal (iniciação de pagamentos)
percent_disp_mensal = média mensal de percent_disp_dia
Conformidade mensal (Iniciação de pagamentos)
percent_disp_mensal ≥  categoria de disponibilidade Pix da instituição = CONFORME
percent_disp_mensal <  categoria de disponibilidade Pix da instituição = NÃO CONFORME
Disponibilidade longa
percent_disp_u90d = média dos últimos 90 dias de percent_disp_dia
Conformidade longa
percent_disp_u90d ≥ 0.995 = CONFORME
percent_disp_u90d < 0.995 = NÃO CONFORME
Interpretação dos Resultados
Os resultados da métrica serão interpretados para verificar se as instituições estão cumprindo os critérios de conformidade para disponibilidade das APIs. A análise incluirá:
Disponibilidade das APIs
Disponibilidade Diária
A disponibilidade pontual (t) é calculada como a fração do total de requisições válidas processadas com sucesso a cada intervalo de 1 minuto. Por exemplo, a disponibilidade pontual de um endpoint referente ao minuto 11:34, de um determinado dia, no qual houve um total de requisições válidas com sucesso de 255 e um total de requisições válidas com erro de 4, é calculada da seguinte forma:
Open
A disponibilidade diária é calculada baseada nas informações das disponibilidades pontuais.
Disponibilidade Longa
A disponibilidade longa é calculada diariamente como média móvel das disponibilidades dos últimos 90 dias corridos. Por exemplo, a disponibilidade longa do último dia de março é a média das disponibilidades diárias dos últimos 90 dias.
A conformidade para a disponibilidade das APIs depende da conformidade em todos os dias da disponibilidade diária das APIs e da sua disponibilidade longa, considerando o último dia do mês de apuração. As APIs de “Serviços de Iniciação de Pagamentos” seguem as metas do índice de disponibilidade do arranjo Pix.
Exemplo Ilustrativo
Para ilustrar as condições de conformidade e desconformidade, considere os seguintes exemplos:
Conformidade
Por exemplo, considerando um dia (ex.: 10/06/2024) em que houve requisições válidas em 1.360 das 1.440 faixas de 1 minuto possíveis (1 dia = 24h * 60min= 1.440 faixas de horário) para um
endpoint
específico "x" de versão 1, e dos quais 30 períodos tiveram a disponibilidade menor que o limite de disponibilidade definido (95%), a Disponibilidade Diária de "x" v1 será igual a:
Open
Interpretação dos Dados no Painel
As informações contidas neste item têm como objetivo ajudar o usuário a compreender cada um dos campos exibidos no painel de “Disponibilidade”. Desta forma, têm-se:
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
” do conglomerado ou da organização, será exibido os detalhamentos do mês de apuração. Além disso, é possível maximizar a visualização do painel e exportar os dados para CSV ou Excel.
Open
Nos detalhes da “
Desconformidade Mensal
”, têm-se:
Open
Campos
Descrição
Mês análise
mês referente a apuração
Organização
organização selecionada em “Controles”
Diária
resultado referente ao mês de apuração da disponibilidade diária
Longa
resultado referente ao mês de apuração da disponibilidade longa
Serviços
resultado referente ao mês de apuração da disponibilidade de serviços
Importante
: as células vazias representam conformidade.
Para que o detalhamento seja exibido, deve-se clicar nas células “NÃO CONFORME” nas colunas “Diária”, “Longa” ou “Serviços”.
Em “
Disponibilidade Diária
”, têm-se:
Open
Campos
Descrição
Dia análise
dia do mês referente a apuração
Método HTTP
método da requisição
Endpoint
endpoint
da requisição
Nr. minutos disponíveis
total de minutos disponíveis de um determinado dia
Nr. minutos indisponíveis
total de minutos indisponíveis de um determinado dia
Disponibilidade diária
percentual da disponibilidade diária de um determinado dia
Status
não conforme
*
*
Só serão exibidos os resultados não conformes.
Ao clicar nas células das colunas “
nr. minutos disponíveis
” ou “
nr. minutos indisponíveis
” serão exibidos os detalhamentos dos dados em “
Disponibilidade Pontual
”.
Em “
Disponibilidade Pontual
”, têm-se:
Open
Campos
Descrição
Intervalo minuto
intervalo em que a requisição apresentou sucesso ou erro
Método HTTP
método da requisição
Endpoint
endpoint
da requisição
Método HTTP
método da requisição
Nr. requisições válidas c/ sucesso
total requisições válidas com sucesso no intervalo de um determinado minuto
Nr. requisições válidas c/ erro
total requisições válidas com erro no intervalo de um determinado minuto
Disponibilidade pontual
percentual da disponibilidade pontual aferida
Importante
: serão exibidos no máximo cinco evidências de reporte.
Em “
Disponibilidade Longa
”, têm-se:
Open
Campos
Descrição
Mês análise
mês referente a análise
Método HTTP
método da requisição
Endpoint
endpoint
da requisição
Disponibilidade aferida
percentual da disponibilidade aferida na requisição
Meta disponibilidade longa
meta definida da disponibilidade longa
Status
não conforme
*
*
Só serão exibidos os resultados não conformes.
Em “
Disponibilidade de Serviços
”, têm-se:
Open
Campos
Descrição
Mês análise
mês referente a análise
Método HTTP
método da requisição
Endpoint
endpoint
da requisição
Disponibilidade aferida
percentual da disponibilidade aferida na requisição
Meta mensal índice de disponibilidade
meta mensal definida do índice de disponibilidade
Status
não conforme
*
*
Só serão exibidos os resultados não conformes.
Dados e Fontes
Para o cálculo da métrica, utiliza-se um conjunto diversificado de dados provenientes de diferentes fontes. A principal fonte informacional é a Plataforma de Coleta de Métricas (PCM), que consolida os dados a partir dos reportes enviados pelas instituições participantes. Além disso, as planilhas auto reportadas pelas instituições são integradas e consolidadas na Plataforma Analítica de Dados (PAD), um repositório centralizado que serve como base para a análise e avaliação da métrica. Essa combinação de dados provenientes da PCM e das planilhas auto reportadas permite uma avaliação precisa da métrica e um monitoramento efetivo do desempenho e disponibilidade das APIs no contexto do Open Finance.
Limitações e Considerações
Atualmente, não há visibilidade ou conhecimento de limitações ou considerações adicionais para esta métrica. A análise será continuamente revisada e aprimorada conforme novos dados e informações se tornem disponíveis.
Responsável pela Aprovação
GT Arquitetura

---
                            title: "Métricas de Desconformidade Consolidadas - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1319993668_M+tricas+de+Desconformidade+Consolidadas"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1319993668/M+tricas+de+Desconformidade+Consolidadas"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Métricas de Desconformidade Consolidadas - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Introdução e Objetivos
Este documento tem como finalidade apresentar a estrutura, a lógica e o propósito do dashboard consolidado das 13 métricas de desempenho. O painel foi desenvolvido para centralizar, em um único ambiente, informações que anteriormente estavam distribuídas em dashboards individuais, facilitando a visualização integrada e permitindo uma análise mais rápida e eficiente.
O objetivo principal é fornecer uma visão unificada que apoie tomadas de decisão, reduza o tempo de navegação entre diferentes relatórios e aumente a consistência das análises. Além disso, o documento descreve o funcionamento do painel, suas principais seções, filtros, regras de cálculo aplicadas e a origem dos dados utilizados.
Sobre as Métricas
O dashboard consolidado reúne
14 métricas principais
, das quais
13
são provenientes de uma mesma fonte de dados e
1 métrica
é obtida separadamente a partir da
fonte PAD
. Para permitir a integração adequada no QuickSight, foram criados
dois datasets
:
um dedicado ao tratamento da métrica derivada da fonte PAD;
outro contendo o tratamento das demais 13 métricas, incluindo o
join
com a métrica da fonte PAD para compor a visão consolidada.
Open
Embora grande parte das métricas já venha parcialmente tratada em suas bases de origem, algumas exigiram tratamentos adicionais diretamente nas queries, tanto para padronização de campos quanto para alinhamento das regras de cálculo.
Um ponto crítico do processo foi a inconsistência nos
nomes de conglomerados e instituições
entre diferentes métricas. Para garantir uniformidade, foi necessário aplicar um tratamento de padronização dentro das queries: todos os nomes disponíveis foram mapeados e, para cada
parent_organisation_reference
, foi selecionado apenas o
primeiro nome válido e recorrente
, evitando divergências e duplicidades entre indicadores.
Esse conjunto de tratamentos garante consistência e comparabilidade entre todas as métricas consolidadas no dashboard.
2.1.I Tempo de Resposta APIs:
A métrica já é fornecida pronta na base
bl_desempenho_consolidado_conformidade_mensal
.
O tratamento realizado foi apenas o
agrupamento por
parent_organisation_reference
,
mes_analise
e
parent_organisation_name
,  aplicando a regra de conformidade conforme a base.
2.1.II Disponibilidade APIs:
A métrica já é fornecida pronta na base
bl_disponibilidade_consolidado_conformidade_mensal
.
O tratamento realizado foi apenas o
agrupamento por
parent_organisation_reference
,
mes_analise
e
parent_organisation_name
, aplicando a regra de conformidade conforme a base.
2.1.III Requisições Status Code HTTP 529:
A métrica já é fornecida pronta na base
bl_server_overloaded_conformidade_mensal
.
O tratamento realizado foi apenas o
agrupamento por
parent_organisation_reference
,
mes_analise
e
parent_organisation_name
, aplicando a regra de conformidade conforme a base.
2.2.I Implementações Novas versões APIs:
A métrica já é fornecida pronta na base
bl_acomp_versoes_apis_conformidade_mensal
.
O tratamento realizado foi apenas o
agrupamento por
parent_organisation_reference
,
mes_analise
e
parent_organisation_name
, aplicando a regra de conformidade conforme a base.
2.2.II Versões Implementadas de APIs e artefatos associados:
A métrica já é fornecida pronta na base
bl_acomp_apis_artefatos_conformidade
.
O tratamento realizado foi apenas o
agrupamento por
parent_organisation_reference
,
mes_analise
e
parent_organisation_name
, aplicando a regra de conformidade conforme a base.
2.2.III Modalidades de participação:
A métrica já é fornecida pronta na base
bl_modalidades_participacao_conformidade_mensal
.
O tratamento realizado foi apenas o
agrupamento por
parent_organisation_reference
,
mes_analise
e
parent_organisation_name
, aplicando a regra de conformidade conforme a base.
2.2.IV Retirada das versões antigas das APIs:
A métrica já é fornecida na base
bl_retirada_api_consolidado_mensal
, porém
somente os registros “NÃO CONFORME” aparecem na fonte
.
No tratamento, foi realizado o
agrupamento por
parent_organisation_reference
,
mes_analise
e
parent_organisation_name
e, no dashboard, todos os valores
nulos foram considerados como “CONFORME”
, garantindo a classificação completa.
2.3 SLA Tickets:
A métrica não é fornecida pronta na base
vw_dl_service_desk_ticket_mensal
, sendo necessário realizar todo o tratamento dentro da query.
O tratamento inclui a criação de um calendário de dias úteis, cálculo de prazos de SLA, dias úteis decorridos, classificação por “DENTRO do SLA” / “FORA do SLA” e verificação do dobro do SLA.
Após os cálculos, os resultados foram
agrupados por
parent_organisation_reference
e
mes_analise
para aplicar a regra final de conformidade.
2.4.1. Report Informações:
A métrica já é fornecida pronta na base
bl_reporte_info_pcm_mqd_conformidade_mensal
.
O tratamento realizado foi apenas o
agrupamento por
parent_organisation_reference
,
mes_analise
e
parent_organisation_name
, aplicando a regra de conformidade conforme a base.
2.4.2 Planilha autorreportada:
A métrica já é fornecida pronta na base
bl_controle_respondentes_mensal
.
O tratamento realizado foi apenas o
agrupamento por
parent_organisation_reference
,
mes_analise
e
parent_organisation_name
, aplicando a regra de conformidade conforme a base.
2.5 Qualidade Dados:
Esta métrica vem de uma fonte diferente das demais (PAD), sendo fornecida pela base
mqd.vw_quicksight_conglomerate_iqd
. O tratamento realizado consistiu na aplicação da regra de conformidade considerando
IQA ≥ 0,95 como CONFORME
, seguida do
agrupamento por
parent_organisation_reference
e
mes_analise
.
2.6.1 Jornada do Cliente:
Esta métrica ainda não foi desenvolvida, pois está em processo de revisão da forma de cálculo e
não possui uma base final disponível
para implementação no momento.
2.6.2.1 Taxa Conversão Transmissor:
A métrica utiliza a base
bl_consentimento_transmissor_taxa_conversao
.
O tratamento realizado foi a
conversão do campo
ano_mes
para data
, a definição do nome da organização a partir do campo
transmissor
e a aplicação da regra de conformidade, onde
“NOTIFICAÇÃO” foi considerado como “NÃO CONFORME”
.
2.6.2.2 Taxa Conversão Detentor:
métrica utiliza a base
bl_funil_detentor_taxa_conversao
.
O tratamento realizado foi a
conversão do campo
ano_mes
para data
, a definição do nome da organização a partir do campo
detentora
e a aplicação da regra de conformidade, onde
“NOTIFICAÇÃO” foi tratado como “NÃO CONFORME”
.
2.6.2.3 Taxa Conversão Vinculo:
A métrica utiliza a base
bl_taxa_conversao_consolidado_mensal
, filtrada apenas para registros cujo
source = 'Vinculo'
.
O tratamento realizado foi o
agrupamento por
parent_organisation_reference
e
mes_analise
, aplicando a regra de conformidade conforme o status da base.
Sobre a query de consolidação das métricas:
Essa etapa cria uma base única contendo todas as organizações e meses presentes em qualquer uma das métricas. Para isso, o bloco
consolidado
faz um
UNION
de todas as tabelas de métricas (tempo de resposta, disponibilidade, requisições, implementações, versões, modalidades, retiradas, reports, autorreport, vínculo, transmissor, detentor e SLA), garantindo que nenhuma combinação de
parent_organisation_reference
e
mes_analise
fique de fora.
Em seguida, cada métrica é incorporada por meio de
LEFT JOIN
usando essas duas chaves. O nome da organização é unificado com
COALESCE
, assegurando que, mesmo quando a nomenclatura varia entre as bases, apenas um nome final seja retornado.
Por fim, a seleção filtra apenas registros com
parent_organisation_reference
e nome válidos, evitando linhas nulas ou não identificadas.

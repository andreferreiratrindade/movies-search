---
                            title: "Índice de Qualidade dos Dados (IQD) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "498500234_ndice+de+Qualidade+dos+Dados+IQD"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/498500234/ndice+de+Qualidade+dos+Dados+IQD"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Índice de Qualidade dos Dados (IQD) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            item 2.5
Controle de versão
Versão
Data
Resumo das alterações
1
Jun 6, 2024
Versão inicial
2
Aug 14, 2024
Implementado o Fator de Consistência no cálculo do IQA para mensurar a regularidade do reporte de dados de cada família de API
3
Apr 16, 2025
Revisão geral do documento
Alteração do Tópico “Classificação de conformidade do IQD”
Inclusão do tópico “Interpretação dos Dados no Painel”
O monitoramento referente ao item 2.5 terá início em 1º de julho de 2025, conforme estabelecido na Instrução Normativa BCB nº 575, de 20 de dezembro de 2024.
Introdução e Objetivos
Para garantir transparência quanto à qualidade dos dados no ecossistema do Open Finance, a Estrutura Responsável pela Governança do Open Finance disponibiliza o Índice de Qualidade dos Dados (IQD), juntamente com seus indicadores e metodologias de cálculo. Esses dados serão divulgados mensalmente, permitindo que o público acompanhe o nível de qualidade dos dados fornecidos pelas instituições participantes. Essa transparência proporciona informações confiáveis para a tomada de decisões relacionadas a riscos e resultados de negócios.
O Índice de Qualidade de Dados (IQD) foi desenvolvido para fornecer informações detalhadas sobre a qualidade dos dados oferecidos pelas instituições participantes aos cidadãos, associações e demais participantes do ecossistema do Open Finance. Com maior transparência, esses grupos têm acesso a um conjunto abrangente de informações para decidir qual instituição desejam utilizar para o compartilhamento de dados e/ou serviços financeiros por meio do Open Finance.
Sobre o Índice
O Índice de Qualidade dos Dados (IQD) é composto por três índices principais: Índice de Resolução (IR), Índice de Confiabilidade (IC) e Índice de Abrangência (IA). Esses índices, quando combinados, fornecem uma visão abrangente da qualidade dos dados fornecidos pelas instituições participantes do Open Finance.
Componentes do IQD
Índice de Resolução (IR)
Esse índice mede a eficiência na resolução de problemas e no atendimento ao suporte relacionado a uma determinada família de APIs. Esse índice é calculado com base na quantidade de tickets encerrados dentro do prazo de SLA em relação ao total de tickets abertos para a família de APIs em questão. Um valor alto de IR indica que a instituição é eficiente na resolução de problemas e no atendimento às demandas dos usuários. A eficiência é avaliada com base nas seguintes condições:
Se não houver tickets abertos ou encerrados e o total de requisições com erro for igual a 0, o IR é considerado 100%, indicando máxima eficiência na gestão de erros;
Se não houver tickets abertos ou encerrados e o total de requisições com erro for maior que 0, o IR é 0%, indicando uma situação onde, apesar da ausência de tickets, há problemas não resolvidos impactando a qualidade dos dados;
Nos demais casos, o IR é calculado pela fórmula a seguir, proporcionando uma medida quantitativa da eficiência na resolução de problemas:
Open
Índice de Confiabilidade (IC)
Esse índice avalia a qualidade e a integridade dos dados fornecidos por uma determinada API. Esse índice indica a proporção de requisições bem-sucedidas em relação ao total de requisições. Um valor alto indica que os dados fornecidos pela API são confiáveis e podem ser utilizados com segurança pelas aplicações e serviços que dependem dessas informações.
Open
Índice de Abrangência (IA)
Esse índice mede o quão abrangente é uma determinada API em relação ao total de APIs analisadas na organização. Esse índice leva em consideração a quantidade de requisições realizadas para uma determinada família de API, comparando-a com todas as famílias de APIs analisadas naquela organização. Um valor alto de IA indica que a API em questão possui uma grande relevância e abrangência dentro da organização.
Open
Cálculo do Índice de Qualidade de Dados (IQD)
O Índice de Qualidade de Dados (IQD) é calculado em várias etapas, considerando diferentes aspectos da qualidade e consistência dos dados fornecidos.
a) Cálculo do Índice de Qualidade da API (IQA)
O IQA é obtido através da combinação ponderada dos índices IR e IC, multiplicada pelo Índice de Abrangência (IA).
Fórmula do IQA
𝐼𝑄𝐴 inicial = ((𝐼𝑅 × Peso IR) + (𝐼𝐶 × Peso IC)) × 𝐼𝐴
Pesos atribuídos
Índice de Resolução (IR): 25%
Índice de Confiabilidade (IC): 75%
b) Aplicação do Fator de Consistência
O Fator de Consistência mede a regularidade do reporte de dados para cada família de API.
Fórmula do Fator de Consistência
Fator de Consistência = (Dias com Reporte / Total de Dias no Período)
IQA final = IQA inicial x Fator de Consistência
O Fator de Consistência incorpora a regularidade do fornecimento de dados ao cálculo do IQA, complementando as métricas de qualidade.
c) Calculo do IQD
O Índice de Qualidade de Dados (IQD) é a somatória de todos os Índices de Qualidade da API (IQA) finais.
Fórmula do IQD
IQD = Σ (IQA final)
Classificação de conformidade do IQD
CONFORME
NÃO CONFORME
CONFORME
NÃO CONFORME
≥ 95%
< 95%
Metodologia Simplificada
Para fins de monitoramento deste item, o período de apuração será mensal, conforme orientado pelo Manual de Monitoramento do Banco Central do Brasil. A avaliação envolverá:
Coleta de Dados: Os dados são coletados a partir do Motor de Qualidade de Dados (MQD).
Cálculo dos Índices:
Índice de Resolução (IR): Calcula a quantidade de tickets encerrados em relação ao total de tickets abertos.
Índice de Confiabilidade (IC): Avalia a integridade dos dados, considerando a quantidade de requisições bem-sucedidas.
Índice de Abrangência (IA): Mede a relevância de uma API em relação ao total de APIs analisadas.
Cálculo do IQA: Combinação ponderada dos índices IR e IC, multiplicada pelo índice IA.
Cálculo do IQD: Soma de todos os Índices de Qualidade da API (IQA).
Enquadramento dos níveis de qualidade em uma escala progressiva
Interpretação dos Resultados
Os resultados do índice serão interpretados para verificar se as instituições estão cumprindo os critérios de qualidade dos dados. A análise incluirá a avaliação dos três índices principais (IR, IC e IA) e a combinação ponderada desses índices para calcular o IQA e, subsequentemente, o IQD.
Exemplo ilustrativo
Considere a organização ABC com diferentes volumes de requisições para as APIs, como mostrado na tabela a seguir:
Organização
Família de API
Total de requisições
Total de requisições com erros
Tickets Abertos
Tickets Encerrados
Índice de
Resolução
Índice de Confiabilidade
Índice de
Abrangência
Índice de Qualidade de Dados
Organização
Família de API
Total de requisições
Total de requisições com erros
Tickets Abertos
Tickets Encerrados
Índice de
Resolução
Índice de Confiabilidade
Índice de
Abrangência
Índice de Qualidade de Dados
ABC
accounts
2.998.324
54.843
2
1
33%
98%
62%
69,5%
credit-cards-accounts
1.155.313
87.156
3
0
0%
92%
24%
loans
686.806
166.179
1
1
50%
76%
14%
Família de API: accounts
IR = Tickets encerrados / (Tickets abertos + Tickets encerrados)
IR = 1 / (2 + 1) = 33%
IC = (Total de requisições - Total de requisições com erros) / Total de requisições
IC = (2.998.324 - 54.843) / 2.998.324 = 98%
IA = Total de requisições / Soma total de requisições (todas as APIs)
IA = 2.998.324 / (2.998.324 + 1.155.313 + 686.806) = 62%
FC = (Dias com reporte / Total de dias no período)
FC = (27 / 30) = 0,9
IQA = ((IR x Peso IR) + (IC x Peso IC)) x IA
IQA = ((33% x 0.25) + (98% x 0.75)) x 62 = 51%
IQA = 51 * 0,9 = 45,9%
Família de API: credit-cards-accounts
IR = Tickets encerrados / (Tickets abertos + Tickets encerrados)
IR = 0 / (3 + 0) = 0%
IC = (Total de requisições - Total de requisições com erros) / Total de requisições
IC = (1.155.313 - 87.156) / 1.155.313 = 92%
IA = Total de requisições / Soma total de requisições (todas as APIs)
IA = 1.155.313 / (2.998.324 + 1.155.313 + 686.806) = 24%
FC = (Dias com Reporte / Total de Dias no Período)
FC = (24 / 30) = 0,8
IQA = ((IR x Peso IR) + (IC x Peso IC)) x IA
IQA = ((0% x 0.25) + (92% x 0.75)) x 24 = 17%
IQA = 17 * 0,8 = 13,6%
Família de API: loans
IR = Tickets encerrados / (Tickets abertos + Tickets encerrados)
IR = 1 / (1 + 1) = 50%
IC = (Total de requisições - Total de requisições com erros) / Total de requisições
IC = (686.806 - 166.179) / 686.806 = 76%
IA = Total de requisições / Soma total de requisições (todas as APIs)
IA = 686.806 / (2.998.324 + 1.155.313 + 686.806) = 14%
FC = (Dias com Reporte / Total de Dias no Período)
FC = (30 / 30) = 1
IQA = ((IR x Peso IR) + (IC x Peso IC)) x IA
IQA = ((100% x 0.25) + (76% x 0.75)) x 14 = 10%
IQA = 10 * 1 = 10%
Cálculo do IQD para a organização A
IQD = ∑ (IQA)
IQD = ∑ IQA ≈ 45,9% + 13,6% + 10% = 69,5%
Interpretação dos Dados no Painel
As informações contidas neste item têm como objetivo ajudar o usuário a compreender cada um dos campos exibidos no painel de “Índice de Qualidade de Dados (IQD)”. Desta forma, têm-se:
Em “
Controles
”:
Open
Campos
Descrição
Data início
informar a data de início ou período desejado, podendo ser uma data relativa ou intervalo de datas absoluto
Data fim
informar a data de fim ou período desejado, podendo ser uma data relativa ou intervalo de datas absoluto
Conglomerado
selecionar o conglomerado desejado
Visualizar por conglomerado ou instituição
selecionar a opção “instituição” para exibir os detalhes da organização pertencentes ao conglomerado ou a opção “conglomerado” para exibir o resultado por conglomerado
Em “
Desconformidade mensal do IDQ por Conglomerado
” (
Figura 1
) é apresentado o resultado consolidado da apuração mensal por conglomerado, de acordo com o filtro selecionado em “
Controles
”.
O painel é interativo. Por exemplo, ao clicar na célula “
NÃO CONFORME
” do conglomerado, serão exibidos os detalhamentos do mês de apuração.
Open
Figura 1 - Desconformidade mensal do IQD por conglomerado
Em “
Desconformidade mensal do IDQ por Instituição Participante
” (
Figura 2
) é apresentado o resultado consolidado da apuração mensal por
Instituição Participante
, de acordo com o filtro selecionado em “
Controles
”.
O painel é interativo. Por exemplo, ao clicar na célula “
NÃO CONFORME
” da Instituição, serão exibidos os detalhamentos do mês de apuração.
Open
Figura 2 - Desconformidade mensal do IQD por instituição participante
Em “
Desconformidade mensal - Instituição Participante
”, têm-se:
Open
Campos
Descrição
Mês apuração
mês referente a apuração
IQD
percentual referente ao Índice de Qualidade dos Dados (IQD) no mês de apuração
Status
não conforme
Em “
Detalhamento do cálculo do IQD por Instituição Participante
”, têm-se:
É possível ampliar a visualização do painel e exportar os dados para CSV ou Excel por meio da opção 'Opções de menu', localizada no canto superior direito”.
Open
Campos
Descrição
Mês/Ano
mês e ano referente a apuração
Conglomerado Participante
conglomerado/instituição selecionado(a)
Família de APIs
família de APIs correspondentes
Quantidade de Requisições
total de requisições reportadas no mês de apuração de determinada família de APIs
Quantidade de Requisições com erros
total de requisições com erros reportadas no mês de apuração de determinada família de APIs
Tickets abertos
total de tickets abertos quando contém erro em requisições de determinada família de APIs no mês de apuração
Tickets encerrados
total de tickets encerrados de determinada família de APIs no mês de apuração
Dia do mês
dia do mês em que houve reporte de dados para determinada família de API
Dias reportados
total de dias do mês de apuração em que houve reporte de dados para determinada família de API
Índice de Resolução (IR)
resultado do percentual do índice de resolução
Índice de Confiabilidade (IC)
resultado do percentual do índice de confiabilidade
Índice de Abrangência (IA)
resultado do percentual do índice de abrangência
Fator de Consistência (FC)
percentual do fator de consistência
Índice de Qualidade da API (IQA)
percentual do índice de qualidade da API
Índice de Qualidade de Família (IQF)
percentual do índice de qualidade de família
Dados e Fontes
Para o cálculo do índice, utilizam-se os dados provenientes do Motor de Qualidade de Dados (MQD). Esses dados são posteriormente consolidados na Plataforma Analítica de Dados (PAD), que é um repositório centralizado e serve como base para a análise e avaliação dos dados para o índice.
Essa estrutura permite uma avaliação precisa do índice e um monitoramento efetivo da qualidade dos dados no contexto do Open Finance.
Limitações e Considerações
Atualmente, não há visibilidade ou conhecimento de limitações ou considerações adicionais para esse índice . A análise será continuamente revisada e aprimorada conforme novos dados e informações se tornem disponíveis.

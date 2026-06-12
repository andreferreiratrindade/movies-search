---
                            title: "Metas de prazo máximo para atendimento de tickets - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "782401538_Metas+de+prazo+m+ximo+para+atendimento+de+tickets"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/782401538/Metas+de+prazo+m+ximo+para+atendimento+de+tickets"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Metas de prazo máximo para atendimento de tickets - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Item 2.3
Controle de versão
Versão
Data
Resumo das alterações
1
May 16, 2024
Versão inicial
2
Jan 3, 2025
Alteração da nomenclatura da métrica de "Requisição de informação, sugestão de melhorias e demanda de resolução de incidentes" para "Meta de prazo máximo para atendimento de tickets".
Flexibilização do percentual de tickets atendidos dentro do prazo máximo para fins de análise de desconformidade, conforme versão 2.0 do Manual de Monitoramento do Open Finance.
3
Apr 1, 2025
Revisão geral do documento
Inclusão dos tópicos “Interpretação dos Dados no Painel” e “Período de Apuração dos Dados”
Introdução e Objetivos
Esta métrica visa monitorar se as instituições participantes do Open Finance estão respeitando os prazos máximos de atendimento de tickets estabelecidos no Manual de Serviços Prestados pela Estrutura de Governança do Open Finance. Esses tickets incluem:
I - Tickets bilaterais
abertos entre instituições participantes no Service Desk
,
relativos a demandas de resolução de incidentes.
II- Tickets abertos pela Estrutura de Governança do Open Finance
que compreendem aqueles abertos por órgãos da Estrutura de Governança do Open Finance, fornecedores e ferramentas.
Sobre a Métrica
A métrica de “Prazo Máximo para Atendimento de Tickets” é uma medida quantitativa que avalia o tempo decorrido entre a abertura de um ticket e sua resolução final.
O prazo máximo para atendimento é estabelecido no Manual de Serviços Prestados pela Estrutura de Governança do Open Finance.
A conformidade é avaliada mensalmente, considerando que as instituições participantes devem atender ao
prazo máximo para pelo menos 80% de seus tickets elegíveis para a métrica, sem apresentar tickets com atraso superior ao dobro do prazo máximo estabelecido
.
Metodologia Simplificada
A metodologia adotada para o monitoramento e análise dos tickets inclui várias etapas:
Classificação dos tickets
Qualificação das categorias, subcategorias e categorias de 3° nível com “Sim” no atributo “Métricas de Monitoramento”, no
Service Desk
, dos tickets que serão elegíveis para fins da avaliação de conformidade
Classificação dos tickets
Qualificação das categorias, subcategorias e categorias de 3° nível com “Sim” no atributo “Métricas de Monitoramento”, no
Service Desk
, dos tickets que serão elegíveis para fins da avaliação de conformidade
Análise de prazos de atendimento dos tickets
Avaliação dos prazos de atendimento desses tickets, identificando a quantidade de tickets que no período de apuração se encontram abertos ou encerrados dentro do prazo estabelecido
versus
a quantidade daqueles com prazo vencido, calculando o percentual de tickets atendidos dentro do prazo
Avaliação detalhada dos tickets com prazo vencido
Cálculo para verificar se os dias em atraso dos tickets com prazo vencido, são superiores ao dobro dos dias de prazo do seu SLA
Os tickets
não elegíveis
são:
Categoria
Subcategoria
Categoria de 3º Nível
Monitoração e Gestão de Consequência
Desconformidades
Painel - Informações
Monitoração e Gestão de Consequência
Desconformidades
Painel - Melhorias
Monitoração e Gestão de Consequência
Notificação
-
Processo de onboarding
-
-
Interpretação dos Resultados
Admite-se, para fins de avaliação sobre a conformidade deste item monitorado, que as instituições participantes atendam ao prazo máximo para 80% dos tickets
elegíveis para fins desta avaliação, desde que não apresentem tickets com atraso superior ao dobro do seu prazo máximo.
A mensuração da quantidade de tickets por mês contempla:
Tickets cujo prazo de SLA esteja no mês de apuração;
Tickets não resolvidos cujo prazo de SLA seja anterior o mês de apuração;
Tickets resolvidos no mês de apuração cujo prazo de SLA seja anterior ao mês apuração.
Exemplo Ilustrativo
No exemplo da Figura 1, é possível visualizar o número total de tickets em cada um dos meses apresentados, assim como os diferentes cenários de resolução.
Open
Figura 1 - Possíveis cenários de resolução dos tickets
Período de Apuração dos Dados
Para fins do processo de monitoramento, o período de apuração referente a este item é mensal, compreendendo sempre entre o primeiro e o último dia no mês.
Interpretação dos Dados no Painel
As informações contidas neste item têm como objetivo ajudar o usuário a compreender cada um dos campos exibidos no painel de “
Atendimento dos tickets
”. Desta forma, têm-se:
Em “
Controles
”:
Open
Campos
Descrição
Mês apuração
informar a data ou período desejado, podendo ser uma data relativa ou intervalo de datas absoluto
Conglomerado
selecionar o conglomerado desejado
Visualizar organização
selecionar a opção “sim” para exibir os detalhes da organização pertencentes ao conglomerado ou a opção “não” para exibir o resultado por conglomerado
Em “
Desconformidade mensal
” é apresentado o resultado consolidado da apuração mensal por conglomerado e/ou organização, de acordo com o filtro selecionado em “
Controles
”.
O painel é interativo. Por exemplo, ao clicar na célula “
NÃO CONFORME
” do conglomerado ou da organização, serão exibidos os detalhamentos do mês de apuração. Além disso, é possível maximizar a visualização do painel e exportar os dados para CSV ou Excel.
Open
Importante
: As células em branco indicam conformidade.
Em “
Detalhes mês apuração
” têm-se, o resultado por conglomerado e por organização.
Open
Campos
Descrição
Conglomerado e/ou Organização
exibição do conglomerado e/ou organização selecionada em “Controles”
Mês apuração
mês referente a apuração
Total acima dobro SLA
quantidade total de tickets que se encontram acima do dobro do prazo do SLA
% mês conforme
percentual total dos tickets encerrados dentro do prazo de SLA no mês de apuração
Em “
Tickets referentes ao mês de apuração
” têm-se:
Open
Campos
Descrição
Conglomerado
exibição do conglomerado selecionado
Organização
exibição da organização selecionado
Mês apuração
mês referente a apuração
Ticket
número do ticket referente a apuração
Tipo
tipo do ticket apurado (bilateral ou estrutura)
Categoria
categoria em que o ticket está enquadrado
Subcategoria
subcategoria em que o ticket está enquadrado
Data de abertura
data de abertura e/ou solicitação do ticket
Prazo SLA
data máxima para resolução ticket
Data fechamento
data em que o ticket foi encerrado
Dias excedente SLA
quantidade total de dias excedentes do prazo do SLA
Acima do dobro SLA
"sim" indica que o ticket ultrapassou o dobro do prazo do SLA, enquanto "não" significa que o ticket não ultrapassou o dobro do prazo do SLA
Dados e Fontes
Para a execução desta métrica, são utilizadas informações oriundas do sistema de
Service Desk
utilizado pela Estrutura de Governança do Open Finance e pelas instituições participantes. Os dados incluem, mas não se limitam a data de solicitação, data de encerramento, prazo de SLA, SLA em dias, SLA dias em atraso e Métricas de Monitoramento. Esses dados são consolidados na Plataforma Analítica de Dados (PAD), um repositório centralizado que serve como base para a análise e avaliação da métrica.
Os tickets sem SLA foram classificados no atributo de “Métricas de Monitoramento” como não elegíveis para a avaliação deste item monitorado.
A data de fechamento que está sendo considerada para os tickets da Subcategoria de “Jornada de UX” e categoria de 3° nível “Descumprimento Ditame Regulatório” corresponde à data na qual o ticket é atualizado para CORREÇÃO IMPLEMENTADA.
Limitações e Considerações
O monitoramento dos prazos máximos de atendimento de tickets estabelecidos no Manual de Serviços Prestados pela Estrutura de Governança do Open Finance, resulta num status de conformidade ou desconformidade de acordo com a data de referência da avaliação, que é sempre o primeiro dia do mês posterior ao de apuração, e por isso, o cancelamento de tickets que ocorrerem após a data de referência, não ensejarão mudança de status de conformidade.
Responsável pela Aprovação
GT Infraestrutura

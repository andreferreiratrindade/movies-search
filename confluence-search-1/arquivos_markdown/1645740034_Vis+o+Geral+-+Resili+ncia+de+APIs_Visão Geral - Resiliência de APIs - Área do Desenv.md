---
                            title: "Visão Geral - Resiliência de APIs - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1645740034_Vis+o+Geral+-+Resili+ncia+de+APIs"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1645740034/Vis+o+Geral+-+Resili+ncia+de+APIs"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Visão Geral - Resiliência de APIs - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Controle de versão
Versão
Data
Resumo das alterações
1
31 de mar. de 2026
Versão inicial
Introdução e Objetivos
Esta aba do painel tem como objetivo demonstrar uma visão geral do sistema e conglomerados quanto a volume, performance e conformidade no grupo de métricas regulatórias denominado Resiliência de APIs, composto por 2.1.I Tempo de resposta das APIs, 2.1.II Disponibilidade das APIs, 2.1.III Volume de requisições com status code HTTP 529 e 2.4 Reporte de Informações.
Interpretação dos Dados no Painel
As informações contidas neste item têm como objetivo ajudar o usuário a compreender cada um dos campos exibidos no painel de “Notas”. Desta forma, têm-se:
Em “
Controls
”:
Open
Campos
Descrição
Visão : Instituição
informar a visão para a exibição dos dados
Conglomerado
selecionar o conglomerado desejado
Referencia
selecionar o mês de referencia
Neste painel é apresentado o resultado consolidado da apuração mensal por conglomerado e/ou organização, de acordo com o filtro selecionado em “
Controles
”.
Open
O painel é interativo. Por exemplo, ao clicar na linha do conglomerado ou da instituição, serão exibidos os detalhamentos da instituição. Além disso, é possível maximizar a visualização do painel e exportar os dados para CSV ou Excel.
Open
Campos
Descrição
Rows
linha de cada instituição
Resiliência
média das notas, desconsiderando métrica com nota “null”
Sobrecarga
nota da métrica
Tempo de Resposta
nota da métrica
Disponibilidade Diária
nota da métrica
Disponibilidade Longa
nota da métrica
Reporte
nota da métrica
Volume
Server
quantidade de chamadas em que o conglomerado atuou como servidor
Volume
Client
quantidade de chamadas em que o conglomerado atuou como cliente
No
detalhamento diário
, são apresentados gráficos que mostram o volume de chamadas
server
e
client
:
Open
Adicionalmente, são exibidos gráficos abrangendo todas as métricas monitoradas de resiliência de APIs.
Open
Dados e Fontes
Para o cálculo da métrica, utiliza-se um conjunto diversificado de dados provenientes de diferentes fontes. A principal fonte informacional é a Plataforma de Coleta de Métricas (PCM), que consolida os dados a partir dos reportes enviados pelas instituições participantes. Além disso, as planilhas auto reportadas pelas instituições são integradas e consolidadas na Plataforma Analítica de Dados (PAD), um repositório centralizado que serve como base para a análise e avaliação da métrica. Essa combinação de dados provenientes da PCM e das planilhas auto reportadas permite uma avaliação precisa da métrica e um monitoramento efetivo do desempenho e disponibilidade das APIs no contexto do Open Finance.
Limitações e Considerações
Atualmente, não há visibilidade ou conhecimento de limitações ou considerações adicionais para esta métrica. A análise será continuamente revisada e aprimorada conforme novos dados e informações se tornem disponíveis.
Material de Suporte
IN706
Exibe Normativo
IN615
Exibe Normativo
Responsável pela Aprovação AOF
Arquitetura e Plataforma (Diretoria de Tecnologia e Operações)
Telemetria (Diretoria de Monitoramento)

---
                            title: "Tempo de Resposta das APIs - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "801996803_Tempo+de+Resposta+das+APIs"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/801996803/Tempo+de+Resposta+das+APIs"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Tempo de Resposta das APIs - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Controle de versão
Versão
Data
Resumo das alterações
1
May 27, 2024
Versão inicial
2
Jan 24, 2025
Segregação da métrica de desempenho de APIs da métrica de disponibilidade de APIs.
Maior detalhamento do cálculo da métrica.
3
Mar 24, 2025
Revisão geral do documento
Inclusão do tópico “Interpretação dos Dados no Painel”
Introdução e Objetivos
Esta métrica visa monitorar se os
endpoints
das APIs das instituições participantes estão cumprindo os SLAs de tempo de resposta, estabelecidos no Manual de APIs do Open Finance.
Considerando que, o tempo de resposta de cada requisição é o tempo transcorrido entre o recebimento de uma requisição que não ultrapassa os limites de tráfego e o momento em que a requisição é completamente respondida.
Sobre a Métrica
A métrica de Tempo de Resposta das APIs considera o valor do percentil 95 e o número de requisições ocorridas no dia.
As medições devem ser realizadas de maneira independente para cada versão "
major
" dos
endpoints
em produção e devem ser consideradas as requisições com todos os códigos de retorno possíveis,
com exceção dos associados a limites de tráfego e limites operacionais
.
O valor do tempo de resposta a ser considerado para uma requisição é o valor reportado pelo consumidor da API,
ou seja, o valor reportado pela instituição iniciadora de pagamentos nas APIs de “Serviços de Iniciação de Pagamentos” e o valor reportado pela receptora de dados no caso de APIs de "Dados Cadastrais e Transacionais".
Na falta de informações dos consumidores, serão utilizadas as informações dos provedores
para o cálculo do SLA de desempenho, ou seja, o valor reportado pela instituição detentora de contas nas APIs de "Serviços de Iniciação de Pagamentos", e o valor reportado pela instituição transmissora de dados no caso de APIs de "Dados Cadastrais e Transacionais".
Os
endpoints
das APIs deverão manter, diariamente, o SLA do percentil 95 do tempo de resposta em no máximo:
I - 1.500ms, em
endpoints
classificados como de alta e média-alta frequências;
II - 2.000ms, em
endpoints
classificados como de média frequência; e
III - 4.000ms, em
endpoints
classificados como de baixa frequência.
A conformidade é avaliada mensalmente, verificando se os
endpoints
das APIs das instituições participantes atenderam aos SLAs do desempenho.
Metodologia Simplificada
A metodologia adotada para o monitoramento do tempo de resposta das APIs avalia se, diariamente, o percentil 95 dos endpoints cumpre o seu SLA, ou seja, se em um dia que o endpoint avaliado receba 100 requisições, o tempo de resposta de pelo menos 95 requisições é inferior ao SLA.
Aspectos Técnicos
O monitoramento inclui várias etapas:
Filtro inicial dos dados provenientes da Plataforma de Coleta de Métricas (PCM)
Serão consideradas apenas as chamadas com tempo de processamento maior que zero, ou seja,
processtimespan
> 0
Serão excluídas as requisições com status ‘PAIRED_INCONSISTENT’ e ‘DISCARDED’ para todos os
endpoints
Serão excluídas as chamadas com
status code
423, 429 e 529
Agrupamento dos dados (serão agrupados para facilitar o cálculo do percentil 95 (P
95
))
Timestamp
:
data da chamada da API (yyyy-mm-dd)
Serverorgid
: identificador da organização consumidora da API utilizada pelo cliente para a solicitação do dado
Endpoint
:
endpoint
da API com o método e recurso
Cálculo do percentil
Coleta dos dados
: Seja R o conjunto de todos os tempos de resposta de um dia, onde “ri” é o tempo de resposta da i-ésima requisição. Ou seja, R={r1, r2, ..., rn}. Nessa coleta é utilizado o
processtimespan
quando
clientorgid
=
organisationid
ou
serverorgid
=
organisationid
e
status
‘UNPAIRED’
Cálculo do índice do percentil 95
: o índice para o percentil 95, denotado por i95, é calculado pela fórmula i95 = 0.95 ∗ n, arredondado para o número inteiro mais próximo, e onde “n” representa número de requisições
Ordenação dos dados
: O conjunto R em ordem crescente para obter o conjunto ordenado Rord={r(1), r(2), ..., r(n)}, onde r(1) é o menor tempo de resposta e r(n) é o maior
Obtenção do valor do percentil 95
: o valor do percentil 95, denotado por P
95
, é o valor no índice i95 no conjunto ordenado Rord. Ou seja, P
95
= r(i95)
Interpretação dos Resultados
Para fins do processo de monitoramento, o período de apuração referente a este item é mensal e a análise de desconformidade é feita por conglomerado. A título de exceção, no caso de conglomerados que possuam equipes N2 por CNPJ, a desconformidade será gerada para a instituição.
Considera-se que um
endpoint
está em conformidade caso tenha respeitado o SLA do desempenho em pelo menos 90% dos dias do mês de referência, arredondando-se para o número inteiro mais próximo, desde que o valor do percentil 95 (P
95
) dos demais dias não tenha sido superior ao SLA do desempenho aumentado em 20%.
Os dias do mês de referência são os dias do mês em que houve requisições para o
endpoint
avaliado.
Assim, consideramos cada conformidade diária:
CONFORME
DENTRO DA TOLERÂNCIA
NÃO CONFORME
P
95
< SLA
SLA < P
95
< SLA * 1,2
P
95
> SLA * 1,2
E fazemos a apuração mensal:
CONFORME
NÃO CONFORME
Se a quantidade de dias conforme ≥ 90% de dias de acionamento
Se a quantidade de dias não conforme > 0
Se a quantidade de dias não conforme < 90% de dias de acionamento
Importante
: A métrica não se aplica às APIs de "
Webhook
".
Exemplo Ilustrativo
I - Em um mês de 30 dias, em que um
endpoint
de alta frequência tenha apresentado valor de P
95
inferior a 1.500ms em 27 dias e, nos demais dias, tenha apresentado valor de P
95
entre 1.500ms e 1.800ms (1.500ms * 1,2 = 1.800ms), o
endpoint
está em
conformidade
para fins do processo de monitoramento naquele mês.
II - Em um mês de 31 dias, em que um
endpoint
de alta frequência tenha apresentado valor de P
95
inferior a 1.500ms em 28 dias e, nos demais dias, tenha apresentado, em pelo menos um dos dias, valor de P
95
superior a 1.800ms (1.500ms * 1,2 = 1.800ms), o
endpoint
está
não conforme
para fins do processo de monitoramento naquele mês.
Interpretação dos Dados no Painel
As informações contidas neste item têm como objetivo ajudar o usuário a compreender cada um dos campos exibidos no painel de “Tempo de Respostas das APIs”. Desta forma, têm-se:
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
Endpoint
selecionar o
endpoint
desejado ou selecionar todos os
endpoint
s
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
Nos detalhes do mês de apuração:
Open
Campos
Descrição
Mês da apuração
mês referente a apuração
Método HTTP
método da requisição
Endpoint
endpoint
da requisição
Dias acionamentos
total de dias do mês de apuração que o
endpoint
foi acionado
Dias P
95
< frequência
total de dias do mês de apuração em que o P
95
(percentil 95) encontra-se inferior a frequência do
endpoint
Dias P
95
entre a frequência
total de dias em que o P
95
(percentil 95) encontra-se no intervalo de tempo da frequência do
endpoint
Dias P
95
> tolerância
total de dias do mês de apuração em que o P
95
(percentil 95) encontra-se superior a tolerância de 20%
Status
não conforme (P95>SLA*1,2)
No detalhamento, é possível visualizar:
Open
Campos
Descrição
Dias acionamento
dia do mês de apuração em que o
endpoint
foi acionado
Método HTTP
método da requisição
Endpoint
endpoint
da requisição
Frequência API (ms)
SLA da frequência de classificação do
endpoint
Quantidade de requisições
total de requisições utilizadas para o cálculo de um determinado dia do mês de apuração
P
95
(ms)
percentil 95 do tempo de requisição por milissegundo
Status
dentro da tolerância (SLA<P95<SLA*1,2) ou
não conforme (P95 > SLA*1,2)
Importante
: para que o detalhamento seja exibido, deve-se sempre clicar na célula “NÃO CONFORME”.
Open
Campos
Descrição
x-fapi-interaction-id
identificador único do reporte
Server
servidor reportado na requisição
Client
cliente reportado na requisição
Método HTTP
método da requisição
Endpoint
endpoint
da requisição
Requisição (ms)
tempo de resposta da requisição
Importante:
serão exibidos no máximo cinco evidências de reporte.
Dados e Fontes
Para o cálculo desta métrica, a fonte informacional é a Plataforma de Coleta de Métricas (PCM), que consolida os dados a partir dos reportes enviados pelas instituições participantes.  Todos os métodos e recursos dos
endpoints
serão avaliados. Esses dados são consolidados na Plataforma Analítica de Dados (PAD), um repositório centralizado que serve como base para a análise e avaliação da métrica.
Limitações e Considerações
Atualmente, não há visibilidade ou conhecimento de limitações ou considerações adicionais para esta métrica. A análise será continuamente revisada e aprimorada conforme novos dados e informações se tornem disponíveis.
Responsável pela Aprovação
GT Arquitetura

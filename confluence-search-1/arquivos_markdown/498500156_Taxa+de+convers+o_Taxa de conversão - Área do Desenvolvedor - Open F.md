---
                            title: "Taxa de conversão - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "498500156_Taxa+de+convers+o"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/498500156/Taxa+de+convers+o"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Taxa de conversão - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            item 2.6.2
Controle de versão
Versão
Data
Resumo das alterações
1
May 20, 2024
Versão inicial
Introdução e Objetivos
Esta métrica tem como propósito de monitorar a eficiência das jornadas de compartilhamento de dados e de iniciação de pagamentos dentro do ecossistema do Open Finance. O objetivo é assegurar padrões de conversão, refletindo a qualidade e a eficácia dessas jornadas na facilitação de operações seguras e eficientes entre as instituições participantes e seus clientes.
Sobre a Métrica
Esta métrica foca em duas áreas principais:
I. Compartilhamento de dados: A taxa de conversão para compartilhamento de dados é calculada com base na proporção de consentimentos gerados com sucesso em relação ao número total de solicitações de criação de consentimentos, direcionadas para a instituição transmissora de dados.
II. Iniciação de Transação de Pagamento: Similarmente, a taxa de conversão para iniciação de transação de pagamento é determinada pela quantidade de consentimentos gerados com sucesso em comparação ao volume de solicitações de criação de consentimentos, direcionadas para a instituição detentora de conta.
As taxas mínimas de conversão são definidas como 80% da média ponderada das três maiores taxas de conversão, tanto para instituições transmissoras de dados quanto para instituições detentoras de conta, calculadas nos últimos três meses, excluindo o mês de referência. Uma tolerância de três pontos percentuais é permitida para essas taxas mínimas.
Metodologia Simplificada
Cálculo da Taxa de Conversão: A taxa é calculada mensalmente, dividindo o número de consentimentos gerados com sucesso pelo número total de solicitações de criação de consentimentos, excluindo-se aquelas que retornaram erros por falta de permissões adequadas.
Período de apuração: As taxas são apuradas mensalmente, considerando todas as semanas cujas sextas-feiras ocorrem dentro do mês de referência.
Exclusões no cálculo: Solicitações de criação de consentimentos que resultaram exclusivamente em erros relacionados a tentativas de acesso sem as devidas permissões não são incluídas no cálculo das taxas de conversão.
Interpretação dos Resultados
Para compreender a taxa de conversão no contexto do Open Finance, usa-se os dados fornecidos pelas instituições participantes abrangendo um período de três meses, excluindo o mês de referência. A taxa de conversão é um indicador crucial que reflete a eficiência das jornadas de compartilhamento de dados e iniciação de pagamentos, calculada pela quantidade de consentimentos gerados com sucesso (access tokens gerados) dividida pela quantidade total de solicitações de criação de consentimentos.
Identificação das três maiores taxas de conversão (Top 3)
Para determinar as três maiores taxas de conversão, calcula-se o percentual de conversão ponderado pela quantidade total de consentimentos solicitados para cada instituição, seguindo esta lógica:
Cálculo da taxa ponderada de conversão:
Para cada instituição, multiplica-se a taxa de conversão pelo total de consentimentos solicitados durante o período de apuração.
Soma-se os valores resultantes para todas as instituições.
Divide-se essa soma pela quantidade total de consentimentos solicitados para as instituições no Top 3.
Usando esse método, identifica-se as instituições com as três maiores taxas de conversão ponderadas.
Cálculo da taxa mínima de conversão
A taxa mínima de conversão é definida como 80% da média ponderada das taxas de conversão das três maiores taxas de conversão. Com base nos cálculos, chega-se a uma taxa mínima de conversão. Adicionalmente, aplica-se um limite de tolerância de três pontos percentuais, resultando numa taxa mínima ajustada de conversão.
Limiares estabelecidos
Limite para notificação: 80% da taxa mínima de conversão.
Limite para diagnóstico (avaliação independente): 60% da taxa mínima.
Exemplo Ilustrativo
Considere o seguinte cenário para ilustrar o processo para o período de janeiro a março, sendo março o mês de referência.
Open
No exemplo anterior, a Instituição A com uma taxa de conversão média de 60,2% lidera as taxas de conversão, seguida pela Instituição B com 50,3% e pela Instituição C com 46,1%.
Cálculo da média ponderada das três maiores taxas de conversão
A média ponderada das três maiores taxas de conversão é calculada somando-se as taxas de conversão ponderadas pelo número de consentimentos solicitados (etapa 2 do funil das jornadas de compartilhamento de dados e etapa 4 do funil da jornada de iniciação de pagamentos) e dividindo esse valor pelo total de consentimentos solicitados. No exemplo, a média ponderada resultou em 56,9%.
Primeiro, calcula-se o total de consentimentos solicitados por cada instituição no período de janeiro a março
Instituição A: 550.581 + 350.210 + 494.310 + 459.320 + 421.015 + 504.100 + 90.451 + 580.211 + 605.051 + 595.151 + 641.510 + 575.101 + 655.011 = 6.522.022
Instituição B: 151.002 + 157.448 + 163.383 + 122.041 + 155.376 + 137.648 + 169.040 + 110.091 + 151.090 + 110.803 + 189.893 + 166.027 + 115.193 = 1.899.035
Instituição C: 57.354 + 67.288 + 79.410 + 60.399 + 76.852 + 70.380 + 68.173 + 67.530 + 74.913 + 75.106 + 64.694 + 58.036 + 73.052 = 893.187
Em seguida, calcula-se a média ponderada das taxas de conversão
Instituição A: 60,2% * 6.522.022 = 3.926.241,24
Instituição B: 50,3% * 1.899.035 = 955.628,61
Instituição C: 46,1% * 893.187 = 411.586,71
Somando os valores ponderados e dividindo pelo total de consentimentos solicitados
Média ponderada = (3.926.241,24 + 955.628,61 + 411.586,71) / (6.522.022 + 1.899.035 + 893.187) = 56,83%, arredondado para 56,9%
Cálculo de 80% da média ponderada
A taxa mínima de conversão é definida como 80% da média ponderada das três maiores taxas de conversão. No exemplo, a taxa mínima de conversão é 45,6%.
80% de 56,6% = 0,8 x 56,6 = 45,52% arredondando para 45,6%
Aplicação da tolerância de três pontos percentuais
Para acomodar pequenas variações e manter uma margem de tolerância, três pontos percentuais são subtraídos da taxa mínima de conversão. No exemplo, a taxa mínima ajustada é 42,6%.
Taxa mínima de conversão ajustada: 45,6% - 3% = 42,6%
Cálculo para notificação (80% da taxa mínima)
Caso uma instituição apresente uma taxa de conversão inferior a 80% da taxa mínima, ela será notificada para tomar ações corretivas. Este limiar é estabelecido para garantir que as instituições mantenham um desempenho aceitável. No exemplo, o limite para notificação é 36,4%.
80% de 45,6% = 0,8 x 45,6 = 36,48%, arredondado para 36,4%
Cálculo para diagnóstico (avaliação Independente - 60% da taxa mínima)
Se a taxa de conversão de uma instituição cair abaixo de 60% da taxa mínima, será necessário uma avaliação independente por uma empresa especializada para diagnosticar e corrigir os problemas subjacentes. No exemplo, o limite para avaliação independente é 27,3%.
60% de 45,6% = 0,6 x 45,6 = 27,36%, arredondado para 27,3%
Com base nos cálculos realizados, os limiares são definidos da seguinte maneira:
Open
Este exemplo ilustra como as taxas de conversão são calculadas e aplicadas no monitoramento das atividades das instituições participantes do Open Finance, visando aprimorar continuamente a eficiência e a eficácia das jornadas de compartilhamento de dados e iniciação de pagamentos.
Dados e Fontes
A coleta de dados para esta métrica é realizada por meio de uma abordagem integrada que envolve várias fontes de dados, garantindo uma avaliação abrangente e precisa no ecossistema do Open Finance.
As informações iniciais são extraídas das planilhas auto reportadas pelas instituições participantes e dos dados consolidados a partir dos reportes enviados através da Plataforma de Coleta de Métricas (PCM).
A combinação dessas fontes de dados cria um ecossistema de informações robusto, permitindo uma avaliação precisa da métrica e um monitoramento efetivo das taxas de conversão no contexto do Open Finance.
Limitações e Considerações
Atualmente, não há visibilidade ou conhecimento de limitações ou considerações adicionais para esta métrica. A análise será continuamente revisada e aprimorada conforme novos dados e informações se tornem disponíveis.
Responsável pela Aprovação
GT Arquitetura

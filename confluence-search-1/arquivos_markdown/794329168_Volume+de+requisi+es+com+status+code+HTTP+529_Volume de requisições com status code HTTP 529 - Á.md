---
                            title: "Volume de requisições com status code HTTP 529 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "794329168_Volume+de+requisi+es+com+status+code+HTTP+529"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/794329168/Volume+de+requisi+es+com+status+code+HTTP+529"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Volume de requisições com status code HTTP 529 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Controle de versão
Versão
Data
Resumo das alterações
1
31 de jan. de 2025
Versão inicial
Introdução e Objetivos
Esta métrica visa monitorar as requisições que excederem os limites de TPS e que devem ser respondidas com
status code
HTTP 529 (
Site is overloaded
). A Estrutura de Governança do Open Finance visa, com esta métrica, fornecer informação sobre a infraestrutura das instituições provendo APIs no
Open Finance
que deve ter a capacidade de, no mínimo, atender a 300 requisições simultâneas por segundo (TPS).
Sobre a Métrica
A métrica se baseia no volume de requisições excedentes que retornam o status code HTTP 529.
Metodologia Simplificada
Para fins de monitoramento deste item, o período de apuração será mensal, conforme orientado pelo Manual de Monitoramento do Open Finance Brasil.
A metodologia adotada para o monitoramento do volume de requisições com status code HTTP 529  avalia se, diariamente, esse volume é inferior a 0,5% das requisições válidas.
Aspectos Técnicos
Excluir chamadas com status 'PAIRED_INCONSISTENT' e ‘DISCARTED’
Considerar as requisições válidas que retornam
status code
da faixa 2XX, 5XX, igual a 408 ou igual a 422
Interpretação dos Resultados
Para fins do processo de monitoramento, o período de apuração referente a este item é mensal e a análise de desconformidade é feita por conglomerado.
Considera-se que uma determinada instituição participante está em conformidade caso tenha respeitado o limite de 0,5% em pelo menos 90% dos dias do mês de referência, arredondando-se para o número inteiro mais próximo, desde que o volume diário de requisições com
status code
HTTP 529 dos demais dias não tenha sido superior a 5%.
Exemplo Ilustrativo
Para ilustrar as condições de conformidade e desconformidade, considere o seguinte exemplo:
O Banco ABC, com uma capacidade inicial de 300 TPS, recebeu um pico de 350 TPS em 05/12. As 50 requisições excedentes retornaram o status HTTP 529, totalizando 0,54% das requisições válidas naquele dia. Isso exige um aumento imediato da capacidade para 450 TPS.
Ainda no mês de dezembro, o Banco ABC teve 28 dias dentro do limite de 0,5%, 2 dias com valores entre 0,51% e 5%, e 1 dia crítico com 6,2%. Como violou o limite de 5% em um dia, foi classificado como não conforme, mesmo tendo 90% dos dias dentro do padrão.
Dados e Fontes
Para o cálculo da métrica, utiliza-se um conjunto diversificado de dados provenientes de diferentes fontes. A principal fonte informacional é a Plataforma de Coleta de Métricas (PCM), que consolida os dados a partir dos reportes enviados pelas instituições participantes. Além disso, as planilhas auto reportadas pelas instituições são integradas e consolidadas na Plataforma Analítica de Dados (PAD), um repositório centralizado que serve como base para a análise e avaliação da métrica. Essa combinação de dados provenientes da PCM e das planilhas auto reportadas permite uma avaliação precisa da métrica e um monitoramento efetivo do desempenho e disponibilidade das APIs no contexto do Open Finance.
Limitações e Considerações
Atualmente, não há visibilidade ou conhecimento de limitações ou considerações adicionais para esta métrica. A análise será continuamente revisada e aprimorada conforme novos dados e informações se tornem disponíveis.
Responsável pela Aprovação
GT Arquitetura

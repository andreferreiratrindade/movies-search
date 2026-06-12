---
                            title: "Cadastro Atualizado das APIs - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "498499760_Cadastro+Atualizado+das+APIs"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/498499760/Cadastro+Atualizado+das+APIs"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Cadastro Atualizado das APIs - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            ITEM 2.2 - II
Controle de versão
Versão
Data
Resumo das alterações
1
May 23, 2024
Versão inicial
Introdução e Objetivos
Esta métrica visa garantir que as informações relativas às APIs das instituições participantes armazenadas pela Estrutura Responsável pela Governança do Open Finance estejam corretas e atualizadas. A conformidade com esta métrica assegura a integridade e a eficácia do ecossistema do Open Finance.
Sobre a Métrica
A métrica se baseia na verificação dos recursos das APIs das instituições participantes para determinar a conformidade das informações. Para que uma instituição esteja em conformidade com essa métrica, todos os critérios abaixo devem ser atendidos com sucesso para cada uma de suas marcas. A Estrutura Responsável pela Governança do Open Finance verifica e exige que as informações estejam corretas e atualizadas.
Recursos das APIs
Verifica se os recursos das APIs publicadas têm todos os endpoints cadastrados.
Confirma se o parâmetro FamilyComplete está definido como True.
Metodologia Simplificada
Para fins de monitoramento deste item, o período de apuração será mensal, conforme orientado pelo Manual de Monitoramento do Open Finance Brasil. A metodologia de análise envolve:
Recursos das APIs: Verificação da publicação completa dos endpoints das APIs e confirmação do parâmetro FamilyComplete como True.
Interpretação dos Resultados
Os resultados da métrica serão interpretados para verificar se as instituições estão cumprindo os critérios de conformidade para o cadastro atualizado das APIs no Diretório de Participantes. A conformidade é evidenciada pelo parâmetro FamilyComplete definido como True, indicando que todos os endpoints previstos para uma família de APIs foram cadastrados.
A desconformidade é pontuada quando forem localizadas hipóteses de falha contendo o valor 'Incomplete Family Type', evidenciando que nem todos os endpoints das APIs foram cadastrados para uma determinada família de APIs.
Exemplo Ilustrativo
Considere uma instituição que, ao cadastrar seus endpoints no Diretório, não os tenha cadastrado integralmente, resultando no atributo FamilyComplete com o valor False. Nesse caso, a instituição seria pontuada em uma situação de desconformidade.
Dados e Fontes
Para o cálculo da métrica, utilizam-se os dados obtidos a partir do Diretório de Participantes e da Ferramenta de Validação de Produção (FVP). A FVP gera logs detalhados sobre o sucesso ou falha do cenário de teste executado. Esses logs são consolidados na Plataforma Analítica de Dados (PAD), um repositório centralizado que serve como base para a análise e avaliação da métrica. A combinação dessas fontes de dados permite uma avaliação precisa da métrica e um monitoramento efetivo da conformidade regulatória no contexto do Open Finance.
Limitações e Considerações
Atualmente, não há visibilidade ou conhecimento de limitações ou considerações adicionais para esta métrica. A análise será continuamente revisada e aprimorada conforme novos dados e informações se tornem disponíveis.
Responsável pela Aprovação
Squad Sandbox

---
                            title: "Publicação das APIs pelas instituições participantes - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "498499852_Publica+o+das+APIs+pelas+institui+es+participantes"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/498499852/Publica+o+das+APIs+pelas+institui+es+participantes"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Publicação das APIs pelas instituições participantes - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            ITEM 2.2 - I
Controle de versão
Versão
Data
Resumo das alterações
1
May 20, 2024
Versão inicial
Introdução e Objetivos
Esta métrica visa garantir que as instituições participantes do Open Finance publiquem devidamente suas APIs, conforme os requisitos estabelecidos pela regulamentação e pela Estrutura Responsável pela Governança do Open Finance. A métrica monitora a conformidade das APIs e suas versões atuais registradas no Diretório de Participantes e no ambiente produtivo, assegurando a consistência e disponibilidade das APIs em ambos os ambientes.
Sobre a Métrica
A métrica abrange a verificação das APIs e suas versões atuais registradas no Diretório de Participantes e no ambiente produtivo, de acordo com o cronograma estabelecido pela regulamentação ou pela Estrutura Responsável pela Governança do Open Finance, incluindo o período de convivência das versões.
Consistência entre Diretório e ambiente produtivo: A métrica verifica se as APIs registradas no Diretório estão publicadas no ambiente produtivo das instituições participantes. A desconformidade é identificada se houver diferenças entre o que está registrado no Diretório e o que foi publicado no ambiente produtivo.
Disponibilidade de versões atuais e em desuso: Durante o período de convivência, tanto a versão atual (current) quanto a versão em desuso (deprecated) das APIs devem estar disponíveis no Diretório e no ambiente produtivo.
A desconformidade é identificada se qualquer uma dessas versões não estiver publicada conforme exigido.
Identificação de endpoints no ambiente produtivo: A identificação dos endpoints no ambiente produtivo é feita por meio de requisições aos endpoints analisados. Requisições respondidas com o código de status HTTP 404 por mais de 8 horas são consideradas como indisponíveis no contexto dessa métrica.
Metodologia Simplificada
Para fins de monitoramento deste item, o período de apuração será no momento da detecção da desconformidade, conforme orientado pelo Manual de Monitoramento do Banco Central do Brasil (BCB). A avaliação envolverá:
Verificação de Consistência: Comparação entre as APIs registradas no Diretório e as APIs publicadas no ambiente produtivo.
Checagem da Disponibilidade: Monitoramento da disponibilidade das versões atuais e em desuso das APIs durante o período de convivência.
Teste de Endpoints: Requisições aos endpoints analisados para verificar a disponibilidade das APIs no ambiente produtivo.
Interpretação dos Resultados
Os resultados da métrica serão utilizados para identificar instituições que não estão cumprindo com os requisitos de publicação das APIs, conforme estabelecido pela regulamentação e pela Estrutura Responsável pela Governança do Open Finance. A análise incluirá:
Consistência entre Diretório e ambiente produtivo: Verificação se todas as APIs registradas no Diretório estão publicadas no ambiente produtivo.
Disponibilidade de versões atuais e em desuso: Confirmação de que ambas as versões das APIs (current e deprecated) estão disponíveis durante o período de convivência.
Disponibilidade dos endpoints: Identificação de endpoints que respondem com o código de status HTTP 404 por mais de 8 horas.
Exemplo Ilustrativo
Suponha que uma instituição tenha registrado no Diretório de Participantes a API Canais de Atendimento (
channels
). A métrica estará em desconformidade se a API estiver presente no Diretório, mas não tiver sido disponibilizada no ambiente produtivo da instituição.
Além disso, considere que essa API esteja na sua versão atual (
current
) 2.0.0 e que sua versão anterior esteja marcada como em desuso (
deprecated
) na versão 1.0.2. Durante o período de convivência, ambas as versões devem estar disponíveis tanto no Diretório quanto no ambiente produtivo. Se alguma dessas versões não estiver publicada, a instituição estará em desconformidade em relação ao item monitorado.
Open
Dados e Fontes
Para o cálculo da métrica, utilizam-se os dados obtidos a partir do Diretório de Participantes do Open Finance. Esses dados são consolidados na Plataforma Analítica de Dados (PAD), um repositório centralizado que serve como base para a análise e avaliação da métrica.
Adicionalmente, integram-se à PAD dados oriundos do Gerenciador de Configuração (GDC). O GDC complementa as informações disponíveis na PAD, consolidando detalhes adicionais sobre todas as versões das APIs mantidas pela Estrutura de Governança do Open Finance, incluindo endpoints, famílias de APIs, versões e as respectivas datas de início e término de vigência. Essas informações são mantidas e atualizadas pelos grupos de produtos responsáveis.
A combinação dessas fontes de dados — Diretório de Participantes, monitoramento sintético, dados consolidados na PAD e informações do GDC, cria um ecossistema de informações, permitindo avaliação da métrica e monitoramento efetivo das APIs no contexto do Open Finance.
Limitações e Considerações
Atualmente, não há visibilidade ou conhecimento de limitações ou considerações adicionais para esta métrica. A análise será continuamente revisada e aprimorada conforme novos dados e informações se tornem disponíveis.
Responsável pela Aprovação AOF
Gerência de Arquitetura e Plataforma (Diretoria de Eficiência Operacional)
Gerência de Produto e Experiência (Diretoria de Tecnologia)

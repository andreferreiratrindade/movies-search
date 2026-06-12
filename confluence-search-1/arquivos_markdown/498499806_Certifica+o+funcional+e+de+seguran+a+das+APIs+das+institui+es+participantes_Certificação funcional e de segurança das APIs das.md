---
                            title: "Certificação funcional e de segurança das APIs das instituições participantes - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "498499806_Certifica+o+funcional+e+de+seguran+a+das+APIs+das+institui+es+participantes"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/498499806/Certifica+o+funcional+e+de+seguran+a+das+APIs+das+institui+es+participantes"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Certificação funcional e de segurança das APIs das instituições participantes - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            item 2.2 iii
Controle de versão
Versão
Data
Resumo das alterações
1
May 23, 2024
Versão inicial
Introdução e Objetivos
Esta métrica visa garantir que as instituições participantes do Open Finance certifiquem suas APIs, conforme a versão em vigor. A Estrutura Responsável pela Governança do Open Finance exige essa conformidade para assegurar a integridade, segurança e eficácia do ecossistema do Open Finance.
Sobre a Métrica
A métrica leva em conta vários critérios para determinar a conformidade das APIs das instituições participantes. Para que uma instituição esteja em conformidade com essa métrica, todos os critérios a seguir devem ser cumpridos com sucesso para cada uma de suas marcas. A Estrutura Responsável pela Governança do Open Finance verifica e exige que as certificações estejam corretas e atualizadas.
Certificação Funcional
Valida se a URI de certificação funcional está correta de acordo com a API ‘<api>’ e versão ‘<major>’.
https://github.com/OpenBanking-Brasil/conformance/)(blob|raw)(/main/submissions/functional/)(<api>/)(<major>.\d.\d)(.*)(<month>)(-)(<year>)((.zip)|(.json))
Verifica se a versão major disponível na URI da certificação funcional é a mesma, quando comparada com a versão major da API publicada.
Certificação de Segurança
Verifica se a URI da certificação de segurança está registrada corretamente no cadastro do servidor de autorização do Diretório de Participantes.
Valida se as certificações de segurança estão corretamente registradas no Diretório, verificando se a data de certificação está de acordo com a data do link e se a certificação não está expirada (com mais de 1 ano desde a data do link).
Metodologia Simplificada
Para fins de monitoramento deste item, o período de apuração será no momento da detecção da desconformidade, conforme orientado pelo Manual de Monitoramento do Banco Central do Brasil. A metodologia de análise envolve:
Certificação Funcional: Validação se a URI de certificação funcional está correta e se a versão major disponível na URI corresponde à versão major da API publicada.
Certificação de Segurança: Verificação se a URI da certificação de segurança está registrada corretamente no cadastro do servidor de autorização do Diretório de Participantes e validação se as certificações de segurança estão corretas e não expiradas.
Interpretação dos Resultados
Os resultados da métrica serão interpretados para verificar se as instituições estão cumprindo os critérios de conformidade para a certificação funcional e de segurança das APIs. A métrica avalia a existência das seguintes hipóteses de falha:
Certificação Funcional
Incorrect API Certification URI
A métrica avalia se a URI de certificação funcional não está correta de acordo com a API e versão especificadas.
A desconformidade é pontuada se a URI não seguir o formato esperado ou se a versão major disponível na URI não corresponder à versão major da API publicada.
Certificação de Segurança
Missing Security Certifications
A métrica avalia se a URI da certificação de segurança não está registrada corretamente no cadastro do servidor de autorização do Diretório de Participantes.
Incorrect Certification URI
A métrica avalia se a URI da certificação de segurança não está seguindo o formato correto ou não está acessível.
Missing CertificationStartDate
A métrica avalia se a data de certificação de segurança não está devidamente preenchida no diretório.
Incorrect CertificationStartDate
A métrica avalia se a data de certificação de segurança está correta e não expirada (com mais de 1 ano desde a data do link).
Exemplo Ilustrativo
Considerando uma instituição em que a URI da certificação de segurança não esteja registrada corretamente no cadastro do servidor de autorização do Diretório. Mesmo que todos os outros critérios estejam em conformidade, a métrica consideraria a instituição em desconformidade devido a esse único item não atendido. Em caso de desconformidade com algum dos critérios, a métrica deverá destacar o item em questão como um ponto de atenção.
Dados e Fontes
Para o cálculo da métrica, utilizam-se os dados obtidos a partir do Diretório de Participantes e da Ferramenta de Validação de Produção (FVP). A FVP gera logs detalhados sobre o sucesso ou falha do cenários de testes executados. Esses logs são consolidados na Plataforma Analítica de Dados (PAD), um repositório centralizado que serve como base para a análise e avaliação da métrica. A combinação dessas fontes de dados permite uma avaliação precisa da métrica e um monitoramento efetivo da conformidade regulatória no contexto do Open Finance.
Limitações e Considerações
Atualmente, não há visibilidade ou conhecimento de limitações ou considerações adicionais para esta métrica. A análise será continuamente revisada e aprimorada conforme novos dados e informações se tornem disponíveis.
Responsável pela Aprovação
Squad Sandbox

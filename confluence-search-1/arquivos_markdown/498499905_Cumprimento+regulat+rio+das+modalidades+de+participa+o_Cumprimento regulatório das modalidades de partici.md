---
                            title: "Cumprimento regulatório das modalidades de participação - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "498499905_Cumprimento+regulat+rio+das+modalidades+de+participa+o"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/498499905/Cumprimento+regulat+rio+das+modalidades+de+participa+o"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Cumprimento regulatório das modalidades de participação - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            item 2.2 - i
Controle de versão
Versão
Data
Resumo das alterações
1
May 20, 2024
Versão inicial
Introdução e Objetivos
Esta métrica visa monitorar o cumprimento regulatório das modalidades de participação das instituições no ecossistema do Open Finance. A Estrutura Responsável pela Governança do Open Finance verifica se as modalidades de participação cadastradas pelas instituições participantes estão em conformidade com o estabelecido na regulamentação e adota as providências necessárias para a regularização, sempre que houver informações disponíveis para tal verificação.
Sobre a Métrica
A métrica se baseia na identificação das modalidades de participação das instituições conforme o artigo 2º da Resolução Conjunta nº 1, de 4 de maio de 2020, e o devido cadastro das roles no Diretório de Participantes. Para integrar o ecossistema do Open Finance, as instituições credenciadas devem se cadastrar de acordo com seus papéis regulatórios, que refletem a autorização do Banco Central e determinam as APIs que podem utilizar. As modalidades assumidas pelos participantes no âmbito do Open Finance são auto declaratórias e podem ser exercidas simultaneamente. Contudo, tais modalidades deverão estar em conformidade com o modelo de negócio do participante e estarão sujeitas à verificação pela fiscalização do Banco Central do Brasil, especialmente com relação ao cumprimento do princípio da reciprocidade no compartilhamento de dados no Open Finance Brasil.
Modalidades de participação
Instituição Transmissora e Receptora de Dados (role DADOS)
Obrigatória para todas as instituições dos segmentos S1 e S2.
Demais instituições autorizadas podem participar facultativamente, observando o princípio da reciprocidade.
Instituições com a role DADOS devem publicar as APIs de Consents e Resources para o compartilhamento de dados.
Instituição Prestadora de Serviço de Iniciação de Pagamentos (role PAGTO)
Destina-se às instituições que tenham publicado sua certificação OpenID Relying Party e constem na Lista de Participantes Ativos do Pix do BCB como iniciador de transação de pagamento.
Devem ter obtido a certificação, e caso sua instituição também seja detentora de conta, deverá já ter obtido a certificação e publicação de suas APIs de serviços do Open Finance conforme item V, do artigo 2º, da Resolução Conjunta no. 1, de 4 de maio de 2020.
Necessitam passar pelo processo de Onboarding de ITPs da Estrutura de Governança do Open Finance, com divulgação em um Informa emitido ao ecossistema.
Instituição Detentora de Conta (role CONTA)
Destinada à instituição participante com a qual o cliente possui relacionamento e detém sua conta para movimentação de recursos.
Verificação se as APIs de serviços estão cadastradas no Diretório para a instituição participante que tenha declarado a role CONTA.
Não há base de dados disponível para consulta prévia junto ao BCB, sendo necessário análise comparativa com os endpoints declarados pela instituição.
Correspondente de Crédito (role CCORR)
Destinada às instituições participantes que tenham firmado contrato de correspondente no país para recepção e encaminhamento de propostas de operações de crédito e de arrendamento mercantil.
A role CCORR no Diretório de Participantes do Open Finance ainda não está em vigor e será discutida em um momento futuro.
Metodologia Simplificada
Para fins de monitoramento deste item, o período de apuração será mensal, conforme orientado pelo Manual de Monitoramento do Open Finance Brasil. A avaliação envolverá:
Identificação das modalidades no Diretório: Verificação das modalidades de participação de cada instituição no Diretório de Participantes.
Publicação das APIs: Checagem das APIs publicadas conforme as roles declaradas.
Conformidade com regulamentações: Avaliação da conformidade das modalidades de participação e APIs publicadas com as regulamentações vigentes.
Interpretação dos Resultados
Os resultados da métrica serão interpretados para verificar se as instituições estão cumprindo os requisitos regulatórios associados às suas modalidades de participação. Para fins de monitoramento, a instituição estará em desconformidade, o que ocasionará o apontamento do item em desconformidade para o conglomerado ao qual essa organização pertence. A análise incluirá:
A verificação das Instituições Transmissora de Dados (role DADOS) envolve confirmar se a role DADOS está declarada em reivindicações de domínio de autoridade (Authority Domain Claim) e se a instituição possui um servidor de autorização para exposição das APIs de serviços, exclusivamente com uma ou mais das APIs payments-consents, payments-pix, payments-pix-recurring-payments, payments-recurring-consents e enrollments. Essa verificação da marca exclusiva como detentora de conta possibilita identificar todos os demais servidores de autorização que devem conter as APIs consents, resources e customer-business ou customer-personal para estarem conformes. Se a organização não possuir um servidor de autorização, deve possuir preenchido o atributo ParentOrganisationReference no Diretório. Para organizações com marcas exclusivas detentoras de contas, não há obrigatoriedade de compartilhamento de dados por essas marcas, inferindo-se que o compartilhamento é realizado pela infraestrutura da organização mãe em uma marca distinta.
A verificação das Instituições Iniciadoras de Transação de Pagamento (role PAGTO) envolve confirmar se a role PAGTO está declarada no software statement da instituição, e se a instituição passou pelo processo de onboarding, indicado pela flag "Habilitada para Iniciação de Pagamento" ou flag "Em processo de onboarding de ITP". A verificação do software statement também abrange o ITP puro, que pode não dispor de authorisation server.
A verificação das Instituições Detentoras de Conta (role CONTA) envolve confirmar se a role CONTA está declarada em reivindicações de domínio de autoridade (Authority Domain Claim) no Diretório, e se as APIs family types ‘payments-consents', 'payments-pix', 'payments-pix-recurring-payments', 'payments-recurring-consents’ está cadastrada em pelo menos um dos authorisation servers da instituição.
Correspondente de Crédito (role CCORR): A declaração da role CCORR está em espera e não será avaliada para fins de monitoramento da métrica até futura regulamentação.
Exemplo Ilustrativo
Considere uma instituição do segmento S1 com a role DADOS declarada no Diretório. A verificação será feita para assegurar que a instituição publicou as APIs ‘consents', ‘resources' e 'customer-personal’ ou 'customer-business’. Se uma Instituição Prestadora de Serviço de Iniciação de Pagamentos (role PAGTO) declarou essa role no Diretório e no software statement, mas não possui flag "Habilitada para Iniciação de Pagamento" ou "Em processo de onboarding de ITP", ela será considerada em desconformidade. Além disso, instituições Detentoras de Conta devem ter a role CONTA declarada em reivindicações de domínio de autoridade (Authority Domain Claim) e as APIs family types ‘payments-consents', 'payments-pix', 'payments-pix-recurring-payments', 'payments-recurring-consents’ cadastrada em pelo menos um dos servidores de autorização para estar em conformidade.
Dados e Fontes
Para o cálculo da métrica, utilizam-se os dados obtidos a partir do Diretório de Participantes do Open Finance. Esses dados são consolidados na Plataforma Analítica de Dados (PAD), um repositório centralizado que serve como base para a análise e avaliação da métrica. Diferentemente das demais informações que atualmente são mantidas pelas instituições, as flags que demonstram que uma instituição concluiu e/ou está participando do processo de onboarding são mantidas e atualizadas pela Equipe de Aceleração e Interoperabilidade.
A combinação dessas fontes de dados permite uma avaliação precisa da métrica e um monitoramento efetivo da conformidade regulatória no contexto do Open Finance, garantindo que a métrica reflita os objetivos observados.
Limitações e Considerações
Atualmente, não há visibilidade ou conhecimento de limitações ou considerações adicionais para esta métrica. A análise será continuamente revisada e aprimorada conforme novos dados e informações se tornem disponíveis.
Responsável pela Aprovação
Squad Sandbox

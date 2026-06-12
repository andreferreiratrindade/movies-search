---
                            title: "Jornada Otimizada - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1128890377_Jornada+Otimizada"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1128890377/Jornada+Otimizada"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Jornada Otimizada - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Introdução
2
O que é
3
Serviços de pagamento contemplados
4
Escopo de dados
5
Consentimentos independentes
6
Relacionamento entre consentimentos
7
Revogação de consentimento
Introdução
Atualmente, a jornada do usuário para compartilhamento de dados e serviços de iniciação de pagamentos possuem fluxos independentes. Dessa forma, o usuário precisa realizar ambas as jornadas de forma individual para ter acesso ao saldo em sua gestão de pagamentos.
A
Jornada Otimizada
tem como objetivo simplificar a experiência do cliente, permitindo o compartilhamento de dados a partir da jornada de pagamentos, em um fluxo unificado e mais simples. Essa abordagem busca garantir maior nível de informação e segurança ao usuário na configuração dos pagamentos, além de reduzir a ocorrência de problemas relacionados a pagamentos sem saldo disponível.
O que é
A
Jornada Otimizada
consiste em permitir que os dois fluxos de jornada do usuário — compartilhamento de
dados
e
pagamentos
— sejam autorizados a partir de uma experiência única de forma que:
Os consentimentos permanecem
segregados
.
As APIs já existentes serão utilizadas, conforme seus fluxos técnicos atuais.
A experiência do usuário é
unificada
.
Serviços de pagamento contemplados
O usuário terá a possibilidade de compartilhar seu saldo a partir de dois produtos de iniciação de pagamento.
Transferências Inteligentes
Jornada sem Redirecionamento (JSR)
Escopo de dados
Os dados compartilhados serão provenientes da
API de Contas
conforme especificação vigente e respeitarão as regras da especificação das
APIs de Consentimentos
e
API de Recursos
publicadas.
Consentimentos independentes
Quando concluída integralmente, a Jornada Otimizada deverá gerar
dois consentimentos
para o mesmo cliente:
Consentimento de Dados
→ define o compartilhamento de informações referentes ao saldo.
Consentimento de Pagamentos
→ define o consentimento do pagamento (se o serviço for Transferências Inteligentes) ou a autorização de vínculo de conta (se o serviço for JSR).
Relacionamento entre consentimentos
Os consentimentos estão relacionados de forma
unidirecional
:
O
consentimento de pagamentos
é considerado
primário
.
O
consentimento de dados
é considerado
secundário
.
Revogação de consentimento
A revogação na Jornada Otimizada segue o relacionamento estabelecido entre consentimentos:
O
usuário pode revogar
o consentimento de dados
sem revogar
o consentimento de pagamentos.
Ao
revogar o consentimento de pagamentos
, o consentimento de dados relacionado deve ser automaticamente revogado.
Em caso de cancelamento apenas do consentimento de dados, o usuário precisará
conceder um novo consentimento de dados
para que o saldo volte a ficar disponível.

---
                            title: "Diretrizes Gerais de Certificação de Conformidade - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "280297514_Diretrizes+Gerais+de+Certifica+o+de+Conformidade"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/280297514/Diretrizes+Gerais+de+Certifica+o+de+Conformidade"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Diretrizes Gerais de Certificação de Conformidade - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Introdução
Esta página tem como objetivo principal dar as
diretrizes gerais
às instituições sobre como funcionam os processos de certificação de segurança e funcional. É recomendado, após a leitura desta página, um estudo mais aprofundado do
Guia de Certificação de Conformidade
, contendo informações mais detalhadas e específicas para a execução dos testes e obtenção das certificações. Vale ressaltar que o Guia de Certificação está em contínuo processo de atualização, sendo passível de sofrer alterações. Qualquer dúvida em relação ao processo, fique à vontade para a submissão de tickets através do
Service Desk
.
Informações Gerais
Para a entrada segura e assertiva no Ecossistema do Open Finance Brasil, a Estrutura de Governança disponibilizou um conjunto de ferramentas e infraestrutura para suportar o processo de testes e homologação dos produtos e serviços desenvolvidos pelas Instituições Participantes. Foram disponibilizados ambientes que habilitam ao participante:
Realizar testes da camada de
segurança
de suas aplicações e posterior certificação dessas aplicações, utilizando a estrutura criada e mantida pela OpenID Foundation (OIDF) - “Motor de Conformidade de Segurança”;
Realizar testes
funcionais
nas implementações das suas APIs dos produtos do Open Finance Brasil e posterior certificação - “Motor de Conformidade Funcional”).
As certificações são obrigatórias para todos os participantes entrarem em produção em cada fase do Open Finance Brasil, ou seja, uma implementação de versão de API só poderá ser registrada no ambiente produtivo do Diretório caso tenha sido certificada nos testes de segurança e funcionais. Vale ressaltar que as certificações de segurança e funcionais são independentes e seguem políticas de (re)certificação diferentes uma da outra.
Calendário de Certificação
As datas relevantes e regulatórias de todos os calendários de certificações de APIs, vigentes ou antigas, podem ser encontradas no
Calendário oficial do Open Finance Brasil
.
Certificação de segurança
Para fins de certificação de segurança, os participantes do Open Finance são categorizados em:
OpenID Provider (OP): transmissores de dados e detentores de conta
Demandam certificação FAPI e DCR e, se forem submetidas juntas, serão cobradas como uma única certificação.
Relying Party (RP): receptores de dados e iniciadores de pagamento
Demandam certificação RP;
Certificação de segurança Relying Parties (RP) de pagamentos (escopo signed) é válida para compartilhamento de dados (escopo unsigned), mas o contrário não é válido.
§  O escopo a ser utilizado é definido no momento da chamada da API. Não existe diferença na parametrização do teste, porém, no momento da execução de cada teste, a ferramenta irá disponibilizar endpoints de accounts e payments e cabe ao receptor/iniciador chamar o endpoint correto conforme o perfil de certificação desejado.
A certificação em cada uma das modalidades citadas acima é obrigatória e possui custos que podem ser consultados no site da OpenID Foundation ou nos Informas do ecossistema.
O processamento dos pedidos de certificação é realizado por ordem de submissão. Portanto, recomendamos que o pedido de certificação seja submetido com, pelo menos, 2 meses de antecedência, devido às limitações de capacidade de processamento da OpenID Foundation.
Certificação Funcional
A certificação de Conformidade Funcional é um mecanismo necessário para garantia de desenvolvimento adequado das APIs por parte dos participantes. Com a obrigação de sucesso completo nos testes do motor de conformidade, essa ferramenta acaba sendo vital para garantia da interoperabilidade e saúde do ecossistema. Vale reforçar que há a obrigatoriedade das instituições implementarem em produção as soluções técnicas testadas e certificadas em sandbox. No caso de atualização da implementação, a instituição deverá solicitar uma nova certificação para garantir a adesão aos padrões do Open Finance.
O período entre o lançamento da beta1 das especificações de um produto do Open Finance e a entrada em produção (go live) é dividido entre o período de maturidade e o período de certificação. Durante o período de maturidade, é esperado que as instituições desenvolvam suas APIs e executem os testes disponíveis com objetivo de garantir a maturidade das especificações, dos testes e das implementações das instituições, visando a interoperabilidade em produção. Sendo assim, para cada lançamento são estabelecidos “marcos de sucesso” que as instituições precisam cumprir em cada data, que vinculam uma quantidade de testes que a instituição precisa obter sucesso como evidência de seu desenvolvimento
.
É importante ressaltar que este resultado deve ser atingido no motor de conformidade funcional hospedado pelo Open Finance Brasil, logo testes executados localmente não são válidos para pedido de certificação.
Utilizando-se do motor de conformidade funcional, o participante deverá atingir a marca de 100% de sucesso nos testes na sua versão final antes do pedido de certificação. Com esta marca de sucesso, o participante deve então seguir o fluxo de certificação, que possui quatro tipos.
Tipos de certificação funcional
Certificação completa
Essa é a certificação padrão do Open Finance. Nesse modelo, o pedido de certificação deverá ser submetido através de um ticket no service desk na categoria (XPTO), anexando os resultados públicos dos testes (um exemplo pode ser acessado em:
https://web.conformance.directory.openbankingbrasil.org.br/log-
detail.html?log=yxaJTHHQjF4to64&public=true
), que será processado pela Estrutura. Após a aprovação, será gerado um link com os documentos utilizados na certificação. Este é o link que deverá ser incluído no Diretório no momento da publicação/atualização dos endpoints das APIs no ambiente de produção do Open Finance Brasil.
O processamento dos pedidos de certificação possui uma automação, portanto, caso tenha alguma dúvida do resultado nós recomendamos a abertura de um novo ticket.
O Guia de submissão de pedidos de certificação (em inglês) está disponível nesse link e o Guia do Diretório, com orientações para a publicação, está disponível nesse link.
Certificação simplificada
Esse modelo de certificação costuma ser adotado para mudanças minor nas APIs e, quando for aplicável, essa informação será comunicada para as instituições com antecedência.
Nesse caso, após a instituição passar em 100% dos testes, ela já poderá atualizar o seu ambiente produtivo, desde que respeitando a data de
go live
. Reforçamos que os testes com sucesso devem estar na sua última versão e os resultados devem estar públicos, conforme orientações do item 3.2.3.
Em casos de alteração de comportamentos isolados, que não impactem a estrutura das APIs, a Estrutura poderá exigir apenas a execução de um conjunto específico dos testes.
Para certificação simplificada não é necessário abrir ticket no Service Desk e enviar
logs
.
Certificação automática
A certificação para as APIs de Dados Abertos ocorre de maneira automática, ou seja, os testes são executados automaticamente
no momento da publicação da API no Diretório de Produção
. Caso a API esteja conforme, a publicação será feita com sucesso. Caso algum problema seja encontrado, a instituição responsável pela publicação será notificada através de uma mensagem de erro no próprio Diretório, indicando o plano de testes que obteve falha, e a publicação não será efetivada.
Portanto, não é necessário realizar pedidos de certificação através de tickets no Service Desk, dado que este ocorre automaticamente.
Após a publicação da API no Diretório produtivo, uma automação reexecuta os testes de Dados Abertos semanalmente, como parte da rotina da FVP.
Caso a instituição não obtenha sucesso na execução do teste, o status da certificação mudará de “Self-Certified” para “Rejected”.
Assim que uma nova execução seja realizada com sucesso, o status voltará para “Self-Certified”.
No cenário de falha em uma rotina automática semanal, a própria instituição poderá reexecutar o teste manualmente, antes da próxima execução automática, a fim de regularizar o status para “Self-Certified”, em caso de sucesso, com maior brevidade.
Para que um novo teste seja executado, o usuário da instituição deve:
Localizar a respectiva API no diretório.
Clicar em “Editar
”.
Alterar o status para “Self-Certified”.
Salvar.
Se o teste for bem-sucedido, o status será atualizado para “Self-Certified”.
Não certificação
Para casos em que a atualização da API não exija atualizações técnicas relevantes das instituições (ex: alguma regra se tornará menos restritiva para permitir a entrada de algum participante, mas as instituições que já estão em pleno funcionamento não precisarão fazer ajustes), a Estrutura poderá optar por não exigir nenhuma certificação. Nesse caso, a instituição deverá apenas atualizar a versão da API no Diretório dentro do cronograma acordado.
Caso a instituição tenha dúvidas, comentários, sugestões ou encontre algum bug, um ticket deve ser aberto para a estrutura no Gitlab ou no Service Desk.
Seguem alguns links úteis relacionados ao motor de conformidade:
Acesso ao Motor de Conformidade Funcional,
que é a ferramenta para execução dos testes de conformidade funcional
Release notes
do motor de conformidade funcional é uma página de nosso fornecedor contendo as principais informações relativas ao motor, separada para cada uma das APIs. Na página de
release notes
¸ após seleção da API específica para detalhamento no menu lateral, podem ser encontradas informações atualizadas relativas à:
Release Dates
:
Especificação das datas de lançamentos do motor de testes funcional, disponibilização dos novos módulos e versão da especificação utilizada de base para a criação dos testes;
Breaking Changes
: São mudanças relevantes no motor de conformidade, tornando um ou mais módulos mais restritivos do que a sua versão anterior, ocorrendo devido a bugs encontrados no motor de conformidade. Assim sendo, módulos de teste impactados por
Breaking Changes
devem obter sucesso apenas a partir da data da alteração relevante no motor. Portanto, torna-se necessária a divulgação e a documentação de módulos impactados, bem como a data da alteração relevante no motor de conformidade;
Lista completa de testes
: Disponível na seção “Test Plan List”, a lista contempla todos os testes disponíveis no motor, junto com o seu detalhamento do que será testado nele.
Issues do motor
de conformidade funcional é uma página destinada à interação dos participantes com o fornecedor, com o objetivo de tirar dúvidas, comunicar e dar visibilidade aos problemas encontrados no motor. Incentivamos os participantes a utilizarem essa plataforma, seja abrindo tickets para eventuais dúvidas, problemas ou divergências encontradas no motor de conformidade funcional. Essa plataforma permite o acompanhamento e interação com dúvidas de outras instituições e dá visibilidade para itens que já estão em correção ou que já foram esclarecidos.
Dashboard de Acompanhamento
para acompanhar o status de execução dos testes e habilitar a visualização de maturidade do motor de conformidade e evitar eventuais transtornos próximos à data de
Go-live
, pois o respeito aos marcos de certificação é fundamental e obrigatório.
Para melhor acompanhamento da evolução da sua instituição com relação aos marcos de conformidade, é possível solicitar acesso ao Dashboard de Acompanhamento de Conformidade, com detalhamento do processo de pedido de acesso descrito no
Informe #431
. No dashboard de acompanhamento, é possível analisar dados como, por exemplo, testes já com sucesso da sua instituição e módulos executados.
Vale ressaltar que, para validar o atendimento dos marcos, alguns filtros podem ser aplicados como a data da última
breaking change
.
Outras certificações
Além das certificações de segurança e funcional, outras certificações poderão ser exigidas a depender do produto e da solução técnica.
Para a implementação de pagamentos via Jornada Sem Redirecionamento (JSR), é necessário que as instituições detentoras utilizem um servidor FIDO certificado, podendo optar por utilizar um servidor FIDO que já foi certificado (próprio ou de terceiro) ou realizar a certificação do próprio servidor junto à FIDO Alliance, instituição responsável pelo processo e calendário dessa certificação.
Outros Links Úteis
Guia de Certificação de Conformidade
: Página contendo informações mais detalhadas e específicas para a execução dos testes e obtenção das certificações;
Service Desk
: Canal para envio de dúvidas das instituições e envio de notificações pela Estrutura;
Repositório de Informes
: Consolidado dos comunicados enviados ao ecossistema;
Canal do Youtube do Open Finance Brasil
: Link para o canal do Youtube com workshops de lançamentos das APIs, contendo detalhamentos e explicações sob diferentes pontos de vista, como de produto, técnico, experiência do usuário (UX) e conformidade (testes e certificação).
Certificação FIDO
:
Orientações para obter a certificação FIDO, obrigatória para as detentoras na Jornada sem Redirecionamento.

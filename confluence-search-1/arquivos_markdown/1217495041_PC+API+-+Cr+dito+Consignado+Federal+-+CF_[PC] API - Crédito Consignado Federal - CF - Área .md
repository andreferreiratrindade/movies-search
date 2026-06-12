---
                            title: "[PC] API - Crédito Consignado Federal - CF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1217495041_PC+API+-+Cr+dito+Consignado+Federal+-+CF"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1217495041/PC+API+-+Cr+dito+Consignado+Federal+-+CF"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # [PC] API - Crédito Consignado Federal - CF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
1. Contexto
2
2. Cronograma
3
3. Obrigatoriedade de Participação
4
4.
Documentação Negocial
5
5.
Mapeamento Visual da Jornada
6
6.
Documentação Técnica
7
7.
Histórico das Especificações
8
8. FAQ
1. Contexto
A portabilidade de crédito no Open Finance permite que os usuários transfiram suas operações de crédito e arrendamento mercantil entre instituições financeiras em busca de melhores condições.
O
Crédito Consignado Federal
é uma modalidade de empréstimo pessoal destinada a
servidores públicos federais,
cuja principal característica é o
desconto automático das parcelas diretamente na folha de pagamento
.
Essa forma de crédito é considerada uma das mais seguras e acessíveis do mercado, tanto para o cliente quanto para as instituições financeiras, porque o
risco de inadimplência é reduzido
, já que o pagamento das parcelas é descontado na origem da renda.
2. Cronograma
Open
Cronograma atualizado em 12/11/2025
3. Obrigatoriedade de Participação
De acordo com o regulador, a obrigatoriedade é vinculada à participação no Compartilhamento de Dados: Com as instituições que ofertam ou possuem clientes na modalidade de empréstimo para o produto Crédito Consignado Federal, no papel de Instituição Credora Original e/ou Instituição Proponente.
Participação obrigatória para instituições do S1, S2 com mais de 5M de clientes.
Regras de reciprocidade para S3–S5, se atuar como Proponente, deverá atuar como Instituição Credora Original.
A participação como Instituição Credora Original é obrigatória, enquanto o papel de Instituição Proponente é voluntário.
Instituição financeira que participar do compartilhamento de dados no Open Finance deve participar da portabilidade como Instituição Credora Original, e vice-versa.
Conforme atualizações recentes na regulamentação do Open Finance, a participação voluntária no compartilhamento de dados e, consequentemente na portabilidade, implica a participação de todas as instituições do conglomerado
4.
Documentação Negocial
As documentações de negócio no contexto do Open Finance e da Portabilidade de Crédito são fundamentais para padronizar regras, jornadas e requisitos, garantindo clareza, alinhamento regulatório e interoperabilidade entre as instituições participantes.
Navegue nos conteúdos:
Documento de Requisitos do Produto - PRD - CF
Guia de UX - [CF]
Changelog - PRD - CF
5.
Mapeamento Visual da Jornada
O mapeamento visual da jornada de Portabilidade de Crédito é um recurso essencial para garantir o entendimento, a padronização e a eficiência no ecossistema do Open Finance Brasil. Ele permite que todos os participantes, instituições financeiras, desenvolvedores e áreas de negócio compreendam de forma rápida e assertiva como o processo funciona de ponta a ponta.
Este material reúne todos os diagramas da jornada de portabilidade de crédito para o produto
Crédito Consignado Federal
, com o objetivo de apresentar, de forma clara, o fluxo principal e os cenários alternativos.
Os conteúdos estão organizados para representar toda jornada, desde a solicitação de portabilidade até os possíveis desfechos, como efetivação, contraproposta ou cancelamento pelo cliente, entre outros.
Navegue nos conteúdos:
Fluxo Principal e cenários alternativos - CF
Diagrama de sequência - CF
Efetivação da portabilidade de crédito - CF
Aceite da contraproposta - CF
Cancelamento pelo cliente - CF
Diagrama de atividades - CF
6.
Documentação Técnica
Esta página reúne as especificações técnicas para a implementação do serviço de Portabilidade de Crédito no âmbito do Open Finance Brasil, com foco no produto
Crédito Pessoal Clean
. O objetivo é fornecer às instituições participantes as informações necessárias para garantir a integração correta com as APIs, assegurando conformidade regulatória, interoperabilidade e consistência nos fluxos operacionais.
Nesta documentação, você encontrará orientações detalhadas sobre:
Swagger - v1.0.0-RC.1 - [PC] Portabilidade de Crédito - CF
Idempotência - v1.0.0-RC.1 - [PC] Portabilidade de Crédito - CF
Como assinar o payload - v1.0.0-RC.1 - [PC] Portabilidade de Crédito - CF
Máquina de Estados - v1.0.0-rc.1 - [PC] Portabilidade de Crédito - CF
Qualidade DTO - CF
O conteúdo aqui apresentado é fundamental para garantir que as implementações sejam realizadas de forma padronizada, segura e eficiente, proporcionando uma jornada fluida para os consumidores no ecossistema do Open Finance.
7.
Histórico das Especificações
O produto
Consignado Federal (CF)
está sendo desenvolvido de forma incremental, em colaboração com as Instituições Financeiras por meio do Grupo de Trabalho (GT), seguindo o escopo definido pela DTO e adotando um modelo de implementações faseadas.
O histórico referente às implementações das especificações do produto
Consignado Federal (CF)
será detalhado nos itens abaixo.
8. FAQ
Para uma melhor organização, as perguntas e respostas a seguir foram organizadas por categorias:
Obrigatoriedade de Participação
O comitê Gestor do Sistema de Autorregulação da Portabilidade de Operações de Crédito será mantido?
Sim, será mantido.
Os novos entrantes na fase de compartilhamento estão dispensados dos marcos?
Sim. Os novos entrantes estão dispensados dos marcos intermediários de certificação, mas serão cobrados pelo ticket de certificação e pela publicação das APIs nas datas definidas no cronograma vigente.
Quais são exatamente as datas que os novos entrantes na fase de compartilhamento de dados devem seguir?
Devem seguir os prazos de certificação e publicação definidos no cronograma oficial.
A participação de instituições classificadas como S3 a S5 na portabilidade de crédito é obrigatória?
Para instituições classificadas como S3 a S5, a participação no serviço de portabilidade de crédito é opcional, mas condicionada à reciprocidade. Isso significa que se uma instituição S3, S4 ou S5 quiser atuar como proponente, ela também deverá atuar como credora original.
Instituições S3, S4 e S5 que participam do compartilhamento de dados são obrigadas a ofertar portabilidade de crédito?
Sim. Os requisitos se complementam. Mesmo que a instituição seja classificada como S3, S4 ou S5, se ela participa da fase de compartilhamento de dados, estará obrigada a implementar a API Portabilidade de Crédito. Além disso, a obrigatoriedade se estende às demais instituições pertencentes ao mesmo conglomerado financeiro.
Instituições com mais de 5 milhões de clientes precisam participar?
Sim. A obrigatoriedade é definida de forma complementar, com base em dois critérios:
A classificação prudencial (ex.: S3, S4);
A participação no compartilhamento de dados, especialmente no caso de instituições com mais de 5 milhões de clientes.
Se uma instituição S4 não participa do compartilhamento de dados e possui menos de 5 milhões de clientes, ela é obrigada a ofertar portabilidade de crédito?
Não. Nesse caso, a participação é considerada voluntária. Caso decida oferecer o serviço, a instituição deverá cumprir todos os requisitos técnicos e operacionais definidos.
Em caso de cessão de contrato para um FIDC, a instituição deixa de ter responsabilidade sobre a portabilidade?
Esse ponto ainda não possui definição formal. Casos assim devem ser submetidos à Associação para análise e eventual posicionamento do Banco Central.
Referências/Dúvidas Técnicas
Há previsão de custo para chamada de API?
Não haverá custo.
A API de empréstimo poderá ser aproveitada?
Sim, com as devidas adaptações. Uma API específica de Portabilidade de Crédito também será criada.
O RCO deverá ser considerado nas especificações para a cobrança?
Sim, mas a discussão do tema não é foco do grupo de trabalho.
Como será feito o aviso à proponente sobre a não retenção?
A comunicação ocorrerá por meio da consulta ao pedido de portabilidade de crédito. A instituição credora deve atualizar o estado da máquina de estados desse pedido, enquanto a instituição proponente acompanhará a evolução do processo por meio de consultas periódicas ao endpoint correspondente.
A máquina de estados deve ser atualizada para qual valor? REJECTED ou CANCELLED?
Deve ser atualizada para
Cancelled
, estado utilizado quando o cliente cancela o pedido de portabilidade de crédito antes de a instituição credora sinalizar a não retenção ou de a instituição proponente realizar a liquidação da operação.
Após os 3 dias, se o cliente não aceitar a contraproposta, o status muda para ACCEPTED_SETTLEMENT_IN_PROGRESS. Se a instituição proponente não consultar os dados de pagamento nem efetuar o pagamento, o que deve acontecer? Será considerado decurso de prazo? A portabilidade será cancelada?
Sim, conforme previsto na documentação técnica (descrição do endpoint GET /portabilities/{portabilityId}), as instituições devem consultar periodicamente o estado do pedido. Caso a instituição proponente não realize a liquidação, a instituição credora poderá atualizar o status para "Portabilidade cancelada por falta de liquidação", conforme previsto nos motivos de recusa mencionados no documento de requisitos do produto (PRD).
Quando é mencionado “tipo do produto”, isso inclui os campos productType e productSubTypeCategory?
Sim. Com a diferenciação de contas baseada na localidade e no produto, será possível ter uma conta específica para cada pagamento, identificada pelo portabilityId. Caberá à credora identificar o produto e a localidade, quando aplicável, para exibir corretamente os dados bancários.
Se já houver um pedido de portabilidade em andamento, a chamada à API POST /portabilities deve retornar um erro ou criar uma portabilidade com status REJECTED?
Deve retornar o erro
422
com a mensagem "
EM_ANDAMENTO
".
Existe algum SLA regulamentado para a notificação da instituição credora sobre a liquidação do contrato?
Sim. O prazo é de 2 dias úteis, conforme descrito no PRD.
A instituição precisa obrigatoriamente implementar os dois fluxos (síncrono e assíncrono)?
Não. A instituição é obrigada a implementar apenas os requisitos do fluxo que adotar. Caso opte pelos dois, deve implementar ambos.
Os motivos de rejeição são padronizados ou o campo rejectionReason é livre?
A justificativa é feita pelo campo type dentro de rejectionReason. Caso não esteja mapeada, informar type = "Outros" e preencher typeAdditionalInfo.
Como é validada a retenção de cliente durante o processo de portabilidade de crédito? A instituição precisa registrar formalmente a ação?
Sim. É necessário registro formal e evidência do aceite do cliente, além da atualização de status e assinatura digital.
A instituição credora aciona ativamente a proponente após o período de retenção do cliente?
Não. A comunicação ocorre via atualização de status no pedido de portabilidade, e a proponente deve consultar a API periodicamente.
No fluxo de cancelamento ou retenção, a instituição credora precisa notificar ativamente a proponente via API ou apenas alterar o status do pedido?
Apenas altera o status. A comunicação é feita por mudança de estado e consulta periódica pela proponente.
Existe risco de duplicidade em pedidos de portabilidade?
Não. Há um mecanismo de gestão de simultaneidade que impede pedidos duplicados para o mesmo contrato.
Regras do Produto
Haverá limitação da quantidade de pedidos de portabilidade? E existirá alguma carência de um pedido para outro?
Não haverá limite de quantidade ou carência entre pedidos.
Será possível a troca de modalidade?
Não será possível neste primeiro momento. A portabilidade será limitada de Consignado Federal para Consignado Federal, mas a possibilidade de troca de modalidade será avaliada futuramente.
Como será realizado o cálculo do saldo devedor?
O cálculo seguirá o método utilizado atualmente pelas instituições financeiras.
Como ficará o fluxo de comparação caso o cliente tenha vários contratos do produto Consignado Federal na mesma proponente?
A solicitação de portabilidade será feita individualmente para cada operação.
O cancelamento da portabilidade pelo cliente no aplicativo da credora é obrigatório?
Sim, é obrigatório.
Com a disponibilização do fluxo de PC no OFB, ainda será possível realizar a solicitação de PC via registradora (Núclea)?
Sim, será possível, porém será necessário que a instituição credora implemente políticas para impedir simultaneidade.
A oferta de contraproposta diminuirá as chances de a instituição credora ofertar a melhor taxa na adesão do contrato? Existirá limite de contraproposta?
Não, desde que as contrapropostas ocorram dentro de 3 dias úteis.
O que acontecerá se a instituição credora original não responder dentro de 3 dias úteis?
Trata-se de uma inconformidade da credora. O pedido ficará pendente de liquidação até atualização obrigatória de status pela credora original. Além disso, casos de inconformidade serão notificados ao Banco Central.
Para uma operação ser portada, ela precisa estar em dia?
Não há regulamentação específica. A decisão de portar ou não operações em atraso caberá à instituição proponente.
Para operações portadas via OFB, é necessário que a Núclea seja notificada ao término do processo?
Não, exceto em casos de simultaneidade.
Qual o procedimento se o cliente solicitar a portabilidade por diferentes IFs para o mesmo contrato em vias distintas?
A regra de simultaneidade será por ordem de solicitação.
Durante a jornada de portabilidade, se o cliente falecer, como será tratada a contraproposta?
O prazo de 3 dias úteis para a contraproposta será respeitado, a menos que haja manifestação para aceitá-la ou cancelar o pedido original.
Se a proponente faz uma proposta ao cliente com base no saldo devedor em D0, o cliente assina concordando com essa proposta e, em D3, o saldo devedor é atualizado, como ficam os valores pactuados com o cliente e o valor a ser enviado à credora original?
No momento da assinatura do contrato, o cliente deve ser informado sobre a possibilidade de atualização/oscilação no saldo devedor. Dessa forma, ele estará ciente de que poderá haver alterações nos valores pactuados inicialmente, decorrentes da variação do saldo na data da liquidação.
Há algum horário limite para o pagamento da proponente no caso de conquista de um contrato?
Para viabilizar o pagamento no mesmo dia, a instituição credora deve atualizar o status do pedido até às 10h. No exemplo apresentado, como a atualização ocorreu às 23h (fora do horário previsto), o prazo para o pagamento será o dia útil seguinte.
E se o cliente decidir não prosseguir com a portabilidade, mesmo sem receber uma contraproposta?
É necessário registrar o aceite do cliente? Para casos de desistência, a única ação da instituição (credora ou proponente) é registrar o desejo do cliente por meio da mudança de estado para
Cancelled
.
Sobre a simultaneidade: caso o cliente já esteja com um pedido de portabilidade em andamento, a instituição proponente terá acesso ao saldo devedor?
A instituição proponente terá acesso aos dados do contrato, incluindo o saldo devedor. No entanto, não será permitida uma nova solicitação de portabilidade para o mesmo contrato enquanto houver outro pedido em andamento
O cliente precisa cancelar manualmente o pedido de portabilidade após aceitar uma contraproposta da credora?
Não. A aceitação da contraproposta implica atualização automática do status pelo credor.
A nova proposta deve replicar o número original de parcelas do contrato ou considerar apenas o saldo remanescente?
Deve considerar apenas as parcelas restantes, nunca ultrapassando o contrato original.
A periodicidade da nova proposta pode ser alterada?
Não. Deve ser mantida exatamente como no contrato original.
O que acontece se houver variação no saldo devedor?
Se a variação for superior a 15%, a proponente pode cancelar a portabilidade. A tolerância não se aplica à quantidade de parcelas.
Haverá cobrança por parte do OFB sobre os pedidos de portabilidade?
A adesão ao OFB é gratuita. Outras taxas estão em análise.
O prazo de 3 dias úteis para a etapa de contraproposta se aplica a todos os produtos?
Inicialmente apenas para CPC e Consignado Federal.
O fluxo do Open Finance será integrado ao da Núclea?
Não. Os fluxos são independentes. A Núclea será informada apenas para visibilidade institucional.
Guia de UX
Existe uma jornada de retenção válida mesmo sem oferta de melhores condições para o cliente?
Sim. Direciona para a jornada de cancelamento por desistência.
As recomendações de cancelamento pelo usuário nos canais da credora, bem como o envio de notificações descritas no guia de UX, são obrigatórias?
E como será feita a homologação dessas experiências?
Sim, algumas são obrigatórias conforme escopo regulatório. O cancelamento deve estar disponível nos canais da credora e da proponente. A homologação de UX será comunicada posteriormente.
O guia de UX define como deve ser a tela ou apenas o conteúdo apresentado?
Define apenas as informações obrigatórias, não o design.
Em relação ao guia de UX, a última atualização incluiu como requisito que a instituição proponente e a instituição credora notifiquem o cliente a cada mudança de status do pedido de portabilidade. Isso não pode impactar negativamente a experiência do cliente?
Cada instituição é responsável pelas notificações relativas às suas próprias ofertas.
Existe uma jornada de retenção válida mesmo sem oferta de melhores condições?
Sim. Está previsto no guia como possibilidade válida.
Ainda sobre a jornada de retenção, será considerada válida uma contraproposta com refinanciamento?
Não. O escopo atual contempla apenas portabilidade de crédito.
O cliente precisa cancelar manualmente o pedido após aceitar uma contraproposta?
Não. A aceitação e o cancelamento são eventos distintos. O sistema atualiza automaticamente.
As recomendações de cancelamento pelo usuário nos canais da credora, bem como o envio de notificações descritas no guia de UX, são obrigatórias?
Sim. O cancelamento deve estar disponível nos canais digitais da proponente e da credora. Algumas notificações são obrigatórias. O formato é flexível, mas o conteúdo é obrigatório.
A definição sobre quais informações devem estar visíveis na tela principal ou em detalhes também é livre?
Não. A nova versão do guia trará definição obrigatória para garantir consistência.

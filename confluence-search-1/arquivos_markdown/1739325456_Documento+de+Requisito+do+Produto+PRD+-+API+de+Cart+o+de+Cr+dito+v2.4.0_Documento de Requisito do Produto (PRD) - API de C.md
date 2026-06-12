---
                            title: "Documento de Requisito do Produto (PRD) - API de Cartão de Crédito v2.4.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1739325456_Documento+de+Requisito+do+Produto+PRD+-+API+de+Cart+o+de+Cr+dito+v2.4.0"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1739325456/Documento+de+Requisito+do+Produto+PRD+-+API+de+Cart+o+de+Cr+dito+v2.4.0"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Documento de Requisito do Produto (PRD) - API de Cartão de Crédito v2.4.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
1. Introdução
1.1
1.1 Contexto
1.2
1.2 Problema
1.3
1.3 Solução
2
2. Escopo
2.1
2.1 Assuntos Contemplados
3
3. Funcionalidades
3.1
3.1 Informações sobre cartões de crédito
3.1.1
3.1.1 Regras para listagem de cartões de crédito
3.1.2
3.1.2 Escopo e permissões
3.2
3.2 Informações sobre transações
3.2.1
3.2.1 Regra para listagem de dados referentes a transações
3.2.2
3.2.2 Escopo e permissões
3.3
3.3 Informações sobre limites
3.3.1
3.3.1 Regra para listagem de limites existentes
3.3.2
3.3.2 Escopo e permissões
3.4
3.4 Informações sobre faturas do cartão de crédito
3.4.1
3.4.1 Regra para listagem de faturas de cartões de crédito
4
4. Glossário
1. Introdução
A API de Cartões de Crédito no âmbito do Open Finance Brasil tem por finalidade viabilizar o compartilhamento padronizado, seguro e interoperável de informações relativas a cartões de crédito emitidos, incluindo limites, transações, saldos e demais dados transacionais associados, mediante consentimento prévio, livre, informado e inequívoco do cliente, em conformidade com a legislação brasileira aplicável. Este documento de requisitos de produtos especifica as informações mínimas, atributos, comportamentos e regras de negócio que deverão ser observados pelas Instituições Participantes na implementação e exposição dos dados de cartões de crédito, garantindo alinhamento às normas do Banco Central do Brasil, às diretrizes do Open Finance Brasil e aos princípios de proteção de dados pessoais.
1.1 Contexto
O documento de requisitos de produtos da API de Cartões de Crédito do Open Finance Brasil insere-se no contexto da agenda regulatória do Banco Central do Brasil voltada à promoção de competição, inovação e eficiência no Sistema Financeiro Nacional, com base na premissa de que o cliente é o titular de seus dados financeiros. A partir dessa diretriz, o Open Finance estabelece um ecossistema de compartilhamento de informações entre instituições participantes, condicionado à obtenção de consentimento prévio, livre, informado e inequívoco pelo titular, em aderência ao marco regulatório setorial e às normas de proteção de dados pessoais.
Nesse ambiente, a API de Cartões de Crédito representa um dos principais instrumentos técnicos para viabilizar o acesso padronizado a informações de cartões emitidos, incluindo limites contratados, transações realizadas, saldos devedores e demais dados transacionais associados, permitindo que diferentes instituições possam consumir e oferecer serviços baseados nesses dados de maneira interoperável e segura. O documento de requisitos de produtos surge, assim, como referência normativa e técnica para a definição dos atributos, estruturas de dados, comportamentos esperados e regras de negócio relacionados aos cartões de crédito, garantindo alinhamento às diretrizes de governança, sigilo bancário, privacidade e segurança da informação estabelecidas pela regulamentação brasileira aplicável.
1.2 Problema
A ausência da API de Cartões de Crédito no ecossistema do Open Finance Brasil geraria um conjunto de problemas estruturais para o cumprimento dos objetivos regulatórios de competição, eficiência, inovação e proteção ao consumidor. Sem uma especificação padronizada para exposição e consumo de dados de cartões de crédito, o compartilhamento de informações permaneceria fragmentado, heterogêneo e potencialmente incompatível entre instituições, prejudicando a interoperabilidade técnica e a comparabilidade de informações exigidas pelo regulador.
Do ponto de vista do titular de dados, a inexistência dessa API impediria que o histórico de uso de cartões de crédito — incluindo limites, transações, saldos e padrões de pagamento — fosse portado de forma simples e segura para outras instituições, limitando a capacidade do cliente de obter melhores condições de crédito, ofertas personalizadas de produtos financeiros e análises de score mais precisas baseadas em seu comportamento real de consumo. Isso reforçaria a assimetria informacional em favor das instituições incumbentes, mantendo barreiras de entrada elevadas para novos participantes e reduzindo o potencial de concorrência e de inovação no Sistema Financeiro Nacional.
Sob a ótica da conformidade regulatória e da proteção de dados pessoais, a falta de uma API de Cartões de Crédito padronizada dificultaria a implementação prática de mecanismos de consentimento granular, transparente e rastreável aplicados especificamente a dados de cartões, enfraquecendo a governança sobre o uso dessas informações. Sem uma interface única, documentada e sujeita a requisitos mínimos de segurança, disponibilidade e auditabilidade, aumentaria o risco de soluções proprietárias díspares, com maior exposição a falhas operacionais, erros de integração e eventuais usos incompatíveis com as finalidades consentidas pelo titular.
Nesse cenário, a política pública de Open Finance perderia um de seus principais vetores de dados — os cartões de crédito — comprometendo a efetividade das iniciativas de inclusão financeira, transparência e empoderamento do consumidor previstas na regulamentação brasileira, bem como a capacidade do regulador de supervisionar, de forma uniforme, o tratamento dessas informações no mercado.
1.3 Solução
A implementação da API de Cartões de Crédito no âmbito do Open Finance Brasil apresenta-se como solução estruturante para os problemas decorrentes da ausência de um modelo padronizado, seguro e interoperável de compartilhamento de dados de cartões, em alinhamento com a legislação brasileira e com a regulação do Banco Central. Essa API estabelece um conjunto único de requisitos técnicos e de negócio para exposição de informações sobre cartões emitidos, incluindo limites contratados, transações, saldos devedores e demais dados transacionais associados, permitindo que diferentes instituições acessem e utilizem tais dados de forma consistente, transparente e auditável, sempre condicionada ao consentimento prévio, livre, informado e inequívoco do titular.
Ao padronizar formatos, permissões, atributos e fluxos de chamada, a API de Cartões de Crédito reduz a fragmentação informacional e viabiliza a comparabilidade de dados entre instituições, fortalecendo a concorrência e a inovação no Sistema Financeiro Nacional, sem afastar as exigências de sigilo bancário e proteção de dados pessoais. O uso obrigatório de mecanismos formais de consentimento, com registro de finalidade, prazo e abrangência dos dados compartilhados, endereça as preocupações jurídicas relacionadas à base legal para tratamento de dados, à autodeterminação informativa do cliente e à conformidade com os princípios de finalidade, necessidade, transparência e responsabilização previstos na legislação brasileira.
Sob a ótica do consumidor, a solução proporcionada pela API de Cartões de Crédito permite a portabilidade efetiva de seu histórico de uso de crédito entre instituições, ampliando o acesso a ofertas mais adequadas ao seu perfil de consumo, a taxas e limites potencialmente mais competitivos, e a serviços de gestão financeira baseados em dados reais de transações e pagamentos. Do ponto de vista operacional e de supervisão, a existência de um padrão único favorece a implementação de controles de segurança, trilhas de auditoria e mecanismos de monitoramento uniformes, conferindo maior previsibilidade regulatória às instituições participantes e facilitando a atuação dos órgãos reguladores e fiscalizadores.
2. Escopo
2.1 Assuntos Contemplados
Este PRD aborda os seguintes assuntos relacionados ao fluxo de compartilhamento de dados de cartões de crédito do cliente:
Informações sobre cartões de crédito:
●
Regras para listagem de cartões de crédito:
Definição das informações necessárias para viabilizar a listagem de cartões de crédito que o cliente possui junto a instituição.
●
Escopo e permissões:
Padrão de segurança adotado pelo ecossistema para a geração de um consentimento.
Informação sobre transações:
●
Regra para listagem de dados referentes a transações:
Definição das informações necessárias para viabilizar listagem de transações efetuadas pelo cliente no cartão de crédito compartilhado.
●
Escopo e permissões:
Padrão de segurança adotado pelo ecossistema para a geração de um consentimento
Informações sobre limites:
●
Regra para listagem de limites existente:
Definição das informações necessárias para viabilizar os dados de limites fornecido ao cliente.
●
Escopo e permissões:
Padrão de segurança adotado pelo ecossistema para a geração de um consentimento
Informações sobre faturas do cartão de crédito:
●
Regra para listagem de faturas do cartão de crédito:
Definição das informações necessárias para listagem de faturas do cartão de crédito do cliente.
3. Funcionalidades
Esta seção detalha as funcionalidades a serem implementadas em cada etapa da API de Cartões de Crédito.
3.1 Informações sobre cartões de crédito
3.1.1 Regras para listagem de cartões de crédito
No contexto de compartilhamento de dados de cartões de crédito, a instituição receptora terá visibilidade dos cartões emitidos e mantidos pelo usuário na instituição transmissora. Dessa forma, é fundamental que todos os cartões sejam listados com informações padronizadas, completas e claras, incluindo a identificação do cartão, seu tipo e demais atributos relevantes.
Pontos Importantes:
Os cartões apresentados na listagem corresponderão exclusivamente aos cartões que possuem integração com os canais digitais da instituição. Cartões sem integração aos canais digitais não fazem parte do escopo do Open Finance Brasil.
3.1.2 Escopo e permissões
O compartilhamento de dados de cartões de crédito pela instituição transmissora somente poderá ocorrer mediante consentimento do usuário, com a seleção das permissões adequadas. A instituição receptora poderá incentivar o usuário a iniciar o compartilhamento de dados e mantê-lo informado sobre o andamento do processo, bem como sobre a inclusão de novos cartões de crédito ao compartilhamento.
Pontos Importantes:
Os cartões de crédito apresentados na listagem devem corresponder exclusivamente àqueles previamente autorizados pelo usuário no escopo do consentimento vigente, não sendo permitido exibir informações de quaisquer outros cartões de crédito não contemplados nesse consentimento. A inclusão de dados de novos cartões de crédito após o consentimento inicial somente será permitida mediante obtenção de um novo consentimento, abrangendo esses novos cartões.
3.2 Informações sobre transações
3.2.1 Regra para listagem de dados referentes a transações
No contexto de compartilhamento de dados transacionais dos cartões de crédito, a instituição receptora terá acesso aos saldos e às transações realizadas nos cartões mantidos pelo usuário na instituição transmissora. Dessa forma, é fundamental que todas as transações sejam apresentadas com informações padronizadas, completas e claras, incluindo a identificação da transação tal como exibida no extrato da instituição transmissora, de modo a possibilitar a fácil interpretação dos dados pelo usuário.
Pontos Importantes:
A listagem de transações de cartões de crédito do usuário deve contemplar transações à vista ou parceladas que já foram consolidadas e não estão pendentes de processamento, de forma a proporcionar entendimento claro tanto para o usuário quanto para a instituição receptora sobre todas as transações associadas ao cartão de crédito.
OBS:
Existe uma previsão de adicionar também transações em processamento.
3.2.2 Escopo e permissões
O compartilhamento de dados de dados transacionais dos cartões de crédito pela instituição transmissora somente poderá ocorrer mediante consentimento do usuário, com a seleção das permissões adequadas. A instituição receptora poderá incentivar o usuário a iniciar o compartilhamento de dados e mantê-lo informado sobre o andamento do processo, bem como sobre a inclusão de novos cartões ao compartilhamento.
Pontos Importantes:
Em caso de encerramento/cancelamento do cartão de crédito e existam transações registradas nos últimos 12 meses, os dados correspondentes devem continuar a ser compartilhados.
3.3 Informações sobre limites
3.3.1 Regra para listagem de limites existentes
No contexto de compartilhamento de limites de cartões de crédito, a instituição receptora terá acesso aos seguintes dados específicos:
Limites contratados:
valores máximos de crédito ou disponibilidade previamente estabelecidos e acordados entre o cliente e a instituição transmissora.
Utilização do limite contratado:
percentual ou valor efetivamente utilizado do limite disponível em determinado momento.
Pontos Importantes:
É permitido limites flexíveis tais como garantias por investimentos entre outros, quando for o caso deverá ser sinalizado de alguma forma que o limite disponível é flexível.
3.3.2 Escopo e permissões
O compartilhamento de dados de limites dos cartões pela instituição transmissora somente poderá ocorrer mediante consentimento do usuário, com a seleção das permissões adequadas. A instituição receptora poderá incentivar o usuário a iniciar o compartilhamento de dados e mantê-lo informado sobre o andamento do processo, bem como sobre a inclusão de novos cartões ao compartilhamento.
3.4 Informações sobre faturas do cartão de crédito
3.4.1 Regra para listagem de faturas de cartões de crédito
O compartilhamento de dados referentes às faturas de cartões de crédito abrange exclusivamente as faturas já encerradas (faturas fechadas).
4. Glossário
●
API:
Interface de Programação de Aplicações.
●
BCB:
Banco Central do Brasil.
●
GT:
Grupo de Trabalho.
●
OFB:
Open Finance Brasil.
●
PRD:
Documento de Requisitos de Produto.

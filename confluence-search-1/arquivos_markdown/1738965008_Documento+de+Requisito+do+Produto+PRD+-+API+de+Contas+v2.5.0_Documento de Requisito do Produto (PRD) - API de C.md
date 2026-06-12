---
                            title: "Documento de Requisito do Produto (PRD) - API de Contas v2.5.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1738965008_Documento+de+Requisito+do+Produto+PRD+-+API+de+Contas+v2.5.0"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1738965008/Documento+de+Requisito+do+Produto+PRD+-+API+de+Contas+v2.5.0"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Documento de Requisito do Produto (PRD) - API de Contas v2.5.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

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
3.1 Informações sobre contas
3.1.1
3.1.1 Regras para listagem de contas
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
3.3.1 Regra para listagem de limites existentes na conta
3.3.2
3.3.2 Escopo e permissões
3.4
3.4 Informações sobre saldo reservados/caixinhas:
3.4.1
3.4.1 Regra para listagem de saldo reservados/caixinhas
4
4. Glossário
1. Introdução
A API de Contas no âmbito do Open Finance Brasil tem por finalidade viabilizar o compartilhamento padronizado, seguro e interoperável de informações relativas a
Conta de Depósito à Vista, Conta Poupança e Conta de Pagamento Pré-Paga
, mediante consentimento prévio, livre, informado e inequívoco do cliente, em conformidade com a legislação brasileira aplicável. Este documento de requisitos de produtos especifica as informações mínimas, atributos, comportamentos e regras de negócio que deverão ser observados pelas Instituições Participantes na implementação e exposição dos dados de contas, garantindo alinhamento às normas do Banco Central do Brasil, às diretrizes do Open Finance Brasil e aos princípios de proteção de dados pessoais.
1.1 Contexto
O documento de requisitos de produtos da API de Contas do Open Finance Brasil insere-se no contexto da agenda regulatória do Banco Central do Brasil voltada à promoção de competição, inovação e eficiência no Sistema Financeiro Nacional, com base na premissa de que o cliente é o titular de seus dados financeiros. A partir dessa diretriz, o Open Finance estabelece um ecossistema de compartilhamento de informações entre instituições participantes, condicionado à obtenção de consentimento prévio, livre, informado e inequívoco pelo titular, em aderência ao marco regulatório setorial e às normas de proteção de dados pessoais.​
Nesse ambiente, a API de Contas representa um dos principais instrumentos técnicos para viabilizar o acesso padronizado a informações de
Conta de Depósito à Vista, Conta Poupança e Conta de Pagamento Pré-Paga
, permitindo que diferentes instituições possam consumir e oferecer serviços baseados nesses dados de maneira interoperável e segura. O documento de requisitos de produtos surge, assim, como referência normativa e técnica para a definição dos atributos, estruturas de dados, comportamentos esperados e regras de negócio relacionadas às contas, garantindo alinhamento às diretrizes de governança, sigilo bancário, privacidade e segurança da informação estabelecidas pela regulamentação brasileira aplicável.
1.2 Problema
A ausência da API de Contas no ecossistema do Open Finance Brasil geraria um conjunto de problemas estruturais para o cumprimento dos objetivos regulatórios de competição, eficiência, inovação e proteção ao consumidor. Sem uma especificação padronizada para exposição e consumo de dados de contas, o compartilhamento de informações permaneceria fragmentado, heterogêneo e potencialmente incompatível entre instituições, prejudicando a interoperabilidade técnica e a comparabilidade de informações exigidas pelo regulador.​
Do ponto de vista do titular de dados, a inexistência dessa API impediria que o histórico de relacionamento e de transações em contas de depósito e contas de pagamento fosse portado de forma simples e segura para outras instituições, limitando a capacidade do cliente de obter melhores condições de crédito, oferta de produtos personalizados e serviços de gestão financeira com base em seu perfil real. Isso reforçaria a assimetria informacional em favor das instituições incumbentes, mantendo barreiras de entrada elevadas para novos participantes e reduzindo o potencial de concorrência e de inovação no Sistema Financeiro Nacional.​
Sob a ótica da conformidade regulatória e da proteção de dados pessoais, a falta de uma API de Contas padronizada dificultaria a implementação prática de mecanismos de consentimento granular, transparente e rastreável aplicados especificamente a dados de contas, enfraquecendo a governança sobre o uso dessas informações. Sem uma interface única, documentada e sujeita a requisitos mínimos de segurança, disponibilidade e auditabilidade, aumentaria o risco de soluções proprietárias díspares, com maior exposição a falhas operacionais, erros de integração e eventuais usos incompatíveis com as finalidades consentidas pelo titular.​
Nesse cenário, a política pública de Open Finance perderia um de seus principais vetores de dados – as contas transacionais – comprometendo a efetividade das iniciativas de inclusão financeira, transparência e empoderamento do consumidor previstas na regulamentação brasileira, bem como a capacidade do regulador de supervisionar, de forma uniforme, o tratamento dessas informações no mercado.
1.3 Solução
A implementação da API de Contas no âmbito do Open Finance Brasil apresenta-se como solução estruturante para os problemas decorrentes da ausência de um modelo padronizado, seguro e interoperável de compartilhamento de dados de contas, em alinhamento com a legislação brasileira e com a regulação do Banco Central. Essa API estabelece um conjunto único de requisitos técnicos e de negócio para exposição de informações sobre
Conta de Depósito à Vista, Conta Poupança e Conta de Pagamento Pré-Paga
, permitindo que diferentes instituições acessem e utilizem tais dados de forma consistente, transparente e auditável, sempre condicionada ao consentimento prévio, livre, informado e inequívoco do titular.​
Ao padronizar formatos, permissões, atributos e fluxos de chamada, a API de Contas reduz a fragmentação informacional e viabiliza a comparabilidade de dados entre instituições, fortalecendo a concorrência e a inovação no Sistema Financeiro Nacional, sem afastar as exigências de sigilo bancário e proteção de dados pessoais. O uso obrigatório de mecanismos formais de consentimento, com registro de finalidade, prazo e abrangência dos dados compartilhados, endereça as preocupações jurídicas relacionadas à base legal para tratamento de dados, à autodeterminação informativa do cliente e à conformidade com os princípios de finalidade, necessidade, transparência e responsabilização previstos na legislação brasileira.​
Sob a ótica do consumidor, a solução proporcionada pela API de Contas permite o compartilhamento de dados de seu histórico financeiro entre instituições, ampliando o acesso a ofertas mais adequadas ao seu perfil, a taxas potencialmente mais competitivas e a serviços de gestão financeira baseados em dados reais, e não apenas em informações declaradas. Do ponto de vista operacional e de supervisão, a existência de um padrão único favorece a implementação de controles de segurança, trilhas de auditoria e mecanismos de monitoramento uniformes, conferindo maior previsibilidade regulatória às instituições participantes e facilitando a atuação dos órgãos reguladores e fiscalizadores.
2. Escopo
2.1 Assuntos Contemplados
Este PRD aborda os seguintes assuntos relacionados ao fluxo de compartilhamento de dados da conta do cliente:
Informações sobre contas:
●
Regras para listagem de contas:
Definição das informações necessárias para viabilizar a listagem de contas que o cliente possui junto a instituição.
●
Escopo e permissões:
Padrão de segurança adotado pelo ecossistema para a geração de um consentimento.
Informação sobre transações:
●
Regra para listagem de dados referentes a transações:
Definição das informações necessárias para viabilizar listagem de transações efetuadas pelo cliente na conta compartilhada.
●
Escopo e permissões:
Padrão de segurança adotado pelo ecossistema para a geração de um consentimento
Informações sobre limites:
●
Regra para listagem de limites existentes na conta:
Definição das informações necessárias para viabilizar os dados de limites fornecido ao cliente.
●
Escopo e permissões:
Padrão de segurança adotado pelo ecossistema para a geração de um consentimento
Informações sobre saldo reservados/caixinhas:
●
Regra para listagem de saldo reservados/caixinhas:
Definição das informações necessárias para listagem de saldos reservados/caixinhas do cliente.
3. Funcionalidades
Esta seção detalha as funcionalidades a serem implementadas em cada etapa da API de Contas.
3.1 Informações sobre contas
3.1.1 Regras para listagem de contas
No contexto de compartilhamento de dados de contas bancárias, a instituição receptora terá visibilidade das contas mantidas pelo usuário na instituição transmissora. Dessa forma, é fundamental que todas as contas sejam listadas com informações padronizadas, completas e claras, incluindo a identificação da conta e seu respectivo tipo.
Pontos Importantes:
As contas apresentadas na listagem corresponderão exclusivamente às contas que possuem integração com os canais digitais da instituição. Contas sem integração aos canais digitais, como por exemplo contas salário, não serão abrangidas pelo escopo do Open Finance Brasil.
3.1.2 Escopo e permissões
O compartilhamento de dados de conta pela instituição transmissora somente poderá ocorrer mediante consentimento do usuário, com a seleção das permissões adequadas. A instituição receptora poderá incentivar o usuário a iniciar o compartilhamento de dados e mantê-lo informado sobre o andamento do processo, bem como sobre a inclusão de novas contas ao compartilhamento.
Pontos Importantes:
As contas apresentadas na listagem devem corresponder exclusivamente àquelas previamente autorizadas pelo usuário no escopo do consentimento vigente, não sendo permitido exibir informações de quaisquer outras contas não contempladas nesse consentimento. A inclusão de contas abertas após a concessão do consentimento inicial somente será permitida mediante obtenção de um novo consentimento, abrangendo essas novas contas e/ou a totalidade das contas do usuário.
3.2 Informações sobre transações
3.2.1 Regra para listagem de dados referentes a transações
No contexto de compartilhamento de dados transacionais de contas bancárias, a instituição receptora terá acesso aos saldos e às transações realizadas nas contas mantidas pelo usuário na instituição transmissora. Dessa forma, é fundamental que todas as transações sejam apresentadas com informações padronizadas, completas e claras, incluindo a identificação da transação tal como exibida no extrato da instituição transmissora, de modo a possibilitar a fácil interpretação dos dados pelo usuário.
Pontos Importantes:
Com a entrada em vigor da IN BCB nº 371, a partir de 02/05/2023, passou a ser obrigatória a inclusão das informações de identificação da contraparte (CPF ou CNPJ) nas transações de pagamento.
Pontos Importantes:
A listagem de transações da conta do usuário deve contemplar “
transação processando" e "transação efetivada
”, de forma a proporcionar entendimento claro tanto para o usuário quanto para a instituição receptora sobre todas as transações associadas à conta.
Pontos Importantes:
No escopo de compartilhamento da API Contas estão incluídas as reservas sem rendimento — destinadas à separação de recursos para gastos futuros — e as reservas com rendimento, desde que não vinculadas a investimentos associados ao CPF ou CNPJ do cliente. Exemplos de nomenclatura para essas reservas incluem "caixinhas", "cofrinhos" e "saldo separado". Reservas associadas a investimentos formalizados sob o CPF ou CNPJ do cliente devem ser compartilhadas exclusivamente por meio das APIs de Investimentos.
3.2.2 Escopo e permissões
O compartilhamento de dados de dados transacionais das contas pela instituição transmissora somente poderá ocorrer mediante consentimento do usuário, com a seleção das permissões adequadas. A instituição receptora poderá incentivar o usuário a iniciar o compartilhamento de dados e mantê-lo informado sobre o andamento do processo, bem como sobre a inclusão de novas contas ao compartilhamento.
Pontos Importantes:
A reserva de saldo integra o mesmo agrupamento de permissões que o saldo. Assim, ao conceder autorização para consulta ao saldo, o cliente também concede consentimento para consultas às reservas de saldo.
Pontos Importantes:
Em caso de encerramento de conta, caso o cliente mantenha acesso aos canais eletrônicos e existam transações registradas nos últimos 12 meses, os dados correspondentes devem continuar a ser compartilhados.
3.3 Informações sobre limites
3.3.1 Regra para listagem de limites existentes na conta
No contexto de compartilhamento de limites de contas bancárias, a instituição receptora terá acesso aos seguintes dados específicos:
Limites contratados:
valores máximos de crédito ou disponibilidade previamente estabelecidos e acordados entre o cliente e a instituição transmissora.
Utilização do limite contratado:
percentual ou valor efetivamente utilizado do limite disponível em determinado momento.
3.3.2 Escopo e permissões
O compartilhamento de dados de limites das contas pela instituição transmissora somente poderá ocorrer mediante consentimento do usuário, com a seleção das permissões adequadas. A instituição receptora poderá incentivar o usuário a iniciar o compartilhamento de dados e mantê-lo informado sobre o andamento do processo, bem como sobre a inclusão de novas contas ao compartilhamento.
3.4 Informações sobre saldo reservados/caixinhas:
3.4.1 Regra para listagem de saldo reservados/caixinhas
No escopo de compartilhamento da API Contas estão incluídas as reservas sem rendimento — destinadas à separação de recursos para gastos futuros — e as reservas com rendimento, desde que não vinculadas a investimentos associados ao CPF ou CNPJ do cliente. Exemplos de nomenclatura para essas reservas incluem "caixinhas", "cofrinhos" e "saldo separado". Reservas associadas a investimentos formalizados sob o CPF ou CNPJ do cliente devem ser compartilhadas exclusivamente por meio das APIs de Investimentos.
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

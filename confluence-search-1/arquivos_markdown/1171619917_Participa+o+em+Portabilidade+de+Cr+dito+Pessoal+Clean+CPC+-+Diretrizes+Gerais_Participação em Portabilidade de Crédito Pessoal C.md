---
                            title: "Participação em Portabilidade de Crédito Pessoal Clean (CPC) - Diretrizes Gerais - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1171619917_Participa+o+em+Portabilidade+de+Cr+dito+Pessoal+Clean+CPC+-+Diretrizes+Gerais"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1171619917/Participa+o+em+Portabilidade+de+Cr+dito+Pessoal+Clean+CPC+-+Diretrizes+Gerais"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Participação em Portabilidade de Crédito Pessoal Clean (CPC) - Diretrizes Gerais - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Introdução
Está sendo lançado o novo produto de Portabilidade de Crédito (CPC). Com isso, tem-se como intuito, nesta página, a centralização das informações relevantes para compartilhamento com as instituições participantes do
Piloto de Portabilidade de Crédito
, que será realizado de
03/11/2025 a 01/02/2026
.
Objetivos do Piloto
O período do Piloto para novos produtos do Open Finance Brasil possui os seguintes
objetivos
:
Garantir o funcionamento e a
interoperabilidade
de novos produtos e APIs em
ambiente produtivo
;
Validar as
integrações e o funcionamento
das APIs dos participantes;
Antecipar
a identificação de problemas em ambiente produtivo;
Viabilizar a
criação de agendas
(bilaterais e multilaterais) antes do
Go Live
, para antecipação e correção de eventuais problemas e dificuldades encontradas;
Especificações da Portabilidade de Crédito
Informações Gerais
sobre as funcionalidades da API de Portabilidade de Crédito podem ser encontradas nessa página;
Informações Técnicas
podem ser encontradas nessa página;
Histórico das especificações
podem também ser encontrados no portal do desenvolvedor.
Obrigatoriedade de participação
O piloto será obrigatório para:
Instituições Credoras Originais
: Instituições que possuem a API de
Loans
publicada e que possuem o produto de Crédito Pessoal Clean (CPC);
Instituições Proponentes
: Instituições que são obrigatoriamente credoras e que também optarem por ofertarem o produto como proponentes.
Público participante do piloto e restrição de usuários
Para viabilizar o piloto, a nova funcionalidade deve ser inicialmente disponibilizada para um público restrito, que contempla apenas funcionários das próprias instituições, servidores do Banco Central, equipe responsável pela execução dos testes e membros da Associação Open Finance;
O formulário abaixo deve ser preenchido para que os usuários tenham acesso à funcionalidade das Proponentes:
Formulário de compartilhamento de usuários
Para acesso à fucionalidade de Portabilidade nas proponentes, as instituições credoras podem enviar as informações de forma individual ou em em massa, através de upload de arquivo csv.
Para compartilhamento de
dados em massa
dos usuários, utilizar CSV, conforme seguinte modelo de arquivo:
Os campos enviados, seja de forma individual ou em massa, devem necessariamente respeitar as seguintes regras abaixo. Caso contrário, os dados
não serão
enviados ou processados.
Campo
Regra de preenchimento
Exemplo
Campo
Regra de preenchimento
Exemplo
CPF
Apenas números,
sem
traços ou pontos
38301141093
Email
(opcional)
Endereço de e-mail dos usuários testadores
email@openfinancebrasil.org.br
OrgID
Conforme OrgID da instituição no diretório,
com
traços
d7384bd0-842f-43c5-be02-9d2b2d5efc2c
Instituição
Conforme nome da instituição no diretório
ASSOCIACAO OPEN FINANCE
Formulário para compartilhamento dos dados dos usuários abaixo:
A liberação de acesso aos usuários pelas instituições deverá acontecer conforme regras abaixo, a depender do escopo de atuação:
Instituições Credoras
: Funcionalidade deverá ser disponibilizada para
toda a base de usuários
.
Instituições Proponentes:
Funcionalidade deverá ser disponibilizada para base de usuários restrita, de forma faseada, seguindo-se as seguintes etapas:
1 - Validação da jornada
:
Acesso à funcionalidade deve ser compartilhada com base de usuários restrita, apenas aos CPFs de usuários compartilhados pela Associação diretamente às Proponentes;
A base de usuários restrita contempla apenas funcionários das próprias instituições, servidores do Banco Central, equipe responsável pela execução dos testes e membros da Associação Open Finance;
Após validação da jornada do produto da proponente pela Associação, a instituição poderá seguir para a próxima etapa.
2 - Liberação gradual da jornada
:
Além do acesso à funcionalidade ser mantida à base de usuários restrita, a instituição poderá disponibilizar a funcionalidade à sua base de clientes;
Para jornadas validadas (Etapa 1)
até 05/01/2026
0% da base até 31/11/2025
Até 1% ou 2.000.000 de clientes entre 01/12/2025 e 04/01/2025
Até 10% ou 20.000.000 de clientes entre 05/01/2026 e 18/01/2026
Até 50% ou 100.000.000 de clientes entre 19/01/2026 e 01/02/2026
100% da base de clientes a partir de 02/02/2026 (Go Live)
Para jornadas validadas (Etapa 1)
a partir de 06/01/2026
Até 1% ou 2.000.000 de clientes a partir da validação da jornada
Até 10% ou 20.000.000 de clientes a partir de 2 semanas depois da validação
Até 50% ou 100.000.000 de clientes a partir de 4 semanas depois da validação
100% da base de clientes a partir de 6 semanas depois da validação
A Caixa Econômica Federal realizará a abertura progressiva de sua funcionalidade para a base de clientes a partir de
7 de abril de 2026
. A abertura da base de clientes da proponente ocorrerá conforme as seguintes datas:
07/04: Começo da abertura da Caixa para a base de clientes, com até 1% ou 2.000.000 de clientes
22/04: Abertura da base de clientes para até 10% ou 20.000.000 de clientes
05/05: Abertura da base de clientes para até 50% ou 100.000.000 de clientes
19/05: 100% da base de clientes. A data poderá ser revista, conforme eventual solicitação da proponente
Indicadores de sucesso das instituições
Painel Integrado de acompanhamento de indicadores
Para o devido acompanhamento das métricas e indicadores de Portabilidade de Crédito, foi-se construído o
Painel Integrado de acompanhamento do Piloto
(Será utilizado o mesmo painel de acompanhamento das certificações. Métricas e critérios de acompanhamento do Piloto estão em construção). Nele, poderão ser encontradas as métricas de acompanhamentos da PCM, portabilidades concluídas, acompanhamento funcional da FVP, dentre outros;
Para solicitação de
acesso ao painel
, é necessário que sejam seguidas as seguintes instruções:
O usuário deve-se cadastrar, em sua instituição no diretório dos participantes, o seu
email
com acesso à funcionalidade PDV.
Para isso, na página da sua instituição no diretório dos participantes, acesse: Papéis > Usuários de domínio > Adicionar novo >
Data visualization platform
> PDV
Após isso, o usuário irá receber um
email
do diretório confirmando o seu devido cadastrado
Após execução da rotina de concessão de acesso, realizada ao final de cada dia, o usuário deverá receber um
email
do Quicksight com as devidas orientações para cadastro
No momento de realização do login, caso solicitado, é necessário inserir em “
account name
”, o seguinte valor “openfinance-brasil”
Critérios e indicadores a serem acompanhados
Durante o piloto, os seguintes
indicadores serão monitorados
:
Plataforma de Coleta de Métricas (PCM)
: Todas as instituições devem ter, em D+1, ao menos 95% de pareamentos com sucesso na PCM;
UX
: Durante o período do piloto, serão realizadas validações de UX para as marcas participantes do Piloto. O questionário de UX, que será utilizado de base para validação das jornadas as instituições, será integralmente baseado nos requisitos do
Guia de Experiência do Usuário
.
Tickets bilaterais
: Tickets bilaterais relativos ao Piloto de Portabilidade de Crédito considerados críticos (sob avaliação e demanda da DTO) devem ser
encerrados
previamente ao final do piloto,
independentemente de sua data de abertura ou do seu SLA
;
Ferramenta de Validação em Produção - FVP Manual
: As credoras participantes devem obter o sucesso nos testes relacionados à FVP Manual. A responsabilidade de execução e obtenção de sucesso nos testes varia de acordo a classificação de cada marca participante, detalhado na seção abaixo "Grupos de validação para o Piloto de Portabilidade de Crédito - Credoras".
Engajamento - Portabilidades Concluídas
: Para cada instituição participante do piloto, um número mínimo de portabilidades deve ser concluído e identificado com sucesso via PCM:
Para Proponentes
: 10 Portabilidades devem ser concluídas e identificadas com sucesso via PCM;
Para Credoras
: 5 Portabilidades devem ser concluídas e identificadas com sucesso via PCM. As
instituições credoras
deverão, ao longo do período estabelecido, atingir os
critérios de engajamento,
conforme marcos descritos abaixo:
15/04: Marco de 1 portabilidade concluída
29/04: Marco de 3 portabilidades concluídas
14/05: Marco de 5 portabilidades concluídas
Instituições que apresentem tickets bilaterais em aberto ou que não tenham atingido os marcos de engajamento poderão ser convocadas para
salas de guerra
conjuntas e bilaterais, previstos para ocorrerem de
13 a 17 de abril e de 4 a 15 de maio de 2026
.
Grupos de validação para o Piloto de Portabilidade de Crédito - Credoras
Com a necessidade de contratação do produto CPC para execução dos testes da FVP ou validações das jornadas de UX, algumas premissas são necessárias serem estabelecidas para classificação das marcas das Credoras originais em diferentes grupos.
As marcas das
Credoras Originais
participantes do Piloto serão divididas em 2 Grupos
:
Grupo 1
: Marcas que o fornecedor possui conta aberta e possui o produto de CPC contratado para realização de validações com a instituição.
FVP Manual
: Sucesso completo esperado nos 3 cenários de curta duração e em um cenário de longa duração, sob responsabilidade de execução do fornecedor;
Validações de UX
: Sucesso completo esperado no questionário de UX;
Engajamento:
Sucesso em ao menos 5 Portabilidades concluídas e identificadas com sucesso via PCM, sob responsabilidade das instituições. Caso aplicável, as instituições também poderão realizar a solicitação de portabilidade via fornecedor.
Grupo 2
: Demais Marcas, que o fornecedor não possui conta aberta ou não possui o produto de CPC contratado para realização de validações com a instituição.
Execução da FVP
: Sucesso completo esperado nos 3 cenários de curta duração, sob responsabilidade de execução da própria instituição;
Validações de UX
: Sucesso completo esperado no questionário de UX. A jornada em ambiente produtivo deverá ser gravada pela instituição e disponibilizada à Associação para validação.
Engajamento:
Sucesso em ao menos 5 Portabilidades concluídas e identificadas com sucesso via PCM, sob responsabilidade das instituições. As instituições do Grupo 2 não poderão realizar a solicitação de portabilidade via fornecedor.
A relação de segmentação de cada marca pode ser acompanhada através do
Painel Integrado de Acompanhamento do Piloto de Portabilidade de Crédito Pessoal Clean (CPC)
;
Consequências em caso de não atingimento dos critérios
Instituições Credoras
:
Que não atingirem os critérios
até 2 semanas antes do final do piloto
: Serão realizados
War rooms
para apresentação e acompanhamento de planos de ação;
Que não atingirem os critérios
até o final do piloto
: Credora poderá não ser listada pelas ITPs na utilização de Portabilidade de Crédito.
Instituições Proponentes
:
Com Jornadas disponíveis e validadas
após 06/01/26
: Não participam do Piloto e terão a funcionalidade disponível para toda a base de clientes após conclusão de processo de onboarding
;
Que não atingirem os critérios
até 2 semanas antes do final do piloto
: Serão realizados
War rooms
para apresentação e acompanhamento de planos de ação;
Que não atingirem os critérios
até o final do piloto
: Não poderão disponibilizar a funcionalidade em produção.
Cronograma de execução dos testes manuais para o Piloto de Portabilidade de Crédito
Com o intuito de dar mais visibilidade ao ecossistema quanto ao cronograma de execução da FVP e de execução de UX pelo fornecedor, compartilhamos, abaixo, as datas previstas que serão realizadas as validações com as Credoras e Proponentes participantes do piloto.
Open
Validações de UX para Credoras
Com o objetivo de realizarmos as validações da experiência de usuário (UX) da área de gestão de portabilidade de crédito das Credoras Originais, estão abaixo descritas as instruções para validação de
(a)
Teste 1 - portabilidade canceladas ou em andamento; (b) Teste 2 - portabilidade concluída
.
1. Preparação da gravação
Para que a jornada seja possível de ser validada, os seguintes pré-requisitos devem ser atendidos pelas credoras:
A jornada que será gravada pela instituição deverá utilizar um
aplicativo atualizado
, contemplando a última versão disponível e utilizando um usuário real em ambiente produtivo. Gravações realizadas em emuladores ou qualquer outro cenário que não representem um aplicativo em ambiente produtivo
não serão considerados.
Para o caso de instituições que não tenham habilitação para gravação das jornadas do aplicativos, é solicitado que seja utilizado um segundo aparelho para gravação da tela.
Para validação da área de gestão, o usuário deverá ter
ao menos um contrato de crédito ativo
(CPC) que possa ser utilizado para a jornada de portabilidade. Caso não exista, o usuário deverá:
Contratar um Crédito Pessoal Clean (CPC);
Garantir que o contrato esteja ativo e visível no aplicativo;
Tenha uma portabilidade concluída com sucesso, para casos do Teste 2 - Portabilidade concluída.
Para validação das jornadas de UX, é necessário que tenham
Portabilidade cancelada ou em andamento
(Teste 1): É necessário que uma portabilidade esteja “Cancelada” ou “Em andamento”. Para que uma portabilidade esteja em qualquer um desses dois status, é possível seguir as seguintes alternativas:
Via FVP:
O sucesso em qualquer um dos testes da FVP garantirá que uma portabilidade será cancelada, podendo seguir para a gravação da jornada do Teste 1 (Etapa 3 “Gravação das jornadas”).
Via Proponente
: Funcionalidades de portabilidade de proponentes também podem ser utilizadas para que uma portabilidade vá para o status de “Em andamento” ou “Cancelada”.
Portabilidade concluída
(Teste 2): É necessário que uma portabilidade esteja “Concluída”, necessariamente utilizando-se a funcionalidade de portabilidade de uma proponente. A gravação da jornada pode ser realizada por qualquer usuário, seja pelos próprios funcionários das instituições ou também pela base de clientes real. Instruções para obtenção de acesso e utilização da funcionalidade da proponente estão descritas nas seções “Público participante do piloto e restrição de usuários“ e “Instruções para utilização da Proponente - Caixa“.
2. Gravação das jornadas
Para validação das jornadas das credoras, é necessário que em uma
única gravação
de tela
, sem interrupção, apareçam as seguintes informações, presentes no questionário e sendo requisitos do Guia de Experiência do Usuário:
Nome da credora
Taxa
Valor da parcela
Número de parcelas
Saldo devedor
Número do contrato
Status da portabilidade: “Em andamento”, “Cancelada” ou “Concluída”, a depender do teste
3. Disponibilização das evidências
Após conclusão da etapa 3 “Gravação das jornadas”, a jornada deverá ser disponibilizada para validação da estrutura através da seguinte categoria do Service Desk: Requisições > Testes em Produção > Processo de Onboarding > Solicitação de Interesse em Participação > Credora de Crédito.
Os títulos dos tickets abertos devem seguir o seguinte padrão:
“Teste 1 – Jornada de portabilidade em andamento ou cancelada”, para validação da área de gestão de portabilidades com status em andamento ou cancelada;
“Teste 2 – Jornada de portabilidade concluída”, para validação da área de gestão de portabilidades com status concluída.
Instruções para utilização da Proponente - Caixa
Material de apoio: “Jornada de Portabilidade Empréstimo pessoal Clean via Caixa“
Open
Pré-requisitos para realização de uma portabilidade de Crédito Pessoal Clean (CPC) via Caixa
Para que uma solicitação de portabilidade de Crédito Pessoal Clean (CPC) seja realizada utilizando-se a
Caixa Econômica Federal como instituição proponente
, é necessário garantir o atendimento de todos os pré-requisitos abaixo. Se alguma dessas condições não for cumprida, a portabilidade
não poderá ser iniciada
ou autorizada.
Pré-requisitos para utilização da Caixa como instituição proponente:
CPF incluído no formulário:
O CPF do usuário (funcionário participante do piloto) deve ser previamente cadastrado por meio do formulário de compartilhamento de usuários disponibilizado nesta mesma página. Somente os CPFs enviados e validados conforme as regras definidas (apenas números, sem pontos ou traços, por exemplo) estarão habilitados a acessar a funcionalidade de portabilidade nas instituições proponentes. Caso o CPF não tenha sido compartilhado, o usuário não conseguirá visualizar nem iniciar a portabilidade envolvendo a Caixa durante esse período. Segundo regras compartilhadas pela própria instituição, as atualizações dos CPFs ocorrem 2x por semana, todas as segundas-feiras e quintas-feiras, por volta das 12h, com base nos dados preenchidos no formulário até o final do dia anterior.
Conta ativa na Caixa:
É necessário que o usuário possua uma conta corrente aberta e ativa na Caixa Econômica Federal. Se o usuário não for correntista ativo da Caixa, não será possível prosseguir com a portabilidade para essa instituição, pois o cliente precisa ter vínculo ativo (cadastro e conta) na Caixa para solicitar uma portabilidade de crédito. A abertura de conta deve ocorrer em unidade física da Caixa, apresentando Documento de identificação original ou CNH digital gerada no APP CNH do Brasil.
Crédito pré-aprovado na Caixa:
O usuário deve estar
aprovado na política de crédito pessoal da Caixa
para realizar uma solicitação de portabilidade. Para verificar previamente se há aprovação de crédito, o usuário deverá acessar o aplicativo CAIXA e navegar até: Menu Empréstimos > Empréstimo Pessoal > Simular e Contratar. Se ao fazer isso for exibida uma simulação de empréstimo disponível para contratação, significa que o cliente possui crédito aprovado na Caixa. Ao invés disso, caso apareça uma opção de “atualização cadastral”, significa que, naquele momento,
não há aprovação
e o cliente deve atualizar seus dados. No dia subsequente após atualização, caso a opção de simulação/contratação ainda não estiver disponível, indica que o usuário não foi aprovado na política de crédito da instituição. Nessa situação,
a portabilidade não poderá ser realizada
, pois não há aprovação de crédito para efetivar a transferência do contrato.
Compartilhamento de dados (Open Finance):
O usuário precisa autorizar o compartilhamento de seus dados financeiros via Open Finance envolvendo a Caixa e a instituição detentora do contrato original. Esse procedimento deve ser realizado pelo próprio app da Caixa, onde o usuário seleciona a instituição de origem do crédito e consente o compartilhamento dos dados solicitados. Sem o devido compartilhamento de dados aprovado, a Caixa não conseguirá recuperar os detalhes do contrato original do cliente, impedindo uma solicitação de portabilidade.
Contrato elegível em outra instituição:
Por fim, o usuário deve ter um contrato de Crédito Pessoal Clean (CPC) ativo em outra instituição financeira. Além de estar ativo, esse contrato precisa atender a alguns
critérios mínimos de elegibilidade
para a portabilidade ser possível via Caixa:
Saldo devedor maior que R$ 150,00:
Contratos com saldos abaixo não são elegíveis.
Valor da parcela mensal acima de R$ 20,00:
Parcelas de valor muito baixo não se qualificam.
Taxa de juros do contrato original superior à taxa ofertada pela Caixa:
O juros vigente no empréstimo atual do cliente deve ser maior do que o juro que a Caixa oferece no novo crédito via portabilidade. A taxa oferecida pela Caixa para portabilidade não é divulgada previamente e pode variar conforme políticas internas da instituição, havendo a necessidade de vantagem financeira para o cliente na migração. Para saber qual taxa será aplicada na oferta de portabilidade, o usuário pode acessar os detalhes ao realizar uma simulação de portabilidade.
Passo a passo para realização de solicitação de portabilidade via Caixa
Atendidas todas as condições acima, o funcionário/usuário participante do piloto poderá realizar o processo de portabilidade do seu empréstimo para a Caixa. O passo a passo abaixo descreve
como solicitar a portabilidade
no aplicativo da Caixa:
Acessar o menu de Portabilidade (Open Finance) no app da Caixa:
Abra o aplicativo CAIXA e acesse Menu “Trazer meus dados de outro banco > Open Finance”. Em seguida, selecione a opção “Crédito”, dentro de “Minhas portabilidades”. Dentro desse menu, navegue até “Solicitar Portabilidade”. Essa seção é dedicada à portabilidade de crédito e permitirá iniciar uma nova solicitação. Se o usuário não visualizar nenhum contrato para solicitar portabilidade, isso pode indicar ausência de compartilhamento ativo de dados e o passo 2 deverá ser realizado.
Iniciar o compartilhamento dos dados do contrato original:
No menu “Trazer meus dados de outro banco > Open Finance”, o usuário deve, em seguida, obter os dados do contrato que se deseja portar. Para isso, clique em “Trazer meus dados”. O aplicativo irá guiar o usuário pelo fluxo de consentimento Open Finance, no qual será preciso selecionar a instituição financeira de origem (onde está o empréstimo atual) e autorizar o compartilhamento das informações desse contrato com a Caixa. Caso o usuário já tenha um consentimento ativo e dados atualizados referentes ao contrato, a etapa de compartilhamento pode ser pulada. Após isso, antes de seguir para a próxima etapa, é necessário que seja aguardado até 1 dia útil para avaliação dos contratos e análise da oferta de portabilidade pela proponente.
Solicitar a portabilidade do contrato:
Após a conclusão do compartilhamento de dados, o sistema da Caixa poderá apresentar as informações dos contratos de crédito pessoal do usuário obtidos junto à instituição original. Em seguida, ainda dentro do Menu “Trazer meus dados de outro banco > Open Finance > Crédito”, selecione a funcionalidade “Solicitar Portabilidade”. Após isso, o usuário iniciará a solicitação de portabilidade junto à Caixa para o contrato selecionado. Caso a opção de “Solicitar Portabilidade” ou o contrato não apareça, é recomendado que seja aguardado até 1 dia útil para avaliação dos contratos e análise da oferta de portabilidade pela proponente.
Selecionar e confirmar o contrato a ser portado:
Caso haja mais de um contrato de crédito listado (por exemplo, se o usuário tiver empréstimos em mais de uma instituição ou mais de um contrato na mesma instituição), será necessário selecionar o contrato específico que se deseja portar para a Caixa. Marque o contrato correto e confirme a solicitação de portabilidade. Depois da confirmação, o fluxo de portabilidade de crédito seguirá normalmente via Open Finance.
Uma vez solicitada, a portabilidade de crédito pessoal clean pode levar
até 7 dias úteis para ser concluída
totalmente. Durante esse período, a portabilidade ficará em andamento e o usuário poderá acompanhar atualizações de status pelo próprio aplicativo da Caixa, na seção de "Minhas solicitações enviadas”, ou por notificações da própria instituição. Após a conclusão, o contrato original será encerrado na instituição de origem e o novo contrato passará a vigorar na Caixa, já com as condições acordadas no momento da solicitação.
Contratação de fornecedor para realização de testes de engajamento bilateral
As instituições que optarem pela contratação de um fornecedor para a execução dos testes bilaterais poderão utilizar o mesmo mesmo fornecedor da Associação Open Finance, responsável pela execução dos demais testes do Piloto.
A contratação do fornecedor refere-se especificamente à realização de solicitação de uma portabilidade de crédito
com uma Proponente de C
r
édito, em instituições nas quais seja possível a contratação de crédito pelo fornecedor, e
não garante a efetivação  da portabilidade
, que depende da apresentação de proposta pela Proponente e da identificação da liquidação pela PCM.
A contratação do fornecedor possui um custo de R$ 1.120,58 por teste realizado
, que será repassado à instituição por meio da cobrança de custeio emitida pela Associação Open Finance. O valor a ser cobrado dependerá do resultado obtido na execução do teste, conforme as condições abaixo:
Impossibilidade de abertura de conta ou contratação do produto:
o chamado será encerrado  com essa justificativa e a instituição não será cobrada;
Falha na etapa de compartilhamento de dados:
será cobrado 50% do va
l
or do teste (R$ 560,29) e a instituição poderá
solicitar uma nova execução através do mesmo ticket;
Em caso de sucesso na nova execução, será cobrado o valor integral do teste;
Em caso de falha na nova execução, será mantida a cobrança de 50% do valor do teste e o ticket será encerrado.
Sucesso no compartilhamento do dado:
será cobrado o valor integral independente do recebimento de proposta da Proponente de Crédito.
A solicitação do. teste ao fornecedor pode ser feita mediante a abertura de um ticket no service desk no caminho: Processo de Onboarding > Solicitação de Testes > Portabilidade de Crédito. Cada ticket corresponde a uma portabilidade única.
Reforçamos que a responsabilidade pelo atingimento do critério de engajamento bilateral é exclusiva de cada instituição e que a contratação o fornecedor é opcional, não garantindo o atingimento do critério.
Considerações adicionais
Consulta das portabilidades
pelas proponentes devem ser realizadas (GET) em todos os dias úteis, de 2h em 2h, das 8h às 18h, conforme documentação técnica;
Integração com PCM
é necessária para a devida identificação e contabilização dos critérios do Piloto;
Por se tratar do uso de
valores e produtos reais
em ambiente produtivo, é recomendada a contratação de produtos com baixos valores
Acompanhamento com as instituições
Para melhor apoiar as instituições participantes do Piloto de Portabilidade de Crédito, a equipe de Sucesso do Participante da Associação acompanhará e apoiará as instituições durante todo o período do Piloto através de:
Agendas semanais
: Toda sexta-feira, das 14h às 15h, de 31/10/25 a 27/02/26
Para compartilhamento de informações relevantes, e esclarecimento de dúvidas com com a Associação ou bilaterais com demais instituições
Clique aqui
para entrar na agenda semanal de acompanhamento
Grupo do
Whatsapp
: Para dúvidas pontuais e interações com outras instituições ou Associação
Clique aqui
para acessar o Grupo do
Whatsapp
do Piloto de Portabilidade de Crédito, ou escaneie o QR Abaixo com a câmera de seu celular:
Open
Outros links úteis
Descrição dos testes da FVP Manual:
Link aqui

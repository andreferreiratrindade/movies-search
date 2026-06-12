---
                            title: "Organizações provedoras de dados (transmissoras/detentoras) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "941818238_Organiza+es+provedoras+de+dados+transmissoras+detentoras"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/941818238/Organiza+es+provedoras+de+dados+transmissoras+detentoras"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Organizações provedoras de dados (transmissoras/detentoras) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            As organizações que desejarem atuar como provedoras de dados devem publicar servidores de autorização. O servidor de autorização representa a identidade da organização (marca) e contém os recursos de dados aos quais os receptores podem solicitar acesso. Além disso, o servidor realiza as validações necessárias, como a autenticação do cliente que está requisitando acesso à determinado recurso e a verificação das permissões, garantindo que o acesso aos dados seja seguro e conforme o consentimento do usuário.
As informações configuradas no servidor de autorização, incluindo seu endpoint de /.well-known, são utilizadas pelos clientes que fornecem o consentimento para o compartilhamento de dados ou serviços. Esta URI contém a maior parte das informações necessárias para uma aplicação de um recebedor interagir com o servidor do provedor de dados.
Após a criação do servidor de autorização, inicialmente em ambiente sandbox
[FV3]
, a organização deverá desenvolver suas APIs, realizar testes funcionais através do motor de conformidade, submeter evidências de sucesso para recebimento de certificação funcional e de segurança e realizar integrações com as ferramentas do perímetro central.
A criação do servidor de autorização em ambiente de produção e a publicação dos recursos deve ocorrer apenas após as etapas mencionadas acima realizadas em ambiente sandbox. A instituição está sujeita ao monitoramento de desconformidade a partir do momento em que realiza suas publicações em ambiente produção.
Pontos de atenção no cadastramento de servidor de autorização (marcas transmissoras de dados/detentoras de conta)
Uma marca é representada por um servidor de autorização e o mesmo sempre deve ser cadastrado associado a uma organização;
O vínculo entre uma organização master (mãe) e uma organização que pertence ao conglomerado é realizado via o preenchimento do campo Parent Organization Reference ID no cadastro da organização filha, informando o CNPJ da organização mãe (caso seja necessário ajuste, favor abrir um ticket no
service desk
);
Quando a estrutura for de um conglomerado (uma organização master e uma ou mais organizações relacionadas) é recomendado o cadastro da marca na instituição mãe, caso as filhas venham a utilizar a mesma marca e arquitetura de autenticação. Importante ressaltar que caso não seja cadastrado uma marca exclusiva para a organização filha, será inferido que os cadastros de marcas para atendimento dos papéis regulatórios foram realizados na organização mãe;
Caso a mesma marca pertença a mais de uma organização, esta deverá ser cadastra como um único servidor de autorização em apenas uma das organizações. É vedado a duplicação de marcas, ou seja, marcas que possuem o mesmo
Customer Friendly Server Name
;
Caso uma marca pertença exclusivamente a uma organização filha o cadastro poderá ser realizado apenas na filha;
Exemplos de possíveis cenários para cadastro de servidor de autorização
Open
Neste exemplo, temos uma “Organização” que não possui organizações filhas e possui os papéis regulatórios DADOS e CONTA. Neste cenário a organização possui apenas um AS/marca, a “Marca 1”, que possui todos os recursos necessários para atendimento dos seus papéis regulatórios.
Open
Neste exemplo, temos uma “Organização” que não possui organizações filhas e possui os papéis regulatórios DADOS e CONTA. Neste cenário a organização possui três AS/marcas, a “Marca 1” que possui os recursos necessários para atendimento do papel DADOS, a “Marca 2” que possui os recursos referente ao papel “CONTA” e a “Marca 3” atende a ambos os papéis regulatórios.
Open
Neste exemplo, temos uma “organização mãe” que possui duas filhas e todas possuem os mesmos papéis regulatórios DADOS e CONTA. Neste cenário a “organização mãe” possui um AS/marca, a “Marca 1”, que possui apenas um AS/marca, a “Marca 1” que possui todos os recursos necessários para atendimento dos seus papéis regulatórios. Ambas as suas organizações filhas compartilham da mesma arquitetura e infraestrutura de autenticação, utilizando o mesmo AS/marca para compartilhamento dos seus recursos.
Open
Neste exemplo, temos uma “organização mãe” que possui duas filhas que possuem papéis regulatórios distintos. A “organização mãe” e a “organização filha 1” possuem o papel regulatório DADOS, enquanto a “Organização Filha 2” possui o papel regulatório CONTA. Neste cenário a “organização mãe” possui um AS/marca, a “Marca 1”, que possui apenas um AS/marca, a “Marca 1”, entregando todos os recursos necessários para atendimento do papéis regulatórios tanto para a “Organização Mãe”, quanto para a “Organização Filha 1”, compartilhando a mesma arquitetura e infraestrutura de autenticação.
A “Organização Filha 2” possui a “Marca 2” que entrega os recursos necessários para atender ao seu papel regulatório. Neste caso, a “Organização Filha 2” possui a sua própria arquitetura e infraestrutura de autenticação.
Open
Neste exemplo, temos uma “organização mãe” que possui duas filhas que possuem papéis regulatórios distintos. A “Organização Mãe” e a “Organização Filha 1” possuem o papel regulatório DADOS, enquanto a “Organização Filha 2” possui o papel regulatório CONTA.
Com a intenção de reuso da arquitetura e infraestrutura de autenticação, o participante replicou o papel regulatório da “Organização Filha 2” para a “Organização Mãe” e desta forma, com uso de uma única marca/AS, a “Marca A”, entrega todos os recursos necessários para atender aos papéis regulatórios do conglomerado.
Open
Neste exemplo, temos uma “Organização Mãe” que possui duas filhas e todas possuem os mesmos papéis regulatórios DADOS e CONTA. Neste cenário a “organização mãe” possui um AS/marca, a “Marca 1”, que possui apenas um AS/marca, a “Marca 1” que possui todos os recursos necessários para atendimento dos papéis regulatórios da “Organização Mãe” e “Organização Filha 1”. A “Organização Filha 2” possui a “Marca 2” que entrega os recursos necessários para atender dos seus papéis regulatórios. Neste caso, a “Organização Filha 2” possui a sua própria arquitetura e infraestrutura de autenticação.
Ciclo de vida do servidor de autorização (marcas transmissoras de dados/detentoras de conta)
Cenários de encerramento, aquisição ou incorporação de marcas, encerramento de produtos ofertados por uma marca, migração de infraestrutura tecnológica ou demais mudanças que demandem alteração no servidor de autorização são descritas na seção do ciclo de vida do servidor de autorização. Essa seção contém recomendações para gestão de mudanças do servidor.
Para o cenário de uma organização ou conglomerado que tome a decisão de descontinuar/aposentar um servidor de autorização, ficam especificadas abaixo, as regras para preenchimento dos campos no diretório e outros pontos importantes:
Nome do Campo
Descrição
Exemplo
Transmissora/Detentora
Receptora/Iniciadora
Deprecation Date
Data programada para iniciar a descontinuação do servidor de autorização
2024-11-01
Data a partir da qual o servidor de autorização não aceitará mais requisições de novos consentimentos
Data limite para solicitação de novos consentimentos naquele servidor.
Retirement Date
Data programada para a aposentadoria do servidor
2024-12-01
Data a partir da qual o servidor de autorização será inativado
Data limite para consultas de consentimentos naquele servidor.
SupersededByAuthorisationServerId
ID do servidor de autorização que substituirá o servidor atual
xxxxxxxx-XXXX-xxxx-XXXX-xxxxXXXXxxxx
ID do servidor de autorização que passará a recepcionar os pedidos de novos consentimentos a partir da inatividade do servidor em questão
Redirecionamento das solicitações de novos consentimentos.
Pontos Importantes:
Os campos
Deprecation Date
e
Retirement Date
serão obrigatórios no contexto de descontinuação de marcas e o campo
SupersededByAuthorisationServerId
só será obrigatório no caso de substituição do servidor de autorização.
O campo
Deprecation Date
deve ser informado com pelo menos 10 dias antes do início da descontinuação.
As datas inseridas nos campos citados, devem ser informadas e acordadas com o regulador.
A boa prática sugerida é que a data de depreciação seja anterior a data de aposentadoria em pelo menos 1 mês (30 dias corridos), a ser validada caso a caso junto ao regulador.
Esses campos são meramente informativos. Isso significa que, é de responsabilidade da Instituição que está descontinuando/aposentando a marca construir uma solução para "recusar" as requisições de consentimento recebidas a partir da data informada no campo "
Deprecation Date
", não sendo responsabilidade das demais Instituições participantes não requisitarem novos consentimentos através do Authorisation Server, uma vez que o mesmo permanece como "Ativo" até a data de sua aposentadoria.
Os consentimentos de transmissão ativos na marca que está sendo descontinuada/aposentada deverão continuar acessíveis para as Instituições receptoras, seguindo as regras de "tempo" determinadas pela regulação e especificações vigentes.
Clique para conferir o passo a passo para registro de um servidor de autorização
Clique para conferir o passo a passo para registro de certificação de segurança do servidor de autorização
Clique para conferir o passo a passo para publicação de recursos no servidor de  autorização
Clique para conferir orientações sobre o ciclo de vida do servidor de autorização
Clique para conferir as regras e obrigações das instituições participantes do Open Finance Brasil

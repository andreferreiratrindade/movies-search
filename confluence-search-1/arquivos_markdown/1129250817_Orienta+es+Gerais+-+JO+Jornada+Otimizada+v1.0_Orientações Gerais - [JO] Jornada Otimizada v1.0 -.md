---
                            title: "Orientações Gerais - [JO] Jornada Otimizada v1.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1129250817_Orienta+es+Gerais+-+JO+Jornada+Otimizada+v1.0"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1129250817/Orienta+es+Gerais+-+JO+Jornada+Otimizada+v1.0"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Orientações Gerais - [JO] Jornada Otimizada v1.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Esta página apresenta as regras básicas que orientam o funcionamento da Jornada Otimizada, servindo como referência padrão para a implementação do fluxo. Entretanto, cada produto poderá adotar adaptações específicas conforme suas particularidades, e essas variações estarão detalhadas nas páginas específicas da respectiva Jornada Otimizada.
As jornadas adaptadas para diferentes contextos se encontram nos links abaixo:
Transferências Inteligentes
Jornada sem Redirecionamento
Jornada Otimizada
O fluxo base de uma Jornada Otimizada para criação e aprovação de consentimentos é apresentado a seguir.
Open
O software cliente cria um access_token do tipo client_credentials com os escopos necessários para criar o consentimento primário e secundário (podem ser dois access_tokens distintos se desejado).
O software cliente cria o consentimento secundário, indicando as permissões desejadas e que o consentimento estará vinculado (isLinked igual a true).
O software cliente cria o consentimento primário, indicando que ele está vinculado (isLinked igual a true) e informando o consentId do consentimento secundário criado anteriormente.
O software cliente chama o endpoint PAR com o objeto request contendo a lista de todos os escopos que serão necessários para a operação dos serviços e realiza o redirecionamento.
O usuário revisa e aprova o consentimento na jornada otimizada.
O software cliente solicita e recebe o access_token incluindo todos os escopos aprovados na jornada, podendo consumir as APIs.
Pré-Requisitos
Do Transmissor/Detentor:
para que uma organização possa oferecer a jornada otimizada, é obrigatório que o servidor de autorização tenha habilitados os papéis de compartilhamento de dados e de detentor de contas (DADOS e CONTAS).
Do Receptor/Iniciador:
o software statement utilizado como receptor de dados deve incluir os papéis de receptor de dados e iniciador de pagamentos (DADOS e PAGTO).
Criação dos Consentimentos
A Jornada Otimizada se baseia na aprovação de dois tipos de consentimentos, que trabalham em conjunto para garantir uma experiência unificada e eficiente: o consentimento primário e o consentimento secundário.
Consentimento Primário:
Este é o consentimento (ou relacionamento de dispositivo) central para a jornada em andamento. Ele representa a autorização principal que o usuário concede para a execução de um serviço ou funcionalidade específica.
Consentimento Secundário:
Trata-se de um consentimento de dados complementar, que é aprovado em conjunto com o consentimento primário dentro da Jornada Otimizada. Ele possui um relacionamento forte com o consentimento primário, o que significa que sua validade está atrelada à do consentimento primário. Além disso, o consentimento secundário possui regras de permissionamento, seleção de recursos e data de validade que são limitadas e definidas especificamente para a Jornada Otimizada em execução, garantindo que o compartilhamento de dados seja adequado e alinhado ao serviço principal.
Chamada ao PAR endpoint
O processo de redirecionamento na jornada otimizada, da mesma forma que em uma jornada convencional, se inicia com a chamada ao PAR endpoint, com a diferença que no JWT enviado no objeto
request
irá conter na sua lista de escopos o id dos consentimentos ou vínculos que deverão ser aprovados em uma única jornada.
Open
Identificação da Jornada
O servidor de autorização possui uma única rota para o front-end, destinado à autorização dos consentimentos. Assim, seguindo o processo atual, o front-end deve utilizar a lista de escopos e os consentimentos/vínculos informados para definir a jornada, o fluxo de telas e as validações a serem executadas.
Jornada
Descrição
Escopos
Jornada
Descrição
Escopos
Compartilhamento de Dados
Cliente deseja aprovar o compartilhamento dos seus dados cadastrais e transacionais. Apenas um escopo dinâmico de consentimento de dados é recebido.
Obrigatório:
openid consents resources consent:consentId
Opcionais:
accounts credit-cards loans investiments…
Iniciação de Pagamentos (imediato, agendado ou múltiplos agendamentos)
Cliente deseja aprovar a execução de um pagamento (imediato, agendado ou múltiplos agendamentos). Apenas um escopo dinâmico  de pagamentos é recebido.
Obrigatório:
openid consent:consentId payments
Vínculo de dispositivo e Iniciação de Pagamentos com JSR
Cliente deseja estabelecer um vínculo para realizar pagamentos através da uma JSR. Apenas um escopo dinâmico de vínculo é recebido.
Obrigatório:
openid enrollment:enrollmentId  payments nrp-consents
Transferências Inteligentes
Cliente deseja habilitar o uso de transferências inteligentes da sua conta
Obrigatório:
openid recurring-consent:recurringConsentId recurring-payments
PIX Automático
Cliente deseja configurar a ocorrência de pagamentos recorrentes
Obrigatório:
openid recurring-consent:recurringConsentId recurring-payments
Vínculo de dispositivo e Transferências Inteligentes com JSR
Cliente deseja habilitar o pagamento sem redirecionamento através do vínculo do seu dispositivo
Obrigatório:
openid  enrollment:enrollmentId  payments nrp-consents
Jornada otimizada de Transferências Inteligentes com compartilhamento de dados de Saldo
Cliente deseja habilitar o uso de transferências inteligentes da sua conta e ao mesmo tempo compartilhar os dados de saldo para facilitar o gerenciamento.
Obrigatório
: openid consent:consentId consents resources accounts recurring-consent:recurringConsentId recurring-payments
Jornada otimizada para vínculo de dispositivo com compartilhamento de dados de Saldo
Cliente deseja habilitar o pagamento sem redirecionamento através do vínculo do seu dispositivo e ao mesmo tempo compartilhar os dados de saldo para facilitar o gerenciamento.
Obrigatório:
openid consent:consentId consents resources accounts enrollment:enrollmentId  payments nrp-consents
Aprovação do Consentimento
No fluxo de aprovação do consentimento será dada, no ambiente da iniciadora, a opção do cliente confirmar ou remover o compartilhamento de dados de forma que:
Caso o cliente rejeite o consentimento primário de serviços, o consentimento secundário de dados também deverá ser rejeitado​
Caso o cliente desmarque a opção de compartilhamento de dados, o consentimento de serviço é aprovado e o de dados rejeitado​
Caso o cliente mantenha a opção de compartilhamento de dados, ambos os consentimentos são aprovados.
Criação do access-token
Ao término da aprovação, o access_token deverá ser gerado e vinculado aos consentimentos que foram aprovados​
Se ambos os consentimentos forem aprovados, todos os escopos relativos aos serviços de dados, transferências inteligentes e dos consentimentos devem ser mantidos no access_token gerado​
Caso apenas o consentimento de serviço seja aprovado, os escopos do consentimento de dados deverão ser removidos do access_token gerado​.
Renovação do access-token
Durante o processo de renovação do access-token, o servidor de autorização deve verificar se os consentimentos vinculados permanecem válidos. Se pelo menos um dos consentimentos ainda for válido, o token deve ser renovado.
Open
Software Cliente realiza uma chamada ao endpoint POST /token do servidor de autorização para realizar a renovação do access-token através do refreh-token;
Servidor de autorização verifica se o consentimento do serviço permanece em um estado válido
Servidor de autorização verifica se o consentimento de dados permanece em um estado válido
Se pelo menos um dos consentimentos estiver em um estado válido, servidor de autorização emite um novo access-token

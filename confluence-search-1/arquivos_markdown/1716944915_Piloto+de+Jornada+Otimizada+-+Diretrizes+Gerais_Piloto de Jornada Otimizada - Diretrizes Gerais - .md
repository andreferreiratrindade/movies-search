---
                            title: "Piloto de Jornada Otimizada - Diretrizes Gerais - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1716944915_Piloto+de+Jornada+Otimizada+-+Diretrizes+Gerais"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1716944915/Piloto+de+Jornada+Otimizada+-+Diretrizes+Gerais"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Piloto de Jornada Otimizada - Diretrizes Gerais - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Introdução
Está sendo lançado o novo produto de Jornada Otimizada (JO). Com isso, tem-se como intuito, nesta página, a centralização das informações relevantes para compartilhamento com as instituições participantes do
Piloto de Jornada
Otimizada
, que será realizado de
22/04/2026 a 22/06/2026
.
A
Jornada Otimizada
é um conjunto de funcionalidades do Open Finance Brasil que visa simplificar e agilizar a experiência dos usuários em fluxos de pagamento, reduzindo fricções na autenticação e eliminando redirecionamentos desnecessários. A Jornada Otimizada abrange dois produtos:
Jornada Otimizada para Transferências Inteligentes
Jornada Otimizada para Vínculo de Dispositivo
O Piloto é regulado pela Instrução Normativa BCB nº 740, de 29 de maio de 2026, que estabelece as orientações, condições e prazos para a realização de testes em produção relativos à jornada otimizada no Open Finance. O escopo técnico dos testes está definido nos Anexos I e II da IN nº 740.
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
a identificação de problemas em ambiente produtivo, previamente ao
Go Live
;
Viabilizar a
criação de agendas
(bilaterais e multilaterais) antes do
Go Live
, para antecipação e correção de eventuais problemas e dificuldades identificadas;
Especificações da Jornada Otimizada
Para implementação e melhor entendimento da Jornada Otimizada, os seguintes materiais devem ser consultados:
Informações
sobre a Jornada Otimizada;
Orientações Gerais
sobre as funcionalidades da API de Jornada Otimizada podem ser encontradas nessa página;
Jornada Otimizada para Transferências Inteligentes
;
Jornada Otimizada para Jornada Sem Redirecionamento
.
Obrigatoriedade de participação
Instituições Detentoras/Transmissoras
: Instituições que atuam tanto como transmissora de dados quanto como detentoras de conta possuem obrigatoriedade de oferta da Jornada Otimizada, devendo estar com a implementação disponível e funcional a partir do início do Piloto (22/04/2026). Ou seja, são instituições que possuem o papel DADOS e CONTA cadastrados no diretório dos participantes.
ITPs facultativas:
ITPs que optarem por disponibilizar serviços de Jornada Otimizada para os novos produtos e serviços abaixo deverão participar dos testes em produção durante o período de Piloto:
Jornada Otimizada para Transferências Inteligentes
Jornada Otimizada para Vínculo de dispositivo
Para que seja uma instituição participante do piloto de Jornada Otimizada, a ITP deverá abrir uma solicitação de Onboarding através do service desk
até
30/04/2026
na categoria: Processo de onboarding > Solicitação de interesse em participação > Iniciadora e selecionar a opção do produto que deseja ofertar: Jornada Otimizada – Transferências Inteligentes ou Jornada Otimizada – Vínculo de Dispositivo. ITPs que optarem por disponibilizar a funcionalidade
após 30/04/2026
deverão realizar os testes em produção seguindo a política de onboarding do Open Finance e apenas poderão ofertar a Jornada Otimizada após o Go Live, em 22/06/26.
ITPs que ainda não atuam como transmissoras de dados estão autorizadas a participar dos testes em produção durante o período do Piloto, conforme §2º do art. 5º da IN BCB nº 725/2026. No entanto, a oferta do serviço ao público em geral, a partir de 22/06/2026, está condicionada à regularização dessa situação, sendo necessária a atuação como transmissora de dados para todo o escopo aplicável à instituição, nos termos do §3º do mesmo artigo.
Público participante do piloto e restrição de usuários
O piloto de Jornada Otimizada ocorrerá exclusivamente com restrição de usuários e seguirá a política vigente de testes em produção do Open Finance, cujos detalhes podem ser consultados na guia
Restrição de recursos e habilitação de usuários para testes em produção
.
Instituições
Detentoras/Transmissoras
:
Deverão indicar restrição das novas funcionalidade através de inclusão de metadado “Homologacao JO” na API de
Consents
no diretório dos participantes;
Deverão indicar os usuários que serão habilitados pelas ITPs para realização de testes em produção, conforme regras e instruções na página acima indicada;
Deverão disponibilizar a funcionalidade de Jornada otimizada para
toda a base de usuários
, não havendo
nenhuma restrição
de acesso às funcionalidades implementadas, cuja implementação deve estar realizada, disponível e funcional
a partir do início do Piloto
.
Instituições
Iniciadoras de transação de pagamentos (ITPs)
:
As credenciais de acesso para a API de consumo dos recursos dos usuários serão disponibilizadas às instituições após solicitação de participação, via Service Desk.
Critérios e indicadores a serem acompanhados
O acompanhamento do Piloto será realizado com base nos critérios abaixo. O não atendimento a qualquer critério nos Pontos de Controle poderá resultar em aberturas de tickets bilaterais, sendo utilizados como referência para levantamento de instituições com sucesso durante o Piloto.
Pareamento com PCM
: Todas as instituições devem ter, em D+1, ao menos 95% de pareamentos com sucesso na Plataforma de Coleta de Métricas (PCM);
Qualidade das chamadas reportadas à PCM
: Nenhum ticket de qualidade da PCM, relacionados à Pagamentos devem estar em aberto durante Pontos de Controle, a serem realizados em 08/05/26, 22/05/26 e 05/06/26;
Jornada de Experiência do Usuário (UX)
: Durante o período do piloto, serão realizadas validações de UX para as marcas participantes do Piloto. O questionário de UX, que será utilizado de base para validação das jornadas as instituições, será integralmente baseado nos requisitos da última versão do
Guia de Experiência do Usuário
.
Tickets bilaterais
: Nenhum ticket bilateral relacionado à Jornada Otimizada deve estar em aberto, independente do SLA, durante Pontos de Controle, a serem realizados em 08/05/26, 22/05/26 e 05/06/26;
Ferramenta de Validação em Produção - FVP Manual
: As
Detentoras/Transmissoras
participantes devem obter o sucesso nos testes relacionados à FVP Manual. Informações sobre solicitação de acesso à FVP e detalhamento dos testes estão na seção “Testes da FVP” abaixo. A responsabilidade de execução varia conforme a classificação de cada marca:
Marcas do Grupo de Controle: Os testes são executados pelo próprio fornecedor contratado pela Associação, com conta aberta pelo fornecedor na instituição.
Marcas com conta aberta pelo fornecedor: Os testes são executados pelo próprio fornecedor contratado pela Associação, com conta aberta pelo fornecedor na instituição.
Demais marcas: A própria instituição deve executar os testes e garantir o sucesso antes das datas estabelecidas em cronograma. As datas limites para sucesso em cada cenário de teste estão descritas abaixo, com maior detalhamento na seção “Testes da Ferramenta de Validação em Produção (FVP)“ desta página:
30/04/2026
: Data limite para sucesso nos
Testes de interoperabilidade
08/05/2026
: Data limite para sucesso nos
Testes de garantia de jornada
15/05/2026
: Data limite para sucesso nos
Testes de garantia de erro
Pontos de Controle
: Os Pontos de Controle são momentos pré-estabelecidos de avaliação parcial do progresso das instituições. Em cada um dos pontos de controle, serão realizados levantamentos das pendências das instituições e um novo ticket as consolidando será aberto e direcionado às instituições. Os pontos de controle serão realizados em 08/05/2026, 22/05/2026 e 05/06/2026, além do levantamento final das pendências realizado no Go Live
Engajamento – Criação de consentimentos e vínculos
: Para acompanhamento do piloto, o engajamento será medido por meio da volumetria de consentimentos e vínculos de dispositivos criados e identificados via PCM, utilizando a funcionalidade de Jornada Otimizada.
Transferências Inteligentes
:
100 consentimentos criados, sendo ao menos 20 PJ, quando aplicável;
Para Detentoras/Transmissoras: 1 consentimento criado com ao menos 50% das ITPs participantes do piloto;
Para ITPs: 1 consentimento criado com ao menos 50% das detentoras participantes do piloto;
Para ITPs: 1 consentimento criado com todas as 16 detentoras do grupo de controle.
Vínculo de Dispositivo
100 vínculos criados, sendo ao menos 20 PJ, quando aplicável;
Para Detentoras/Transmissoras: 1 vínculo criado com ao menos 50% das ITPs participantes do piloto;
Para ITPs: 1 vínculo criado com ao menos 50% das detentoras participantes do piloto;
Para ITPs: 1 vínculo criado com todas as 16 detentoras do grupo de controle.
Engajamento – Liquidação de pagamentos
: Para acompanhamento do piloto, o engajamento será medido por meio da volumetria de pagamentos liquidados e identificados via PCM, utilizando-se a funcionalidade de Jornada Otimizada.
Transferências Inteligentes
:
Mínimo de 40 pagamentos liquidados, sendo ao menos 10 PJ, quando aplicável;
Para Detentoras/Transmissoras: 1 pagamento liquidado com ao menos 50% das ITPs participantes do piloto;
Para ITPs: 1 pagamento liquidado com ao menos 50% das detentoras participantes do piloto;
Para ITPs: 1 pagamento liquidado com todas as 16 detentoras do grupo de controle.
Vínculo de Dispositivo
40 pagamentos liquidados via JSR, sendo ao menos 20 pagamentos imediatos e 10 PJ, quando aplicável;
Para Detentoras/Transmissoras: 1 pagamento liquidado via JSR com ao menos 50% das ITPs participantes do piloto;
Para ITPs: 1 pagamento liquidado via JSR com ao menos 50% das detentoras participantes do piloto;
Para ITPs: 1 pagamento liquidado via JSR com todas as 16 detentoras do grupo de controle.
Marcos de engajamento
: São pontos de verificação, ao longo do Piloto, que indicam o quanto cada instituição participante já atingiu do volume total exigido para o Go Live. Ou seja, funcionam como metas intermediárias que permitem à Associação e ao ecossistema acompanhar o progresso e identificar instituições com dificuldades antes do prazo final. A tabela abaixo apresenta os volumes mínimos a serem atingidos em cada marco, calculados proporcionalmente ao volume total exigido para o Go Live, conforme definido no Anexo I da IN BCB nº 725/2026.
Marcos Intermediários - Transferência Inteligentes
Indicador
30% - 08/05
50% - 22/05/26
80% - 05/06/26
Go Live - 22/06/26
Indicador
30% - 08/05
50% - 22/05/26
80% - 05/06/26
Go Live - 22/06/26
Consentimentos Autorizados - Total
30
50
80
100
Consentimentos Autorizados - PJ
6
10
16
20
Pagamentos Liquidados - Total
12
20
32
40
Pagamentos Liquidados - PJ
3
5
8
10
Diversidade - Consentimentos Autorizados
-
-
-
Para detentoras: 1 ITP
Para ITPs: 20 detentoras
Diversidade - Pagamentos Liquidados
-
-
-
Para detentoras: 1 ITP
Para ITPs: 20 detentoras
Marcos Intermediários - Vínculo de Dispositivo
Indicador
30% - 08/05
50% - 22/05/26
80% - 05/06/26
Go Live - 22/06/26
Indicador
30% - 08/05
50% - 22/05/26
80% - 05/06/26
Go Live - 22/06/26
Vínculos Autorizados - Total
30
50
80
100
Vínculos Autorizados - PJ
6
10
16
20
Pagamentos Liquidados - Total
12
20
32
40
Pagamentos Liquidados - PJ
3
5
8
10
Pagamentos Liquidados - Imediatos
6
10
16
20
Diversidade - Vínculos Autorizados
-
-
-
Para detentoras: 2 ITPs
Para ITPs: 20 detentoras
Diversidade - Pagamentos Liquidados
-
-
-
Para detentoras: 2 ITPs
Para ITPs: 20 detentoras
Cronograma de execução dos testes manuais para o Piloto Jornada Otimizada
Com o intuito de dar mais visibilidade ao ecossistema quanto ao cronograma de execução da FVP e de execução de UX pelo fornecedor, compartilhamos, abaixo, as datas previstas que serão realizadas as validações com as
Detentoras/Transmissoras
e
ITPs
participantes do piloto.
Open
1: Selecionadas principais marcas de 16 conglomerados, de acordo com Anexo II da
Instrução Normativa BCB 725
de 16/04/26. Relação das instituições está presente na seção “Grupo de Controle” desta página
Indicadores de sucesso das instituições
Painel Integrado de acompanhamento de indicadores
Para o devido acompanhamento das métricas e indicadores jornada otimizada, foi-se construído o
Painel Integrado de acompanhamento do Piloto
. Nele, poderão ser encontradas as métricas de acompanhamentos de pareamento, engajamento, acompanhamento funcional da FVP, dentre outros;
Para solicitação de
acesso ao painel
, é necessário que sejam seguidas as seguintes instruções:
O usuário deve cadastrar, em sua instituição no diretório dos participantes, seu
email
com acesso à funcionalidade PDV;
Para isso, na página da sua instituição no diretório dos participantes, acesse: Papéis > Usuários de domínio > Adicionar novo >
Data visualization platform
> PDV;
Após isso, o usuário irá receber um
email
do diretório confirmando o seu devido cadastrado;
Após execução da rotina de concessão de acesso, realizada ao final de cada dia, o usuário deverá receber um
email
do Quicksight com as devidas orientações para cadastro;
No momento de realização do login, caso solicitado, é necessário inserir em “
account name
”, o seguinte valor “openfinance-brasil”.
Relação de ITPs participantes
ITP
Segmento
Ambiente
Canal de acesso
ITP
Segmento
Ambiente
Canal de acesso
Iniciador
PF e PJ
App Android, App iOS, Desktop e App Browser
JSR:
https://app.iniciador.com.br/jo/login
Transferências Inteligentes:
Login — Iniciador
Google Pay
PF
App Android
JSR:
Google Wallet - Your Fast and Secure Digital Wallet
Lina
PF e PJ
Desktop e App Browser
JSR:
https://doacao.linaopenx.com.br/piloto-jornada-otimizada
Pluggy
PF e PJ
App Android, App iOS, Desktop e App Browser
JSR:
Index
Transferências Inteligentes:
http://sweeping.of.pluggy.ai/
Testes da Ferramenta de Validação em Produção (FVP)
A FVP Manual é utilizada para validar o funcionamento técnico das implementações em ambiente de produção das instituições transmissoras/detentoras.
Solicitação de acesso à FVP
O acesso à FVP deve ser realizado pela própria instituição através do diretório dos Participantes. Instruções detalhadas sobre o processo de solicitação estão disponíveis na seção “4 - Configurando e executando testes da FVP Manual“ do
Guia de Operação da Ferramenta de Validação em Produção
.
Maiores instruções sobre a execução dos testes da FVP de Jornada Otimizada podem ser encontradas na página de
Orientações de Execução da FVP
.
Responsabilidades de execução da FVP Manual
As
Detentoras/Transmissoras
participantes devem obter o sucesso nos testes relacionados à FVP Manual. A responsabilidade de execução e datas limites para obtenção de sucesso variam conforme a classificação de cada marca:
Marcas do Grupo de Controle: Os testes são executados pelo próprio fornecedor contratado pela Associação, com conta aberta pelo fornecedor na instituição.
Marcas com conta aberta pelo fornecedor: Os testes são executados pelo próprio fornecedor contratado pela Associação, com conta aberta pelo fornecedor na instituição.
Demais marcas: A própria instituição deve executar os testes e garantir o sucesso até as datas estabelecidas em cronograma:
30/04/2026
: Data limite para sucesso nos
Testes de interoperabilidade
08/05/2026
: Data limite para sucesso nos
Testes de garantia de jornada
15/05/2026
: Data limite para sucesso nos
Testes de garantia de erro
Escopo e cenários dos testes
disponíveis para execução na FVP Manual
Produto
Cenário
Módulo de teste
Resumo do teste
Transferências inteligentes
Interoperabilidade
fvp-optimised-journey_sweeping_payments-balances_test-module-v1
Valida a execução com sucesso da jornada otimizada com sweeping, incluindo autorização e pagamento, atualizando-se o saldo e consultando-se o limite da conta
Transferências inteligentes
Garantia de erro
fvp-optimised-journey_sweeping_invalid-par_test-module-v1
Garante falha na jornada quando o PAR é chamado sem o recurringConsentId vinculado
Transferências inteligentes
Garantia de erro
fvp-optimised-journey_sweeping_invalid-request_test-module-v1
Garante falha na jornada quando o objeto journey não é enviado na criação do recurringConsent
Transferências inteligentes
Garantia de jornada
fvp-optimised-journey_sweeping_revoked-consent_payments_test-module-v1
Garante que a revogação do consentimento de dados bloqueia acesso ao saldo, mantendo o journey e o recurring consent autorizados, ainda permitindo realizar um pagamento
Transferências inteligentes
Garantia de jornada
fvp-optimised-journey_sweeping_revoked-recurring-consent_test-module-v1
Garante que a revogação do recurring consent atualiza corretamente ambos os recursos vinculados, mantendo-se o journey
Vínculo de Dispositivo
Interoperabilidade
fvp-optimised-journey_enrollments-balances_test-module-v1
Valida a execução com sucesso da jornada sem redirecionamento, com enrollment autorizado e vínculo correto entre enrollment e consentimento de dados, realizando-se um pagamento imediato, consultando-se saldo e limte
Vínculo de Dispositivo
Garantia de erro
fvp-optimised-journey_enrollments-invalid_par_test-module-v1
Garante falha na jornada quando o PAR é chamado sem o enrollmentId vinculado
Vínculo de Dispositivo
Garantia de erro
fvp-optimised-journey_enrollments-invalid-request_test-module-v1
Garante falha na jornada de vínculo de dispositivo quando o objeto journey não é enviado no enrollment
Vínculo de Dispositivo
Garantia de jornada
fvp-optimised-journey_enrollments_revoked-consent_payments_test-module-v1
Garante que a revogação do consentimento de dados bloqueia acesso ao saldo, mantendo o journey e o enrollment autorizados, ainda permitindo realizar um pagamento
Vínculo de Dispositivo
Garantia de jornada
fvp-optimised-journey_enrollments_revoked-enrollment_test-module-v1
Garante que a revogação do enrollment atualiza corretamente ambos os recursos vinculados, mantendo-se o journey
Transferências inteligentes e JSR
Garantia de erro
fvp-optimised-journey_invalid-permissions_test-module-v1
Garante falha para quando a jornada otimizada utiliza permissões incorretas
Transferências inteligentes e JSR
Garantia de erro
fvp-optimised-journey_automatic-pix_test-module-v1
Valida que a jornada otimizada é rejeitada quando vinculada a consentimento de Pix Automático
Transferências inteligentes e JSR
Garantia de erro
fvp-optimised-journey_payments_test-module-v1
Valida que a jornada otimizada é rejeitada quando vinculada a consentimento da API de Pagamentos
Grupo de Controle
Selecionadas principais marcas de 16 conglomerados, de acordo com Anexo II da
Instrução Normativa BCB 725
de 16/04/26:
Banco do Brasil (marca "Banco do Brasil" para clientes pessoa natural e pessoa jurídica);
Banco PAN (marca "Banco PAN" para clientes pessoa natural);
Bradesco (marca "Bradesco Pessoa Física" para clientes pessoa natural e marca "Bradesco Pessoa Jurídica" para clientes pessoa jurídica);
BTG Pactual (marca "BTG Banking" para clientes pessoa natural e marca "BTG Empresas" para clientes pessoa jurídica);
C6 (marca "C6 Bank" para clientes pessoa natural e pessoa jurídica);
Caixa Econômica Federal (marca "CAIXA" para clientes pessoa natural e pessoa jurídica);
Digio (marca "Banco Digio" para clientes pessoa natural);
Itaú (marca "Itaú" para clientes pessoa natural e marca "Itaú Empresas" para clientes pessoa jurídica);
Mercado Pago (marca "Mercado Pago" para clientes pessoa natural e pessoa jurídica);
Neon Pagamentos (marca "Neon" para clientes pessoa natural);
Nu Pagamentos (marca "Nubank" para clientes pessoa natural e pessoa jurídica);
Pagseguro (marca "PagBank" para clientes pessoa natural e pessoa jurídica);
PicPay (marca "PicPay" para clientes pessoa natural e marca "PicPay Negócios" para clientes pessoa jurídica);
Santander (marca "Banco Santander Pessoa Física" para clientes pessoa natural e marca "Banco Santander Pessoa Jurídica" para clientes pessoa jurídica);
Sicredi (marca "Sicredi" para clientes pessoa natural e pessoa jurídica); e
Sicoob (marca "Sicoob" para clientes pessoa natural e pessoa jurídica).
Acompanhamento com as instituições

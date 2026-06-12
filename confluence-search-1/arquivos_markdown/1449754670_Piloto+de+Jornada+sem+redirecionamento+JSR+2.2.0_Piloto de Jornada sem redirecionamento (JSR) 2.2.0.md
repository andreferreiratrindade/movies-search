---
                            title: "Piloto de Jornada sem redirecionamento (JSR) 2.2.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1449754670_Piloto+de+Jornada+sem+redirecionamento+JSR+2.2.0"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1449754670/Piloto+de+Jornada+sem+redirecionamento+JSR+2.2.0"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Piloto de Jornada sem redirecionamento (JSR) 2.2.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Introdução
O piloto da Jornada sem Redirecionamento 2.2.0 está previsto para ocorrer entre 06/02/2026 e 21/04/2026 e tem como objetivo testar a participação de novos entrantes na jornada e validar, para as instituições já operantes, as novas funcionalidades introduzidas nesta versão, incluindo o produto Pix Automático, o suporte ao ambiente desktop e a ampliação da jornada para o segmento PJ.
Obrigatoriedade de participação
O piloto será obrigatório para:
Instituições Detentoras de conta
:
Que já operam JSR
: Instituições que participaram do piloto de JSR v2.1.0 deverão realizar testes exclusivamente para as funcionalidades introduzidas na v2.2.0
Novos entrantes
: Instituições obrigatórias no arranjo Pix deverão obter sucesso nos testes de todos os escopos da jornada sem redirecionamento (Pagamentos imediatos e agendados; Pix automático; PF; PJ; Mobile e Desktop)
Instituições Iniciadoras de Transação de Pagamentos (ITPs)
: Instituições que optarem por disponibilizar serviços de JSR para os novos produtos e serviços introduzidos neste versionamento:
JSR
– Pagamentos imediatos e agendados
JSR
– Pix automático – Mobile
JSR
– Pix automático – Desktop
Declaração de interesse em participação – ITPs
Para que seja uma instituição participante do piloto de JSR v2.2.0,
a ITP deverá abrir um ticket no service desk até 30/01/2026, indicando o produto, segmento e ambiente que pretende ofertar.
A ITP deve abrir um ticket por produto na categoria Processo de onboarding > Solicitação de interesse em participação > Iniciadora e selecionar a opção do produto que deseja ofertar:
JSR – Pagamentos imediatos e agendados
JSR – Pix automático
Instituições que optarem por disponibilizar a funcionalidade após essa data deverão realizar os testes em produção seguindo a política de onboarding do Open Finance e não farão parte deste go live
Público participante do piloto e restrição de usuários
O piloto de jornada sem redirecionamento ocorrerá exclusivamente com restrição de usuários e seguirá a política vigente de testes em produção do Open Finance, cujos detalhes podem ser consultados na guia
Restrição de recursos e habilitação de usuários para testes em produção
.
Instituições detentoras de conta:
Que já operam JSR:
Deverão indicar o metadado da Familia de API
‘Em homologacao'
novos recursos’ no momento de publicação da API no Diretório de Participantes
Novos entrantes:
Deverão indicar o metadado da Familia de API
‘Em homologacao’
no momento de publicação da API no Diretório de Participantes
A partir de 23/01/2026 deverão indicar os usuários que deverão ser habilitados pelas ITPs para realização de testes. Informações adicionais serão compartilhadas nessa data
Instituições iniciadoras de transação de pagamentos:
As credenciais de acesso para a API de consumo dos recursos dos usuários serão disponibilizadas pelo service desk até 23/01/2026
Indicadores de sucesso das instituições
Detentoras
Item
Indicador
Detalhe do requisito
Obrigatoriedade
Implementação de jornada adequada
Atendimento de requisitos mínimos
Área de gestão (com edição de limites)
Exclusivo para marcas detentoras do grupo de controle
Comportamento funcional e de segurança
Execução com sucesso dos testes na FVP Manual
Sucesso em todos os testes de jornada sem redirecionamento para todos os servidores de autorização (PF e PJ, quando aplicável)
11 módulos de Vínculo + Pagamentos imediatos
5 módulos de Vínculo + Pagamento (Pix Automático)
Todas as detentoras de conta
•Instituições que já tenham participado do piloto de JSR estão dispensada da execução de testes de vínculo + pagamentos imediatos (PF)
Integração com ferramentas
% pareamento de chamadas
>= 95% PAIRED
Todas as detentoras de conta
Envio de
additionalinfos
Envio de 100% de
additionalInfos
Engajamento
Liquidação de pagamentos
Realização de pagamentos liquidados a partir do vínculo de dispositivo com 10 ITPs ou o máximo de ITPs que ofertar o produto
Todas as detentoras de conta
100 pagamentos, com pelo menos 30 pagamentos agendados e 15 pagamentos PJ
100 pagamentos (Pix automático), com pelo menos 30 first payments, 70 recurring payments e 15 pagamentos PJ
Comportamento bilateral
Tickets bilaterais abertos
Sem tickets bilaterais aberto no final do processo
Todas as detentoras de conta
ITPs
Item
Indicador
Pagamentos imediatos e agendados
Pix automático
Implementação de jornada adequada
Atendimento de requisitos mínimos
Vínculo e Pagamento + Área de gestão
Mobile e/ou desktop
Vínculo e Pagamento (Pix automático) + Área de gestão
Mobile e/ou desktop
O vínculo com a empresa recebedora (CNPJ recebedor) é de total responsabilidade da instituição iniciadora de pagamento. Será permitida, de forma voluntária, a utilização do CNPJ de um cliente da iniciadora de pagamentos que não tenha contrato firmado para o produto de Pix Automático. O uso deve ser restrito a testes e não pode envolver a contratação do produto “real”.
Integração com ferramentas
% pareamento de chamadas
>= 95% PAIRED
Envio de
additionalinfos
Envio de 100% de
additionalInfos
Engajamento
Liquidação de pagamentos
Realização de pagamentos liquidados com 20 detentoras, sendo pelo menos 50% das instituições pertencentes aos conglomerados do grupo de controle¹
100 pagamentos, com pelo menos 30 pagamentos agendados e 15 pagamentos PJ (se a instituição ofertar este serviço)
100 pagamentos (Pix automáticos), com pelo menos 30 first payments, 70 recurring payments e 15 pagamentos PJ
Comportamento bilateral
Tickets bilaterais abertos
Sem tickets bilaterais aberto no final do processo
1Banco Bradesco S.A., Banco BTG Pactual S.A., Banco C6 S.A., Banco Digio S.A., Banco do Brasil S.A., Banco Inter S.A.., Banco Pan S.A., Banco Santander (Brasil) S.A., Banco Votorantim, Banco XP S.A., Caixa Econômica Federal, CloudWalk, Sicredi, Sicoob, Itaú Unibanco S.A., Mercado Pago, Neon Pagamentos S.A., Nu Pagamentos S.A., PagSeguro, PicPay
Volumetria de testes de engajamento bilateral por produto e obrigatoriedade de participação
Novos entrantes
Já opera
Volumetria
Diversidade
Volumetria
Diversidade
Pagamentos imediatos e agendados
100
pagamentos:
•30 agendados
•15 PJ
8 ITPs
45
pagamentos:
•30 agendados
•15 PJ
3 ITPs
Pix automático
100
pagamentos:
•30 first payments
•70 recurring payments
•15 PJ
3 ITPs
100
pagamentos:
•30 first payments
•70 recurring payments
•15 PJ
3 ITPs
Relação de ITPs participantes
Pagamentos imediatos e agendados
Pix Automático
Canal ofertado
(Pagamentos imediatos)
Canal ofertado
(Pix Automático)
Instituição
PF-Mobile
PJ
Desktop
PF
PJ
Mobile
Desktop
BANCO BTG PACTUAL
ITP Homologada
X
X
https://developer.btgpactual.com/login
Belvo IP
ITP Homologada
X
https://jsr.belvo.com
CUMBUCA IP
ITP Homologada
X
X
X
X
X
X
https://web.cumbuca.com
Iniciador IP
ITP Homologada
X
X
X
X
X
X
https://app.iniciador.com.br/jsr/login
https://app.iniciador.com.br/automatic
LINA IP
ITP Homologada
X
X
X
X
X
X
https://doacao.linaopenx.com.br/
https://doacao.linaopenx.com.br/piloto-pix-automatico
MUEVY IP
ITP Homologada
X
X
X
X
X
https://app.openfinance.muevy.com.br/jsr
https://app.openfinance.muevy.com.br/automatic
PLUGGY
X
X
X
X
X
https://app.of.pluggy.ai/jsr
https://app.of.pluggy.ai/automatic
Relação de ITPs Homologadas (Pagamentos-PF-Mobile)
As instituições abaixo já obtiveram autorização para disponibilizar a jornada sem redirecionamento para pagamentos imediatos, pessoa física em ambiente mobile. Embora não sejam participantes deste Piloto, suas soluções poderão ser utilizadas pelos detentores para atingimento dos testes bilaterais:
ADYEN
BANCO BRADESCO
BANCO RIBEIRAO PRETO
CELCOIN
DLOCAL BRASIL IP
EFI S.A. - IP
GOOGLE PAY
OKTO IP
Cronograma do piloto
Open
Certificação FIDO
Instituições detentoras de conta deverão registrar a certificação FIDO no seu servidor de autorização no momento de publicação da API Vínculo de Dispositivo no tipo de perfil ‘Others’ e variante ‘FIDO’.
Se for feita uma certificação própria utilizar a URL
https://fidoalliance.org/certification/fido-certified-products/
Se utilizar um servidor de terceiro certificado utilizar URL para o site do produto utilizado (página do AS utilizado)
Painel Integrado de acompanhamento de indicadores
Para o devido acompanhamento das métricas e indicadores de Portabilidade de Crédito, foi-se construído o
Painel de Jornada sem redirecionamento
. Nele, poderão ser encontradas as métricas de acompanhamentos da PCM, pagamentos liquidados, acompanhamento funcional da FVP, dentre outros;
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
Acompanhamento com as instituições
Para melhor apoiar as instituições participantes do Piloto de Jornada sem redirecionamento a Associação acompanhará e apoiará as instituições durante todo o período do Piloto através de:
Agendas semanais
: Toda sexta-feira, das 15h às 16h, de 13/02/26 a 22/05/26
Para compartilhamento de informações relevantes, e esclarecimento de dúvidas com a Associação ou bilaterais com demais instituições
Grupo do
Whatsapp
: Para dúvidas pontuais e interações com outras instituições ou Associação
Clique aqui
para acessar o Grupo do
Whatsapp
do Piloto de JSR 2.2.0, ou escaneie o QR Abaixo com a câmera de seu celular:
Open
Outros links úteis
Orientações para execução dos testes da FVP Manual:
Link aqui
Painel de consulta de contas abertas
Workshop do Piloto de Jornada sem redirecionamento - 23/01/2026
Material do Workshop:
Formulário de validação simplificada da jornada de experiência do usuário:

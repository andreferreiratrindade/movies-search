---
                            title: "Informações Gerais - [SV] Vínculo de dispositivo - v2.2.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1436516369_Informa+es+Gerais+-+SV+V+nculo+de+dispositivo+-+v2.2.0"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1436516369/Informa+es+Gerais+-+SV+V+nculo+de+dispositivo+-+v2.2.0"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Informações Gerais - [SV] Vínculo de dispositivo - v2.2.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Conteúdo comum entre os produtos
2
Informações Iniciais
3
Introdução sobre FIDO
4
Visão Geral
Conteúdo comum entre os produtos
Para o entendimento correto do produto você deve levar em consideração as informações presentes na página
[SV] Iniciação de Pagamentos - Conteúdo comum entre os produtos
.
Informações Iniciais
O serviço de iniciação de pagamentos sem redirecionamento (ou Jornada Sem Redirecionamento) é aquele em que o cliente inicia e conclui a solicitação de transação sem sair do ambiente da ITP – ou seja, sem ser redirecionado ao ambiente da detentora de conta.
O desenvolvimento da Jornada Sem Redirecionamento foi sugerido pelo Banco Central do Brasil com o objetivo de melhorar a experiência do usuário, preservando a segurança de pagamento e ser uma alternativa à jornada de iniciação de pagamento com redirecionamento.
Para habilitar a Jornada Sem Redirecionamento, o BCB delineou as seguintes Diretrizes:
O processo deve ser constituído de duas etapas: (i) Vínculo de Conta e (ii) Pagamento;
Vínculo de conta:
Processo em que o cliente vincula sua conta a ITP, com autenticação usual no detentor de contas;
Pagamento:
Processo em que o cliente solicita a iniciação de pagamento, onde é autenticado no próprio ITP e não é redirecionado ao ambiente da detentora de conta.
Instituição detentora de conta permanece responsável pela autenticação do cliente;
Processo de autenticação do cliente delegado pela detentora de conta a ITP;
Relação da detentora com ITP deve ser regida pela regulação de segurança cibernética e contratação de serviços de processamento e armazenamento de dados.
Contrato é necessário em função da terceirização parcial da autenticação;
BCB poderá disciplinar os requisitos mínimos do respectivo contrato
baseline
com objetivo de preservar os objetivos do Open Finance;
O modelo deve ser padronizado e aberto, e a Estrutura de Governança deve definir as especificações e o protocolo de segurança a ser adotado como padrão pelos participantes.
Por último, a Estrutura de Governança responsável pelo desenvolvimento da Jornada Sem Redirecionamento elegeu o FIDO2 como padrão de segurança que irá habilitar o serviço de acordo com as Diretrizes do Banco Central do Brasil.
Introdução sobre FIDO
FIDO (
Fast Identity Online
) é uma tecnologia desenvolvida pela FIDO Alliance (
http://fidoalliance.org
) com o objetivo de facilitar, agilizar e tornar mais seguro o processo de autenticação de usuários em plataformas digitais. FIDO permite que os usuários façam login com chaves de acesso (i.e.: chave biométrica ou chave de segurança) em seus dispositivos.
Ao longo dos últimos anos, a FIDO Alliance lançou especificações abertas como UAF, U2F, FIDO2 e CTAP2. Para fins de Jornada Sem Redirecionamento, a Estrutura de Governança elegeu o FIDO2 como protocolo aderente aos seus propósitos.
FIDO2 foi um projeto entre a FIDO Alliance e a World Wide Web Consortium (W3C) que teve como principal objetivo estabelecer um padrão de forte autenticação para o ambiente web.
De acordo com a FIDO Alliance, os benefícios do FIDO2 são:
Segurança:
as credenciais de login criptográficas FIDO2 são exclusivas em cada site, nunca saem do dispositivo do usuário e nunca são armazenadas em um servidor. Este modelo de segurança elimina os riscos de
phishing
, todas as formas de roubo de senhas e ataques de repetição;
Conveniência:
os usuários desbloqueiam credenciais de login
criptográficas com métodos integrados simples, como leitores de impressão digital ou câmeras em seus dispositivos, ou aproveitando chaves de segurança FIDO fáceis de usar. Os consumidores podem selecionar o dispositivo que melhor atende às suas necessidades;
Privacidade:
Como as chaves criptográficas FIDO são exclusivas para cada site da Internet, elas não podem ser usadas para rastrear usuários entre sites. Além disso, os dados biométricos, quando usados, nunca saem do dispositivo do usuário;
Escalabilidade:
Os sites podem ativar o FIDO2 por meio de uma simples chamada de API JavaScript que é compatível com os principais navegadores e plataformas em bilhões de dispositivos que os consumidores usam todos os dias.
Visão Geral
A Estrutura de Governança responsável pelo desenvolvimento da Jornada Sem Redirecionamento definiu que essa deverá utilizar:
Endpoints
para a etapa de vinculação de conta para a Jornada sem Redirecionamento;
Utilizar os
endpoints
da versão vigente da API de Iniciação de Pagamentos, sem alterações na etapa de iniciação de pagamento para a jornada sem redirecionamento.
Deste modo, todas as informações abaixo, também definidas para o serviço de iniciação de pagamentos com redirecionamento, se aplicam à jornada sem redirecionamento:
Idempotência - v4.0.0 - [SV] Pagamentos
Recomendação Uso de Polling e Controle de Acesso - v4.0.0 - [SV] Pagamentos
Como Assinar o Payload - v4.0.0 - [SV] Pagamentos
Assinatura de Mensagem vs Idempotência - v4.0.0 - [SV] Pagamentos
Validação de informações no DICT - v4.0.0 - [SV] Pagamentos
Convenções de formatação e fuso horário de campos de data e hora - v4.0.0 - [SV] Pagamentos

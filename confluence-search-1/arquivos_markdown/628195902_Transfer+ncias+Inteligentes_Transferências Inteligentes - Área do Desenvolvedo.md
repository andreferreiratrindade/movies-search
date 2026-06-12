---
                            title: "Transferências Inteligentes - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "628195902_Transfer+ncias+Inteligentes"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/628195902/Transfer+ncias+Inteligentes"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Transferências Inteligentes - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1 - Introdução
Bem-vindo ao guia de Transferências Inteligentes, exploraremos essas funcionalidades no cenário do Open Finance Brasil. Este guia destina-se a oferecer uma compreensão aprofundada da ferramenta, delineando como é a implementação no contexto do Open Finance Brasil e como pode transformar a maneira como usuários lidam com suas finanças.
Transferências Inteligentes:
No universo do Open Finance Brasil, a funcionalidade de Transferências Inteligentes destaca-se como uma abordagem estratégica para a gestão inteligente de saldos em contas relacionadas. Seja para consumidores pessoa naturais ou jurídicas, essa API é de implementação obrigatório para os detentores de conta, oferecendo ao ecossistema uma solução que permita a transferência automática de fundos.
O produto está presente na API de pagamentos automáticos, a partir de sua versão 1.0.0. O link para a API pode ser encontrado abaixo.
Pagamentos automáticos
2 - Regras de negócios para
Transferências Inteligentes
Transferências Inteligentes
Transferências Inteligentes
Casos de uso
(Sugestões BC)
Transferências Inteligentes e similares (investimentos inteligentes, proteção contra uso desnecessário de cheque especial)
Configurações de recorrência
Motor de recorrência
Criação de um consentimento para recorrência com limites de quantidade, valores e prazos
Valor
Fixo ou variável
Modelo de recorrência, intervalos de pagamentos
Restrito aos limites definidos no consentimento
Gestão da Agenda
Iniciador
Comanda o pagamento
Iniciador
Recebedor
PN ou PJ de mesma titularidade
Primeiro pagamento
Imediato
Demais pagamentos
Imediato
Permite pagamentos imediatos
Sim
Definição do final do período da recorrência
Opcional
Prazo máximo de duração para recorrência do consentimento
Opcional
Permite a configurar data de início do consentimento?
Sim
Permite a configurar data de expiração do consentimento?
Sim
Permite limites globais do consentimento?¹
Não
Permite limites periódicos por consentimento?
Sim
Permite limites por transação?
Sim
Processo de adesão
Fluxo de adesão
Consentimento FAPI
long-lived tokens
Role
no diretório
CONTA, PAGTO
Será possível editar configurações de recorrência no processo de adesão no Detentor?
Não
Cancelamento do fluxo da adesão
Via Iniciador ou Detentor
Permite múltiplas alçadas?
Sim
Iniciador terá acesso aos status do processo de adesão via Webhook?
Sim
Adesão tem id de contrato?
Não
Gestão de adesão
Permite edição técnica dos dados do consentimento pós adesão²?
Não
Cancelamento da recorrência
Pelo pagador, no ambiente da iniciadora ou detentora
Revogação da recorrência
Iniciador ou Detentor poderão revogar a adesão por motivos de fraude
Consumação³ da recorrência?
Detentor
Processo de liquidação
Canal para liquidação
Primário
(Seguir a utilização e regras do arranjo)
Dispara o pagamento⁴
Iniciador
Onde o cliente cancela o pagamento?
Não é possível
Erros de saldo insuficiente modificam o status do consentimento?
Não
Listagem das informações do pagamento
Busca por id do consentimento
Iniciador é responsável pelo envio da ocorrência do pagamento?
Sim, imediatamente
Quem avisa o pagador sobre pagamento com falha?
Iniciador
Responsável pela geração do endToEndId
Iniciador
A data agendada no consentimento e a data agendada do E2EID podem ser distintas?
Sim
Qual é o localInstrument utilizado na liquidação?
DICT, INIC e MANU
Outras informações
É possível habilitar crédito?
Sim - Conteúdo explicativo no header da API de pagamentos
Retentativas
Não
Funcionalidade de contestação
MED
Legenda
1 - Limite específico para um determinado consentimento, por exemplo, limite de R$100 por dia (periódico) ou R$300 para o intervalo do consentimento (global)
2 - O GT questionou o BC sobre o comportamento esperado quando houver a edição –se o usuário deverá ser redirecionado para a detentora ou não para confirmar os novos dados do consentimento
3 - Entende-se como consumação a mudança do estado, por exemplo, após 10/10 parcelas o estado será alterado de aprovado para consumido
4 - Responsável por garantir que no momento do agendamento a liquidação ocorra
3 - Descrição da usabilidade para
Transferências Inteligentes
3.1- Jornada de autorização
Diferente dos pagamentos realizados via agendamento recorrente ou pagamentos imediatos,  as Transferências Inteligentes possuem consentimentos de longa duração. Entraremos mais no detalhe do processo de consentimento a seguir.
3.1.1 - Jornada 1 - Autorização de consentimento
Open
BPMN: Jornada de autorização de consentimentos para Transferências Inteligentes
ID
CAMADA
TIPO
DESCRIÇÃO
ID
CAMADA
TIPO
DESCRIÇÃO
1
Pagador
Ação
No app do iniciador, seleciona as transferências inteligentes
2
Pagador
Ação
Informa a conta de débito que utilizará para as movimentações
3
Pagador
Comunicação
APP do iniciador envia os dados inseridos para o backend do iniciador
4
Iniciador
Comunicação
Recebe as informações inseridas no seu backend
5
Iniciador
Ação
Processa as informações recebidas
6
Iniciador
Ação
Prepara a solicitação para criação de consentimento no PSP Pagador selecionada pelo pagador
7
Iniciador
Comunicação
Envia a solicitação de consentimento para o PSP Pagador
8
PSP Pagador
Comunicação
Recebe a solicitação de um novo consentimento
9
PSP Pagador
Ação
Processa a solicitação de novo consentimento
10
PSP Pagador
Comunicação
Informa ao iniciador o sucesso na criação do consentimento
11
Iniciador
Comunicação
Recebe a resposta de sucesso na criação do consentimento
12
Iniciador
Ação
Prepara o redirecionamento do Pagador para o autenticação e autorização no ambiente do PSP Pagador
13
Iniciador
Comunicação
Redireciona o Pagador para autenticação e autorização
14
Pagador
Ação
Realiza a autenticação na instituição detentora
15
Pagador
Ação
Autoriza o consentimento. Nesta etapa, o Pagador pode selecionar uma conta de débito diferente da informada pelo ITP, basta que ele seja o titular da conta de débito no PSP Pagador.
16
PSP Pagador
Ação
Muda o estado do consentimento para AUTHORISED, conforme manifestado pelo Pagador.
17
PSP Pagador
Ação
Recolhe as confirmações ou rejeições de todos os aprovadores registrados para a conta
18
PSP Pagador
Comunicação
Redireciona o Pagador de volta ao ambiente do Iniciador
19
Iniciador
Comunicação
Recebe o Pagador de volta no seu aplicativo.
20
Iniciador
Ação
Valida os dados recebidos no redirecionamento
21
Iniciador
Ação
Loop para consulta do estado do consentimento até que o mesmo esteja em AUTHORISED
22
Iniciador
Comunicação
Notifica ao Pagador que o consentimento foi criado com sucesso e pode ser utilizado.
23
Pagador
Comunicação
Recebe notificação sobre o consentimento criado com sucesso e pode ser utilizado.
3.1.3 - Sobre rejeição e revogação de consentimentos de longa duração.
Tratando agora dos motivos de revogação, a regra é que para um consentimento de longa duração ser revogado, primeiro ele precisou ser aprovado. Apenas consentimentos no status “AUTHORISED” são passíveis de revogação, vamos trazer os motivos de revogação e como eles se aplicam.
REVOGADO_RECEBEDOR: Não se aplica ao produto Transferências inteligentes. Nesse produto, o recebedor e o pagador são de mesma titularidade, portanto, sempre que revogado, será revogado pelo usuário.
REVOGADO_USUARIO:  Indica que o usuário pagador, via ambiente do iniciador ou detentor, solicitou a revogação do consentimento de longa duração.
NAO_INFORMADO: Deve ser utilizado para motivos de revogação que envolvam informações que não devem ser compartilhadas no ecossistema por respeito a privacidade do usuário. Ex: Suspeita de Fraude, Bloqueio Judicial.
3.2 - Processo de pagamento
3.2.1 - Fluxo para criação de um pagamento para Transferências Inteligentes
Open
BPMN: Fluxo para criação de uma solicitação de transferência
ID
CAMADA
TIPO
DESCRIÇÃO
ID
CAMADA
TIPO
DESCRIÇÃO
1
Iniciador
Ação
Dispara processo de transferência
2
Iniciador
Ação
Busca informações de contas de usuário habilitadas por ele para realização da transferência
3
Iniciador
Ação
Analisa as regras definidas pelo usuário pagador no momento da criação do consentimento de longa duração
4
Iniciador
Comunicação
Envia solicitação de access_token
5
PSP Pagador
Comunicação
Recebe solicitação de access_token
6
PSP Pagador
Ação
Processa solicitação de access_token
7
PSP Pagador
Comunicação
Retorna access_token
8
Iniciador
Comunicação
Recebe access_token
9
Iniciador
Ação
Processa retorno da solicitação de access_token
10
Iniciador
Ação
Cria solicitação de transferência
11
Iniciador
Comunicação
Envia a solicitação de transferência
12
PSP Pagador
Comunicação
Recebe solicitação de transferência
13
PSP Pagador
Ação
Processa solicitação de transferência
14
PSP Pagador
Ação
Realiza a transferência de fundo
15
PSP Pagador
Comunicação
Retorna sucesso na solicitação de transferência
16
Iniciador
Comunicação
Recebe sucesso na transferência
17
Iniciador
Ação
Processa o retorno da transferência
18
Iniciador
Ação
Consulta informações da transferência
19
Iniciador
Comunicação
Notifica usuário contratante do sucesso na transferência
20
Usuário contratante
Comunicação
Recebe notificação de sucesso na transferência

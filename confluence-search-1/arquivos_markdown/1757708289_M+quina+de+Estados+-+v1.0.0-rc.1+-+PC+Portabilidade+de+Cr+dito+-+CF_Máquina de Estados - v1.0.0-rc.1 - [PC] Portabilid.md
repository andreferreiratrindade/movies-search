---
                            title: "Máquina de Estados - v1.0.0-rc.1 - [PC] Portabilidade de Crédito - CF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1757708289_M+quina+de+Estados+-+v1.0.0-rc.1+-+PC+Portabilidade+de+Cr+dito+-+CF"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1757708289/M+quina+de+Estados+-+v1.0.0-rc.1+-+PC+Portabilidade+de+Cr+dito+-+CF"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Máquina de Estados - v1.0.0-rc.1 - [PC] Portabilidade de Crédito - CF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Open
Estados da Portabilidade de Crédito Consignado Federal
*A atualização da máquina de estado é de responsabilidade da credora, por ser a detentora dos contratos.
RECEIVED
Estado inicial da portabilidade de crédito.
Este estado indica que o pedido de portabilidade foi recebido pela instituição credora. O pedido permanece neste estado até o início do próximo dia útil e deverá ser movido automaticamente para o estado
PENDING
.
Isso significa que:
Caso o pedido seja registrado em qualquer horário de um dia útil (ex.: 14:00), ele permanecerá no estado
RECEIVED
até 00:00. Somente a partir desse momento a máquina de estados será atualizada automaticamente para
PENDING
, em um processo de responsabilidade da instituição credora, iniciando-se assim a próxima etapa do processo.
Caso o cliente solicite o cancelamento do pedido de portabilidade no canal digital da instituição proponente ou da instituição credora, a portabilidade deverá ser movida para o estado
CANCELLED
. No caso de solicitação realizada no canal da instituição proponente, essa informação deverá ser previamente comunicada à instituição credora.
PENDING
Indica que o pedido de portabilidade está na fase de contraproposta pela instituição credora.
Nesta etapa, a instituição credora possui prazo máximo de
3 dias úteis
, contados a partir do momento em que a máquina entra nesse estado.
Atualizações na máquina de estados feitas após as
10:00 horas
de cada dia serão processadas apenas no próximo dia útil.
A contraproposta pode ser apresentada ao cliente por qualquer canal de comunicação (telefone, e-mail, aplicativo etc.). Porém, o aceite da contraproposta será considerado válido somente se realizado no canal digital da instituição credora.
Possíveis desfechos do estado PENDING
Cliente aceita a contraproposta
Caso o cliente aceite a contraproposta até as
09:00 horas do terceiro dia útil
, no canal digital da instituição credora, o pedido de portabilidade deverá ser movido para o estado
REJECTED
.
Cliente solicita o cancelamento via credora
O cliente poderá solicitar o cancelamento do pedido de portabilidade por meio do canal digital da instituição credora, enquanto a solicitação estiver no estado PENDING. Caso essa solicitação seja realizada nessa condição, o pedido de portabilidade deverá ser alterado para o estado CANCELLED.
Cliente solicita o cancelamento via proponente
O cliente poderá solicitar o cancelamento do pedido de portabilidade por meio do canal digital da instituição proponente. Caso a solicitação ocorra nesse estado, a informação deverá ser devidamente comunicada à instituição credora.
Expiração do prazo de contraproposta
Caso nenhuma ação seja realizada pela instituição credora até as
10:00 horas do terceiro dia útil
, a máquina de estados deverá ser atualizada para o estado
ACCEPTED_SETTLEMENT_IN_PROGRESS
.
A instituição credora poderá, a seu critério, ofertar uma contraproposta e/ou antecipar o processo de atualização da máquina de estados.
Caso a instituição opte por antecipar a atualização da máquina de estados para
ACCEPTED_SETTLEMENT_IN_PROGRESS
, a alteração deverá ocorrer até
10:00 de cada dia útil
. Alterações realizadas após esse horário somente produzirão efeito no próximo dia útil.
ACCEPTED_SETTLEMENT_IN_PROGRESS
Indica que a contraproposta não foi aceita pelo cliente ou que a instituição credora não apresentou contraproposta dentro do prazo estabelecido.
Nesta etapa, a instituição proponente deverá realizar a liquidação do contrato
no mesmo dia
em que o pedido entrar neste estado, desde que se trate de dia útil, conforme o calendário bancário.
Após realizar a liquidação do contrato via
STR0052
, recomenda-se que a proponente comunique a liquidação à instituição credora via
API padronizada
.
A máquina de estados será atualizada para
ACCEPTED_SETTLEMENT_COMPLETED no próximo dia útil
.
Caso a instituição proponente não realize a liquidação do contrato, a instituição credora deve atualizar a máquina de estados, no próximo dia útil, para
REJECTED
, informando o motivo
PORTABILIDADE_CANCELADA_POR_FALTA_DE_LIQUIDACAO
.
Nesta etapa o cliente pode solicitar o cancelamento do pedido de portabilidade somente no canal digital da instituição proponente e desde que o contrato ainda não tenha sido liquidado. É de dever da instituição proponente, informar o cancelamento a instituição credora.
ACCEPTED_SETTLEMENT_COMPLETED
Indica que a instituição proponente realizou a liquidação do contrato e comunicou a operação à instituição credora.
A partir da entrada neste estado, inicia-se o prazo máximo de
2 dias úteis
para conclusão total do processo de portabilidade. Para garantir previsibilidade operacional e evitar atrasos no processo de liquidação, devem ser respeitadas as regras abaixo:
A instituição credora deverá realizar a validação inicial da liquidação
no mesmo dia útil em que o pedido entrou neste estado
, até as
10:00 horas
.
Em caso de inconsistências, o pedido deverá ser movido imediatamente para o estado
PAYMENT_ISSUE
.
Caso a liquidação esteja correta, a credora deverá mover o pedido para
AWAITING_CONTRACT_DISCHARGE
.
Importante:
A transição para
PAYMENT_ISSUE
não interrompe nem reinicia o prazo de
2 dias úteis
para conclusão do processo.
PAYMENT_ISSUE
Indica que a instituição credora identificou inconsistências e deverá estornar o pagamento via
STR0010
, informando o motivo
DIVERGENCIA_DE_PAGAMENTO_EFETUADO
.
A instituição proponente deverá realizar os ajustes necessários
no mesmo dia útil em que for informada da divergência
.
Caso a instituição proponente realize o ajuste dentro do prazo estabelecido e a instituição credora reconheça a regularização da liquidação, o pedido deverá ser movido para
ACCEPTED_SETTLEMENT_COMPLETED
, para que a etapa de validação seja refeita.
Caso a instituição proponente não realize os ajustes necessários, a instituição credora deverá rejeitar o pedido de portabilidade, movendo o estado para
REJECTED
, informando o motivo
DECURSO_DO_PRAZO_PARA_PAGAMENTO
.
AWAITING_CONTRACT_DISCHARGE
Indica que a instituição credora finalizou a portabilidade de crédito, fornecendo as informações referentes à quitação do contrato original. Contudo, permanece pendente a solicitação de
desaverbação junto à averbadora
do contrato consignado, para transferência da margem consignada.
Caso a instituição credora consiga realizar a desaverbação dentro do prazo (segundo a autorregulação de
2 dias úteis
, contados a partir da etapa anterior de confirmação do recebimento), deverá mover o pedido de portabilidade para o estado
PORTABILITY_COMPLETED
.
Caso a instituição credora não consiga realizar a desaverbação no prazo de
10 dias corridos
, contados a partir do envio da
STR0052
(realizada para liquidar a operação de crédito), deverá restituir o valor por meio da
STR0010 (motivo 85)
. Em seguida, deverá mover o pedido para o estado
REJECTED
, com o motivo
DESAVERBACAO_NAO_REALIZADA
.
PORTABILITY_COMPLETED
Indica que o pedido de portabilidade foi concluído com sucesso.
Isso significa que:
A instituição credora confirmou a quitação do contrato.
O processo de portabilidade foi finalizado.
A partir dessa etapa, o contrato da IF Proponente deverá ser efetivado
.
CANCELLED
Indica que o pedido de portabilidade foi cancelado pelo cliente.
O cliente pode solicitar o cancelamento do pedido de portabilidade no canal digital da instituição credora enquanto estiver no estado
PENDING
e caso isso aconteça a portabilidade deverá ser movida para o estado
CANCELLED
.
Caso o cliente solicite o cancelamento do pedido de portabilidade no canal digital da instituição proponente, no estado
ACCEPTED_SETTLEMENT_IN_PROGRESS
e
antes da quitação do contrato
, essa informação deverá ser previamente comunicada à instituição credora e a portabilidade deverá ser movida para o estado
CANCELLED
.
REJECTED
Indica que o pedido de portabilidade foi rejeitado.
Isso pode ocorrer, entre outros motivos, nas seguintes situações:
O cliente aceitou a contraproposta da instituição credora.
A instituição proponente recusou a liquidação quando o valor atualizado do contrato ultrapassou
15% do valor originalmente informado
.
As inconsistências registradas no estado
PAYMENT_ISSUE
não foram resolvidas dentro do prazo estabelecido.
Mapeamento por motivo de rejeição:
Máquina de Estados
data.status
Motivo da Rejeição
data.statusReason.reasonType
data.rejection.reason.type
Responsável pela solicitação da rejeição
data.rejection.rejectedBy
Máquina de Estados
data.status
Motivo da Rejeição
data.statusReason.reasonType
data.rejection.reason.type
Responsável pela solicitação da rejeição
data.rejection.rejectedBy
REJECTED
POLITICA_DE_CREDITO
PROPONENTE
RETENCAO_DO_CLIENTE
CREDORA
CONTRATO_JA_LIQUIDADO
CREDORA
SALDO_DEVEDOR_ATUALIZADO_SUBSTANCIALMENTE_DIVERGENTE
PROPONENTE
DECURSO_DO_PRAZO_PARA_PAGAMENTO
CREDORA
PORTABILIDADE_CANCELADA_POR_FALTA_DE_LIQUIDACAO
CREDORA
PORTABILIDADE_EM_ANDAMENTO
CREDORA
MODALIDADE_DA_OPERACAO_INCOMPATIVEL
CREDORA
CLIENTE_COM_ACAO_JUDICIAL
CREDORA
RESERVA_MARGEM
CREDORA
OUTROS
CREDORA, PROPONENTE
AWAITING_CONTRACT_DISCHARGE
DESAVERBACAO_NAO_REALIZADA
CREDORA
CANCELLED
CANCELADO_PELO_CLIENTE
USUARIO
PAYMENT_ISSUE
DIVERGENCIA_DE_PAGAMENTO_EFETUADO
CREDORA
OUTROS
CREDORA

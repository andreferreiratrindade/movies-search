---
                            title: "Máquina de Estados - v1.0.0-rc.1 - [PC] Portabilidade de Crédito - CPC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1040547891_M+quina+de+Estados+-+v1.0.0-rc.1+-+PC+Portabilidade+de+Cr+dito+-+CPC"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1040547891/M+quina+de+Estados+-+v1.0.0-rc.1+-+PC+Portabilidade+de+Cr+dito+-+CPC"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Máquina de Estados - v1.0.0-rc.1 - [PC] Portabilidade de Crédito - CPC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            A máquina de estados para o produto Portabilidade de crédito é composta de 8 estados, listados a seguir:
RECEIVED
PENDING
ACCEPTED_SETTLEMENT_IN_PROGRESS
ACCEPTED_SETTLEMENT_COMPLETED
PORTABILITY_COMPLETED
CANCELLED
REJECTED
PAYMENT_ISSUE
Máquina de estados do produto Portabilidade de Crédito
Open
Descrição dos estados da Portabilidade de crédito:
RECEIVED
Estado inicial. Indica que o pedido de portabilidade foi solicitado junto à instituição credora. O pedido deve permanecer neste estado até o próximo dia útil (D+1), quando começará a contar o prazo de 3 dias úteis para a etapa de contraproposta. Nesse momento, o pedido de portabilidade deverá ser movido para o estado PENDING. Caso o cliente cancele o pedido de portabilidade no canal digital da proponente, e a mesma comunique à instituição credora, a portabilidade de crédito deverá ser movida para o estado CANCELLED.
PENDING
Indica que o pedido de portabilidade de crédito está na fase de contraproposta, durante a qual a instituição credora pode enviar uma contraproposta ao cliente por qualquer canal (e-mail, telefone, etc.). Contudo, o aceite será válido apenas se o cliente aprovar a contraproposta no canal digital da instituição credora.
Caso a contraproposta não seja aceita no canal digital da credora e transcorrido 3 dias úteis OU a contraproposta não seja aceita pelo cliente, a portabilidade de crédito deve ser movida para ACCEPTED_STTLEMENT_IN_PROCESS
Caso a credora não tenha ou não queira fazer uma contraproposta, ela poderá mover a portabilidade para o status ACCEPTED_SETTLEMENT_IN_PROGRESS antes do término dos 3 dias úteis. Essa atualização de status deve obrigatoriamente ser atualizada em dia útil, até às 10h da manhã.
Caso a contraproposta seja aceita pelo cliente no canal digital da credora, a portabilidade de crédito deve ser movida para REJECTED.
Caso o cliente cancele o pedido de portabilidade no canal digital da proponente e a mesma comunicar o cancelamento à instituição credora, a portabilidade de crédito deverá ser movida para CANCELLED.
ACCEPTED_SETTLEMENT_IN_PROGRESS
Indica que a contraproposta não foi aceita pelo cliente e a instituição proponente deverá quitar o valor do contrato no mesmo dia em que o estado foi ativado.
Quando a proponente realizar a liquidação do contrato de empréstimo do cliente, ela deverá comunicar a respeito do fato à credora, que poderá atualizar o estado atual da portabilidade para ACCEPTED_STTLEMENT_COMPLETED.
Caso o valor atualizado do contrato para quitação ultrapasse (suba) mais do que 15% do valor original, a instituição proponente poderá cancelar a portabilidade, comunicando a credora, que atualizará o estado atual da portabilidade para REJECTED.
Caso o cliente cancele o pedido de portabilidade no canal digital da proponente, e esta comunicar o fato à instituição credora, a portabilidade de crédito deverá ser movida para CANCELLED.
ACCEPTED_SETTLEMENT_COMPLETED
Indica que a instituição proponente já liquidou o contrato e comunicou à credora, que está validando os dados do contrato, bem como os valores recebidos para a quitação do mesmo. Nesta etapa, a instituição credora tem 2 dias úteis para fornecer a confirmação e o recibo de quitação do contrato de empréstimo. Quando a credora reconhecer a quitação do contrato, ela deverá fornecer o recibo de quitação e mover a portabilidade para o estado PORTABILITY_COMPLETED.
PAYMENT_ISSUE
Indica que a Instituição Credora encontrou alguma inconsistência na liquidação efetuada e que a Instituição Proponente deverá realizar ajustes conforme sugerido pela Instituição Credora para solucionar a pendencia antes do cancelamento do pedido de portabilidade de crédito.
Caso a Instituição Proponente resolva as pendencias encontradas, o pedido de portabilidade poderá seguir e quando a credora reconhecer a quitação do contrato ela deverá fornecer o recibo de quitação e mover a portabilidade para o estado PORTABILITY_COMPLETED
Caso a Instituição Proponente não resolva a pendência no prazo a instituição credora deverá mover o estado para REJECTED e, se aplicável, devolver o valor recebido para a origem do pagamento
OBS.: Lembrando que todo o processo, a partir do estado ACCEPTED_SETTLEMENT_COMPLETED até sua conclusão, deve ocorrer em até 2 dias úteis.
PORTABILITY_COMPLETED
Indica que o pedido de portabilidade foi concluído com sucesso.
CANCELLED
Indica que o cliente cancelou o pedido de portabilidade de crédito antes de a instituição credora informar que a operação não foi retida ou de a instituição proponente realizar a liquidação da operação.
REJECTED
Indica que o pedido de portabilidade foi rejeitado, seja porque o cliente aceitou a contraproposta ou porque a proponente rejeitou a liquidação que excedeu em 15% o valor do contrato original, entre outras possibilidades.
OBS.: São considerados dias úteis apenas os dias de segunda a sexta-feira, exceto feriados nacionais
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
OUTROS
CREDORA, PROPONENTE
CANCELLED
CANCELADO_PELO_CLIENTE
USUARIO
PAYMENT_ISSUE
DIVERGENCIA_DE_PAGAMENTO_EFETUADO
CREDORA
OUTROS
CREDORA

---
                            title: "Máquina de Estados - v2.2.0 - [SV] Pagamentos Automáticos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1178042440_M+quina+de+Estados+-+v2.2.0+-+SV+Pagamentos+Autom+ticos"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1178042440/M+quina+de+Estados+-+v2.2.0+-+SV+Pagamentos+Autom+ticos"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Máquina de Estados - v2.2.0 - [SV] Pagamentos Automáticos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Consentimento
Os possíveis status do consentimento são:
AWAITING_AUTHORISATION - Aguardando autorização
PARTIALLY_ACCEPTED - Parcialmente aceito
AUTHORISED - Autorizado
REJECTED - Rejeitado
REVOKED - Revogado
CONSUMED - Consumido
Open
Algumas definições são importantes para tratar a transição dos estados do consentimento em diferentes momentos do fluxo:
AWAITING_AUTHORISATION
O consentimento é sempre criado com o status AWAITING_AUTHORISATION.
Esse prazo pode ser de até 60 minutos, ou a critério do recebedor (dentro dos 60 minutos), contados a partir da criação do consentimento
. Após aprovação assume o estado AUTHORISED (ou PARTIALLY_ACCEPTED, em casos de múltiplas alçadas de aprovação). Se nenhuma das condições forem atendidas, o consentimento deve assumir o status REJECTED, caso expire ou seja cancelado pelo usuário recebedor ou pagador antes da expiração.
Lembrando que o usuário pode cancelar o consentimento no lado da detentora de conta e por sua vez ela deve mudar o status do consentimento para REJECTED.
PARTIALLY_ACCEPTED
O status indica que o consentimento precisa da confirmação de mais autorizadores para que o processamento da transação possa prosseguir; e;
Caso o cliente defina uma data de expiração do consentimento, e esta seja menor que 30 dias (contados a partir da criação do consentimento), a autorização do consentimento não pode ultrapassar D, sendo D o dia previsto para expiração do consentimento, ou;
Caso o cliente defina uma data de expiração do consentimento, e esta seja maior que 30 dias (contados a partir da criação do consentimento), a autorização do consentimento não deve ultrapassar esses 30 dias, ou;
Caso o cliente não defina data de expiração do consentimento, o prazo máximo para expiração desse consentimento é 30 dias, contados a partir da data em que o consentimento foi criado, ou;
Prazo máximo de aprovação estipulado pelo cliente (pagador) através de seu relacionamento com a instituição detentora e informado à iniciadora através do campo /data/approvalDueDate. A data estipulada pelo cliente (pagador) não deve ultrapassar 30 dias, contados a partir da criação do consentimento;
Por fim, consentimentos não autorizados a tempo devem ser movidos para REJECTED.
AUTHORISED
Para o cenário em que o status assumiu AUTHORISED, o tempo máximo do consentimento deve assumir é "(expirationDateTime) - (startDateTime)" . Este é o tempo para consumir o consentimento autorizado, mudando seu status para CONSUMED. É possível prorrogar este tempo editando o consentimento. Caso necessário alterar um campo que não é passível de edição, a criação de um novo consentimento será necessária.
O expirationDateTime pode ser definido ou não pelo usuário, caso não seja definido, o consentimento não tem data para ser consumido. É possível que o usuário edite esse campo e defina um expirationDateTime posteriormente.
REJECTED
Em caso de consentimento expirado a Detentora deverá retornar o status REJECTED.
Em caso de consentimento rejeitado pelo usuário, pelo recebedor (Pix Automático) ou por regra de negócio da Detentora, o status deverá ser retornado como REJECTED.
REVOKED
Apenas consentimentos em AUTHORISED podem trafegar para REVOKED.
Em casos de consentimento revogado pelo usuário, pelo detentor ou pelo iniciador, o detentor deve retornar o status REVOKED.
CONSUMED
A detentora de conta deve ativamente realizar a mudança do status do consentimento de AUTHORISED para CONSUMED quando a data de expiração do consentimento for ultrapassada.
O consentimento para Transferências Inteligentes deve ser movido para CONSUMED caso o somatório dos valores transacionados igualem o valor máximo definido para o consentimento (campo "/data/recurringConfiguration/sweeping/totalAllowedAmount").
Recomendação uso de polling
A consulta via GET, para verificar o processamento da transação, pode ser efetuada a qualquer momento desde que se respeite o rate limit definido na página
Recomendação Uso de Polling e Controle de Acesso
.
Pagamento: Arranjo Pix
Os possíveis status do pagamento Pix, são:
RCVD
CANC
ACCP
ACPD
RJCT
ACSC
PDNG
SCHD
Open
Abaixo segue a descrição dos status relacionados a máquina de estados pertinente aos tipos de pagamento Pix:
RCVD (Received)
O status indica que a requisição de pagamento foi recebida com sucesso pela detentora, mas ainda há validações a serem feitas antes de ser submetida para liquidação.
CANC (Cancelled)
O status indica que a transação Pix pendente foi cancelada com sucesso pelo usuário antes que fosse confirmada (ACCP) ou rejeitada (RJCT) pela detentora.
ACCP( Accepted Customer Profile)
O status indica que todas as verificações necessárias já foram realizadas pela detentora e que a transação está pronta para ser enviada para liquidação (no SPI se for Pix para outra instituição ou internamente se for para outra conta na mesma instituição).
ACPD (Accepted Clearing Processed)
O status indica que a detentora já submeteu a transação para liquidação, mas ainda não tem a confirmação se foi liquidada ou rejeitada.
RJCT (Rejected)
O status indica que a transação foi rejeitada pela detentora ou pelo SPI.
ACSC (Accepted Settlement Completed Debtor Account)
O status indica que a transação foi efetivada pela detentora ou pelo SPI.
PDNG (Pending)
O status indica que a detentora reteve temporariamente a transação Pix para análise. Não aplicável para o produto Transferências Inteligentes.
SCHD (Scheduled)
O status indica que a transação Pix foi agendada com sucesso na detentora. Pagamentos neste estado que tiverem o consentimento revogado devem ser rejeitados com a reason CONSENTIMENTO_REVOGADO, com exceção aos pagamentos agendados para o mesmo dia em que o consentimento foi revogado, os quais devem ocorrer normalmente.

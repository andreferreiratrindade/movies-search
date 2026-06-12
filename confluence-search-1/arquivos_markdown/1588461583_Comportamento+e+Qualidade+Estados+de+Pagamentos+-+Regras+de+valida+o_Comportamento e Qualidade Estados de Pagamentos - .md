---
                            title: "Comportamento e Qualidade Estados de Pagamentos - Regras de validação - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1588461583_Comportamento+e+Qualidade+Estados+de+Pagamentos+-+Regras+de+valida+o"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1588461583/Comportamento+e+Qualidade+Estados+de+Pagamentos+-+Regras+de+valida+o"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Comportamento e Qualidade Estados de Pagamentos - Regras de validação - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.01
Objetivo desta página
Demonstrar funcionalmente as regras de validação dos pagamentos com seus respectivos estados de pagamento. Estas validações são utilizadas para aberturas de tickets e monitoramento através do dashboard de Monitoramento Operacional.
Guia de leitura
Nos endpoints, a referência “v
x
” deve ser substituída pela versão da API que está sendo enviada. Por exemplo, para a versão 4 (v4) dos endpoints de pagamento, enviar “open-banking/automatic-payments/
v
4
/recurring-consents/{recurringConsentId}”.
Nos endpoints, a referência % significa que vale para qualquer conteúdo antes ou depois, de acordo com o endpoint em questão. Por exemplo, “%/automatic-payments/v
x
/recurring-consents%” significa que vale para os endpoints “/open-banking/automatic-payments/v2/recurring-consents” e “/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}”.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Conexão entre reportes de Pagamentos e Estados de Pagamento
A conexão entre os reportes de Pagamentos e seus Estados de Pagamento se dá através da chave
serverOrgId + paymentId + clientOrgId (Pagamentos) → orgId + paymentId + clientOrgId (Estados de Pagamento)
.
Campos utilizados
Abaixo estão os campos utilizados para as validações e suas formas de identificação nos reportes de pagamentos ou estados de pagamento
Campo
Forma de identificação
Campo
Forma de identificação
paymentId
O paymentId dos reportes de pagamento é identificado dentro do additionalInfo paymentList no endpoints /payments/v
x
/pix/payments (paymentId) ou no additionalInfo recurringPaymentId no endpoint /automatic-payments/v
x
/pix/recurring-payments (recurringPaymentId).
Por ser um campo do tipo objeto, pode haver mais de um paymentId dentro do paymentList.
Tipo de pagamento (paymentType)
O tipo de pagamento em reportes de pagamento é enviado no additionalInfo paymentType
Validações
Mensagem
Regra
Mensagem
Regra
paymentId / recurringPaymentId não encontrado em estados de pagamento
O paymentId ou recurringPaymentId informado no reporte de Pagamentos não foi encontrado nos reportes de Estados de Pagamento.
paymentType infomado no Estado de Pagamento é diferente do informado no Pagamento
O tipo de pagamento do reporte de Pagamentos não pode ser diferente do informado no reporte de Estados de Pagamento.
Último estado de pagamento informado inconsistente
Dentre os status ACSC, RJCT e CANC, o último status do Pagamento não deve ser diferente do informado no Estado de Pagamento.
Não foi informado o motivo de cancelamento / rejeição
Se o pagamento tiver sido cancelado ou rejeitado, deve ser obrigatoriamente informado um motivo.
Ausência de status SCHD em Estados de Pagamento
Caso o pagamento não tenha sido rejeitado ou cancelado, deve haver obrigatoriamente um Estado de Pagamento SCHD

---
                            title: "Informações Gerais - [SV] Pagamentos Automáticos - v2.2.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1178042385_Informa+es+Gerais+-+SV+Pagamentos+Autom+ticos+-+v2.2.0"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1178042385/Informa+es+Gerais+-+SV+Pagamentos+Autom+ticos+-+v2.2.0"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Informações Gerais - [SV] Pagamentos Automáticos - v2.2.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Visão geral
2
Conteúdo comum entre os produtos
3
Criar consentimento para iniciação de pagamento
: (POST /automatic-payments/v2/recurring-consents)
3.1
Dicionário de dados
4
Consultar consentimento para iniciação de pagamento
: (GET /automatic-payments/v2/recurring-consents/{recurringConsentId})
4.1
Dicionário de dados
5
Editar, rejeitar ou revogar consentimento para iniciação de pagamento
: (PATCH /automatic-payments/v2/recurring-consents/{recurringConsentId})
5.1
Dicionário de dados
6
Pix - Criar iniciação de pagamento
: (POST /automatic-payments/v2/pix/recurring-payments)
6.1
Dicionário de dados
7
Pix - Criar nova tentativa de pagamento para Pix Automático
: (POST /automatic-payments/v2/pix/recurring-payments/{originalRecurringPaymentId}/retry)
7.1
Dicionário de dados
8
Pix - Consultar iniciação de pagamento
: (GET /automatic-payments/v2/pix/recurring-payments)
8.1
Dicionário de dados
9
Pix - Consultar iniciação de pagamento
: (GET /automatic-payments/v2/pix/recurring-payments/{recurringPaymentId})
9.1
Dicionário de dados
10
Pix - Cancelar iniciação de pagamento
: (PATCH /automatic-payments/v2/pix/recurring-payments/{recurringPaymentId})
10.1
Dicionário de dados
Visão geral
A API tem como objetivo coletar o consentimento e realizar a iniciação de pagamento entre bancos, instituições financeiras e é acessível também à estabelecimentos comerciais participantes do Open Finance Brasil.
Os recursos estão disponíveis para pagadores que possuem registro em uma instituição detentora de conta participante do Open Finance, independentemente de serem pessoa física ou jurídica.
Conteúdo comum entre os produtos
Para o entendimento correto do produto você deve levar em consideração as informações presentes na página
[SV] Iniciação de Pagamentos - Conteúdo comum entre os produtos
.
Criar consentimento para iniciação de pagamento
: (POST /automatic-payments/v2/recurring-consents)
Método para a criação do consentimento para iniciação de pagamento.
Dicionário de dados
Campos de resposta do endpoint de /recurring-consents
Consultar consentimento para iniciação de pagamento
: (GET /automatic-payments/v2/recurring-consents/{recurringConsentId})
Método para consultar o consentimento para iniciação de pagamento.
Dicionário de dados
Campos de resposta do endpoint de /recurring-consents
Editar, rejeitar ou revogar consentimento para iniciação de pagamento
: (PATCH /automatic-payments/v2/recurring-consents/{recurringConsentId})
Método para consultar o consentimento para iniciação de pagamento.
Dicionário de dados
Campos de resposta do endpoint de /recurring-consents/{recurringConsentId}
Pix - Criar iniciação de pagamento
: (POST /automatic-payments/v2/pix/recurring-payments)
Método para a criação de uma iniciação de pagamento.
Dicionário de dados
Campos de resposta do endpoint de /pix/recurring-payments
Pix - Criar nova tentativa de pagamento para Pix Automático
: (POST /automatic-payments/v2/pix/recurring-payments/{originalRecurringPaymentId}/retry)
Cria nova tentativa de pagamento para o Pix Automático.
Dicionário de dados
Campos de resposta do endpoint de /pix/recurring-payments
Pix - Consultar iniciação de pagamento
: (GET /automatic-payments/v2/pix/recurring-payments)
Método para a criação de uma iniciação de pagamento.
Dicionário de dados
Campos de resposta do endpoint de /pix/recurring-payments
Pix - Consultar iniciação de pagamento
: (GET /automatic-payments/v2/pix/recurring-payments/{recurringPaymentId})
Método para consultar uma iniciação de pagamento.
Dicionário de dados
Campos de resposta do endpoint de /pix/recurring-payments/{recurringPaymentId}.
Pix - Cancelar iniciação de pagamento
: (PATCH /automatic-payments/v2/pix/recurring-payments/{recurringPaymentId})
Método para cancelar uma iniciação de pagamento.
Dicionário de dados
Campos de resposta do endpoint de /pix/recurring-payments/{recurringPaymentId}.

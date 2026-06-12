---
                            title: "Informações Gerais - [PC] Portabilidade de Crédito - CPC - v1.0.0-beta.3 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1005420563_Informa+es+Gerais+-+PC+Portabilidade+de+Cr+dito+-+CPC+-+v1.0.0-beta.3"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1005420563/Informa+es+Gerais+-+PC+Portabilidade+de+Cr+dito+-+CPC+-+v1.0.0-beta.3"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Informações Gerais - [PC] Portabilidade de Crédito - CPC - v1.0.0-beta.3 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Visão geral
2
Conteúdo comum entre os produtos
3
Realiza pedido de portabilidade de crédito
: (POST /portabilities)
3.1
Dicionário de dados
4
Consulta portabilidade de crédito através da propriedade portabilityId
: (GET /portabilities/{portabilityId})
4.1
Dicionário de dados
5
Comunica a respeito do cancelamento da portabilidade de crédito
: (PATCH /portabilities/{portabilityId}/cancel)
5.1
Dicionário de dados
6
Consultar contrato de portabilidade de crédito
: (GET /credit-operations/{contractId}/portability-eligibility)
6.1
Dicionário de dados
7
Obtém os dados necessários para realização do pagamento da operação via TED
: (GET /account-data)
7.1
Dicionário de dados
8
Comunica a Instituição Credora a respeito da liquidação da portabilidade de crédito
: (POST /portabilities/{portabilityId}/payment)
8.1
Dicionário de dados
Visão geral
A API de Portabilidade de Crédito permite que usuários transfiram suas operações de crédito e arrendamento mercantil entre instituições financeiras em busca de melhores condições para o Open Finance Brasil.
Conteúdo comum entre os produtos
Para o entendimento correto do produto você deve levar em consideração as informações presentes na página
[PC] API - Portabilidade de Crédito - CPC
.
Realiza pedido de portabilidade de crédito
: (POST /portabilities)
Realiza pedido de portabilidade de crédito para um determinado contrato junto a instituição credora. Solicitação de portabilidade de crédito via OFB.
Dicionário de dados
Campos de resposta do endpoint de /portabilities.
Fazer download do dicionário de dados
Consulta portabilidade de crédito através da propriedade portabilityId
: (GET /portabilities/{portabilityId})
Endpoint responsável por consultar pedidos de portabilidade de crédito.
Cada portabilityId deve respeitar o prazo de consulta. Fortemente recomendado que ocorra a cada 2 horas, entre 8h e 18h, em dias úteis. As consultas também podem ser realizadas de forma esporádica, conforme ação do usuário (neste caso, sem restrição de dia e horário).
Dicionário de dados
Campos de resposta do endpoint de /portabilities/{portabilityId}.
Fazer download do dicionário de dados
Comunica a respeito do cancelamento da portabilidade de crédito
: (PATCH /portabilities/{portabilityId}/cancel)
Comunica a Instituição Credora a respeito do cancelamento da portabilidade de crédito.
Dicionário de dados
Campos de resposta do endpoint de /portabilities/{portabilityId}/cancel.
Fazer download do dicionário de dados
Consultar contrato de portabilidade de crédito
: (GET /credit-operations/{contractId}/portability-eligibility)
Informa se um contrato pertencente a um determinado cliente estará habilitado para a realização do pedido de portabilidade de crédito considerando a regra de só existir um pedido de portabilidade para um determinado contrato.
Dicionário de dados
Campos de resposta do endpoint de /credit-operations/{contractId}/portability-eligibility.
Fazer download do dicionário de dados
Obtém os dados necessários para realização do pagamento da operação via TED
: (GET /account-data)
Método responsável por recuperar informações de contas  para realização do pagamento via TED.
Dicionário de dados
Campos de resposta do endpoint de /account-data.
Fazer download do dicionário de dados
Comunica a Instituição Credora a respeito da liquidação da portabilidade de crédito
: (POST /portabilities/{portabilityId}/payment)
Comunica a Instituição Credora a respeito da liquidação da portabilidade de crédito.
Dicionário de dados
Campos de resposta do endpoint de /portabilities/{portabilityId}/payment.
Fazer download do dicionário de dados

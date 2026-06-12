---
                            title: "Liquidação de QR Codes via API Pagamentos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1836744705_Liquida+o+de+QR+Codes+via+API+Pagamentos"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1836744705/Liquida+o+de+QR+Codes+via+API+Pagamentos"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Liquidação de QR Codes via API Pagamentos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1. Introdução
Este guia orienta Instituições Iniciadoras de Transação de Pagamento (ITPs) na implementação dos fluxos de liquidação de QR Codes Pix através da API de Pagamentos do Open Finance Brasil.
O documento cobre exclusivamente os cenários envolvendo leitura e liquidação de QR Codes para a API Pagamentos, desde a decodificação do código até a consulta de status do pagamento, e foi elaborado para responder às dúvidas operacionais mais recorrentes observadas no ecossistema.
1.1 Escopo
Este guia abrange os seguintes tipos de QR Code e suas variantes NFC:
Sigla
Tipo
localInstrument
purpose
aplicáveis
Sigla
Tipo
localInstrument
purpose
aplicáveis
QRES
QR Code Estático
QRES
IMMEDIATE
,
SINGLE_SCHEDULED
,
RECURRENT_SCHEDULED
APES
QR Code Estático via NFC
APES
IMMEDIATE
,
SINGLE_SCHEDULED
,
RECURRENT_SCHEDULED
QRDN COB
QR Code Dinâmico — Cobrança Imediata
QRDN
IMMEDIATE
APDN COB
QR Code Dinâmico via NFC — Cobrança Imediata
APDN
IMMEDIATE
QRDN COBV
QR Code Dinâmico — Cobrança com Vencimento
QRDN
IMMEDIATE
ou
SINGLE_SCHEDULED
APDN COBV
QR Code Dinâmico via NFC — Cobrança com Vencimento
APDN
IMMEDIATE
ou
SINGLE_SCHEDULED
QRES Saque
QR Code Estático — Pix Saque
QRES
WITHDRAW
APES Saque
QR Code Estático via NFC — Pix Saque
APES
WITHDRAW
QRDN Saque
QR Code Dinâmico — Pix Saque
QRDN
WITHDRAW
APDN Saque
QR Code Dinâmico via NFC — Pix Saque
APDN
WITHDRAW
QRDN Troco
QR Code Dinâmico — Pix Troco
QRDN
CHANGE
APDN Troco
QR Code Dinâmico via NFC — Pix Troco
APDN
CHANGE
QR Composto - Recorrência
QR Code Composto com dados de recorrência
Não aplicável
Não aplicável¹
QR Composto - Estático e recorrência
QR Code composto com QRES e dados da recorrência
APES, QRES
²
IMMEDIATE
,
SINGLE_SCHEDULED
QR Composto - Dinâmico e recorrência
QR Code composto com QRDN e dados da recorrência
QRDN, APDN
²
IMMEDIATE
ou
SINGLE_SCHEDULED
Equivalência NFC:
Os
localInstrument
APES e APDN são os equivalentes NFC de QRES e QRDN, respectivamente. As regras de preenchimento de todos os campos da API são idênticas entre cada par — a única diferença é o método de captura do QR Code (câmera/copia-e-cola vs. NFC). Por essa razão, ao longo deste guia as referências a QRES se aplicam igualmente a APES, e as referências a QRDN se aplicam igualmente a APDN, salvo indicação contrária.
Restrição de agendamento recorrente:
Para consentimentos com
schedule
diferente de
single
(ou seja,
daily
,
weekly
,
monthly
ou
custom
), apenas os
localInstrument
MANU, DICT ou QRES são permitidos. Isso significa que QR Codes Dinâmicos (QRDN/APDN)
não podem
ser utilizados para agendamentos recorrentes.
Fora de escopo:
Autenticação, mTLS, certificados BRCAC/BRSEAL, assinatura JWS e demais aspectos de segurança. Para esses tópicos, consulte os guias de segurança publicados pelo ecossistema Open Finance Brasil.
Legenda:
¹ - QR Composto apenas com dados da recorrência não é suportado na API Pagamentos.
² - Um ou outro, a depender da forma que foram capturados os dados da cobrança.
2. Visão Geral do Fluxo
O fluxo de iniciação de pagamento via QR Code segue sempre a mesma estrutura, independente do tipo de QR Code. A diferença entre os cenários reside nos dados enviados e nas validações aplicadas pela detentora.
2.1 Fluxo Resumido
ITP (Iniciadora)                                Detentora
│                                              │
│  1. Leitura do QR Code                       │
│  2. Decodificação e extração dos dados        │
│  3. (QRDN/APDN) Consulta ao payload JSON via URL│
│                                              │
│──── POST /consents ──────────────────────────>│
│<─── 201 Created (consentId, status: AW_AUTH) ─│
│                                              │
│          [Redirecionamento / FIDO]            │
│          [Usuário autoriza na detentora]      │
│                                              │
│──── POST /pix/payments ──────────────────────>│
│<─── 201 Created (paymentId, status: RCVD) ───│
│                                              │
│  ┌─── Processamento assíncrono ───┐          │
│  │  Detentora valida, consulta     │          │
│  │  DICT, envia ao SPI             │          │
│  └─────────────────────────────────┘          │
│                                              │
│──── GET /pix/payments/{paymentId} ───────────>│
│<─── 200 OK (status: ACSC | RJCT | SCHD ...) ─│
2.2 Etapas críticas para QR Codes
Etapa 1 — Leitura e decodificação:
A ITP lê o QR Code (via câmera, NFC ou copia-e-cola) e decodifica seu conteúdo conforme o padrão EMV ou, no caso de QR Dinâmico, acessa a URL para obter o payload JSON.
Etapa 2 — Identificação do tipo:
A ITP identifica se o QR Code é estático, dinâmico ou composto, e no caso de dinâmico, se é COB, COBV, Saque ou Troco e, no caso de composto, se contem os dados da recorrencia, ou se possui os dados da recorrência e um QRES para pagamento, ou dados para recorrência e um QRDN. Essa identificação determina:
O valor de
localInstrument
(QRES ou QRDN)
O valor de
purpose
(IMMEDIATE, WITHDRAW, CHANGE)
As regras de composição do campo
amount
A obrigatoriedade do campo
payloadJWS
Etapa 3 — Criação do consentimento:
A ITP envia os dados para criação do consentimento via
POST /consents
.
Etapa 4 — Criação do pagamento:
Após autorização do consentimento, a ITP envia o pagamento via
POST /pix/payments
.
Etapa 5 — Polling de status:
A ITP consulta o status do pagamento via
GET /pix/payments/{paymentId}
até que atinja um status terminal (ACSC, RJCT ou CANC).
3. Guia por Tipo de QR Code
3.1 QR Code Estático (QRES / APES)
O QR Code Estático segue o padrão EMV e seus dados são extraídos diretamente da string codificada — não há URL para consulta de payload. As regras desta seção aplicam-se igualmente ao
localInstrument
APES (leitura via NFC).
Dados extraídos do QR Code:
Campo EMV
Dado
Mapeamento na API
Campo EMV
Dado
Mapeamento na API
26 (Merchant Account Info)
Chave Pix
proxy
54 (Transaction Amount)
Valor (se presente)
amount
62-05 (Reference Label)
TxId (se presente)
transactionIdentification
Regras de preenchimento:
Campo API
Regra
Campo API
Regra
localInstrument
QRES
(câmera/copia-e-cola) ou
APES
(NFC)
purpose
IMMEDIATE
para pagamento imediato.
SINGLE_SCHEDULED
para agendamento único.
RECURRENT_SCHEDULED
para agendamento recorrente.
amount
Se o campo 54 do EMV estiver presente, usar esse valor. Se ausente, o valor é informado pelo usuário pagador.
transactionIdentification
Se o TxId estiver presente no QR Code, preencher com esse valor (até 25 caracteres). Se ausente,
não preencher
.
qrCode
Obrigatório. Enviar a string completa do QR Code (copia-e-cola).
payloadJWS
Não se aplica.
Não deve ser enviado.
Sobre agendamento com QRES:
O QRES é um dos poucos
localInstrument
compatíveis com agendamento recorrente (
daily
,
weekly
,
monthly
,
custom
). Nestes cenários, o
purpose
deve ser
RECURRENT_SCHEDULED
e o objeto
schedule
no consentimento deve conter a configuração de recorrência desejada.
3.2 QR Code Dinâmico — Cobrança Imediata (QRDN / APDN COB)
O QR Code Dinâmico contém uma URL que aponta para o payload JSON da cobrança, protegido por JWS. As regras desta seção aplicam-se igualmente ao
localInstrument
APDN (leitura via NFC).
Fluxo de obtenção dos dados:
A ITP lê o QR Code e extrai a URL (campo 26 do EMV).
A ITP acessa a URL e obtém o payload JWS (header.payload.signature).
A ITP decodifica o payload (fragmento central do JWS) para extrair os dados da cobrança.
O JWS completo é enviado no campo
payloadJWS
do consentimento.
Dados extraídos do payload JSON:
Campo do payload
Dado
Mapeamento na API
Campo do payload
Dado
Mapeamento na API
valor.original
Valor da cobrança
amount
valor.modalidadeAlteracao
Permite alterar valor (0 ou 1)
Regra de validação do
amount
txid
Identificador da transação
transactionIdentification
chave
Chave Pix do recebedor
proxy
Regras de preenchimento:
Campo API
Regra
Campo API
Regra
localInstrument
QRDN
(câmera/copia-e-cola) ou
APDN
(NFC)
purpose
IMMEDIATE
amount
Preencher com
valor.original
. Se
valor.modalidadeAlteracao
= 1, o valor pode ser alterado pelo usuário pagador.
transactionIdentification
Obrigatório. Preencher com o
txid
do payload (26–35 caracteres).
qrCode
Obrigatório. Enviar a string completa do QR Code.
payloadJWS
Obrigatório. Enviar o JWS completo (header.payload.signature).
3.3 QR Code Dinâmico — Cobrança com Vencimento (QRDN / APDN COBV)
O fluxo de obtenção dos dados é idêntico ao QRDN/APDN COB. A diferença está na composição do valor e na ausência do campo
modalidadeAlteracao
.
Dados extraídos do payload JSON:
Campo do payload
Dado
Campo do payload
Dado
valor.original
Valor nominal da cobrança
valor.multa
Multa aplicável (se houver)
valor.juros
Juros aplicáveis (se houver)
valor.abatimento
Abatimento aplicável (se houver)
valor.desconto
Desconto aplicável (se houver)
txid
Identificador da transação
chave
Chave Pix do recebedor
Composição do valor final:
O campo
amount
deve ser preenchido com o valor final da cobrança, calculado a partir da composição: valor original − abatimentos − descontos + juros + multa. O calculo é realizado pelo PSP Recebedor com base nos parâmetros enviados na consulta ao QRCode através da API Pix. O campo
modalidadeAlteracao
não existe
no payload COBV; portanto, o valor
não pode ser alterado
pelo usuário pagador.
Regras de preenchimento:
Campo API
Regra
Campo API
Regra
localInstrument
QRDN
(câmera/copia-e-cola) ou
APDN
(NFC)
purpose
IMMEDIATE
(pagamento no ato) ou
SINGLE_SCHEDULED
(agendamento para data de vencimento)
amount
Preencher com o valor final composto (original ± ajustes).
transactionIdentification
Obrigatório. Preencher com o
txid
do payload (26–35 caracteres).
qrCode
Obrigatório.
payloadJWS
Obrigatório.
ibgeTownCode
Obrigatório para COBV. Deve prevalecer o código do município do usuário pagador informado pela ITP.
Sobre o DPP (Data Prevista de Pagamento):
A DPP é informada pela ITP no consentimento através da data do pagamento. Para pagamentos imediatos, o valor está em
/data/payment/date
; para pagamentos agendados, em
/data/payment/schedule/single/date
. Independente de ser imediato ou agendado, a detentora utilizará essa data para consultar a cobrança com vencimento nos endpoints da API Pix do BCB, o que impacta diretamente o cálculo de juros, multa e descontos aplicáveis.
3.4 QR Code Estático — Pix Saque (QRES / APES Saque)
No Pix Saque via QR Code Estático, os dados do Facilitador de Serviço de Saque (FSS) já estão contidos na própria string EMV do QR Code. Portanto, não há payload JWS envolvido — a detentora valida os dados do FSS diretamente a partir do conteúdo do QRES recebido no campo
qrCode
. As regras desta seção aplicam-se igualmente ao
localInstrument
APES.
Regras de preenchimento:
Campo API
Regra
Campo API
Regra
localInstrument
QRES
(câmera/copia-e-cola) ou
APES
(NFC)
purpose
WITHDRAW
amount
Valor do saque informado pelo usuário pagador.
transactionIdentification
Mesmo comportamento do QRES convencional.
qrCode
Obrigatório. A detentora extrairá os dados do FSS diretamente desta string.
payloadJWS
Não se aplica.
O QRES não possui payload JWS.
3.5 QR Code Dinâmico — Pix Saque (QRDN / APDN Saque)
No Pix Saque via QR Dinâmico, a cobrança imediata possui a estrutura
valor.retirada.saque
no payload. Diferente do cenário QRES Saque, aqui os dados do FSS estão no payload JSON do JWS, e portanto o envio do
payloadJWS
é obrigatório para que a detentora possa validá-los. As regras desta seção aplicam-se igualmente ao
localInstrument
APDN.
Regras estruturais da API Pix BCB para Saque:
O campo
valor.original
da cobrança deve ser
0.00
(zero).
O campo
valor.modalidadeAlteracao
(nível da cobrança) deve ser
0
.
O valor do saque está em
valor.retirada.saque.valor
.
Se
valor.retirada.saque.modalidadeAlteracao
= 1, o valor do saque pode ser alterado pelo usuário pagador.
Regras de preenchimento:
Campo API
Regra
Campo API
Regra
localInstrument
QRDN
(câmera/copia-e-cola) ou
APDN
(NFC)
purpose
WITHDRAW
amount
Preencher com o valor do saque (
valor.retirada.saque.valor
).
transactionIdentification
Obrigatório. Preencher com o
txid
do payload.
qrCode
Obrigatório.
payloadJWS
Obrigatório. A detentora utilizará o JWS para validar os dados do agente e do facilitador do serviço de saque (FSS).
3.6 QR Code Dinâmico — Pix Troco (QRDN / APDN Troco)
No Pix Troco, a cobrança imediata possui a estrutura
valor.retirada.troco
no payload. As regras desta seção aplicam-se igualmente ao
localInstrument
APDN.
Regras estruturais da API Pix BCB para Troco:
O campo
valor.original
da cobrança deve ser
maior que
0.00
(representa o valor da compra).
O campo
valor.modalidadeAlteracao
(nível da cobrança) deve ser
0
.
O valor do troco está em
valor.retirada.troco.valor
.
Se
valor.retirada.troco.modalidadeAlteracao
= 1, o valor do troco pode ser alterado pelo usuário pagador.
O valor da compra (
valor.original
)
não pode ser alterado
.
Regras de preenchimento:
Campo API
Regra
Campo API
Regra
localInstrument
QRDN
(câmera/copia-e-cola) ou
APDN
(NFC)
purpose
CHANGE
amount
Preencher com o valor total da transação:
valor.original
(compra) +
valor.retirada.troco.valor
(troco).
transactionIdentification
Obrigatório. Preencher com o
txid
do payload.

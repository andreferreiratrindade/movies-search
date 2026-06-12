---
                            title: "MDQ - Fluxo da Transmissora - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "362578850_MDQ+-+Fluxo+da+Transmissora"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/362578850/MDQ+-+Fluxo+da+Transmissora"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # MDQ - Fluxo da Transmissora - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Este fluxo representa o processo de enfileramento de messagens e integração com o MQD na visão da TRANSMISSORA.
Open
Passos
Passo
Participante
Descrição
Passo
Participante
Descrição
1.
SERVICE
O serviço gera uma solicitação para a API da TRANSMISORA
2.
API
A API processa a solicitação recebida
3.
API
A API retorna um resultado para a solicitação
4.
API
A API atualiza a solicitação, incluindo a resposta enviada para a RECEPTORA - Corpo+Cabeçalho - e adicionando oa parâmetros clientOrgID (clientOrgID: OrganisationID (cadastrado no Diretório Central) da Receptora que esta solicitando a informação, este campo deve ser incluso como parte de cabeçalho) - o ID da RECEPTORA - e endpointName ao cabeçalho (enviar somente validações de solicitações bem-sucedidas - 2xx)
5.
API
A API da TRANSMISSORA envia a nova resposta válida para o MQD
6.
MQD
MQD Valida se as informações do cabeçalho estão completas e corretas
7.
MQD
MQD encaminha as informações para serem processadas posteriormente
8.
MQD
MQD responde OK se o processo foi bem-sucedido
Exemplo de Soliciação da API - MQD
endpointName
serverOrgId
x-fapi-interaction-id
Corpo
endpointName
serverOrgId
x-fapi-interaction-id
Corpo
/loans/v2/contracts/{contractId}/payments
Nome do endpoint e deve corresponder à lista de
endpoints
aceitos
c73bcdcc-2669-4bf6-81d3-e4ae73fb11fd
Id da TRANSMISORA
241e202-e8f0-5f5a-9651-ebc257371e24
valor x-fapi usado durante a transação
Valor retornado como resposta da TRANSMISORA
curl --location 'http://localhost:8080/ValidateResponse' \
--header 'serverOrgId: c73bcdcc-2669-4bf6-81d3-e4ae73fb11fd' \
--header 'endpointName: /loans/v2/contracts/{contractId}/payments' \
--header 'x-fapi-interaction-id: 241e202-e8f0-5f5a-9651-ebc257371e24' \
--header 'Content-Type: text/plain' \
--data '{
"data": {
"paidInstalments": 73,
"contractOutstandingBalance": "1000.0400",
"releases": [
{
"paymentId": "XlthLXpBLVowLTldW2EtekEtWjAtOVwtXXswLDk5fSQ",
"isOverParcelPayment": true,
"instalmentId": "WGx0aExYcEJMVm93TFRsZFcyRXRla0V0V2pBdE9Wd3RYWH",
"paidDate": "2021-05-21",
"currency": "BRL",
"paidAmount": "1000.0400",
"overParcel": {
"fees": [
{
"feeName": "Reavaliação periódica do bem",
"feeCode": "aval_bem",
"feeAmount": "100000.0400"
}
],
"charges": [
{
"chargeType": "JUROS_REMUNERATORIOS_POR_ATRASO",
"chargeAdditionalInfo": "Informações adicionais",
"chargeAmount": "1000.0400"
}
]
}
}
]
},
"links": {
"self": "https://api.banco.com.br/open-banking/api/v1/resource",
"first": "https://api.banco.com.br/open-banking/api/v1/resource",
"prev": "https://api.banco.com.br/open-banking/api/v1/resource",
"next": "https://api.banco.com.br/open-banking/api/v1/resource",
"last": "https://api.banco.com.br/open-banking/api/v1/resource"
},
"meta": {
"totalRecords": 1,
"totalPages": 1,
"requestDateTime": "2021-05-21T08:30:00Z"
}
}'

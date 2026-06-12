---
                            title: "SLA de Envio de Reportes - 95% até 08:00h de D+1 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1212186625_SLA+de+Envio+de+Reportes+-+95+at+08+00h+de+D+1"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1212186625/SLA+de+Envio+de+Reportes+-+95+at+08+00h+de+D+1"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # SLA de Envio de Reportes - 95% até 08:00h de D+1 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.03
Objetivo
Apontar os casos em que o envio dos reportes pelas organizações não ocorreu dentro do SLA de no mínimo 95% em D+1 até às 8:00.
Para melhor visualização dos dados, é possível consultar os detalhes no Dashboard de Monitoramento Operacional - Aba Reporte de Informações.
Escopo
São analisados envios dos reportes de Dados Cadastrais e Transacionais (Fases 2 e 4b), Dados de Pagamentos (Fase 3) e Estoque de Consentimentos.
Terminologia
Os termos abaixo estão no contexto da Plataforma de Coleta de Métricas, que por sua vez está no contexto do Open Finance Brasil.
Client e Server
Em uma interação, a parte que solicita os dados é chamada de
client
, ao passo que a parte que devolve os dados é
server
. Portanto, supondo que A faça uma consulta em B pelos dados de uma conta, esses dados serão transmitidos por quem recebeu a solicitação, e recebidos por quem a fez. Neste caso, A é o
client
e B é o
server
.
Faltante
Quando uma organização envia um reporte contra uma outra organização, caso esta última não envie sua contraparte ela será considerada
faltante
no processo de pareamento.
Forma de avaliação do percentual de SLA
Diariamente são apurados os reportes que não cumpriram o SLA de envio da seguinte forma:
Contam-se todos os reportes enviados pela organização que foram recebidos pela PCM até D-1 às 08:00 (GMT) por endpoint e método
Contam-se todos os reportes enviados contra a organização e que não foram pareados (faltantes) por endpoint e método; este número representa o total de reportes não enviados
Calcula-se o total de reportes esperados: não enviados + recebidos até 08:00 de D+1
O quociente entre os faltantes pelos esperados representa o percentual de não cumprimento, e o SLA do dia para a organização é calculado por
[1-(faltantes/esperados)]*100
Em um exemplo prático:
Apuração em 03/08/2025 para o Banco X
Quantidade de reportes de 01/08/2025 enviados pelo Banco X até 02/08/2025 às 08:00 para o endpoint /payments, método POST = 18
Quantidade de reportes de 01/08/2025 enviados contra o Banco X, endpoint /payments, método POST e que não foram pareados (Banco X faltante) = 2
Quantidade de reportes esperados em 01/08/2025= = 18 + 2 = 20
SLA do Banco X de 01/08/2025 para o endpoint /payments e método POST = [1 - (2/20)] * 100 = 90%
Neste exemplo, o Banco X receberá um ticket de não cumprimento do SLA
Pontos importantes
O envio do ticket ocorre se qualquer os endpoints reportados pela organização e contra a organização estiver abaixo de 95%, independente do total de envios realizados pela organização no dia.
Neste caso, se uma organização enviar reportes de 10 endpoints diferentes mas 1 deles estiver com SLA abaixo de 95%, o ticket será enviado independente do percentual dos outros endpoints.
Arquivo de evidências
Todo ticket aberto possui anexado um arquivo de evidências, onde são listados até 5 fapiInteractionId para cada caso encontrado por dia, para facilitar a investigação das causas pelas organizações.
Campos do arquivo de evidências
timestamp_gmt_date: timestamp do reporte no formato GMT
fapiinteractionid: xfapi de exemplo do endpoint e método que não cumpriu o SLA diário
organisationid: id da organização reportadora do reporte encontrado contra a organização notificada
clientorgid: id da organização identificada com client no reporte encontrado contra a organização notificada
serverorgid: id da organização identificada com server no reporte encontrado contra a organização notificada
role: role do reporte encontrado contra a organização notificada
status: status do reporte encontrado contra a organização notificada
httpmethod: método do reporte que não cumpriu o SLA
endpoint: endpoint do reporte que não cumpriu o SLA
timestamp: timestamp do reporte encontrado contra a organização notificada

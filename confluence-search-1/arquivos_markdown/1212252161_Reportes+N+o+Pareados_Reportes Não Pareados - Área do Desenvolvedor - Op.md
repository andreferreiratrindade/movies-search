---
                            title: "Reportes Não Pareados - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1212252161_Reportes+N+o+Pareados"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1212252161/Reportes+N+o+Pareados"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Reportes Não Pareados - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.00
Objetivo
Apontar os casos em que não houve o pareamento de reportes enviados contra as organizações dentro de um determinado período.
Para melhor visualização dos dados, é possível consultar os detalhes no Dashboard de Monitoramento Operacional - Aba Reportes Não Enviados.
Escopo
São analisados o pareamento dos reportes de Dados Transacionais e Cadastrais (fases 2 e 4b) e Dados de Pagamentos (Fase 3).
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
Percentual de pareamento
O percentual de pareamento é calculado levando-se em conta a quantidade de reportes enviados contra uma organização (total esperado) e sua relação com a quantidade não enviada por esta última (total faltante). É calculado pela fórmula abaixo:
Open
De acordo com a Normativa 575 do Banco Central, o percentual esperado de pareamento é de no mínimo 95% desde 01/07/2025.
Identificação do não-paraemento
O processo de identificação do não-pareamento por organização é apurado da seguinte maneira:
Open
Neste exemplo, olhando para a organização A, vemos que foram enviados contra ela 5 reportes (2,3,4,5 e 8), sendo que somente 2 (3 e 5) foram enviados pela organização A. Note que, olhando para a organização A como faltante, os reportes 6 e 7 não são considerados, pois são comunicações entre outras organizações.
Assim, teríamos um percentual de não pareamento igual a 2 / 5 = 40%, portanto fora do mínimo esperado e passível de recebimento de ticket.
Arquivo de evidências
Todo ticket aberto possui anexado um arquivo de evidências, onde são listados até 5 fapiInteractionId para cada caso encontrado por dia, para facilitar a investigação das causas pelas organizações.
Campos do arquivo de evidências
org_faltante, nome_faltante, role_faltante: informações da organização que não enviou os dados
data_referencia: data GMT do envio do reporte
api_family, api_version, endpoint, httpmethod, statuscode: identificação do reporte enviado
contagem_unpaired_referencia: quantidade de reportes não pareados na data de referência
contagem_chamadas_referencia: quantidade de reportes total na data de referência (pareados, pareados inconsistentes e não pareados)
perc_unpaired_referencia: percentual de não-pareamento na data de referência
contagem_total_unpaired, contagem_total_chamadas, perc_total_unpaired: valores de referência da API no período selecionado
evidencias_de_xfapi: lista de até 5 xfapis que não estão pareados, informados por outras organizações contra a organização faltante
Referências
Fluxo de pareamento de reportes na PCM
Processamento

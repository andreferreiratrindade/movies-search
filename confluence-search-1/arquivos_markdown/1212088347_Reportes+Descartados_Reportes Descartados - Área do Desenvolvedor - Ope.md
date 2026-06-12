---
                            title: "Reportes Descartados - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1212088347_Reportes+Descartados"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1212088347/Reportes+Descartados"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Reportes Descartados - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.01
Objetivo
Apontar os casos em que os reportes enviados pelas organizações dentro de um determinado período foram descartados e seus motivos.
Para melhor visualização dos dados, é possível consultar os detalhes no Dashboard de Monitoramento Operacional - Aba Reportes Descartados.
Escopo
São analisados os descartes dos reportes de Dados Transacionais e Cadastrais (fases 2 e 4b) e Dados de Pagamentos (Fase 3), Hybridflow e Segurança.
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
Motivos de descartes
Os motivos de descarte de um reporte dependem de regras específicas para cada campo de cada API. As regras de descarte para cada campo podem ser consultadas em em cada domínio:
Especificações por domínio
.
Descarte do reporte
O processo de identificação e descarte do reporte pode ser encontrado em
Processamento
Arquivo de evidências
Todo ticket aberto possui anexado um arquivo de evidências, onde são listados até 5 fapiInteractionId para cada caso encontrado por dia, para facilitar a investigação das causas pelas organizações.
Campos do arquivo de evidências
role, orgid, nome: informações da organização que enviou os dados
data_referencia: data GMT do envio do reporte
data_deescartado: data em que foi feito o descarte do reporte
serverorgid e clientorgid: dados das organizações envolvidas na comuicação
api_family, api_version, endpoint, httpmethod, statuscode: identificação do reporte enviado
mensagem_erro_1, mensagem_erro_2, mensagem_erro_3, mensagem_erro_4: motivo pelo qual o relatório foi descartado; é apresentado em até 4 campos separados porque é possível que o reporte tenha sido descartado por mais de um motivo. Neste caso, cada motivo será demonstrado separadamente
campo_error_1, campo_erro_2, campo_erro_3, campo_erro_4: campo do reporte que foi validado para o desscarte
evidencias_de_xfapi: lista de até 5 xfapis que foram descartados pelos motivos apresentados em cada linha do arquivo de evidências. No caso de Hybridflow, são os reportid relacionados.
Referências
Fluxo de pareamento de reportes na PCM
Processamento

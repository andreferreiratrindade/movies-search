---
                            title: "Qualidade de Dados - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1212219393_Qualidade+de+Dados"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1212219393/Qualidade+de+Dados"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Qualidade de Dados - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.00
Objetivo
Apontar os casos em que a qualidade dos dados dos reportes enviados pelas organizações dentro de um determinado período não cumpriu as regras definidas.
Para melhor visualização dos dados, é possível consultar os detalhes no Dashboard de Monitoramento Operacional - Aba Qualidade de Reportes
Escopo
São analisados os dados (comuns e additionalinfo) dos reportes de Dados Transacionais e Cadastrais (fases 2 e 4b) e Dados de Pagamentos (Fase 3), Hybridflow, Segurança e Estoque de Consentimentos.
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
Motivos da crítica de qualidade
Os motivos de crítica de qualidade de um reporte dependem de regras específicas para cada campo de cada API. As regras de validação para cada campo podem ser consultadas em em cada domínio:
Especificações por domínio
Arquivo de evidências
Todo ticket aberto possui anexado um arquivo de evidências, onde são listados até 5 fapiInteractionId para cada caso encontrado por dia, para facilitar a investigação das causas pelas organizações.
Campos do arquivo de evidências
role, orgid, nome: informações da organização que enviou os dados
data_referencia: data GMT do envio do reporte
data_deescartado: data em que foi feito o descarte do reporte
serverorgid e clientorgid: dados das organizações envolvidas na comuicação
api_family, api_version, endpoint, httpmethod, statuscode: identificação do reporte enviado
*_status: campo ou additionalinfo que foi identificado como fora da qualidade establelecida pelo ecossistema OFB
evidencias_de_fapi_*: lista de até 5 xfapis que foram criticados pelos motivos apresentados em cada campo/additionalinfo. No caso de Hybridflow, são os reportid relacionados.

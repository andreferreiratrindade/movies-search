---
                            title: "Funcionalidade e Campos - PC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1212088321_Funcionalidade+e+Campos+-+PC"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1212088321/Funcionalidade+e+Campos+-+PC"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Funcionalidade e Campos - PC - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.01
Objetivo
Disponibilização de uma nova API dedicada à obtenção de dados referentes às solicitações da portabilidade por parte dos clientes das instituições financeiras. Esta solução permite que as instituições forneçam dados à PCM de forma completa e transparente sobre o fluxo de solicitações de Portabilidade de Crédito ao ecossistema do Open Finance Brasil.
Esta API atende os produtos de Portabilidade de Crédito - Crédito Pessoal Clean (CPC) e Crédito Consignado Federal (CF)
Esta é uma documentação funcional. Para a documentação técnica, acesso o link:
Documentação da API - PCM
Terminologia
Os termos abaixo estão no contexto da Plataforma de Coleta de Métricas, que por sua vez está no contexto do Open Finance Brasil.
Portabilidade de Crédito
A Portabilidade de Crédito permite que usuários transfiram suas operações de crédito e arrendamento mercantil entre instituições financeiras em busca de melhores condições. Atualmente, a solicitação de portabilidade pode ser feita via registradora. A implementação da solicitação de portabilidade, alinhada à agenda do Open Finance Brasil (
OFB
), visa agilizar e simplificar o processo.
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
Descrição funcional das APIs
API de inclusão de reportes de portabilidade - SERVER
Campo
Descrição
xfapi¹
UUID que identifica uma transação específica entre dois participantes. Esse dado pode ser encontrado no header x-fapi-interaction-id informado pelo Client e devolvido pelo Server. Mais informações em Cabeçalhos HTTP na documentação do Open Finance Brasil. O envio dessa informação é obrigatório, exceto nos casos ontem ela não esteja disponível como, por exemplo, em respostas com status 5xx, ou em chamadas que terminaram por timeout onde o reporte tem que ser enviado, mas sem esse atributo. Nos demais cenários, o envio é obrigatório.
Id da Portabilidade¹
Código identificador do pedido de portabilidade realizado.
endpoint¹
Identificação do endpoint que foi utilizado na transação reportada. A identificação do endpoint deve estar entre as entradas desse enum para ser considerado válido. Nesse campo não deve ser utilizado o path da requisição original, uma vez que ao comparar com os valores dessa enum, ele não será considerado válido.
statusCode¹
Status de retorno HTTP da solicitação.
Método¹
Método HTTP da solicitação.
[ GET, POST, PUT, DELETE, PATCH ]
Id de Correlação
ID de correlação que identifica uma sequência de chamadas inter-relacionadas no ecossistema. Diferente do fapiInteractionId que serve para identificar cada par request-response (interação), o identificador de correlação serve para ligar diferentes reportes quando estes representam uma jornada ou uma sequência de chamadas. Este valor é de livre provimento pelo reportador.
timestamp¹
Data/Hora UTC no formato ISO8601 com milissegundos (YYYY-MM-DDTHH:mm:ss.sssZ) do momento em que a chamada foi disparada, imediatamente antes do primeiro byte enviado na requisição.
Intervalo de tempo do processo
Tempo em milissegundos inteiros decorrido desde o registro do timestamp até a chegada do primeiro byte da resposta do server.
Id da organização atuando como CLIENT¹
Identificador da organização de onde a chamada foi disparada.
Id da organização atuando como SERVER¹
Identificador da organização para onde a chamada foi feita.
Data e hora da atualização do status
Data e hora em que o contrato teve o status atualizado. Uma string com data e hora conforme especificação ISO-8601, sempre com a utilização de timezone UTC(UTC time format).
Motivo da recusa
Motivo de recusa do pedido de portabilidade.
Só será preenchido caso o status seja REJECTED, CANCELLED ou PAYMENT_ISSUE
A consulta ao endpoint de GET é requerida para o fluxo de portabilidade
Rejeitado por
Informar usuário responsável pela rejeição da proposta, onde: PROPONENTE - Indica que o pedido de portabilidade de crédito foi rejeitado pela proponente, seja porque a proponente rejeitou a liquidação que excedeu em 15% o valor do contrato original, entre outras possibilidades. USUARIO - Indica que o cliente cancelou o pedido de portabilidade de crédito. CREDORA- Indica que a Instituição Credora cancelou o contrato por retenção do cliente ou outros motivos conforme motivo de recusa.
Só será preenchido caso o status seja REJECTED ou CANCELLED
[ PROPONENTE, USUARIO, CREDORA ]
Papel¹
ENUM indicando se o reporte que está sendo enviado apresenta a visão do server ou do client.
[ CLIENT, SERVER ]
Status da portabilidade
Informação sobre o status de um pedido de portabilidade de crédito, onde:
RECEIVED: Estado inicial. Indica que o pedido de portabilidade foi solicitado junto à instituição credora. O pedido deve permanecer neste estado até o próximo dia útil (D+1) onde começará a contar o prazo de 3 dias úteis para a etapa de contraproposta e o pedido de portabilidade deverá ser movido para PENDING
PENDING: Indica que o pedido de portabilidade de crédito está na fase de contraproposta, onde a instituição credora poderá enviar uma contraproposta ou não para o cliente por qualquer canal (email, telefone, etc.) porém o aceite só deverá ser valido se o cliente aprovar no canal digital da instituição credora
ACCEPTED_SETTLEMENT_IN_PROGRESS: Indica que a contraproposta não foi aceita pelo cliente e a instituição proponente terá que quitar o valor do contrato no mesmo dia em que o estado foi ativado.
ACCEPTED_SETTLEMENT_COMPLETED: Indica que a instituição proponente já liquidou o contrato e comunicou a respeito à credora que está validando os dados do contrato bem como valores recebidos para a quitação do mesmo (nesta etapa a instituição credora tem 2 dias úteis para fornecer a confirmação e o recibo de quitação do contrato de empréstimo)
PORTABILITY_COMPLETED: Indica que o pedido de portabilidade foi concluído com sucesso REJECTED: Indica que o pedido de portabilidade de crédito foi rejeitado, seja porque o cliente aceitou a contraproposta, ou porque a proponente rejeitou a liquidação que excedeu em 15% o valor do contrato original, entre outras possibilidades
REJECTED: Indica que o pedido de portabilidade de crédito foi rejeitado, seja porque o cliente aceitou a contraproposta, ou porque a proponente rejeitou a liquidação que excedeu em 15% o valor do contrato original, entre outras possibilidades
CANCELLED: Indica que o cliente cancelou o pedido de portabilidade de crédito
PAYMENT_ISSUE: Indica que a Instituição Credora encontrou alguma inconsistência na liquidação efetuada e que a Instituição Proponente deverá realizar ajustes conforme sugerido pela Instituição Credora para solucionar a pendência antes do cancelamento do pedido de portabilidade de crédito
hasFinancialAgent¹
Indica se a instituição trabalha com agente financeiro ao invés da conta reserva
¹ Campos com preenchimento obrigatório para que a mensagem seja considerada válida na ingestão
API de inclusão de reportes de portabilidade - CLIENT
Campo
Descrição
Campo
Descrição
timestamp¹
Data/Hora UTC no formato ISO8601 com milissegundos (YYYY-MM-DDTHH:mm:ss.sssZ) do momento em que a chamada foi disparada, imediatamente antes do primeiro byte enviado na requisição.
Id da Portabilidade¹
Código identificador do pedido de portabilidade realizado.
Id do contrato¹
Identifica de forma única o contrato da operação de crédito do cliente, mantendo as regras de imutabilidade dentro da instituição transmissora.
Data/hora da criação¹
Data e hora em que a Proponente registrou a presente proposta (chamada ao POST /portabilities). Uma string com data e hora conforme especificação ISO8601, sempre com a utilização de timezone UTC-0 (UTC time format).
Prazo do contrato original¹
Prazo restante do contrato original de empréstimo.
Prazo da proposta¹
Prazo da proposta de portabilidade de crédito
Status da portabilidade¹
Informação sobre o status de um pedido de portabilidade de crédito, onde:
RECEIVED: Estado inicial. Indica que o pedido de portabilidade foi solicitado junto à instituição credora. O pedido deve permanecer neste estado até o próximo dia útil (D+1) onde começará a contar o prazo de 3 dias úteis para a etapa de contraproposta e o pedido de portabilidade deverá ser movido para PENDING
PENDING: Indica que o pedido de portabilidade de crédito está na fase de contraproposta, onde a instituição credora poderá enviar uma contraproposta ou não para o cliente por qualquer canal (email, telefone, etc.) porém o aceite só deverá ser valido se o cliente aprovar no canal digital da instituição credora
ACCEPTED_SETTLEMENT_IN_PROGRESS: Indica que a contraproposta não foi aceita pelo cliente e a instituição proponente terá que quitar o valor do contrato no mesmo dia em que o estado foi ativado.
ACCEPTED_SETTLEMENT_COMPLETED: Indica que a instituição proponente já liquidou o contrato e comunicou a respeito à credora que está validando os dados do contrato bem como valores recebidos para a quitação do mesmo (nesta etapa a instituição credora tem 2 dias úteis para fornecer a confirmação e o recibo de quitação do contrato de empréstimo)
PORTABILITY_COMPLETED: Indica que o pedido de portabilidade foi concluído com sucesso REJECTED: Indica que o pedido de portabilidade de crédito foi rejeitado, seja porque o cliente aceitou a contraproposta, ou porque a proponente rejeitou a liquidação que excedeu em 15% o valor do contrato original, entre outras possibilidades
CANCELLED: Indica que o cliente cancelou o pedido de portabilidade de crédito
PAYMENT_ISSUE: Indica que a Instituição Credora encontrou alguma inconsistência na liquidação efetuada e que a Instituição Proponente deverá realizar ajustes conforme sugerido pela Instituição Credora para solucionar a pendência antes do cancelamento do pedido de portabilidade de crédito
Data e hora da atualização do status
Data e hora em que o contrato teve o status atualizado. Uma string com data e hora conforme especificação ISO-8601, sempre com a utilização de timezone UTC(UTC time format).
Motivo da recusa
Motivo de recusa do pedido de portabilidade.
Só será preenchido caso o status seja REJECTED, CANCELLED ou PAYMENT_ISSUE
A consulta ao endpoint de GET é requerida para o fluxo de portabilidade
Rejeitado por
Informar usuário responsável pela rejeição da proposta, onde: PROPONENTE - Indica que o pedido de portabilidade de crédito foi rejeitado pela proponente, seja porque a proponente rejeitou a liquidação que excedeu em 15% o valor do contrato original, entre outras possibilidades. USUARIO - Indica que o cliente cancelou o pedido de portabilidade de crédito. CREDORA- Indica que a Instituição Credora cancelou o contrato por retenção do cliente ou outros motivos conforme motivo de recusa.
Só será preenchido caso o status seja REJECTED ou CANCELLED
[ PROPONENTE, USUARIO, CREDORA ]
xfapi¹
UUID que identifica uma transação específica entre dois participantes. Esse dado pode ser encontrado no header x-fapi-interaction-id informado pelo Client e devolvido pelo Server. Mais informações em Cabeçalhos HTTP na documentação do Open Finance Brasil. O envio dessa informação é obrigatório, exceto nos casos ontem ela não esteja disponível como, por exemplo, em respostas com status 5xx, ou em chamadas que terminaram por timeout onde o reporte tem que ser enviado, mas sem esse atributo. Nos demais cenários, o envio é obrigatório.
endpoint¹
Identificação do endpoint que foi utilizado na transação reportada. A identificação do endpoint deve estar entre as entradas desse enum para ser considerado válido. Nesse campo não deve ser utilizado o path da requisição original, uma vez que ao comparar com os valores dessa enum, ele não será considerado válido.
endpointUriPrefix¹
Endereço do servidor de destino da chamada, incluindo o prefixo quando houver. O formato do campo deverá ser o seguinte:
https://{host}/{prefixo
}, sendo:
host: endereço FQDN do servidor de destino
prefixo: toda a parte do path que vem antes da string /open-banking
Método¹
Método HTTP da solicitação.
[ GET, POST, PUT, DELETE, PATCH ]
Id de Correlação
ID de correlação que identifica uma sequência de chamadas inter-relacionadas no ecossistema. Diferente do fapiInteractionId que serve para identificar cada par request-response (interação), o identificador de correlação serve para ligar diferentes reportes quando estes representam uma jornada ou uma sequência de chamadas. Este valor é de livre provimento pelo reportador.
statusCode¹
Status de retorno HTTP da solicitação. No caso de ocorrer um timeout client side preencher com um código 403 (conforme documentação ).
Intervalo de tempo do processo
Tempo em milissegundos inteiros decorrido desde o registro do timestamp até a chegada do primeiro byte da resposta do server.
Id da organização atuando como CLIENT¹
Identificador da organização de onde a chamada foi disparada.
Id da organização atuando como SERVER¹
Identificador da organização para onde a chamada foi feita.
clientSSId¹
Identificador do software statement de onde a chamada foi disparada. A PCM garante que foi esta orgId que obteve o token de acesso utilizado neste reporte.
Papel¹
ENUM indicando se o reporte que está sendo enviado apresenta a visão do server ou do client.
[ CLIENT, SERVER ]
hasFinancialAgent¹
Indica se a instituição trabalha com agente financeiro ao invés da conta reserva
¹ Campos com preenchimento obrigatório para que a mensagem seja considerada válida na ingestão
Documentação da API
Documentação da API - PCM

---
                            title: "Documento de Requisitos do Produto - PRD - CF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1500348417_Documento+de+Requisitos+do+Produto+-+PRD+-+CF"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1500348417/Documento+de+Requisitos+do+Produto+-+PRD+-+CF"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Documento de Requisitos do Produto - PRD - CF - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Portabilidade de Crédito – Consignado Federal (CF)
2
1. Introdução
2.1
1.1 Contexto
2.2
1.2 Problema
2.3
1.3 Objetivo
2.4
1.4 Solução
3
2. Escopo
3.1
2.1 Assuntos contemplados
4
3. Funcionalidades
4.1
3.1 Etapa de Solicitação
4.1.1
3.1.1 Mapeamento dos Dados Necessários para Pedido da Portabilidade
4.1.2
3.1.2 Consentimento e Formalização do Pedido
4.1.3
3.1.3 Adequações na especificação de Dados Transacionais
4.1.4
3.1.4 Gestão de Simultaneidade
4.1.5
3.1.5 Comunicações
4.1.6
3.1.6 Regra de Limitação e Avaliação da Proposta
4.2
3.2 Etapa de Efetivação
4.2.1
3.2.1 Regra de Envio da Contraproposta
4.2.2
3.2.2 Desistência do pedido de portabilidade antes da efetivação
4.2.3
3.2.3 Motivos de Recusa
4.2.4
3.2.4 Cenários de Disputa
4.3
3.3 Etapa de Liquidação
4.3.1
3.3.1 Mapeamento de Dados Necessários e Transferência de Recursos
4.3.2
3.3.2 Confirmação de Recebimento e Confirmação da Efetivação
4.3.3
3.3.3 Registro e armazenamento
5
4. Obrigatoriedade de participação
6
5. Perguntas e respostas
7
6. Glossário
8
7. Apêndice
9
8. Referências
Portabilidade de Crédito – Consignado Federal (CF)
GT
Responsável:
Portabilidade de Crédito
Responsável pela frente:
Rudy Parra Corrêa
Data da Última Atualização:
06/05/2026
1. Introdução
Este documento descreve os requisitos de produto para a implementação do serviço de solicitação de Portabilidade de Crédito no âmbito do Open Finance Brasil (
OFB
). A iniciativa visa aumentar a competitividade, reduzir o tempo de solicitação e simplificar o processo para o usuário final.
1.1 Contexto
A Portabilidade de Crédito permite que usuários transfiram suas operações de crédito e arrendamento mercantil entre instituições financeiras em busca de melhores condições. Atualmente, a solicitação de portabilidade pode ser feita via registradora. A implementação da solicitação de portabilidade, alinhada à agenda do Open Finance Brasil (
OFB
), visa agilizar e simplificar o processo.
1.2 Problema
O processo atual de solicitação de portabilidade de crédito pode ser demorado e complexo, o que desestimula a utilização do serviço por parte dos clientes. Além disso, o desconhecimento do público em relação à portabilidade de crédito limita o potencial de utilização desse serviço.
1.3 Objetivo
O objetivo deste projeto é viabilizar um serviço de portabilidade de crédito ágil e fácil no âmbito do
OFB
, tornando o processo mais competitivo e transparente, proporcionando aos clientes:
Aumento da competitividade entre instituições financeiras.
Redução do tempo de solicitação.
Simplificação do processo.
1.4 Solução
Para viabilizar a Portabilidade de
Crédito Consignado Federal
, a solução utilizará de recursos do Open Finance para obter o consentimento dos dados transacionais do cliente e acessar as informações dos seus contratos elegíveis a portabilidade. Para as demais etapas do processo de portabilidade, será desenvolvida uma nova especificação.
2. Escopo
2.1 Assuntos contemplados
Este
PRD
aborda os seguintes assuntos relacionados ao fluxo de portabilidade de crédito:
Etapa de Solicitação:
Mapeamento dos dados:
Definição das informações necessárias para viabilizar o pedido de portabilidade de crédito.
Consentimento e formalização do pedido:
Utilização do consentimento atual para dados de crédito e criação de um processo de formalização específico para validar o pedido.
Mapeamento de adequações nos Dados Transacionais:
Adaptação da especificação de Empréstimos para o produto Consignado Federal.
Gestão de simultaneidade:
Regra para lidar com múltiplas solicitações de portabilidade para o mesmo contrato.
Notificações e alertas:
Definição das etapas e mensagens para notificar o cliente sobre o progresso da solicitação.
Regra de limitação e avaliação da proposta:
Garantir o cumprimento da regra referente ao prazo da operação.
Etapa de Efetivação:
Regra de envio da contraproposta:
Definição do prazo e regras para o envio e aceite da contraproposta pela instituição credora original.
Desistência do pedido antes da efetivação:
Permitir que o cliente desista da portabilidade antes da liquidação.
Motivos de recusa:
Definir os principais motivos de recusa da portabilidade.
Cenários de disputa:
Elaboração de cenários de disputa específicos para portabilidade de crédito.
Etapa de Liquidação:
Mapeamento dos dados necessários para liquidação:
Definição das informações necessárias para a transferência de recursos.
Transferência de recursos:
Definição do processo de transferência de recursos entre as instituições.
Confirmação de recebimento:
Confirmação do recebimento dos recursos pela instituição credora original.
Confirmação da efetivação:
Confirmação da efetivação da portabilidade de crédito via API.
Registro e armazenamento:
Definição do prazo e informações a serem armazenadas pelas instituições.
3. Funcionalidades
Esta seção detalha as funcionalidades a serem implementadas em cada etapa do fluxo de portabilidade de crédito.
3.1 Etapa de Solicitação
3.1.1 Mapeamento dos Dados Necessários para Pedido da Portabilidade
Os seguintes dados serão necessários para solicitar a portabilidade de crédito:
Dados do Devedor:
CPF, telefone ou e-mail.
Dados do Contrato:
Número do contrato, taxa anual, taxa nominal, taxa efetiva, custo  efetivo Total - CET (com identificação se tem seguro contratado), prazo da operação, sistema de amortização e valor das prestações.
Proposta da Instituição Proponente:
Taxa anual, taxa nominal, taxa efetiva, CET, prazo da operação, sistema de amortização, valor das prestações e o saldo devedor utilizado como base para construção da proposta.
Índice de Preço:
Índice ou base de remuneração a ser utilizada (se aplicável).
Observação: Índice de Preço é calculado com base em indicadores previamente definidos, geralmente vinculados a índices oficiais de inflação, como o
IPCA
ou o
IGP-M
.
Dados da Instituição Proponente:
CNPJ (opcional).
3.1.2 Consentimento e Formalização do Pedido
Consentimento:
Se o cliente já consentiu o compartilhamento de dados de operações de crédito e o consentimento estiver ativo, não será necessário um novo. Caso contrário, será preciso obtê-lo.
Expiração do consentimento:
Para garantir a continuidade do processo de portabilidade pelo trilho do
OFB
, a instituição proponente deve assegurar que o consentimento esteja válido por, no mínimo, 15 dias corridos após a solicitação. Caso o consentimento esteja próximo da expiração, é necessário solicitar sua renovação antes do início do pedido, evitando contratempos no fluxo e garantir a continuidade do processo conforme o esperado.
Revogação do consentimento:
Caso o cliente revogue o consentimento após a solicitação de portabilidade de crédito já estar em andamento, o pedido deverá seguir normalmente. A revogação do consentimento de operação de crédito não implica o cancelamento automático da portabilidade. O cancelamento do pedido deve ocorrer somente mediante manifestação expressa do cliente, por meio da funcionalidade de cancelamento disponível no canal digital da instituição proponente ou credora, conforme descrito no item “Desistência do pedido de portabilidade antes da efetivação”.
Ponto importante:
Na etapa de liquidação, a instituição proponente poderá efetuar o pagamento com base no saldo devedor e nos dados contratuais previamente capturados. Caso a instituição credora identifique divergência no valor recebido, deverá atualizar a máquina de estados para refletir a ocorrência dessa inconsistência, conforme o fluxo previsto para este cenário.
Observação: A instituição receptora dos dados deve garantir que o escopo dos dados acessados seja adequado à finalidade de uso, conforme a Resolução Conjunta nº 1.
Formalização:
Cada instituição definirá seu mecanismo de autenticação para formalizar o pedido (senha, token SMS, token por e-mail etc.). A formalização deverá ser realizada exclusivamente por meio eletrônico, exceto nos casos ou estados onde houver regulamentação que exija obrigatoriamente a assinatura física.
3.1.3 Adequações na especificação de Dados Transacionais
Para obter a lista de contratos de empréstimos do cliente na Instituição Credora consulte as regras estabelecidas na documentação técnica da
API de Empréstimos
.
3.1.4 Gestão de Simultaneidade
Para evitar o envio de múltiplas solicitações de portabilidade para o mesmo contrato, as instituições devem implementar mecanismos que permitam: recusar solicitações simultâneas de portabilidade de crédito referentes ao mesmo contrato, seja por meio da registradora ou do Open Finance Brasil (
OFB)
, priorizando sempre a solicitação mais antiga. A instituição credora original é responsável por atualizar o status do contrato diariamente.
Consultar solicitações de portabilidade em andamento:
A instituição proponente deve consultar a
API
de Portabilidade de Crédito para verificar se um contrato de empréstimo já possui um pedido de portabilidade anterior, seja pelo fluxo da registradora ou pelo do
OFB
. A atualização dessas informações na API é de responsabilidade da instituição credora original.
Recusar novas solicitações de portabilidade, caso já tenha uma em andamento:
Não será permitido registrar um novo pedido de portabilidade para um contrato que já possua uma solicitação em andamento, garantindo a prioridade para a primeira solicitação registrada.
3.1.5 Comunicações
As comunicações previstas devem ser compartilhadas com o cliente durante a solicitação da portabilidade, por meio de textos definidos na jornada ou por notificações, conforme a estratégia de negócio adotada por cada instituição.
Evento
Gatilho
Origem
Casos de Uso
Resposta
Destinatário
Premissa da Notificação
Evento
Gatilho
Origem
Casos de Uso
Resposta
Destinatário
Premissa da Notificação
Fornecer o consentimento
Cliente informa a instituição credora
Canal digital proponente
Cliente deseja realizar o consentimento
Notificação de início do processo de consentimento
Cliente
Destacar a importância de realizar o consentimento para dar continuidade ao fluxo de solicitação da portabilidade.
Seleção do contrato
Cliente informa o contrato que deseja portar
Canal digital proponente
Cliente deseja portar o crédito para a instituição proponente
Confirmação de recebimento da solicitação e prazo estimado para análise
Cliente
Em casos de análise assíncrona, é essencial informar o prazo estimado para conclusão e apresentação da nova proposta.
Análise da proposta
Proposta de portabilidade recebida
Canal digital proponente
Cliente realiza avaliação das condições para seguir com o pedido da portabilidade
Confirmação de que a proposta foi aceita e seguirá para os próximos passos
Cliente
Destacar que a proposta apresentada foi aceita e que o processo de formalização do pedido terá continuidade.
Aceite do contrato
Contrato da nova operação é exibido
Canal digital proponente
Cliente realiza conferência das informações do contrato
Notificação para aceite do contrato
Cliente
Destacar que para dar continuidade ao pedido de portabilidade, é necessário que leia e aceite as condições contratuais, sinalizando que o valor da parcela pode sofrer alterações (essa informação deve ser apresentada no documento de formalização - CCB ou jornada de acordo com a estratégia da instituição).
Nesta etapa, é importante que o documento (CCB) seja exibido, para que o cliente tenha visibilidade do resumo da nova operação de crédito e do resumo contratual. O modelo e as cláusulas do documento serão definidos por cada instituição.
Autenticação do aceite
Autenticação/validação do aceite
Canal digital proponente
Cliente realiza a autenticação/validação do contrato
Notificação para confirmar a autenticação
Cliente
Ressaltar que o mecanismo de autenticação utilizado foi validado com sucesso.
Conclusão do aceite
Portabilidade concluída com sucesso
Canal digital proponente
Finalização do pedido de portabilidade de crédito
Confirmação de que o pedido da portabilidade foi concluído com sucesso
Cliente
Ressaltar que o pedido de portabilidade será enviado à instituição credora original e que o processo pode levar até 5 dias úteis.
Contraproposta
Estímulo/oferta da contraproposta
Canal credora
Credora aciona o cliente para envio da contraproposta
Notificação para informar o envio da contraproposta
Cliente
Sinalizar que o acionamento foi necessário pelo pedido de portabilidade de crédito com o banco XPTO, e que o aceite da proposta deve ser feito em até 3 dias úteis, caso contrário, o pedido será automaticamente sequenciado.
Contraproposta
Aceite da contraproposta
Canal digital credora
Cliente realiza aceite da contraproposta
Confirmação de que o pedido da portabilidade foi cancelado
Cliente
Informar que o pedido de portabilidade foi cancelado.
Conclusão do pedido
Não aceite da contraproposta
Canal digital proponente
Cliente não aceita a contraproposta enviada
Notificação para informar que a portabilidade foi efetivada.
Cliente
Ressaltar que o pedido de portabilidade foi concluído com sucesso.
Problemas no processo
Erro durante o processo de portabilidade
Canal digital proponente e credora
Interrupção do processo devido a erro
Notificação de erro e instruções para resolução
Cliente
Não exibir erros no formato 4xx, 5xx (ex.:403, 404, 409 e 422). A API deve retornar o erro, que deve ser interpretado e, se necessário, exibir ao cliente uma mensagem clara do que precisa ser feito para resolução.
Realizar autorização no site SouGov
Cliente informa o contrato que deseja portar
Canal digital Proponente
Cliente deseja portar o crédito para a instituição proponente, porém ainda não realizou a autorização no site do SouGov
Notificação para solicitar a autorização
Cliente
Destacar a importância de fornecer a autorização para dar continuidade ao fluxo da solicitação da portabilidade.
Autorização não identificada
Cliente tenta realizar a autorização
Site SouGov
Cliente deseja realizar a autorização do contrato para seguir com o pedido de portabilidade
Proponente redireciona o cliente ao site SouGov para nova tentativa
Cliente
Destacar a importância de realizar a autorização do contrato no site SouGov antes de dar continuidade ao fluxo de solicitação da portabilidade.
3.1.6 Regra de Limitação e Avaliação da Proposta
A instituição proponente deve exibir os contratos elegíveis para solicitação de portabilidade do produto Crédito Consignado Federal, considerando que a proposta pode incluir carência, conforme a estratégia da instituição financeira. A validação do percentual de comprometimento de renda é responsabilidade da instituição. Além disso, deve estabelecer um processo que assegure a exibição do comparativo entre o contrato original e a nova proposta, destacando as informações listadas a seguir:
Saldo devedor.
Para
(indicando a instituição de destino).
De
(indicando a instituição de origem).
Diferença das parcelas
(indicando o valor de redução/aumento em relação ao contrato de origem).
Diferença total do somatório das parcelas
(indicando o valor de redução/aumento total em relação ao contrato de origem).
Novo prazo
(indicando a quantidade de parcelas remanescentes até o fim do novo contrato).
Prazo remanescente
(indicando a quantidade de parcelas remanescentes até o fim do contrato de origem).
Nova parcela
(indicando o valor da parcela do novo contrato).
Parcela atual
(indicando o valor da parcela do contrato de origem).
Nova taxa de juros
(indicando a taxa de juros do novo contrato).
Taxa de juros atual
(indicando a taxa de juros do contrato de origem).
Novo CET
(indicando o Custo Efetivo Total do novo contrato).
CET atual
(indicando o Custo Efetivo Total do contrato de origem).
Data da primeira parcela do novo contrato.
Data da última parcela do novo contrato.
Além da exibição da tela comparativa, é necessário garantir o cumprimento das seguintes regras:
Prazo remanescente da operação:
A nova proposta deverá estabelecer um prazo igual ou inferior ao do contrato original, propostas que não sigam essa regra devem ser bloqueadas automaticamente pela instituição proponente e não ser exibida ao cliente.
Saldo devedor:
O valor da operação da nova proposta não deve exceder o saldo devedor do contrato original.
Periodicidade:
Não deve haver mudança de periodicidade entre o novo contrato e o contrato original.
Ponto importante:
Conforme orientação do regulador transmitida na reunião bilateral realizada em 05/12, não será mais necessária a aplicação de uma regra para o valor da parcela a maior, conforme previsto inicialmente. Ainda assim, é fundamental manter a comunicação sobre as condições operacionais nessa etapa.
Fluxograma da Regra de Limitação e Avaliação da Proposta:
O fluxograma detalhado está apresentado na imagem abaixo.
Open
Abandono e Retomada da jornada:
Em caso de abandono da jornada na etapa de avaliação da proposta, a retomada poderá ocorrer em dois momentos, definidos pela instituição proponente:
Cliente retoma a jornada na etapa de seleção dos contratos.
Cliente retoma a jornada na etapa de apresentação da proposta.
Para que o cliente possa retomar a jornada na etapa de apresentação da proposta, as condições operacionais apresentadas inicialmente precisam estar ativas.
Ponto importante:
O pedido de portabilidade de crédito só será efetivado na etapa de autenticação.
3.2 Etapa de Efetivação
3.2.1 Regra de Envio da Contraproposta
A instituição credora original terá até 3 dias úteis para enviar uma contraproposta ao cliente, contados a partir do primeiro dia útil após a solicitação de portabilidade. A instituição credora pode enviar quantas propostas entenderem aderente à sua estratégia dentro do prazo estabelecido, desde que a máquina de estados não tenha sido atualizada. As regras mencionadas no item “Regra de Limitação e Avaliação da Proposta” também devem ser consideradas para a oferta da contraproposta.
Na contagem dos dias, devem ser considerados dias úteis somente os dias de segunda a sexta-feira, exceto os feriados bancários.
Ponto importante:
No escopo do serviço de Portabilidade de Crédito para o produto
Crédito Consignado Federal
no trilho do OFB, não está prevista a oferta de troco.
Regras Detalhadas:
Para garantir o cumprimento do prazo de 3 dias úteis, foram definidas as seguintes regras:
Início do Prazo de Portabilidade:
A contagem do prazo de 3 dias úteis inicia no primeiro dia útil após a solicitação de portabilidade.
Notificação de Retenção:
A instituição credora original deverá informar a instituição proponente sobre a retenção ou não da operação e atualizar a máquina de estados até as 10 horas da manhã, independentemente do dia útil.
Ponto importante:
Conforme orientação do regulador transmitida na reunião bilateral realizada em 05/12, o horário para a instituição credora original informar a instituição proponente deve ser o mesmo, independentemente de a operação ter sido retida ou não.
Aceite da Contraproposta:
O cliente poderá aceitar a contraproposta até às 9h do terceiro dia útil.
Ponto importante:
Após a disponibilização da contraproposta ao cliente em seu canal digital, a instituição credora original não poderá removê-la ou bloqueá-la antes do prazo previsto para aceite. A partir das 9h do terceiro dia, a contraproposta não poderá mais ser aceita. Nesse momento, a instituição credora original poderá removê-la do canal digital ou bloqueá-la para impedir o aceite.
Procedimentos:
A instituição credora original, caso tenha interesse em reter a operação, poderá contatar o cliente por meio do canal de sua escolha (físico ou digital) para apresentar a contraproposta.
A oferta da contraproposta deve estar disponível no canal digital da instituição credora original, pois o aceite do cliente deverá ocorrer exclusivamente por esse canal.
Ponto importante:
Nesta etapa, deve ser exibida uma tela comparativa no canal digital da instituição credora original para evidenciar as condições operacionais das propostas da instituição proponente e da instituição credora original (ex.: CET). O objetivo é permitir que o cliente compare as condições com facilidade e escolha a proposta mais vantajosa. As regras mencionadas no item “Regra de Limitação e Avaliação da Proposta” devem ser consideradas esta etapa.
Se o cliente aceitar a contraproposta dentro do prazo previsto na regra “Aceite da Contraproposta”, a instituição credora original deve informar à instituição proponente que a operação foi retida, atualizando o status do pedido de portabilidade na máquina de estados até às 10h da manhã. Além disso, é de responsabilidade da instituição credora original atualizar o contrato no SouGov (autorização para renovar o contrato), logo após a assinatura/aceite do cliente.
Caso o cliente não aceite ou não responda à contraproposta dentro do prazo previsto em regra, a instituição credora original deve comunicar à instituição proponente que o pedido de portabilidade pode prosseguir, atualizando o status do pedido na máquina de estados até às 10h da manhã. Após essa notificação, a instituição proponente deve solicitar à averbadora a reserva da margem consignável referente ao contrato de empréstimo em questão.
Exemplo:
Caso a credora receba o pedido de portabilidade entre 10h e 23h59 e opte por liberar imediatamente o contrato para a proponente, a atualização da máquina de estados para o estado adequado deve ocorrer apenas entre 0h e 10h do próximo dia útil. Essa prática garante que a proponente tenha tempo hábil para efetuar o pagamento ainda no mesmo dia em que a máquina de estados for atualizada.
3.2.2 Desistência do pedido de portabilidade antes da efetivação
O cliente poderá desistir do pedido de portabilidade de crédito a qualquer momento antes de ocorrer a liquidação da operação, tanto no canal digital da instituição proponente quanto no canal digital da instituição credora original.
Ponto importante:
O prazo final para desistência do pedido será até o primeiro evento entre: (i) 9h do terceiro dia útil após a solicitação ou (ii) atualização da máquina de estados pela instituição credora original.
Procedimentos:
Na jornada de portabilidade de crédito via
OFB
, nos canais digitais da instituição proponente e da instituição credora original, o cliente deve ter uma opção clara para cancelar o pedido a qualquer momento antes da liquidação.
Se o cliente desistir do pedido de portabilidade através do canal digital da instituição proponente, esta deve comunicar a desistência à instituição credora original. Da mesma forma, se a desistência ocorrer no canal digital da instituição credora original, esta deve comunicar a desistência à instituição proponente. A comunicação de ambas deve ocorrer por meio da atualização da máquina de estados.
O contrato original deve permanecer disponível para um novo pedido de portabilidade no futuro, após o cancelamento.
Interface do Cliente:
Tanto a jornada da instituição proponente, como a jornada da instituição credora original devem contemplar uma interface/menu que permita ao cliente visualizar o status do pedido de portabilidade e acessar a opção de cancelamento.
Serviço de Comunicação:
● Para gerenciar as desistências do devedor, será criado um serviço de comunicação (endpoint – API Portabilidade de Crédito) baseado em eventos.
● O serviço comunicará a instituição envolvida sobre mudanças no estado do pedido de portabilidade de crédito, incluindo a desistência.
Diagrama do Serviço de Comunicação:
Open
3.2.3 Motivos de Recusa
Motivos padronizados de recusa e inconsistências que possam impedir a conclusão de um pedido de portabilidade na jornada do
OFB
.
O manual deve:
Justificar a não aceitação do pedido de portabilidade.
Assegurar a conformidade do processo.
Motivos de Cancelamento pela Instituição Proponente:
Motivo de Recusa
Detalhamento
Etapa
Considerações
Motivo de Recusa
Detalhamento
Etapa
Considerações
Cancelado pelo cliente
Cliente desiste do pedido da portabilidade
Após solicitação do pedido de portabilidade
Sem considerações
Valor do saldo devedor atualizado substancialmente divergente do valor informado inicialmente
Saldo devedor atualizado divergente (superior a 15%) do informado inicialmente
Liquidação
Sem considerações
Política de crédito
Proponente desiste da oferta ao cliente por políticas internas
Liquidação
Sem considerações
Reserva da margem
Não foi possível realizar a reserva da margem consignada pela instituição proponente.
Liquidação
Todas as situações relacionadas a problemas com a margem devem ser tratadas de forma agrupada. Exemplos: contrato não existir mais no SERPRO, perda da autorização da instituição proponente para reserva da margem, verificação sobre a averbação, entre outros.
Ponto importante:
Na averbação, o estorno de STR pela proponente deve ser solicitado apenas após o prazo técnico de liberação da margem expirar, caso a credora não a tenha liberado
Motivos de Recusa pela Instituição Credora:
Motivo de Recusa
Detalhamento
Etapa
Considerações
Motivo de Recusa
Detalhamento
Etapa
Considerações
Retenção do Cliente
Cliente aceitou contraproposta da instituição credora original (dentro do prazo).
Aceite da contraproposta
Deve ocorrer monitoramento para assegurar que a contraproposta foi aceita pelo cliente no canal digital da instituição credora, mediante apresentação de evidências geradas pelo log da API.
Contrato já liquidado
Contrato liquidado pelo
cliente.
Liquidação
Sem considerações.
Divergência de dados referente ao pagamento efetuado
Proponente realizou a liquidação com valor divergente e retentativas não foram satisfatórias
Confirmação do recebimento
Sem considerações.
Portabilidade cancelada por falta de liquidação
Proponente não realizou a liquidação da portabilidade
Confirmação do recebimento
Sem considerações.
Portabilidade em andamento
Posteriormente à efetivação do pedido de portabilidade, a
IF
credora original identificou que o cliente já possui outro pedido de portabilidade em andamento para o mesmo contrato.
Formalização/antes do envio da contraproposta
Sem considerações.
Cliente com ação judicial
Possui ação judicial
Liquidação
Avaliar a possibilidade de quando for selecionado este motivo, o cliente seja orientado de como resolver a situação.
Modalidade da operação incompatível
Modalidade divergente da indicada pela instituição proponente
Solicitação do pedido de portabilidade
Sem considerações
Cancelado pelo cliente
Cliente desiste do pedido da portabilidade
Após solicitação do pedido de portabilidade
Sem considerações
3.2.4 Cenários de Disputa
Cenários de disputa relacionados ao fluxo de portabilidade de crédito no trilho do Open Finance.
Esses cenários visam:
Atualizar o manual de cenários de disputa do
OFB
.
Incluir fluxos padronizados que detalhem o processo de portabilidade de crédito.
Permitir que as instituições consultem e sigam as orientações de forma consistente.
Os cenários definidos serão incorporados ao manual existente em uma seção específica dedicada ao fluxo de portabilidade de crédito.
Cenários de Disputa:
Cenário Macro
Cenário
Categorias
Responsável Inicial
Cenário Macro
Cenário
Categorias
Responsável Inicial
Informações para pagamento
Saldo devedor atualizado com valor muito superior ao esperado
Saldo devedor com valores inconsistentes, em um percentual muito maior do que o esperado (sugestão inicial conforme ciclo da registradora de 15%), devido a uma inconsistência no sistema e/ou benefício para a credora original, que deseja que a portabilidade seja cancelada pela proponente.
Credora
Informações para pagamento
Dados bancários inconsistentes
Dados bancários incorretos por culpa ou dolo da credora original.
Credora
Informações para pagamento
Dados bancários indisponíveis

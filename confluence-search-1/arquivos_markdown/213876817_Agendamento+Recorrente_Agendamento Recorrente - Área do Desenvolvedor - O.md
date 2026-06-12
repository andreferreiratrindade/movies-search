---
                            title: "Agendamento Recorrente - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "213876817_Agendamento+Recorrente"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/213876817/Agendamento+Recorrente"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Agendamento Recorrente - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1 - Histórico de versionamento
O Guia segue seu próprio versionamento. Cada versão do documento é salva com um numero incremental: 0.1, 0.2, 0.3 sucessivamente, até que a versão do documento seja aprovada e publicada. Com a publicação, passa a ser versão 1.0. Versões editadas subsequentemente a versão inicial publicada, passam a ser 1.1, 1.2, ..., 1.x. Sendo "x" um número que represente mudanças pequenas, conhecidas como
minor
. Se a mudança proposta for considerada uma
major
, mudamos a numeração completa, indo para 2.0, 3.0, etc.
O GT especificações e serviços será o responsável por definir o versionamento do documento para cada uma das alterações futuras.
2 - Introdução
Bem-vindo ao guia sobre a funcionalidade de agendamento de pagamentos recorrentes, uma poderosa ferramenta projetada para proporcionar conveniência e eficiência em transações financeiras. Ao longo deste guia, exploraremos em detalhes como essa funcionalidade é implementada no âmbito do Open Finance Brasil.
A funcionalidade tem como principal objetivo permitir que usuários agendem múltiplos pagamentos para um recebedor específico, mantendo uma relação direta e eficiente de "1:1" entre pagador e recebedor. Oferecida como um micro serviço no ecossistema do Open Finance Brasil, esta funcionalidade é uma adição valiosa das opções de pagamento existentes, que incluem pagamentos únicos, agendados ou imediatos.
Os pagamentos podem ser programados de acordo com a preferência do usuário, seja mensalmente, semanalmente, diariamente ou em datas customizadas definidas pelo próprio usuário, proporcionando uma experiência altamente personalizada. Destinada tanto a consumidores individuais quanto a empresas, a funcionalidade visa atender às necessidades diversificadas de uma gama ampla de usuários. A segurança é prioridade, com a autenticação realizada através do fluxo FAPI Hybrid Flow com OAuth2, garantindo transações seguras e protegidas.
Além da facilidade no agendamento de múltiplos pagamentos, esta funcionalidade promete economia de tempo e uma gestão simplificada de pagamentos recorrentes, proporcionando uma solução abrangente para os desafios financeiros cotidianos. Ao seguir este guia, você será guiado por todos os aspectos necessários para a implementação e aproveitamento máximo dessa funcionalidade de agendamento de pagamentos recorrentes.
Essa funcionalidade está presente na API de pagamentos, a partir de sua versão 4.0.0. O link para a API pode ser encontrado abaixo.
Pagamento único, imediato ou agendado, e agendamento recorrente
Pagamentos únicos, agendados ou imediatos, são pagamentos que ocorrerão, por natureza e definição, apenas uma vez, instantâneos ou agendados para uma data futura. Já os agendamentos recorrentes representam mais de um pagamento agendado utilizando o mesmo consentimento.
3 - Regras de negócios para agendamentos recorrentes
No quadro abaixo, entraremos com mais detalhes sobre as regras de negócio dos agendamentos recorrentes, o que deve-se considerar quando consumir o serviço e quais são os parâmetros necessários para utilizar corretamente o modelo de pagamentos descrito e passível de realização.
Atentem-se que
pagamentos únicos imediatos ou agendados não estão contemplados
na documentação abaixo, visto que é um produto já consolidado no ecossistema, sua documentação não será alterada e nem contemplada neste guia.
Agendamento recorrente
Agendamento recorrente
Casos de uso
(Sugestões BC)
Mesada, doação, outras remessas recorrentes, pagamento de serviços diversos (ex.: diarista, professor particular)
Configurações de recorrência
Motor de recorrência
Criação de um consentimento para recorrência com limites de quantidade, valores e prazos
Valor
Fixo
Modelo de recorrência, intervalos de pagamentos
Diário, semanal, mensal ou customizado
Gestão da Agenda
Compartilhada: Iniciador e Detentor
Comanda o pagamento
Pagador (quem iniciou o pagamento)
Recebedor
PJ ou PN
Primeiro pagamento
Agendado
Demais pagamentos
Agendado
Permite pagamentos imediatos
Não
Definição do final do período da recorrência
Período determinado
Prazo máximo de duração para recorrência do consentimento
24 meses
Permite a configurar data de início do consentimento?
Sim
Permite a configurar data de expiração do consentimento?
Não, período já determinado
Permite limites globais do consentimento?¹
Não
Permite limites periódicos por consentimento?
Não (valor limite é fixo)
Permite limites por transação?
Não (valor limite é fixo)
Processo de adesão
Fluxo de adesão
Consentimento de uso único
Role
no diretório
CONTA, PAGTO
Será possível editar configurações de recorrência no processo de adesão no Detentor?
Não
Cancelamento do fluxo da adesão
Via Iniciador ou Detentor
Permite múltiplas alçadas?
Sim
Iniciador terá acesso aos status do processo de adesão via Webhook?
Sim
Adesão tem id de contrato?
Não
Gestão de adesão
Permite edição técnica dos dados do consentimento pós adesão²?
Não. Necessário cancelar consentimento atual e criação de um novo consentimento.
Cancelamento da adesão
Pelo pagador, no ambiente da iniciadora ou detentora
Revogação da adesão
Não há
Consumação³ da adesão?
Detentor
Processo de liquidação
Canal para liquidação
Canal secundário (obedecendo as regras da trilha Pix)
Dispara o pagamento⁴
Detentor
Onde o cliente cancela o pagamento?
Iniciadora ou Detentora
Erros de saldo insuficiente modificam o status do consentimento?
Não
Listagem das informações do pagamento
Busca uma a uma das incidências via
paymentId
Iniciador é responsável pelo envio da ocorrência do pagamento?
Sim, todos os pagamentos são enviados em um unico
payload
pós a criação do consentimento
Quem avisa o pagador sobre pagamento com falha?
Iniciador e Detentor⁵. Detentor deverá notificar via webhook o iniciador e o iniciador decidir se e como notificar o pagador
Responsável pela geração do endToEndId
Iniciador
A data agendada no consentimento e a data agendada do E2EID podem ser distintas?
Sim, somente nos casos do dia “não existir”. (ex.: agendamento para todo dia 31. Alguns meses não possuem dia 31)
Qual é o localInstrument utilizado na liquidação?
MANU | QRES | DICT
Outras informações
É possível habilitar crédito?
Seguir a regra do arranjo. Habilitar na detentora no momento da adesão do consentimento. Na confirmação do consentimento é necessário um aviso ao cliente que o uso de linha de crédito pré-aprovada na instituição detentora de conta está habilitado e poderá ser alterado na detentora em ambiente de gestão do Pix Automático.
Retentativas
Seguir as regras do arranjo.
Funcionalidade de contestação
Não
Legenda
1 - Limite específico para um determinado consentimento, por exemplo, limite de R$100 por dia (periódico) ou R$300 para o intervalo do consentimento (global)
2 - O GT questionou o BC sobre o comportamento esperado quando houver a edição –se o usuário deverá ser redirecionado para a detentora ou não para confirmar os novos dados do consentimento
3 - Entende-se como consumação a mudança do estado, por exemplo, após 10/10 parcelas o estado será alterado de aprovado para consumido
4 - Responsável por garantir que no momento do agendamento a liquidação ocorra
5 - GT está avaliando se existe alguma normativa que obrigue uma das partes avisar ao pagador
4 - Descrição da usabilidade para agendamento recorrente
Aqui trataremos dos principais pontos de atenção que devem ser considerados quando criar uma nova solicitação de agendamento recorrente. No fluxo abaixo é possível identificar quais os passos necessários para possibilitar a criação deste tipo de pagamento.
4.1 - Fluxo do agendamento recorrente
Open
Imagem: BPMN com fluxo para realização de agendamentos recorrentes para pagamentos
ID
CAMADA
TIPO
DESCRIÇÃO
ID
CAMADA
TIPO
DESCRIÇÃO
1
Pagador
Comunicação
Início do processo. Pagador acessa ambiente do Iniciador.
2
Pagador
Ação
Pagador inclui os dados da transação. Define tipo de recorrência (diária, semanal, mensal ou personalizada) e configura os parâmetros necessários para o agendamento.
3
Pagador
Comunicação
Dados inseridos pelo usuário são encaminhados para o Iniciador.
4
Iniciador
Comunicação
Iniciador recebe as informações inseridas pelo usuário.
5
Iniciador
Ação
Valida as informações inseridas pelo usuário pagador e realiza as validações de datas de agendamentos que podem ser modificadas de acordo com feriados nacionais, estaduais ou municipais. Além das configurações do agendamento definidas pelo usuário pagador.
6
Iniciador
Comunicação
Caso alguma validação impeça o avanço, o Iniciador solicita ao usuário pagador novamente as informações que necessitam correção.
7
Iniciador
Comunicação
O Iniciador solicita ao Detentor um access_token com o scope de pagamento.
8
Detentor
Comunicação
O Detentor recebe a solicitação de access_token feita pelo Iniciador.
9
Detentor
Ação
O Detentor processa a solicitação recebida do Iniciador
10
Detentor
Comunicação
Detentor envia para o Iniciador o access_token solicitado.
11
Iniciador
Comunicação
Iniciador recebe o access_token enviado pelo Detentor.
12
Iniciador
Ação
Iniciador cria a solicitação de consentimento. O payload enviado deve estar configurado com as informações providas pelo usuário Pagador no passo 2.
13
Iniciador
Comunicação
O Iniciador envia ao Detentor a solicitação de consentimento contendo os parâmetros definidos pelo usuário Pagador.
14
Detentor
Comunicação
Detentor recebe a solicitação de consentimento enviada pelo Iniciador
15
Detentor
Ação
Detentor processa as informações recebidas do Iniciador e valida as regras de negócio definidas para os campos.
16
Detentor
Comunicação
Detentor retorna a resposta da criação do consentimento e a URL de redirecionamento.
17
Iniciador
Comunicação
Iniciador recebe a resposta da criação e a URL de redirecionamento do usuário Pagador para aplicação do Detentor.
18
Iniciador
Ação
Iniciador processa o retorno da criação do consentimento enviada ao Detentor.
19
Iniciador
Comunicação
Iniciador redireciona o Usuário Pagador para a aplicação do Detentor.
20
Pagador
Ação
No ambiente do Detentor: Usuário Pagador realiza a autenticação
21
Pagador
Ação
No ambiente do Detentor: Usuário Pagador autoriza o consentimento.
22
Pagador
Ação
Detentor muda o status do consentimento para
AUTHORISED.
23
Pagador
Ação
Se para a aprovação do consentimento for necessário múltiplos aprovadores, o Detentor deve então, através de seus mecanismos internos, notificar os outros aprovadores informando a necessidade da ação aprovação no ambiente do Detentor.
24
Pagador
Comunicação
Detentor redireciona o usuário para a aplicação da Iniciadora.
25
Iniciador
Comunicação
Iniciador recebe as informações do redirecionamento.
26
Iniciador
Ação
Iniciador valida as informações recebidas.
27
Iniciador
Comunicação
Iniciador envia solicitação de access_token com scope de pagamento.
28
Detentor
Comunicação
Detentor recebe pedido de access_token.
29
Detentor
Ação
Detentor valida a solicitação de access_token.
30
Detentor
Comunicação
Detentor retorna o access_token para o Iniciador.
31
Iniciador
Comunicação
Iniciador recebe o access_token com scope do pagamento agendado.
32
Iniciador
Ação
Iniciador cria solicitação do pagamento agendado.
33
Iniciador
Comunicação
Iniciador envia a solicitação do agendamento recorrente para o detentor de contas.
34
Detentor
Comunicação
Detentor recebe a solicitação do agendamento recorrente da Iniciadora.
35
Detentor
Ação
Detentor valida as informações da solicitação de agendamento de pagamentos e demais validações de regras de negócio.
36
Detentor
Comunicação
Detentor envia a resposta de solicitação de pagamento.
37
Detentor
Ação
Se consentimento com status
AUTHORISED
, Detentor cria recorrência de pagamentos agendados.
38
Iniciador
Comunicação
Recebe a resposta da solicitação de pagamento.
39
Iniciador
Ação
Processa o retorno do agendamento.
40
Iniciador
Comunicação
Notifica pagador do sucesso da criação da recorrência de pagamentos.
41
Pagador
Comunicação
Pagador recebe notificação de sucesso.
Alguns passos necessitam uma maior explicação do comportamento esperado do Iniciador ou Detentor dentro do fluxo, são esses:
12 - "Cria o consentimento":
Iniciador preenche o payload de consentimento contendo o objeto
schedule
. O preenchimento deve seguir as informações providas pelo usuário Pagador durante o passo 2. Considerando dois casos de uso, vejamos o preenchimento dos
payloads
, o primeiro onde o usuário pagador está tentando pagar algo semanal e o segundo algo mensal, conforme seu objetivo financeiro.
Semanal - Todas as sextas-feiras, a partir do dia 01 de janeiro de 2024, durante três semanas consecutivas.
O campo
quantity
indica a quantidade de recorrências permitidas para esse consentimento.
Neste cenário, onde o usuário pagador precisa agendar o pagamento para ocorrer uma vez por semana, o objeto
schedule
deve ser preenchido conforme o JSON abaixo:
{
"data": {
"loggedUser": {
"document": {
"identification": "11111111111",
"rel": "CPF"
}
},
"businessEntity": {
"document": {
"identification": "11111111111111",
"rel": "CNPJ"
}
},
"creditor": {
"personType": "PESSOA_NATURAL",
"cpfCnpj": "58764789000137",
"name": "Marco Antonio de Brito"
},
"payment": {
"type": "PIX",
"schedule": {
"weekly": {
"startDate": "2024-01-05",
"quantity": 3,
"dayOfWeek": "SEXTA_FEIRA"
}
},
"date": "2024-01-03",
"currency": "BRL",
"amount": "100.12",
"ibgeTownCode": "5300108",
"details": {
"localInstrument": "DICT",
"qrCode": "00020104141234567890123426660014BR.GOV.BCB.PIX014466756C616E6F32303139406578616D706C652E636F6D27300012\nBR.COM.OUTRO011001234567895204000053039865406123.455802BR5915NOMEDORECEBEDOR6008BRASILIA61087007490062\n530515RP12345678-201950300017BR.GOV.BCB.BRCODE01051.0.080450014BR.GOV.BCB.PIX0123PADRAO.URL.PIX/0123AB\nCD81390012BR.COM.OUTRO01190123.ABCD.3456.WXYZ6304EB76\n",
"proxy": "12345678901",
"creditorAccount": {
"ispb": "12345678",
"issuer": "1774",
"number": "1234567890",
"accountType": "CACC"
}
}
},
"debtorAccount": {
"ispb": "12345678",
"issuer": "1774",
"number": "1234567890",
"accountType": "CACC"
}
}
}
OBS
: Notem, não é possível agendar um pagamento recorrente para ocorrer no mesmo dia da criação do consentimento, para este caso o correto é utilizar o pagamento imediato. Caso seja interesse da instituição, ela pode oferecer o pagamento imediato junto ao agendado, utilizando os dois serviços em sequência, de maneira separada, onde o pagamento imediato e os pagamentos agendados terão seus próprios consentimentos.
Mensal - Durante um ano, todo dia 10 a partir da data de início definida pelo usuário pagador na adesão solicitação
{
"data": {
"loggedUser": {
"document": {
"identification": "11111111111",
"rel": "CPF"
}
},
"businessEntity": {
"document": {
"identification": "11111111111111",
"rel": "CNPJ"
}
},
"creditor": {
"personType": "PESSOA_NATURAL",
"cpfCnpj": "58764789000137",
"name": "Marco Antonio de Brito"
},
"payment": {
"type": "PIX",
"schedule": {
"monthly": {
"startDate": "2024-01-01",
"quantity": 12,
"dayOfMonth": 10
}
},
"date": "2024-01-03",
"currency": "BRL",
"amount": "100000.12",
"ibgeTownCode": "5300108",
"details": {
"localInstrument": "DICT",
"qrCode": "00020104141234567890123426660014BR.GOV.BCB.PIX014466756C616E6F32303139406578616D706C652E636F6D27300012\nBR.COM.OUTRO011001234567895204000053039865406123.455802BR5915NOMEDORECEBEDOR6008BRASILIA61087007490062\n530515RP12345678-201950300017BR.GOV.BCB.BRCODE01051.0.080450014BR.GOV.BCB.PIX0123PADRAO.URL.PIX/0123AB\nCD81390012BR.COM.OUTRO01190123.ABCD.3456.WXYZ6304EB76\n",
"proxy": "12345678901",
"creditorAccount": {
"ispb": "12345678",
"issuer": "1774",
"number": "1234567890",
"accountType": "CACC"
}
}
},
"debtorAccount": {
"ispb": "12345678",
"issuer": "1774",
"number": "1234567890",
"accountType": "CACC"
}
}
}
15 - "Procesa solicitação de consentimento"
A partir do sucesso da chamada deste passo, iniciam-se as validações assíncronas do consentimento.
Detentor precisa realizar as validações assíncronas levando em consideração os momentos descritos no Diagrama de sequencia da API de pagamentos, os quais podemos correlacionar com as etapas do fluxo aqui da seguinte maneira:
Etapa Diagrama de Sequência
Etapa Fluxograma do Pagamento Recorrente Agendado
Erros possíveis
Etapa Diagrama de Sequência
Etapa Fluxograma do Pagamento Recorrente Agendado
Erros possíveis

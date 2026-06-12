---
                            title: "Informações Gerais - Webhook - v1.0.0-rc.2 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "146669587_Informa+es+Gerais+-+Webhook+-+v1.0.0-rc.2"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/146669587/Informa+es+Gerais+-+Webhook+-+v1.0.0-rc.2"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Informações Gerais - Webhook - v1.0.0-rc.2 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Obrigatoriedade do Webhook
1.1
Notificação sobre consentimento:
POST /payments/[Versão da API]/consents/{consentId}
1.2
Notificação sobre pagamento:
POST /payments/[Versão da API]/pix/payments/{paymentId}
2
Notificações do Webhook
2.1
Premissas
2.2
Em caso de falha de notificação
Nessa sessão será possível encontrar orientações sobre quais eventos de resposta que a detentoras de conta devem repassar para iniciadora de pagamentos referente ao processamento de um pagamento na máquina de estado do pagamento: Consentimento e na máquina de estado do pagamento: Arranjo Pix na adoção do Webhook.
Obrigatoriedade do Webhook
Adoção do Webhook pelas instituições e para o ecossistema geram diversos benefícios, quando relacionados ao número de chamadas gerando otimização do ecossistema do Open Finance Brasil.
A implementação da funcionalidade das notificações por Webhook é:
Obrigatória para as detentoras de conta
Opcional para as iniciadoras de pagamento. Quando a iniciadora optar por implementar as notificações por Webhook deverá realizar o cadastro da URL no diretório central e demais procedimentos detalhados no guia do diretório.
Notificação sobre consentimento:
POST /payments/[Versão da API]/consents/{consentId}
Os eventos que acionarão notificações na máquina de estados do consentimento do pagamento serão os status REJECTED e CONSUMED.
Open
Eventos que acionarão notificações na máquina de estados do pagamento: Consentimento
Notificação sobre pagamento:
POST /payments/[Versão da API]/pix/payments/{paymentId}
Os eventos que acionarão as notificações via Webhook na máquina de estados pagamento: Arranjo Pix da API de Iniciação de Pagamentos serão: ACSC, RJCT, CANC, PATC, PDNG e SCHD.
Open
Eventos que acionarão notificações na máquina de estados do pagamento: Arranjo Pix
Notificações do Webhook
O consumo de informações pelos participantes do Open Finance Brasil é feito através de diversas consultas (polling), onde um participante busca avaliar se houve alguma atualização no estado de um recurso, dessa maneira eleva-se de forma significativa o consumo da infraestrutura das instituições participantes do Open Finance Brasil.
No diagrama de exemplo abaixo, é possível identificar como será o comportamento da Iniciadora de pagamentos no processo de consulta de um pagamento.
A detentora de contas envia uma notificação à instituição iniciadora de pagamento informando que ocorreu uma mudança significativa da máquina de status da API e que a mesma deverá consultar o pagamento para obter mais informações.
Exemplo
:
Open
Diagrama de sequência da consulta de um consentimento por parte da iniciadora
Open
Diagrama de sequência da consulta de um pagamento por parte da iniciadora
Premissas
O payload será composto pela informação do timestamp do momento da alteração da situação do pagamento;
A detentora de conta deve encaminhar o paymentId para iniciadora pela URL.
Em caso de falha de notificação
Detentora
A detentora de conta fará no máximo 3 tentativas de notificação:
A primeira tentativa de notificação do evento, pela detentora de conta, deverá ocorrer em até 1,5 segundo após o evento;
A segunda e a terceira tentativas só ocorrerão em caso de falha;
A segunda tentativa deverá ocorrer 10 segundos após a falha da primeira tentativa;
A terceira tentativa deverá ocorrer 60 segundos após a falha da segunda tentativa.
ITP
A iniciadora de pagamentos, ao perceber que não está recebendo as notificações oriundas da detentora de contas, poderá utilizar os endpoints de consulta para obter informações sobre o andamento de uma determinada transação do consentimento e/ou pagamento.

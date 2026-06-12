---
                            title: "Definições para o Lançamento Escalonado da Fase 3 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "17378821_Defini+es+para+o+Lan+amento+Escalonado+da+Fase+3"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378821/Defini+es+para+o+Lan+amento+Escalonado+da+Fase+3"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Definições para o Lançamento Escalonado da Fase 3 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Mensagens de erro para escalonamento da Fase 3
Estão disponíveis as orientações da Estrutura para comunicação com os usuários que passarem por algum erro na jornada, que seja ocasionado pelas definições de escalonamento da Fase 3. Mais especificamente, erros motivados por extrapolar limite de valor, limite de horário e/ou limite de público. A iniciadora deve garantir que o usuário seja impedido de iniciar um pagamento que extrapola as restrições impostas.
Orientações quanto a restrição de iniciação em função do dispositivo do usuário.
A iniciadora de pagamentos em função do período de escalonamento poderá restringir o acesso a determinados dispositivos (Celular ou desktop) e jornadas em múltiplos devices, conforme determinações estabelecidas pelo regulador.
Em ambos os casos, a iniciadora deverá avisar o cliente antes da jornada de redirecionamento seguindo as diretrizes de UX do Open Finance Brasil.
Código de erro
Mensagem de erro
Código de erro
Mensagem de erro
1
Response Code 422: limite de valor
O valor do pagamento ultrapassa o limite de R$ 1.000,00 estabelecido nesta fase inicial. O Open Finance está sendo disponibilizado gradualmente para garantir um sistema seguro e estável.
2
DraftOFS.: Proposta a respeito das especificações devido à limitações do escalonamento:
3
Em caso de extrapolação dos limites impostos para o lançamento escalonado, o consentimento não deve ser criado e a detentora deve retornar o seguinte de acordo com o caso:
4
Limites operacionais (valor da transação): atributo DETALHE_PGTO_INVALIDO)
5
Limites operacionais (funcionalidade): atributo FORMA_PGTO_INVALIDA)
6
(Recomendação para que a Instituição Iniciadora sugira o que fazer, ex.: call to action)
7
Responde Code 425: limite de horário
Esta solicitação não poderá ser atendida pois está fora do horário de funcionamento estabelecido nesta fase inicial (recomendação para que a Instituição Iniciadora apresente a grade de horários, se quiser). O Open Finance está sendo disponibilizado gradualmente para garantir um sistema seguro e estável.
8
DraftOFS.: O horário de funcionamento definido no normativo se refere à disponibilidade do endpoint POST do consentimento. Demais endpoints deverão ficar disponíveis por mais 1 hora.
9
(Recomendação para que a Instituição Iniciadora sugira o que fazer, ex.: call to action)
10
Response Code 429: limite de público
No momento, a instituição detentora da conta não poderá atender esta solicitação, pois atingiu os limites de transações estabelecidos. O Open Finance está sendo disponibilizado gradualmente para garantir um sistema seguro e estável.
11
(Recomendação para que a Instituição Iniciadora sugira o que fazer, ex.: call to action)

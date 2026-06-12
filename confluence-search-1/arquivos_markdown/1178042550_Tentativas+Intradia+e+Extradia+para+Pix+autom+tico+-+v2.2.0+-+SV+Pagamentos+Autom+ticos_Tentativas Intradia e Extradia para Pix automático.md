---
                            title: "Tentativas Intradia e Extradia para Pix automático - v2.2.0 - [SV] Pagamentos Automáticos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1178042550_Tentativas+Intradia+e+Extradia+para+Pix+autom+tico+-+v2.2.0+-+SV+Pagamentos+Autom+ticos"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1178042550/Tentativas+Intradia+e+Extradia+para+Pix+autom+tico+-+v2.2.0+-+SV+Pagamentos+Autom+ticos"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Tentativas Intradia e Extradia para Pix automático - v2.2.0 - [SV] Pagamentos Automáticos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Conceito geral do fluxo de tentativas Intradia e Extradia para o produto Pix automático
Fluxo Intradia: A transação ocorre no mesmo dia em que foi programada.
Primeira Tentativa: A liquidação da transação é realizada entre 0h e 8h do dia programado
Detentora já está em posse da solicitação de pagamento enviada pela ITP e é responsabilidade da Detentora o envio ao SPI na data programada.
Segunda Tentativa (Retentativa Intradia):
Ocorre apenas em casos de falha na primeira janela (0h e 8h).
Em caso de falha na primeira tentativa que impeça a reutilização do e2eID, o ITP deverá enviar um novo pagamento com um novo e2eID.
O envio do novo e2eID deve ser feito até, no máximo, 12h (meio-dia) do mesmo dia.
As regras sobre quais erros exigem reenvio de e2eID e quais não exigem estão detalhadas na Tabela 1.
Essa tentativa é condicionada ao reenvio do endToEndId pelo ITP, uma vez que a geração desse identificador é responsabilidade do ITP.
Esse envio deve ser realizado por meio de uma nova chamada ao endpoint de criação de novas tentativas de pagamentos. Detalhes estão disponíveis no Guia de Implementação do Pix Automático, na página: Serviços → [SV] Iniciação de Pagamentos - Guias de Implementação → Pix Automático.
Para os casos que exigem reevio de e2eID, se a ITP não enviar o novo e2eID dentro do prazo exigido, não será possível para a instituição detentora realizar a segunda tentativa intradia posteriormente.
O detentor deverá mover o pagamento que falhou para rejeitado. O novo pagamento enviado pelo ITP, para a segunda tentativa intradia, deverá permanecer como SCHD até a realização da segunda janela (único caso possível de agendamento para o mesmo dia).
Casos que não exijam um novo endToEndId deverão ser persistidos na segunda janela exclusivamente pelo detentor.
O pagamento deverá permanecer em SCHD até a falha na segunda janela (18h as 21h), se houver.
É permitida a instituição detentora a realização de mais tentativas além das duas obrigatórias (uma em cada janela), conforme IN BCB 513.
Fluxo Extradia: Aplica-se quando a transação não for liquidada na data programada, mesmo após as tentativas intradia.
O ITP poderá realizar novas tentativas de liquidação em dias subsequentes, desde que haja solicitação expressa do recebedor.
Essa solicitação não é trafegada via API, cabendo ao ITP garantir esse controle em suas integrações.
O prazo máximo para tentativas extradia é de:
7 dias corridos após a data original de liquidação para a maioria das periodicidades, exceto a semanal;
5 dias corridos no caso de cobranças com periodicidade semanal;
O dia imediatamente anterior ao dia de início de um novo ciclo de cobrança.
Cada tentativa extradia deve ser feita por meio de um novo pagamento criado pela ITP, enviado ao PSP Pagador até às 23h59 do dia imediatamente anterior à nova data de liquidação através do endpoint dedicado a novas tentativas.
Os novos pagamentos criados pela ITP nas tentativas extradia poderão alterar apenas os campos: novo e2eID; adição do originalRecurringPaymentId; e nova data.
O recebedor pode consolidar os valores em atraso e incluí-los na próxima cobrança do novo ciclo, desde que respeitados os limites do consentimento e da conta do pagador
, e desde que o consentimento não possua um valor fixo (fixedAmount).
O ITP pode realizar até três tentativas extradia em datas diferentes, dentro do prazo permitido. Cada uma das tentativas extradia possuem as mesmas regras das tentativas intradia.
Sobre a tabela:
A leitura da tabela deve ser realizada da seguinte maneira:
Contabiliza tentativa?:
Define se a tentativa de pagamento, ao encontrar o erro listado, é considerada uma das tentativas formais do ciclo de pagamento. Se 'NÃO', geralmente indica uma falha de validação prévia que não consome uma tentativa de liquidação, permitindo a correção e reenvio do payload. Se 'SIM', a tentativa é registrada, impactando o total de tentativas restantes.
Permite nova tentativa intradia?:
Indica se o sistema detentor da conta (PSP Pagador) deve realizar uma nova tentativa de envio ao SPI no mesmo dia. Certos erros ('SIM') permitem uma nova tentativa (podendo ser obrigatória até as 21h em alguns cenários), enquanto outros ('NÃO') sugerem que uma nova tentativa intradia resultaria no mesmo erro.
Exige reenvio de e2eID?:
Especifica se, para a próxima tentativa, o iniciador (ITP) deve gerar um novo identificador fim-a-fim (e2eID), referenciando o pagamento original. 'SIM' é necessário quando a tentativa anterior foi invalidada no SPI, exigindo uma nova mensagem de pagamento.
Exemplos de interpretação:
Se ocorrer o erro
SALDO_INSUFICIENTE
:
Contabiliza tentativa?
Sim.
Permite nova tentativa intradia?
Sim. (O usuário pode ter recebido fundos).
Exige reenvio de e2eID?
Não. O mesmo e2eID pode ser usado na nova tentativa intradia ou extradia, pois o problema era o saldo, portanto o pagamento não saiu do detentor para o SPI)."
Se ocorrer o erro
PAGAMENTO_DIVERGENTE_CONSENTIMENTO
:
Contabiliza tentativa?
Não. O erro é uma validação de regra de negócio prévia.
Permite nova tentativa intradia?
Não. A divergência precisa ser corrigida no payload; reenviar o mesmo payload resultará no mesmo erro.
Exige reenvio de e2eID?
Não. A questão é a conformidade do pagamento com o consentimento. Uma vez corrigido o payload, uma nova submissão(criação de novo pagamento) deve ser feita.
Tabela 1: Situações de erro que exigem a realização de novas tentativas de liquidação pelo iniciador, com e sem reenvio de e2eID para o agendamento do pagamento
Código de erro
Contabiliza tentativa?
Permite nova tentativa intradia ³
Exige reevio de e2eID
NAO_INFORMADO
SIM
SIM
SIM
PAGAMENTO_RECUSADO_SPI
SIM
SIM
SIM
FALHA_INFRAESTRUTURA_SPI
SIM
SIM
SIM
FALHA_INFRAESTRUTURA_ICP
SIM
SIM
SIM
FALHA_INFRAESTRUTURA_PSP_RECEBEDOR
SIM
SIM
SIM
SALDO_INSUFICIENTE
SIM
SIM
NÃO
VALOR_ACIMA_LIMITE
SIM
SIM
NÃO
PAGAMENTO_RECUSADO_DETENTORA
SIM
SIM
NÃO
FALHA_INFRAESTRUTURA_DETENTORA
SIM
NÃO
NÃO
LIMITE_VALOR_TRANSACAO_CONSENTIMENTO_EXCEDIDO²
SIM
NÃO
NÃO
DETALHE_TENTATIVA_INVALIDO
NÃO
SIM
NÃO
VALOR_INVALIDO
NÃO
NÃO
NÃO
PAGAMENTO_DIVERGENTE_CONSENTIMENTO
NÃO
NÃO
NÃO
CONSENTIMENTO_INVALIDO
N/A
NÃO
NÃO
TITULARIDADE_INCONSISTENTE
N/A
NÃO
NÃO
LIMITE_PERIODO_VALOR_EXCEDIDO¹
N/A
NÃO
NÃO
LIMITE_PERIODO_QUANTIDADE_EXCEDIDO¹
N/A
NÃO
NÃO
LIMITE_VALOR_TOTAL_CONSENTIMENTO_EXCEDIDO¹
N/A
NÃO
NÃO
LIMITE_TENTATIVAS_EXCEDIDO²
N/A
NÃO
NÃO
CONSENTIMENTO_REVOGADO²
N/A
NÃO
NÃO
FORA_PRAZO_PERMITIDO
N/A
NÃO
NÃO
PERMISSAO_INSUFICIENTE
N/A
NÃO
NÃO
¹ - Erro exclusivo para o produto Transferências inteligentes
² - Erro não ocorre no momento da liquidação, apenas no momento do agendamento
³ - Conforme previsto no Art. 7, parágrafo 1 da IN BCB 513 - "Caso a ordem de pagamento não seja enviada para liquidação no horário previsto, por ausência de recursos suficientes ou de limite transacional disponível, o prestador de serviços de pagamento do usuário pagador deve enviar notificação para seu cliente informando-o sobre a não liquidação do Pix Automático (...)"
Exemplo de aplicabilidade - Diagrama
Open
Imagem 1: Tentativa intradia
Open
Imagem 2: Nova tentativa em dia subsequente (extradia) após as falhas na tentativa original
Exemplos de aplicabilidade - Cenário
Data envio: 14/09/24 – (02 a 10 dias de antecedência da liquidação)
Data liquidação: 16/09/2024.
A primeira tentativa (Intradia):
Data liquidação: 16 de setembro de 2024
Primeira Tentativa: A liquidação é tentada entre 0h e 8h.
Se houver saldo suficiente, os limites forem respeitados e nenhum problema estrutural ocorra, a transação é concluída.
Caso falhe (por exemplo, por saldo insuficiente), segue-se para as novas tentativas.
Segunda Tentativa: Uma nova tentativa é feita entre 18h e 21h.
Se houver saldo suficiente, os limites forem respeitados e nenhum problema estrutural ocorra, a transação é concluída.
Em caso de falha considerar o cenário de tentativas (Extradias)
Novas tentativas nos 7 dias seguintes (Extradias):
Se a liquidação não for concluída no dia 16 de setembro, o detentor pode tentar realizar novas liquidações durante os próximos 7 dias corridos(exceto se a periodicidade for semanal, onde são 5 dias), através de uma nova criação de pagamento realizada pelo ITP, sendo até 3 tentativas em dias diferentes.
Primeira Tentativa Extradia: 18 de setembro de 2024
A primeira tentativa após a falha no dia 16 pode ser feita.
Payload é enviado no dia 17 com a data de liquidação do dia 18, respeitando “D+1” entre pedido de retentativa e nova data de liquidação.
A liquidação é tentada novamente dentro das janelas de liquidação.
Segunda Tentativa Extradia: 20 de setembro de 2024
Payload é enviado no dia 19 com a data de liquidação do dia 20, respeitando “D+1” entre pedido de retentativa e nova data de liquidação.
Se a tentativa do dia 20 falhar, o iniciador pode realizar uma nova tentativa
Terceira Tentativa Extradia: 22 de setembro de 2024, é feita no dentro do período de 7 dias corridos.
Payload é enviado no dia 21 com a data de liquidação do dia 22 , respeitando “D+1” entre pedido de retentativa e nova data de liquidação.
Se essa tentativa falhar, o ITP não poderá mais criar novas tentativas de liquidação para o ciclo em questão. O recebedor deverá entrar em contato com o usuário pagador caso queira cobra-lo por outros meios.

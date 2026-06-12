---
                            title: "[SV] Idempotência - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "728301590_SV+Idempot+ncia"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/728301590/SV+Idempot+ncia"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # [SV] Idempotência - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Por que é necessário tratarmos a Idempotência do POST/PATCH?
2
Como mitigarmos esse risco?
2.1
Conjunto inicial de regras propostas na aplicação da idempotência:
2.2
Cenários de uso de idempotência
Segundo a W3C, "um método HTTP idempotente é um método HTTP que pode ser chamado muitas vezes sem resultados diferentes ou efeitos colaterais. Não importa se o método é chamado apenas uma vez ou dez vezes. O resultado deve ser o mesmo. Essencialmente, significa que o resultado de uma solicitação executada com sucesso é independente do número de vezes que ela é executada. Por exemplo, na aritmética, adicionar zero a um número é uma operação idempotente."
Os conhecidos métodos GET, PUT e DELETE são naturalmente idempotentes, assim como HEAD, OPTIONS e TRACE também são.
Porém, o método POST e PATCH requer um tratamento especial para que se torne idempotente e, por estarmos tratando aqui de meios de pagamentos, fazer esse tratamento é algo necessário para que não ocorram acidentes.
Por que é necessário tratarmos a Idempotência do POST/PATCH?
Imagine que seja realizado um POST/PATCH no pagamento e, depois de alguns segundos, é retornada uma mensagem de Timeout. Nesse caso, não é possível saber se o POST/PATCH foi efetivo e enviar o POST/PATCH novamente, sem tratar a idempotência, poderá ocasionar em duplicidade da operação.
Como mitigarmos esse risco?
Do lado da iniciadora do pagamento: É necessário que seja enviado o POST/PATCH com um GUID de Idempotência. Caso o mesmo POST/PATCH seja reenviado por acidente ou precise ser reenviado, por qualquer motivo que seja, basta reenviar o POST/PATCH com o mesmo GUID de Idempotência.
Do lado da detentora da conta: É necessário validar o GUID de Idempotência recebido. Caso tenha recebido o mesmo GUID de Idempotência, a nova mensagem de POST/PATCH não deve alterar o recurso e a resposta deve ser a mesma oferecida para a primeira requisição recebida.
Importante reforçar que cada nova operação com POST/PATCH deverá ter um novo GUID de Idempotência.
Conjunto inicial de regras propostas na aplicação da idempotência:
A iniciadora/TPP não deve alterar o corpo da solicitação ao usar a mesma chave de idempotência. Se a iniciadora alterar o corpo da solicitação, a detentora/ASPSP não deve modificar o recurso final;
A detentora não deve criar um novo recurso para uma solicitação POST/PATCH se estiver determinada como uma solicitação idempotente;
Na criação a detentora deve responder à solicitação com o status atual do recurso (ou um status que seja pelo menos tão atual quanto o que estiver disponível nos canais eletrônicos existentes) e um código de status HTTP 201 (CREATED);
A iniciadora não deve usar comportamento idempotente para pesquisar o status dos recursos;
A detentora pode usar a assinatura da mensagem, junto com a chave de idempotência, para garantir que o corpo da solicitação não seja alterado;
Para a
API de Iniciação de
Pagamentos, a chave de idempotência deverá ser armazenada para controle quando a requisição for processada com sucesso (HTTP Status 201) ou quando ocorrer um erro de negócio (HTTP Status 422);
Para
a API
Consentimentos de Pagamento, a chave de idempotência deverá ser armazenada para controle quando a requisição for processada com sucesso (HTTP Status 201);
O comportamento idempotente deve ser mantido por 24 horas para uma mesma chave de idempotência;
Toda nova requisição exige que a assinatura da mensagem seja refeita, contendo um novo jti e iat.
Cenários de uso de idempotência
Ao receber uma requisição com o mesmo x-idempotency-key e com a claim data do JWT com conteúdo idêntico ao da requisição original, a requisição deverá ser processada entregando o mesmo resultado obtido anteriormente. Isso significa que, caso a requisição inicial tenha criado um recurso, este mesmo recurso deverá ser retornado, com seu status atualizado;
Ao receber uma requisição com o mesmo x-idempotency-key e com a claim data do JWT com conteúdo diferente do original a requisição deverá ser recusada com o HTTP Status 422 com código ERRO_IDEMPOTENCIA;
Ao receber uma requisição com o mesmo x-idempotency-key e com a claim iss não pertencente a organização que possui o software cliente (clientId) a requisição deve ser recusada com o HTTP Status 403;
A validação de idempotência deve ser feita no escopo de cada endpoint separadamente (não globalmente), ou seja, toda detentora deve aceitar o reuso da chave de idempotência (x-idempotency-key) em endpoints diferentes.

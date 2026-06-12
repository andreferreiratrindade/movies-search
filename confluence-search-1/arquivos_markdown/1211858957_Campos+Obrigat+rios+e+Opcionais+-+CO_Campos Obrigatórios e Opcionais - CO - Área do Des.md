---
                            title: "Campos Obrigatórios e Opcionais - CO - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1211858957_Campos+Obrigat+rios+e+Opcionais+-+CO"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1211858957/Campos+Obrigat+rios+e+Opcionais+-+CO"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Campos Obrigatórios e Opcionais - CO - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.01
Dica: para rolar a tabela horizontalmente, segure SHIFT e utilize o botão de rolagem do mouse.
Dica: não existe a opção de exportar as tabelas para Excel, porém pode-se selecionar o conteúdo da página com CTRL+A, copiar e colar no Excel.
Consents API
Campos que devem ser informados à PCM via POST
Campo
Definição
Obrigatório
Tipo
Domínio
Tamanho máximo
Padrão
Exemplo
Campo
Definição
Obrigatório
Tipo
Domínio
Tamanho máximo
Padrão
Exemplo
date
Data UTC no formato ISO8601 (YYYY-MM-DD) do momento em que a chamada foi disparada, imediatamente antes do primeiro byte enviado na requisição. Deve conter a data a que se referem os dados de consentimento enviados na mensagem
Sim
string <date-time>
10
YYYY-MM-DD
2021-11-11
orgId
Organização de envio da mensagem referente ao papel do Transmissor ou Receptor, conforme Role, a ser preenchido a partir do Certificado
Sim
string <uuid>
36
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
c1ca8e62-9d6f-4ea3-84f2-d66bc0a8f7dc
role
Indica se o reporte que está sendo enviado apresenta a visão do SERVER ou do CLIENT
Sim
enum<string>
CLIENT, SERVER
CLIENT
scope
Escopo do reporte
Sim
enum<string>
DADOS
DADOS
totalCustomerPF
Total de clientes PF com consentimentos ativos
Não
number
50
totalCustomerPJ
Total de clientes PJ com consentimentos ativos
Não
number
100
consentsStockList
Lista de estoque de consentimentos. Caso não haja estoque a reportar, enviar o array vazio.
Os itens indentados abaixo pertencem ao objeto consentsStockList e seguem as mesmas regras de obrigatoriedade
Sim
array [object {3}]
[{"clientOrgId": "d78fc4e5-37ca-4da3-adf2-9b082bf92280", "serverOrgId": "c1ca8e62-9d6f-4ea3-84f2-d66bc0a8f7dc", "totalActiveConsents": 30}]
clientOrgId
Identificador da organização de onde a chamada foi disparada
Não
string <uuid>
36
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
d78fc4e5-37ca-4da3-adf2-9b082bf92280
serverOrgId
Identificador da organização para onde a chamada foi feita
Não
string <uuid>
36
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
c1ca8e62-9d6f-4ea3-84f2-d66bc0a8f7dc
totalActiveConsents
Estoque total de consentimentos ativos, correspondendo ao número de consentimentos totais válidos até a data de referência.
Não
number
30
Campos retornados em response
Campo
Definição
Tipo
Domínio
Tamanho máximo
Padrão
Exemplo
Campo
Definição
Tipo
Domínio
Tamanho máximo
Padrão
Exemplo
reportId
Identificador único interno do reporte no formato UUID v4.
string <uuid>
36
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
9a97c2df-b261-4fc2-aa66-d1b5168397da
status
Informa o status do registro de reporte.
ACCEPTED:
O status ACCEPTED indica que a validação de formato do reporte não tem erros e este será enviado para processamento.
DISCARDED:
O status DISCARDED indica que o reporte enviado pelo participante foi rejeitado pela PCM. O motivo do descarte será enviado com a resposta, podendo ser por conta de um reporte inválido ou por um erro no processamento. Não é possível modificar um reporte DISCARDED, portanto o reportador deverá corrigir o registro que apresentou erro e reenviar via POST.
enum <string>
ACCEPTED, DISCARDED
ACCEPTED

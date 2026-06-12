---
                            title: "Informações Gerais - APIs Service Desk - v0.5 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "17377992_Informa+es+Gerais+-+APIs+Service+Desk+-+v0.5"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17377992/Informa+es+Gerais+-+APIs+Service+Desk+-+v0.5"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Informações Gerais - APIs Service Desk - v0.5 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Especificação API Service Desk Open Finance Brasil
O objetivo desse documento é prover material para publicação das informações referentes a APIs do Service Desk no portal do Open Finance Brasil.
A Documentação completa e também utilizada como fonte deste conteúdo pode ser encontrada em:
Join the SysAid Community Discord Server!
1. Modelo de Fluxo de atendimento:
Open
2. URLs de acesso:
https://servicedesk.openfinancebrasil.org.br/
: Ambiente Produtivo do Service Desk Open Finance.
https://servicedesksandbox.openfinancebrasil.org.br/
: Ambiente Sandbox (Homologação) do Service Desk Open Finance.
3. Tabela DE/PARA front-end para API
Nome do Campo
API
Detalhes
Categoria
problem_type
1ºNível_2ºNível_3ºNível / Na resposta: 1º Nível de Categoria
Subcategoria
problem_sub_type
Na resposta: 2º Nível de Categoria
Categoria de 3º Nível
third_level_category
Na resposta: 3º Nível de Categoria
Título
title
Descrição
description
Anotações
notes
{“userName”:{NOME DO USUÁRIO},”createDate”:{DATA EM MILISEGUNDOS},”text”:{TEXTO}}
Solução
solution
Atividades
activities
Iterações entre N1 e N2
Data de solicitação
insert_time
Em milisegundos
Data de modificação
uptade_time
Em milisegundos
Data de encerramento
close_time
Em milisegundos
Prazo de SLA
due_date
Em milisegundos
Data Prevista para Implementação da
Correção
CustomColumn82sr
Necessária quando utilizado o status “AGUARDANDO CORREÇÃO N2” em categorias de Incidentes
Usuário Solicitante
request_user
Equipe de Atendimento
assigned_group
Instituição Requerente
CustomColumn155sr
Nome da instituição que está abrindo o chamado
Especialista Atribuído
responsibility
Status
status
Conferir lista de status
Contador de Reabertura
reopen_counter
Número de vezes que o chamado foi reaberto
Anexos
attachments
Tipo de Registro de
Serviço
sr_type
Arquivado
arquive
Tipo Booleano
Nível de Suporte Atual
current_support_level
Tipo do Chamado
type
Incidentes = 1; Solicitação de Serviço = 10
Formulário Utilizado
template
Padrão Incidente = 20; Padrão Solicitação de Serviço = 12
O conteúdo da
reclamação é procedente?
CustomColumn129sr
Necessário o preenchimento ao encerrar um chamado tipo Incidente (status: ATENDIMENTO ENCERRADO)
Tipo de Erro
CustomColumn119sr
Disponível apenas para consulta nos chamados da categoria “Erro na Jornada ou Dados”
4. APIs
Tipo de API: REST
Formato dos dados de retorno e envio: JSON Fonte do conteúdo:
Join the SysAid Community Discord Server!
FAQ Service Desk:
https://servicedesk.openfinancebrasil.org.br/KBFAQTree.jsp
4.1 Login
Responsável pela autenticação na API, é pré-requisito para a execução de qualquer requisição. As credenciais devem ser solicitadas via Portal do Service Desk Open Finance.
É necessário um usuário Administrador (Atendimento N2) para a utilização da API.
POST - {URL}/api/v1/login
Campos Obrigatórios:
“user_name” = Nome de usuário de integração “password” = Senha do usuário de integração
Exemplo de Body:
{"user_name":"{NOME DO USUÁRIO}", "password":"{SENHA}"}
No retorno é necessário armazenar o Cookie JSESSIONID para consumo dos demais métodos.
Nesta requisição de login, também é necessário identificar o
ID do Grupo
de Atendimento que será utilizado nas requisições de
consulta de chamados
, para identificar este número na resposta deve ser capturado o valor do "id" na key "user_groups". De acordo com o exemplo a seguir:
"key": "user_groups",
"value": [
{
"id": 10,
"name": "N1 Service Desk", "type": 1,
"supportLevel": 1, "visible": true
}
4.2 Consulta de Chamados
Retorna todos os chamados, ativos e encerrados, que se encontram na equipe de atendimento do usuário autenticado, com exceção dos chamados que já foram arquivados. Neste tipo de requisição é necessário passar o parâmetro “assigned_group” para que apenas os tickets pertencentes ao grupo de atendimento do usuário sejam retornados.
GET – {URL}/api/v1/sr?assigned_group={ID do Grupo}
Body:
Manter vazio
Para refinar a busca é necessário incluir parâmetros na requisição.
Estes são alguns exemplos de keys comuns a serem utilizadas:
“problem_type” = Categoria: 1º nível_2º nível_3ºnível “status” = Qual status que o chamado se encontra “insert_time” = Abertura do chamado
“due_date” = SLA
Consultar a Tabela DE/PARA (Tópico 3.)
Exemplo de requisição:
GET – {URL}/api/v1/sr?problem_type=Incidentes_APIs_Erros&assigned_group=10
Body:
Manter vazio
O retorno virá com todas as informações referentes aos chamados que entrarem nos parâmetros estabelecidos. Para retornar campos específicos na reposta é necessário utilizar a key “fields" na requisição e selecionar os parâmetros de retorno.
Estes são alguns exemplos de keys comuns a serem utilizadas:
“id” = ID do chamado
“update_time” = Data e hora da última modificação “solution” = Solução do chamado
“request_user” = Usuário Solicitante Consultar a Tabela DE/PARA (Tópico 3.)
Exemplo de requisição:
GET – {URL}/api/v1/sr?problem_type=Incidentes_APIs_Erros&fields=id,update_time&assigned_group=10
Aplicando os mesmos parâmetros da requisição anterior, os chamados exibidos serão os mesmos, porém agora apenas a informações indicadas em “fields” serão exibidas em cada chamado respectivamente.
Existem outros parâmetros que podem ser consultados na Documentação Completa do SysAid (Tópico 4.)
Exemplo de retorno:
[ {
"id": "1273",
"canUpdate": true, "canDelete": true, "canArchive": true, "hasChildren": false, "info": [
{
"key": "update_time", "value": 1646856953697,
"valueClass": "",
"keyCaption": "Data de modificação", "valueCaption": "09-03-2022 17:15:53"
}
]
},
{
"id": "1274",
"canUpdate": true, "canDelete": true, "canArchive": true, "hasChildren": false, "info": [
{
"key": "update_time", "value": 1646862779347,
"valueClass": "",
"keyCaption": "Data de modificação", "valueCaption": "09-03-2022 18:52:59"
} ]
Para uma consulta que considere os chamados arquivados, deve ser passado um parâmetro a mais no endpoint da requisição: "archive=1".
Portanto, caso o objetivo seja trazer toda a base de chamados (arquivados e não) o ideal é que seja executada a query da seguinte forma:
GET – {URL}/api/v1/sr?assigned_group={idgrupo}&archive=0,1
4.3 Consulta de chamado específico
Traz todas as informações de um chamado específico, possível aplicar parâmetros de busca e de retorno para customizar a consulta.
GET – {URL}/api/v1/sr/{ID DO CHAMADO}
4.4 Abertura de Chamados
Abre um chamado para o Service Desk. Todos os campos a serem inseridos no chamado devem ser passados no Body da requisição.
Consultar a Tabela DE/PARA (Tópico 3.) para informar o “type” e “template”
Algumas categorias podem possuir formulários customizados, sendo necessário utilizar templates específicos e informar campos customizados. Nestes casos deve-se acessar a FAQ do Service Desk e consultar a categoria específica no seguinte link:
https://servicedesk.openfinancebrasil.org.br/KBFAQTree.jsp
POST – {URL}/api/v1/sr?type={TIPO DE CHAMADO}&template={ID DO FORMULÁRIO}
Campos Obrigatórios:
“problem_type” = Categoria (São 3 níveis de categorização, devem ser separados utilizando “_”)
“title” = Título
“description” = Descrição
Exemplo de requisição:
POST – {URL}/api/v1/sr?type=1&template=20
Exemplo de Body:
{
"info": [{"key":"problem_type", "value":"Incidentes_Diretório_Erro"},
{"key":"title", "value":"Abertura de Chamado via API"},
{"key":"description", "value":"Teste de abertura de incidente através de API."}]
}
4.5 Alteração no Chamado
Alterar um chamado, modificando as informações. Todos os campos a serem modificados no chamado devem ser passados no Body da requisição.
(Para consultar a lista com os IDs dos Status, visite a FAQ).
PUT - {URL}/api/v1/sr/{ID DO CHAMADO}
Exemplo de Body:
{
"id": "1275",
"info": [
{"key":"status", "value": "8"},
{"key":"notes", "value":
[{"userName":"João Teste","createDate":1647019229000,"text":"Teste Nota"}]}
]
}
4.6 Recuperado Anexos
Para consultar os anexos dentro do chamado é necessário a utilização do campo "attachments" na chave "fields", de acordo com o exemplo a seguir:
GET - {URL}/api/v1/sr/{ID do CHAMADO}?fields=attachments
Body:
Manter vazio
Exemplo de retorno:
"key": "attachments", "value": [
{
"fileId": "{ID do ANEXO}", "fileName": "nome_do_anexo.pdf", "realFileName": null, "chatSessionId": null,
"fileDate": "22-10-2021 09:35"
}
],
Com o ID do anexo contido no campo "fileId" você vai poder utilizar a URL de Download para obter o arquivo.
URL de download:
{URL}/getFile?table=service_req&id={ID do CHAMADO}&getFile={ID do ANEXO}
4.7 Inserindo Atividades
Para utilizar o campo de atividades, deve ser feita a seguinte requisição:
POST – {URL}/api/v1/sr/{ID DO CHAMADO}/activity
Campos obrigatórios:
"id" = ID do chamado onde será adicionada a atividade "userId" = ID do usuário que está inserindo a atividade "fromTime" = Data e hora do início da atividade "toTime” = Data e hora do término da atividade "description” = Descrição da Atividade
Obs: A data e hora de início e término da atividade podem ser as mesmas, mas devem indicar o momento em que foi inserida a atividade.
Exemplo do Body
:
{
"id": "2507",
"userId":123456, "fromTime":1652904309000, "toTime":1652904309000,
"description":"Adicionando Atividade via API"
}
4.8 Consulta de chamados como solicitante
Além das consultas que podem ser feitas como Equipe de Atendimento dos chamados, para aqueles chamados que são abertos pelo seu usuário, tanto via API quanto via Portal do Usuário Final, também é possível fazer a consulta dos mesmos via API, para isso deve-se acrescentar um Header na requisição.
Header:
Key: Referer
Value: /servicePortal
Portanto ambas as requisições dos tópicos
4.2
e
4.3
podem ser executadas adicionando este novo header para efetuar as consultas no papel de usuário
solicitante
. Lembrando que mesmo efetuando a consulta como solicitante é pré-requisito que o seu usuário seja N2 (Administrador) e tenha as permissões necessárias para o consumo da API.
Caso o usuário seja supervisor, também será possível obter os chamados abertos por outros membros da instituição utilizando um parâmetro adicional no endpoint:
Key: supervisedRequests
Value: Y
Como no exemplo a seguir:
GET - {URL}/v1/sr?status=1&fields=id,insert_time,status&supervisedRequests=Y
4.9 Adição de notas como solicitante
Seguindo o que foi instruído no item
4.8
além de fazer a consulta das informações, também é possível fazer a adição de notas ao chamado no papel de requisitante via API. Para isso é necessário a utilização do Header e executar o processo descrito no item
4.5
seguindo os parâmetros para a adição de notas contida na Tabela DE/PARA no item
3.0
deste documento:
Key: notes
Value: {“userName”:{NOME DO USUÁRIO},”createDate”:{DATA EM MILISEGUNDOS},”text”:{TEXTO}}
Requisição:
PUT - {URL}/api/v1/sr/{ID DO CHAMADO}
Exemplo do Body
:
{
"id": "1234",
"info": [
{"key":"notes", "value":
[{"userName":"João Teste","createDate":1647019229000,"text":"Teste Nota"}]}
]
}
É importante ressaltar que
não devem ser alterados os demais campos do chamado
incluindo o status, apenas a adição da nota deve ser executada e o chamado já terá o status alterado de forma automática pelo SysAid.
4.10 Adição de anexos
Para adicionar anexos a um chamado é necessário a utilização do body como “form-data” e a key como “file”, de acordo com o exemplo a seguir:
Key: file
Value: exemplo.txt
POST - {URL}/api/v1/sr/{ID do CHAMADO}/attachment
Importante:
No value da requisição, é necessário informar o nome e a extensão do arquivo a ser adicionado.
4.11 Consulta de Chamados Supervisionados
Caso o usuário seja supervisor, também será possível obter os chamados abertos por outros membros da instituição utilizando um parâmetro adicional no endpoint.
Essa requisição retorna todos os chamados, ativos e encerrados com exceção dos chamados que já foram arquivados.
GET – {URL}/api/v1/sr/supervisor
Body:
Manter vazio
Para refinar a busca é necessário incluir parâmetros na requisição.
Estes são alguns exemplos de keys comuns a serem utilizadas:
“problem_type” = Categoria: 1º nível_2º nível_3ºnível
“status” = Qual status que o chamado se encontra
“insert_time” = Abertura do chamado
“due_date” = SLA
Consultar a Tabela DE/PARA (Tópico 3.)
Exemplo de requisição:
GET – {URL}/api/v1/sr/supervisor?problem_type=Incidentes_APIs_Erros
Body:
Manter vazio
O retorno virá com todas as informações referentes aos chamados que entrarem nos parâmetros estabelecidos. Para retornar campos específicos na reposta é necessário utilizar a key “fields" na requisição e selecionar os parâmetros de retorno.
Estes são alguns exemplos de keys comuns a serem utilizadas:
“id” = ID do chamado
“update_time” = Data e hora da última modificação
“solution” = Solução do chamado
“request_user” = Usuário Solicitante
Consultar a Tabela DE/PARA (Tópico 3.)
Exemplo de requisição:
GET – {URL}/api/v1/sr/supervisor?problem_type=Incidentes_APIs_Erros&fields=id,update_time
Aplicando os mesmos parâmetros da requisição anterior, os chamados exibidos serão os mesmos, porém agora apenas a informações indicadas em “fields” serão exibidas em cada chamado respectivamente.
Existem outros parâmetros que podem ser consultados na Documentação Completa do SysAid (Tópico 4.)
Exemplo de retorno:
[
{
"id": "1273",
"canUpdate": true,
"canDelete": true,
"canArchive": true,
"hasChildren": false,
"info": [
{
"key": "update_time",
"value": 1646856953697,
"valueClass": "",
"keyCaption": "Data de modificação",
"valueCaption": "09-03-2022 17:15:53"
}
]
},
{
"id": "1274",
"canUpdate": true,
"canDelete": true,
"canArchive": true,
"hasChildren": false,
"info": [
{
"key": "update_time",
"value": 1646862779347,
"valueClass": "",
"keyCaption": "Data de modificação",
"valueCaption": "09-03-2022 18:52:59"
}
]
Para uma consulta que considere os chamados arquivados, deve ser passado um parâmetro a mais no endpoint da requisição: "archive=1".
Portanto, caso o objetivo seja trazer toda a base de chamados (arquivados e não) o ideal é que seja executada a query da seguinte forma:
GET – {URL}/api/v1/sr/supervisor?archive=0,1
Em caso de dúvidas ou dificuldades na utilização da API entrar em contato com o Service Desk através do Portal:
https://servicedesk.openfinancebrasil.org.br/

---
                            title: "FVP Automática - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "553254972_FVP+Autom+tica"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/553254972/FVP+Autom+tica"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # FVP Automática - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Escopo de testes
Com rotina de execução diária e automática, a ferramenta realiza testes de conformidade periódicos em servidores selecionados e reporta os resultados à instituição testada via plataforma Service Desk de maneira automática.
Os testes realizados contemplam validações que não precisam de interação de usuário, especialmente DCR, FAPI, testes funcionais e de cadastro no Diretório.
Esses testes também estão disponíveis para execução pelas instituições através da FVP Manual.
Fluxo de notificação das instituições através de tickets no Service Desk
a.      Abertura de Tickets
Após a execução da FVP automática, caso a instituição falhe em algum dos testes executados, a rotina abrirá um ticket ou atualizará os existentes. Dois tipos de tickets podem ser criados:
I. "Teste Automático DCR -
CustomerFriendlyName
" - aberto se o servidor falhar em pelo menos um teste relacionado ao DCR ou testes funcionais.
II. "Teste Automático Cadastro Diretório -
CustomerFriendlyName
" - aberto se o servidor falhar em pelo menos um teste relacionado à validação de cadastro no diretório.
Se o servidor falhar em ambos os tipos de testes, ambos os tickets serão abertos para a instituição. Dentro do ticket, as seguintes informações devem estar presentes:
Lista dos testes que retornaram falha
Hipóteses sobre as falhas para ajudar os participantes a ajustar suas implementações
Well-Known
do servidor testado
ID do
Authorisation Server
encontrado no Diretório
·       Evidências apontando onde a instituição falhou no plano de testes em dois formatos potenciais:
o   URI para página de resultados, que poderá ser acessada apenas por usuários autenticados com as credenciais do Diretório
o   Arquivo
zip
com os
logs
de execução
b.     Manutenção de Tickets
Caso a instituição continue com falha na execução, as falhas serão anexas ao ticket existente com os novos logs de execução. Se a instituição obtiver sucesso em todos os módulos de teste, o ticket é fechado automaticamente com uma nota de sucesso.
Os testes DCR realizados no ambiente de produção estão acessíveis no
Motor de Conformidade
regular, permitindo que as instituições os executem no ambiente de Sandbox para correção de problemas identificados na produção.
Em caso de dúvidas ou problemas nos testes executados, a instituição deve abrir um novo ticket no Service Desk de conformidade, onde as questões serão analisadas pela equipe de conformidade.
Ocasionalmente, a equipe do motor de conformidade pode adicionar notas aos tickets junto com os logs de execução, especificando comportamentos ou ações esperadas da instituição.
Open
Página de Resultados
Após cada execução da FVP automática, são geradas páginas de resultados de testes com os
logs
das execuções e detalhamentos dos pontos de falha, semelhante aos resultados do motor de conformidade.
A URL base da plataforma é
https://results.sandbox.directory.openbankingbrasil.org.br/TestID/index.html
, onde
TestID
é uma sequência aleatória de caracteres que será fornecida à instituição após a abertura de um ticket no Service Desk.
Para acessar os resultados, é necessário autenticar-se com credenciais do Diretório Open Finance e estar vinculado a uma organização ativa. Também não há possibilidade de indexar os resultados de testes existentes, então a instituição deve salvar o URI do teste para futuras consultas.
Clients
de Teste
É responsabilidade da instituição realizar a checagem diária e a exclusão de eventuais
clients
remanescentes de execuções anteriores das FVPs. Com a introdução do novo
software statement
para testes de longa duração, cujos
clients
não devem ser deletados, aplicam-se as seguintes diretrizes:
Software statements
cujos
clients
devem
ser deletados: É mantida a necessidade da checagem diária e deleção dos
clients
remanescentes associados aos seguintes SSIDs:
bcc3ba64-faf5-456c-a162-8fef7ee67170;
bc97b8f0-cae0-4f2f-9978-d93f0e56a833;
70ee2970-038b-44d6-9300-d3af3a890154;
21ef921f-7d9f-4fa5-afae-d24545d6c880;
f61e3065-ca7b-4982-8ff5-86dff43ece63;
d52c9049-a67b-432f-bdde-fe613099f83b
Software statements
cujos
clients
não devem
ser deletados: O
client
não deverá ser deletado, uma vez que o mesmo clientId será usado em novos testes. SSIDs:
44ffd907-2318-496b-ad91-07bbb0a836da;
25402dd0-7553-477b-b635-b9ce79da18f2.
Reforçamos que, para os
software statements
cujos
clients
devem ser deletados, mantem-se a sugestão de realizar a exclusão preferencialmente entre
22h e 6h
, a fim de evitar interferências na execução dos testes conduzidos pela Associação Open Finance.
Exemplo de Configuração de Teste – Sandbox
Os testes executados pela FVP automática também podem ser visualizados no motor de conformidade de Sandbox e na FVP manual. Esses testes estão incluídos no plano de testes chamado: "
Functional Tests
for DCR - FVP 1.0 -
Live Tests
". Abaixo está uma configuração de exemplo que inclui credenciais geradas no Sandbox do Diretório e executa testes contra o
Mock Bank
, com certificados gerados em maio de 2024.
Exemplo de Configuração de Sandbox (
Link de um exemplo
C:\Users\Chicago\AppData\Roaming\Microsoft\Word\gitlab.com\raidiam-conformance\open-finance\certification\-\wikis\Automated-Production-Tests - test-plan-list
)
Observe que os testes da FVP Automática foram projetados para serem executados em produção. Os certificados e chaves utilizados no exemplo acima diferem dos utilizados em produção. Portanto, não há garantia de que a aprovação nos testes de Sandbox resultará em aprovação na execução automatizada em produção.
Interação com o Diretório
Para iniciar a execução dos testes automatizados, a FVP interroga a API pública do Diretório, analisa a resposta JSON e extrai informações sobre todas as organizações registradas no diretório.
Essas informações incluem:
ID da Organização
Nome da Organização
Lista de todos os servidores de autorização registrados sob esta organização
URL do
Well-Known
Customer Friendly Name
ID do
Authorisation Server
URI de
Consents
Após extrair todas as informações do diretório, a FVP interroga e processa os
endpoints Well-Known
de cada servidor de autorização nesta parte da rotina. Em seguida, as informações obtidas são atualizadas.
As informações incluem:
Métodos de autorização suportados (chave privada ou MTLS)
Se PAR é suportado, e se é obrigatório
Com todas essas informações em mãos, uma série de planos de teste será criada para cada cenário potencial de teste válido. Aqui, o número de planos válidos por servidor de autorização depende do número de credenciais X variantes de autorização suportadas.
Baseado nas informações extraídas, a FVP cria planos de teste para cada cenário potencial. O número de planos válidos por servidores de autorização depende do número de credenciais X
supported_authorisation_variants,
por exemplo, se um AS suporta duas variantes de autorização e os testes são feitos com dois tipos de
software statments
, 4 planos de teste válidos são gerados.

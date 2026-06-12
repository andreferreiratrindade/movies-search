---
                            title: "Limites operacionais - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "17924220_Limites+operacionais"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17924220/Limites+operacionais"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Limites operacionais - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            É facultado às instituições participantes implementarem um limite de acesso mensal por
endpoint
e por cliente.
Em
endpoints
que acessem recursos ou produtos, os limites serão também considerados por recurso ou produto.
A contabilização dos acessos deve ser realizada por:
I. mês
II. endpoint
III. objeto mais granular referenciado na chamada (consentimento/recurso/produto)
IV. cliente (CPF ou CNPJ)
V. instituição consumidora da informação
Por exemplo: uma instituição receptora ‘A’ pode acessar um endpoint ‘B’, acessando o recurso ‘C’, de um cliente “D” da instituição transmissora ‘E’, no mínimo ‘N’ vezes (ou chamadas) com sucesso por mês.
Aplicabilidade dos limites operacionais: todos
endpoints
das APIs do tipo Dados Cadastrais e Transacionais (conforme classificação de Tipo), destes excetuam-se aqueles
endpoints
das APIs de Consentimento (
Consents
) e Recursos (
Resources
). As APIs de Segurança, de Dados Abertos e de Serviços (como de Iniciação de Pagamento) não podem ter restrições de limites operacionais.
A implementação dos limites operacionais é opcional pelas instituições transmissoras, mas, uma vez que sejam implementados, devem garantir o consumo mínimo. É facultada à instituição a possibilidade de ampliar esses limites, mas vedada a implementação de limites inferiores aos estabelecidos.
Os valores mínimos de limites operacionais a serem considerados, por
endpoint
, que devem ser iguais ou maiores que os abaixo, de acordo com a classificação de frequência de utilização:
I. 8 chamadas ao mês, para endpoint classificado como de baixa frequência
II. 30 chamadas ao mês, para
endpoint
classificados como de média frequência
III. 120 chamadas ao mês, para
endpoint
classificado como de média-alta frequência
IV. 240 chamadas ao mês, para
endpoint
classificado como de alta frequência
V. 420 chamadas ao mês, para os seguintes
endpoints
da API de Contas: ‘Saldos da conta’ e ‘Limites da conta’
Só deverão ser contabilizadas nos limites operacionais requisições respondidas com HTTP
Status
Code
2XX, sendo que as requisições adicionais a um endpoint para fins de paginação não devem ser contabilizadas.
As requisições que excederem os limites operacionais deverão ser respondidas com o HTTP
Status
Code
423.
Todas as requisições autenticadas em
endpoints
sujeitos ao limite operacional devem possuir o atributo
x-fapi-interaction-id
preenchido no seu
header
pela receptora, que deve ser copiado pela transmissora nos
headers
da resposta. Essa definição objetiva permitir um adequado rastreamento de divergências que podem ocorrer entre transmissoras e receptoras associadas ao limite operacional.
Paginação no contexto dos limites operacionais
Para a não contabilização de rechamadas, considerando que eventuais chamadas que possuam paginação devam ser interpretadas como uma única chamada, foi estabelecido a criação de um
query
parameter
adicional para funcionar como identificador de rechamadas.
Esse novo parâmetro deve ter o nome
pagination-key
.
Cabe à Transmissora criar o identificador e enviá-lo via HATEOAS no retorno da chamada.
O tempo máximo de utilização do identificador pelo Receptor é de 60 minutos.
A Transmissora deve implementar validações para garantir a coerência da utilização do identificador, de acordo com as regras de limites operacionais.
Caso a Receptora utilize um
pagination-key
inválido ou expirado, a Transmissora deverá gerar um novo
pagination-key
retornando o resultado com sucesso. Esta chamada será contabilizada para os limites operacionais.
Essa implementação deve ser realizada em todos
endpoints
atuais com paginação.
A Transmissora poderá gerar um único ID para controle das chamadas das próximas páginas.
Open
Exemplo do uso do pagination-key
Primeira chamada
GET /accounts/v2/accounts/12345678/transactions?page=1&page-size=1000
{
“data”: [
“...”
],
“links”: {
“self”:  ”https://api.banco.com.br/open-banking/accounts/v2/accounts/12345678/transactions?page=1&page-size=1000&pagination-key=123456”,
“first”: ”https://api.banco.com.br/open-banking/accounts/v2/accounts/12345678/transactions?page=1&page-size=1000&pagination-key=123456”,
“next”: ”https://api.banco.com.br/open-banking/accounts/v2/accounts/12345678/transactions?page=2&page-size=1000&pagination-key=123456”
},
“meta”: {
“requestDateTime”:”2021-05-21T08:30:00Z”
}
}
Próximas chamadas
GET /accounts/v2/accounts/12345678/transactions?page=2&page-size=1000&pagination-key=123456
{
“data”: [
“...”
],
“links”: {
“self”: ”https://api.banco.com.br/open-banking/accounts/v2/accounts/12345678/transactions?page=2&page-size=1000&pagination-key=123456”,
“prev”: ”https://api.banco.com.br/open-banking/accounts/v2/accounts/12345678/transactions?page=1&page-size=1000&pagination-key=123456”,
“first”: ”https://api.banco.com.br/open-banking/accounts/v2/accounts/12345678/transactions?page=1&page-size=1000&pagination-key=123456”,
“next”: ”https://api.banco.com.br/open-banking/accounts/v2/accounts/12345678/transactions?page=3&page-size=1000&pagination-key=123456”
},
“meta”: {
“requestDateTime”:”2021-05-21T08:30:00Z”
}
}

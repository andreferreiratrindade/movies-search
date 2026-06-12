---
                            title: "Obrigatoriedade de Campos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "225280001_Obrigatoriedade+de+Campos"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/225280001/Obrigatoriedade+de+Campos"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Obrigatoriedade de Campos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Contexto
A
obrigatoriedade de campos
em uma API se refere à
especificação
de certos
campos
como sendo
necessários
ou
obrigatórios
para serem
fornecidos pelo cliente
ao
enviar uma requisição
para a API. Isso significa que, ao fazer uma chamada à API, o cliente
deve incluir determinados campos
com seus
respectivos valores
para que a requisição
seja válida
e a API possa
processá-la corretamente
.
A obrigatoriedade de campos
é uma prática comum no desenvolvimento de APIs
, pois ajuda a garantir a
integridade dos dados
e a
consistência das informações
recebidas pela API. Além disso, ela facilita a
validação dos dados
de entrada e ajuda a
prevenir erros
ou
comportamentos indesejados
na aplicação.
No
Open Finance
podemos ter
obrigatoriedade regulatória
e
técnica
. A diferença entre elas, está no
contexto
em que são aplicadas e às
razões pelas quais são exigidas
.
Obrigatoriedade regulatória dos campos
A
Instrução Normativa nº 371
, de 10 de abril de 2023, juntamente com suas eventuais atualizações, estabelece quais
dados devem ser obrigatoriamente implementados
pelas instituições participantes e
quais são opcionais
.
Para efeito deste manual, definiremos estes dados como
obrigatórios por regulamentação
e para efeito de
conformidade
as instituições devem enviar estes nas API do Open Finance Brasil.
Porém, em certos contextos de negócio e para determinadas instituições, pode ocorrer que dados classificados como obrigatórios por regulamentação sejam incoerentes.
Obrigatoriedade técnica dos campos
Em certas
situações
, pode ocorrer que dados que são
obrigatórios
do ponto de vista
regulatório, deixem de fazer sentido em determinados contextos de negócio
. Nesses casos,
é necessário permitir
que,
tecnicamente
, esses dados não sejam enviados. Essa característica é explicitada na
Instrução Normativa nº 306
, de 19 de setembro de 2022, que
estabelece
que todos os elementos das
especificações das APIs
(endpoints, operações, parâmetros, propriedades de respostas, etc.)
devem ser declarados
explicitamente como "
Obrigatório
", "
Opcional
" ou "
Condicional
"
Obrigatório
Um campo
obrigatório
é aquele que
deve ser fornecido
pelo cliente em
todas
as
circunstâncias
ao
enviar uma requisição para a API
. Se o cliente
não enviar
esse campo ou enviá-lo com um
valor inválido
, a API retornará um erro indicando que o campo é obrigatório e
deve ser preenchido corretamente
;
Os atributos
obrigatórios devem estar presentes
e ter um valor
não nulo
, seja em uma
requisição
ou
resposta
, para que
payload
seja
considerado válido
.
Opcional
Um campo
opcional
é aquele que o cliente
pode
ou
não fornecer na requisição
, independentemente da situação. A API
aceitará
a requisição
mesmo
que esses campos
não sejam fornecidos
;
A
opcionalidade
dos campos é especificada para
tratar situações de negócio
em que um campo
deixe de fazer sentido
(por exemplo: 'o campo só deve ser preenchido se o produto for do tipo x') ou, para comportar cenários de exceções quando uma instituição não possuir o dado.
Condicional
Um campo
condicional
é aquele que
só precisa ser fornecido
pelo cliente em
certas situações específicas
, de acordo com
alguma lógica
ou
condição estabelecida
pela API. Essa lógica pode ser baseada em outros campos enviados na requisição, no estado atual do sistema ou em outros fatores relevantes;
Os atributos
condicionais
devem ter uma marcação de
restrição vinculada a eles na documentação da API
(Swagger), no campo 'description'. Esses atributos terão a coluna '
Mandatoriedade
' preenchida como '
Condicional
', além de terem a situação descrita na coluna '
Restrições
' do
dicionário de dados
.
Em resumo, os
campos
das APIs no Open Finance Brasil são
classificados
em
duas dimensões
de
obrigatoriedade
: a
regulatória
, que determina quais informações
devem ser enviadas para cumprir a regulamentação
, e a
técnica
, que permite o
atendimento de cenários específicos de negócio
. Como regra geral, as
instituições devem adotar a premissa
de que se um campo é
regulatoriamente obrigatório
e
faz sentido para o negócio
, ele
deve ser sempre enviado
, mesmo que seja
tecnicamente opcional
no
Swagger
.
Regras para definir as dimensões de obrigatoriedade
A tabela abaixo
exemplifica
o
comportamento
que deve ser
adotado
pelas instituições em relação a variação entre a
obrigatoriedade por regulação
, a
obrigatoriedade técnica
e o cenário de negócio.
Regras para definir obrigatoriedade do envio do campo
Índice
Campo é Regulatório por alguma IN?
Campo é requerido pela documentação no Swagger?
Cenário de Negócio
Deve-se enviar a informação do campo?
Índice
Campo é Regulatório por alguma IN?
Campo é requerido pela documentação no Swagger?
Cenário de Negócio
Deve-se enviar a informação do campo?
1
Obrigatório
Obrigatório
Sim
2
Obrigatório
Condicional
Sensibilizado pelo critério de condicionalidade
Sim
3
Obrigatório
Condicional
Não sensibilizado pelo critério de condicionalidade
Não
4
Obrigatório
Opcional
Dado faz sentido no contexto
Sim
5
Obrigatório
Opcional
Dado não faz sentido no contexto
Não
6
Opcional
Obrigatório
Sim
7
Opcional
Condicional
Sensibilizado pelo critério de condicionalidade
A critério da instituição
8
Opcional
Condicional
Não sensibilizado pelo critério de condicionalidade
Não
9
Opcional
Opcional
Dado faz sentido no contexto
A critério da instituição
10
Opcional
Opcional
Dado não faz sentido no contexto
Não
Utilização de Nulos, NA e outros valores fictícios
No Open Finance Brasil é
vetado
o uso de
nulos
, de String vazias, “
NA
” ou valores que
não se adequam ao domínio em questão
. As "
transmissoras
" e "
detentoras de conta
" devem utilizar os
padrões estabelecidos
para obrigatoriedade de campos.
Ainda se
prevê
um
período
de
transição
entre versões da
Fase 1 e 4A
para o uso de
Atributos Vazios / Nulos
.
Fase 1 e 4A
Um
atributo omitido
(ou seja, um atributo que não está presente no payload)
será considerado
equivalente a um
atributo que esteja presente
com o valor
null
.
Uma
string vazia
(“”)
não será
considerada equivalente a
null
.
O
valor
booleano
false
não será considerado equivalente a
null
. Os atributos booleanos
opcionais
, por definição, possuirão
três valores
possíveis: verdadeiro (
true
), falso (
false
) e indeterminado (
null
).
Na situação onde o
campo a ser informado
no payload seja
obrigatório
e a Instituição, seja
consumidora
no envio ou
transmissora
no retorno,
não a possuir
, deve-se implementar o
valor padronizado: “NA” - Não se Aplica
, com exceção dos campos declarados como
ENUM
que
deverão ser sempre
preenchidos com os valores válidos para o
ENUM
correspondente.
Ainda se
prevê
um
período
de
transição
entre versões da
Fase 1 e 4A
para o uso de
Atributos Vazios / Nulos
.
Fase 1 e 4A
Um
atributo omitido
(ou seja, um atributo que não está presente no payload)
será considerado
equivalente a um
atributo que esteja presente
com o valor
null
.
Uma
string vazia
(“”)
não será
considerada equivalente a
null
.
O
valor
booleano
false
não será considerado equivalente a
null
. Os atributos booleanos
opcionais
, por definição, possuirão
três valores
possíveis: verdadeiro (
true
), falso (
false
) e indeterminado (
null
).
Na situação onde o
campo a ser informado
no payload seja
obrigatório
e a Instituição, seja
consumidora
no envio ou
transmissora
no retorno,
não a possuir
, deve-se implementar o
valor padronizado: “NA” - Não se Aplica
, com exceção dos campos declarados como
ENUM
que
deverão ser sempre
preenchidos com os valores válidos para o
ENUM
correspondente.
Instrução para instituições que não possuem dados para um campo definidos como obrigatório (por regulação / tecnicamente)
É
obrigação
dos participantes
atender
a todas as
regras estabelecidas
nas especificações das APIs
sobre risco de não conformidade
. Qualquer
divergência deve ser comunicada
ao
ecossistema
e ao
regulador
, sendo estabelecido pela instituição um
plano de ação
para que a situação
seja regularizada
.
Caso a instituição
não possua um dado obrigatório
e
não seja possível através das regras de obrigatoriedade
técnica
omitir o dado (índice 1 e 4 da tabela “Regras para definir obrigatoriedade do envio campo”), a instituição
deverá abrir um chamado
no Service Desk para que o grupo técnico
analise a situação
e recomende a
ação a ser adotada
até que todas as pendências sejam resolvidas.
Instrução para campos não definidos nas instruções normativas
Em determinadas situações o grupo técnico do Open Finance pode entender que um dado não previsto em regulação deve ser trafegado para atender uma API. Nesse caso, o próprio grupo técnico irá indicar qual o tratamento deverá ser adotado para o campo, devendo todas as instituições seguir o que for especificado na documentação da API.
Representação da obrigatoriedade nos documentos técnicos
Swagger
No
Swagger
, a
obrigatoriedade técnica
é refletida no atributo
required
dos
componentes da mensagem
, enquanto a
obrigatoriedade por regulação
será refletida em um atributo
customizado
chamado
x-regulatoryrequired.
O uso do
required
para representar
campos tecnicamente obrigatórios
permite que
geradores de código
consigam automaticamente
refletir a necessidade
e
regra de validações
, inclusive
forçando os erros técnicos
no descumprimento de uma regra.
Por outro lado, o uso do campo customizado
x-regulatory-required
não traz impactos técnicos
, garantindo
compatibilidade
, porém
exigindo
que
próprio desenvolvedor
implemente as
validações de cumprimento da regulação
.
Exemplo:
Open
No
exemplo
fictício, que
representa
os
dados de uma conta
, o
regulador exige
que os seus dados (o identificador único da conta, o seu tipo, instituição, agência e número)
sejam obrigatoriamente informados
.
Entretanto,
tecnicamente
, contas do tipo
pré-pagas
não possuem agência e por isso o campo
Branch
se torna
condicionado
ao cenário em que a conta não é pré-paga.
Dicionário de Dados
O
dicionário de dados
das APIs os dados de
obrigatoriedade regulatória
e
técnica
são
refletidos
respectivamente nas colunas “
Mandatoriedade Regulatória
” e “
Mandatoriedade Técnica
”.
Xpath
Nome
Tipo de dado
Mandatoriedade Regulatória
Mandatoriedade Técnica
Xpath
Nome
Tipo de dado
Mandatoriedade Regulatória
Mandatoriedade Técnica
/data
data
Lista
Obrigatório
Obrigatório
/data/accountId
accountId
Texto
Obrigatório
Obrigatório
/data/type
type
Texto
Obrigatório
Obrigatório
/data/compeCode
compeCode
Texto
Obrigatório
Obrigatório
/data/branchCode
branchCode
Texto
Obrigatório
Obrigatório
/data/number
number
Texto
Obrigatório
Obrigatório
/data/address
address
Objeto
Opcional
Opcional
Exemplo de documentação da mandatoriedade no dicionário de dados. Dados meramente ilustrativos.

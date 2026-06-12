---
                            title: "Tipos de Dados Comuns - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "17377445_Tipos+de+Dados+Comuns"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17377445/Tipos+de+Dados+Comuns"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Tipos de Dados Comuns - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Propriedades
Tipo
Descrição
Exemplos válidos
Tipo
Descrição
Exemplos válidos
AmountString
Uma
string
que representa um valor monetário.
Um número positivo, zero ou negativo.
Sem o símbolo da moeda.
Com pelo menos 1 e no máximo 16 dígitos antes do ponto decimal.
Com no mínimo 2 dígitos (mais dígitos são permitidos, porém não obrigatórios).
Sem formatação adicional. Ex: Separador de milhar.
"1.37"
"54.85"
"3456928.98"
"-2387.02"
Boolean
Valor booleano padrão.
true
false
CurrencyString
Uma
string
que representa a abreviação da moeda conforme especificação ISO-4217.
"BRL"
"USD"
"EUR"
DateTimeString
Campos onde o tipo é string ($date-time), o formato utilizado é AAAA-MM-DDTHH:MM:SSZ, onde T e Z são marcações, representando T a divisão entre data e horário e Z o timezone UTC.
Seu fuso horário atual é o UTC-0 e eventuais validações necessárias devem seguir essas definições.
2022-12-01T08:30:00Z, esse formato é especificado pela RFC-3339
DurationString
Uma
string
que representa um período de duração conforme especificação ISO-8601.
"P23DT23H"
"PT2H30M"
Enum
Uma
string
que representa um domínio de valores
Todos os possíveis valores são definidos.
Os valores devem estar em letras maiúsculas.
Espaços em branco devem ser substituídos por _.
Artigos e preposições devem ser removidos.
Não devem possuir caracteres acentuados.
"PRIMEIRA_OPCAO"
"OUTRA_OPCAO_EXISTENTE"
Integer
Números inteiros.
-1
0
1
RateString
Uma string que representa um valor percentual, tendo como referência que 100% é igual ao valor 1.
Com pelo menos 1 e no máximo 16 dígitos antes do ponto decimal.
Com no máximo 16 dígitos após o ponto decimal.
Sem formatação adicional. Ex: Separador de milhar.
"0.01"
"0.1"
"-0.05"
"-0.98365"
"0.1023"
String
Padrão de texto UTF-8 sem restrição de conteúdo.
"Uma
string
qualquer."
TimeString
Uma
string
que representa a hora conforme especificação RFC-3339,sempre com a utilização de timezone UTC(UTC time format).
"00:39:57Z"
URIString
Uma
string
que representa URI válida.
"
http://www.google.com.br
"
CountryCode
Código do pais de acordo com o código “alpha3” do ISO-3166.
"BRA"
IbgeCode
Código IBGE de Município. A Tabela de Códigos de Municípios do IBGE apresenta a lista dos municípios brasileiros associados a um código composto de 7 dígitos, sendo os dois primeiros referentes ao código da Unidade da Federação.
"3550308"
DateString
Campos onde o tipo é string ($date), o formato utilizado é AAAA-MM-DD.
Seu fuso horário atual é o horário de Brasília UTC-3 e eventuais validações necessárias devem seguir essas definições.
2022-12-01, esse formato é especificado pela RFC-3339
DateTimeMillesecond
Campos onde o tipo é string ($date-time) com precisão de milissegundos, o formato utilizado é  AAAA-MM-DDTHH:MM:SS.sssZ, onde T e Z são marcações, representando T a divisão entre data e horário e Z o timezone UTC.
Seu fuso horário atual é o UTC e eventuais validações necessárias devem seguir essas definições.
2016-01-29T12:29:03.374Z
TimeStampMillesecond
Campos onde o tipo é interger ($int64) com precisão de milissegundos representa o número de milessegundos desde 1º de janeiro de 1970 a 00:00 no horário UTC.
Seu fuso horário atual é o UTC e eventuais validações necessárias devem seguir essas definições.
1454070543374

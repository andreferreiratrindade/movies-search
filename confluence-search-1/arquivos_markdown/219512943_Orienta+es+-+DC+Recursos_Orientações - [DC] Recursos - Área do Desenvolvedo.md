---
                            title: "Orientações - [DC] Recursos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "219512943_Orienta+es+-+DC+Recursos"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/219512943/Orienta+es+-+DC+Recursos"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Orientações - [DC] Recursos - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Finalidade da API Recursos
2
Recursos presentes na API Recursos de acordo com a seleção de produtos pelo cliente para compartilhamento, no ambiente da transmissora
3
Recomendação de uso da API Recursos
4
Estado do recurso e Transições de estado
5
Recomendação uso de
polling
6
Principais mudanças com a entrada da v3 da API Recursos
6.1
Mudanças na recomendação de uso
6.2
Disponibilidade de novo tipo de recurso
6.3
Orientação sobre status code 202
Finalidade da API Recursos
A API Recursos foi criada para dar visibilidade dos recursos atrelados a um determinado consentimento (valido e no status AUTHORISED), bem como da existência de ocorrências que possam impedir o compartilhamento de determinados recursos por parte da instituição transmissora dos dados.
Importante notar que novos recursos podem aparecer na APIRecursos, já que algumas opções de seleção de produtos na confirmação contemplam contratos que venham a ser firmados durante a vigência do consentimento.
Recursos presentes na API Recursos de acordo com a seleção de produtos pelo cliente para compartilhamento, no ambiente da transmissora
Existem três formas de seleção de compartilhamento de recursos ao efetuar a confirmação no ambiente da transmissora (sempre respeitando a seleção na receptora):
i. Seleção
individual de recursos
, na qual é obrigatório que o cliente selecione pelo menos um recurso para compartilhamento daquele tipo de produto (caso o possua na transmissora, de acordo com os critérios para exposição do produto¹), como no caso de Contas e Cartões de Crédito.
ii. Seleção
agrupada de recursos
, na qual não há seleção individual e todos os recursos daquele tipo de produto são contemplados (inclusive contratos firmados durante a vigência do consentimento), como no caso de Câmbio.
iii. Seleção
agrupada de produtos
, na qual não há seleção individual de um tipo de produto ou recurso, e sim de um agrupamento de vários produtos, como no caso de Operações de Crédito e Investimentos. Todos os recursos dos produtos que fazem parte do agrupamento são contemplados (inclusive contratos firmados durante a vigência do consentimento).
No caso da forma de seleção i, é obrigatório que o(s) recurso(s) selecionado(s) pelo cliente seja(m) exposto(s) pela API Recursos, independente de seus status.
No caso da forma de seleção ii e iii, caso o cliente possua recursos de tais produtos na transmissora os mesmos devem obrigatoriamente ser expostos pela API Recursos, independente de seus status. O cliente pode não ter recursos para exposição pela transmissora, no momento da chamada:
pelo fato da transmissora não comercializar os produtos no momento da confirmação
ou
pelo fato de o cliente não ter contratado nenhum produto daquele tipo da transmissora, ou já ter contratado no passado, mas não estar nos critérios de exposição¹ definidos para o produto em questão (p. ex. produto encerrado a mais que 12m).
De acordo com a situação listada acima é possível não haver recursos para compartilhamento, quando selecionadas somente as opções ii e iii na confirmação.
Em situações nas quais não houver recursos para retorno na API Recursos é esperado que seja devolvido um status de sucesso (
status code
http 200) na chamada a API.
¹Consultar as regras específicas nas páginas de orientações dos produtos mencionados
Recomendação de uso da API Recursos
Especialmente após a entrada da v3 da API Recursos, seu uso é de extrema importância para o correto consumo de novos recursos e de forma a evitar erros de interoperabilidade.
Abaixo alguns casos de uso nas quais seu uso pode economizar chamadas e consumo de recursos, pelos motivos listados abaixo:
Primeiro consumo de dados pela receptora.
No primeiro consumo de dados o retorno da Recursos é útil para que a receptora saiba quais recursos estão disponíveis e a quais APIs produtos tais recursos pertencem, de forma a apenas efetuar chamadas à APIs de produtos existentes e consequentemente racionalizando o consumo de recursos computacionais tanto pela receptora quanto pela transmissora.
Receptora efetua chamada a uma API de listagem de produtos e não mais encontra recursos disponíveis para consumo, que anteriormente existiam.
A não existência de recursos no momento do consumo da listagem não necessariamente implica em não haver recursos daquele produto compartilhados. A API Recursos pode ser utilizada para verificação da existência de recursos em status que não são listados nas APIs de listagem de produtos, como UNAVAILABLE ou TEMPORARILY_UNAVAILABLE.
Cliente confirmou uma seleção de produtos agrupados, porém as URLs para consumo das APIs dos produtos não são encontradas no diretório.
Pelas regras definidas a partir da entrada da v3 da API Recursos, a transmissora deve permitir ao cliente confirmar uma seleção de produtos agrupados mesmo que o cliente não possua produtos daquela seleção ou até mesmo em situações nas quais a transmissora não comercialize tais produtos. Dessa forma, a API Recursos deve ser utilizada para verificar a existência de produtos agrupados, e a receptora deve chamar as API de produtos correspondentes. No momento em que recursos de um produto antes não comercializado por uma transmissora estiverem disponíveis na API Recursos, a transmissora obrigatoriamente já precisa ter disponibilizado as URL’s correspondentes no Diretório Central. Recomenda-se atualizações frequentes de leitura das informações do Diretório pelas receptoras, de forma a evitar problemas no consumo na situação descrita.
Recomendações de uso:
Recomenda-se que a receptora consulte a API Recursos logo após identificar que o consentimento se encontra autorizado de modo a obter todos os recursos consentidos pelo cliente e seus respectivo identificadores.
Recomenda-se que a receptora consulte a API Recursos periodicamente, de forma a identificar a existência de novos recursos e produtos, e a atualização de status de recursos existentes.
Recomenda-se que a receptora, caso obtenha um HTTP
Status Code
403 -
Forbidden
nas APIs de Produtos, avalie o JSON retornado no
body
da requisição para identificar as informações adicionais referentes ao erro, como o status especifico do Recursos que impede o consumo da informação.
Recomenda-se que a receptora consulte a API Recursos caso obtenha um erro nas APIs de Produto de modo a identificar uma possível alteração de status do recurso.
Em relação a primeira chamada da API Recursos, caso a Transmissora ainda esteja preparando a listagem dos recursos autorizados, deve ser retornado o código HTTP
Status Code
202 com o
body
vazio e a receptora deverá seguir as recomendações de
polling
Estado do recurso e Transições de estado
O recurso compartilhado pode se encontrar em diferentes estados na API Recursos, de acordo com o status do produto na instituição transmissora. Significado de cada status:
AVAILABLE: status para uso quando o recurso estiver disponível para consumo.
TEMPORARILY_UNAVAILABLE: status para o uso quando por algum motivo o recurso estiver indisponível temporariamente, porém ele pode voltar a ficar disponível.
UNAVAILABLE: status utilizado para indicar que o recurso está indisponível e não voltará a ficar disponível para consumo. A exceção a esse comportamento se dá em alguns produtos de investimentos (Fundos e Renda Variável). Especificamente nesses produtos o recurso pode voltar a ficar disponível - recomendada a leitura de orientação gerais de investimentos.
PENDING_AUTHORISATION: status indicado para recursos que fazem parte do consentimento, porém ainda estão pendentes de alçada(s) de aprovação
A máquina de estados possíveis encontra-se abaixo:
Open
As transições de estados possíveis conforme a imagem acima:
PENDING_AUTHORISATION é um status apenas inicial e não deve ser alcançado a partir dos demais status.
PENDING_AUTHORISATION pode ser transicionado para AVAILABLE, TEMPORARILY_UNAVAILABLE e UNAVAILABLE.
UNAVAILABLE é um status final e não permite mais transições aos demais status, exceto no caso especificado (produtos Renda Variável e Fundos, nas API de Investimentos)
AVAILABLE pode ser transicionado para TEMPORARILY_UNAVAILABLE e UNAVAILABLE.
TEMPORARILY_UNAVAILABLE pode ser transicionado para AVAILABLE e UNAVAILABLE.
Abaixo alguns exemplos de casos de uso de recursos (considerando consentimento autorizado e válido) e o status esperado para os mesmos:
Recursos que se encontram em
plena utilização
e disponíveis nos canais de atendimento eletrônico para os usuários finais devem ter seus status como AVAILABLE;
Recursos que se encontram em
bloqueios temporários
, quando o cliente não possui acesso ao recurso por meio dos canais de atendimento eletrônico, devem retornar o status TEMPORARILY_UNAVAILABLE;
Recursos que se encontram em
bloqueios definitivos
, quando o cliente não possui acesso ao recurso por meio dos canais de atendimento eletrônico, devem retornar o status UNAVAILABLE;
Recursos que se encontram
encerrados
, quando o cliente não possui acesso ao recurso por meio dos canais de atendimento eletrônico, devem retorna o status UNAVAILABLE;
Recursos que foram migrados e se encontram indisponíveis nos canais de atendimento eletrônico devem retornar o status UNAVAILABLE;
Recursos em status UNAVAILABLE por mais de 3 meses podem ser expurgados da base da transmissora e não necessita retornar como status UNAVAILABLE em futuras requisições ao endpoint /resources;
Casos de uso que um cliente final efetue um consentimento para mais de um recurso e um deles exija a aprovação de
múltiplas alçadas
(PENDING_AUTHORISATION) e o outro esteja
disponível para consulta
(AVAILABLE, o comportamento esperado é que cada recurso tenha seu status representado de forma independente.
Importante notar que os casos de uso descritos não são exaustivos, e de acordo com a especificidade das APIs de produtos as regras podem ser complementadas. é recomendada a leitura complementar das regras aplicáveis a cada API de produto.
Recomendação uso de
polling
É recomendado que a Instituição Receptora implemente um
retry
exponencial (o tempo de espera entre a última chamada e a próxima chamada da API deve crescer exponencialmente), de forma a não sobrecarregar a API Recursos.
O tempo máximo para o retorno 202 após a criação do consentimento nas primeiras chamadas à API Recursos deve ser de 5 minutos. O erro de retorno após o tempo máximo deve ser 504, com detalhes conforme definição abaixo:
"errors":[
{
"code":"RETRY_EXCEDIDO",
"title":"Retry exponencial excedido.",
"detail":"O tempo de retry exponencial foi excedido."
}
]
Em casos em que seja retornado o código de erro HTTP Status Code 5xx de forma persistente, recomenda-se que a Instituição Receptora consulte a API Comum (Discovery) para verificar a disponibilidade da API requisitada antes de realizar uma nova tentativa de consulta.
Principais mudanças com a entrada da v3 da API Recursos
Mudanças na recomendação de uso
Com a entrada da v3 da API Recursos, seu uso deixa de ser opcional e passa a ser necessário para o correto funcionamento das mudanças introduzidas com tal versão. A v3 da API Consents permite que o cliente compartilhe em seu consentimento produtos ainda não comercializados pela transmissora – para maiores detalhes consultar “Orientações Importantes – Consentimento”. Com tal mudança, a receptora já possuirá os scopes e permissions necessários ao consumo dos novos produtos. No momento em que forem implementados pela transmissora, a forma de identificar a contratação de tais produtos pelo cliente será através da leitura de recursos da API Recursos.
Disponibilidade de novo tipo de recurso
Com a entrada da v3 da API Recursos, passa a ser disponibilizado um novo tipo de recurso, para possibilitar o consumo de recursos de produtos de Câmbio.
Orientação sobre status code 202
O
status code
202 pode ser utilizado pela transmissora na primeira chamada da API Resources por uma receptora (para um novo consentimento). Com a entrada da v3 da API Resources, passa a haver o tempo máximo de 5 minutos para o retorno 202. Após esse tempo a transmissora deve usar o
status code
de erro apropriado para o não retorno das informações.

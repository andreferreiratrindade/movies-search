---
                            title: "FAQ - MQD - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "362579143_FAQ+-+MQD"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/362579143/FAQ+-+MQD"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # FAQ - MQD - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            O que significa a sigla M.Q.D.?
M.Q.D. é a sigla para Motor de Qualidade de Dados, ferramenta de código aberto que avalia a qualidade dos dados que são compartilhados entre os participantes do Open Finance, assegurando assim a integridade das informações.
Qual é o escopo de endpoints que o MQD vai receber?
Os endpoints suportados pelo MQD podem ser vistos na página abaixo:
Tabela de endpoints validados pelo Motor de Qualidade de Dados (MQD) - Draft - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor (atlassian.net)
Temos a necessidade de teste funcional ou certificação específica dos participantes para o MQD?
Será disponibilizado um ambiente Sandbox seguro para que as instituições possam realizar testes funcionais da aplicação antes de entrar em produção.
Quais são os padrões de certificado de segurança que precisam ser adotados para se instalar o MQD?
MQD utiliza as práticas de confiabilidade e segurança do ecossistema de finanças abertas, incluindo uso de certificados para ICP-Brasil, para conexão mTLS e fluxo de segurança de “client_credentials” com token de acesso
A instalação do MQD e obrigatória?
Sim, seguindo o cronograma aprovado pelo GT de Qualidade de Dados.
Como validar a data da request?
O Body é dinâmico (é o mesmo response obtido da TRANSMISSORA), por isso ele não foi incluso no Swagger.
O report enviado para o servidor central deverá conter todos os requests de um x intervalo de tempo, ou caso alguns dados ainda estejam em processamento poderão ser enviados na próxima janela?
Esse relatório conterá todos os relatórios que estão validados corretamente, caso existam itens a serem validados na memória, estes serão enviados no próximo envio.
A Instituição Financeira precisa estar com a organization id registrada em algum lugar pro getJWKToken?
O cliente precisa de dois IDs:
ID da RECEPTORA é configurado coo variable de ambiente na configuração do container
ID da TRANSMISORA, que precisa ser incluso como Header no request
Temos cenários com retornos de grandes payloads (por exemplo contas). O Motor de qualidade de Dados está preparado para lidar com esses retornos grandes? Existe algum limite de tamanho de payload para o MQD, pensando inclusive na Mensageria interna do MQD, ela suportará mensagens grandes?
Hoje não há limite para o Motor de Qualidade de Dados, tanto no tamanho quanto na quantidade de mensagens. Mas ainda recomendamos o monitoramento constante do contêiner da aplicação, pois dependendo da carga entregue será necessário aumentar os recursos (RAM e CPU) para processar adequadamente todas as mensagens.
Hoje não temos acesso ao repositório do Motor de Qualidade de Dados, há um previsão de quando ele será disponibilizado no Github?
O acesso ao repositório do MQD pode ser solicitado através do Portal de Solicitação de Acessos através do link abaixo.
https://openfinancebrasil.atlassian.net/servicedesk/customer/portal/1/group/17
Estou com uma dúvida que não está explicada nem na documentação neste FAQ. Como faço para fazer perguntas para especialistas em MQD?
Você pode acessar o
canal no Slack do Motor de Qualidade de Dados
para sanar possíveis dúvidas sobre a instalação e funcionamento da feramenta.

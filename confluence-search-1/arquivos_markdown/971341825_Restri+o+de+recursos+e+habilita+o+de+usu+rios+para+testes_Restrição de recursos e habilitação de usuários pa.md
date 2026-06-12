---
                            title: "Restrição de recursos e habilitação de usuários para testes - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "971341825_Restri+o+de+recursos+e+habilita+o+de+usu+rios+para+testes"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/971341825/Restri+o+de+recursos+e+habilita+o+de+usu+rios+para+testes"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Restrição de recursos e habilitação de usuários para testes - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Durante o período de testes em produção, os novos produtos, funcionalidades ou marcas deverão ser disponibilizados apenas para uma base controlada e variável de usuários, que poderá incluir funcionários ou prestadores de serviço de instituições participantes, funcionários ou prestadores de serviço da Associação Open Finance e servidores do Banco Central do Brasil.
A aplicação dessa restrição é de responsabilidade das instituições consumidoras de dados, cabendo às instituições provedoras de dados indicar, por meio do Diretório de Participantes, quais recursos se encontram em processo de homologação. À Associação Open Finance compete consolidar a relação de usuários habilitados para testes e disponibilizá-la às instituições consumidoras
Open
Publicação no Diretório e configuração de restrição do recurso
Instituições provedoras de dados e serviços (transmissoras, detentoras e credoras originais) devem configurar a restrição de recurso no Diretório de Participantes no momento de publicação do recurso em produção.
Nova marca:
Flag
no servidor de autorização
Servidores de autorização > Editar servidor de autorização > Flags: “Homologacao”
A atribuição dessa
flag
é
exclusiva para novas organizações
Novo produto ou funcionalidade em produto existente: Metadado na Família da API
Servidores de autorização > Recursos de API > Ações > Configurar Metadados da API: “Em homologacao” ou metadado específico a ser definido para cada piloto
Indicação de usuários para realização de testes em produção
Após a publicação, a instituição deverá indicar, por meio de formulário abaixo, a relação de usuários (CPFs) que deverão ser habilitados pelas consumidoras de dados e serviços (receptoras, iniciadoras e proponentes) para a realização de testes.
Para compartilhamento de
dados em massa
dos usuários, utilizar CSV, conforme seguinte modelo de arquivo:
Os campos enviados, seja de forma individual ou em massa, devem necessariamente respeitar as seguintes regras abaixo. Caso contrário, os dados
não serão
enviados ou processados.
Campo
Regra de preenchimento
Exemplo
Campo
Regra de preenchimento
Exemplo
CPF
Apenas números,
sem
traços ou pontos
38301141093
CNPJ
14 caracteres, sem traços ou pontos
58569410000138
Email
Endereço de e-mail dos usuários testadores¹
email@openfinancebrasil.org.br
OrgID
Conforme OrgID da instituição no diretório,
com
traços
d7384bd0-842f-43c5-be02-9d2b2d5efc2c
Instituição
Conforme nome da instituição no diretório
ASSOCIACAO OPEN FINANCE
1 Envio opcional. Exclusivo para utilização de Consumidores de Dados e Serviços que utilizam endereço de e-mail para habilitação de usuários para testes. Atualmente, apenas a ITP Google Pay declarou essa necessidade.
Formulário para compartilhamento dos dados dos usuários abaixo:
Verificação de restrição de uso
A aplicação da restrição é de
responsabilidade das instituições consumidoras de dados
, que deverão implementar mecanismo de consulta de restrição de recursos e habilitação dos usuários indicados pelas provedoras. A consulta desses usuários poderá ocorrer através do link
https://api.openfinance-brasil.org.br/participantes-piloto
Credenciais para acesso à API podem ser solicitados para a Associação através de abertura de chamado no
service desk
Prazos de implementação de mecanismo de restrição e habilitação de usuários
Instituições consumidoras de dados deverão implementar os mecanismos de habilitação de usuários para testes em produção até
06/02/2026
O
onboarding
de transmissores e detentores poderá ocorrer sem restrição de usuários até essa data. A partir de então, passará a ocorrer exclusivamente com a aplicação do fluxo de restrição
O
onboarding
de receptoras e iniciadoras não depende deste fluxo para restrição usuários, e, portanto, os testes em produção deverão ocorrer com restrição imediata

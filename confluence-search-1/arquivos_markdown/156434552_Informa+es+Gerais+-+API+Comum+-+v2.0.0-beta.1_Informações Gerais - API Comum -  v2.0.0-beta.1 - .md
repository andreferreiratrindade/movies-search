---
                            title: "Informações Gerais - API Comum -  v2.0.0-beta.1 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "156434552_Informa+es+Gerais+-+API+Comum+-+v2.0.0-beta.1"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/156434552/Informa+es+Gerais+-+API+Comum+-+v2.0.0-beta.1"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Informações Gerais - API Comum -  v2.0.0-beta.1 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Contexto:
Conforme IN nº
306 de 19/02/2022
, o Item 2 do Anexo lista todas as APIs integrantes do Open Finance. Dentre elas, as APIs de Status, de Outages e Métricas são comuns a todos os participantes do Open Finance Brasil, independentemente da fase de adesão.
Relatórios e Métricas
Situação do Ambiente
Deve dar acesso a dados sobre a disponibilidade atual das implementações das APIs, bem como a dados sobre indisponibilidades programadas.
Métricas
Deve dar acesso a dados de performance de todas as APIs disponibilizadas.
Sendo assim:
Todas as instituições devem publicar essas APIs que monitoram a situação do ambiente;
APIs comuns devem reportar os dados de disponibilidade e indisponibilidade programada de
todas as APIs
que a instituição oferece;
APIs comuns devem ser atualizadas conforme lançamento de novas APIs pela instituição ou atualização das APIs já existentes.
API de status: (GET /discovery/v1/status)
Visão geral
A instituição deve disponibilizar o código de status de todas as suas APIs nesse endpoint
Visão de alto nível das estruturas de dados
Open
Dicionário de dados
Fazer download do dicionário de dados
API de outages: (GET /discovery/v1/outages)
Visão geral
A instituição deve disponibilizar previamente a previsão de indisponibilidade agendada dos seus serviços através desse endpoint.
Visão de alto nível das estruturas de dados
Open
Dicionário de dados
Fazer download do dicionário de dados
Exemplo de código
Na estrutura de retorno exemplificada abaixo, no caso em que o parâmetro isPartial devolvido seja true, o array unavailableEndpoints deve conter a lista de endpoints indisponíveis:
{
"data": [
{
"outageTime": "2020-07-21T08:30:00Z",
"duration": "PT2H30M",
"isPartial": false,
"explanation": "Atualização do API Gateway"
}
],
"links": {
"self": "https://api.banco.com.br/open-banking/channels/v1/<resource>",
"first": "https://api.banco.com.br/open-banking/channels/v1/<resource>",
"prev": "https://api.banco.com.br/open-banking/channels/v1/<resource>",
"next": "https://api.banco.com.br/open-banking/channels/v1/<resource>",
"last": "https://api.banco.com.br/open-banking/channels/v1/<resource>"
},
"meta": {
"totalRecords": 1,
"totalPages": 1
}
}

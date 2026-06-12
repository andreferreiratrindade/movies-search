---
                            title: "Diretrizes gerais dos testes em produção - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1209892867_Diretrizes+gerais+dos+testes+em+produ+o"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1209892867/Diretrizes+gerais+dos+testes+em+produ+o"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Diretrizes gerais dos testes em produção - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Introdução
Este guia tem como objetivo disponibilizar aos participantes as diretrizes para testes em produção, incluindo seus objetivos, critérios e procedimentos operacionais. A realização desses testes é obrigatória para todas as instituições participantes, independentemente de sua modalidade de participação no Open Finance, e deverá ocorrer antes da disponibilização de novas marcas, produtos ou serviços à população.
Objetivos
A política de testes em produção está em consonância com as Resolução BCB 463, e tem como principais objetivos:
I) Garantir o comportamento funcional dos produtos e serviços do Open Finance;
II) Garantir uma jornada de experiência do usuário fluida e sem fricções ao usuário final;
III) Garantir a qualidade de dados compartilhados;
IV) Garantir a integração entre as instituições com as ferramentas de monitoramento do perímetro central;
V) Garantir a interoperabilidade do ecossistema e reduzir a quantidade de incidentes bilaterais.
Modelos de testes em produção
Os testes em produção poderão ser realizados em modelos de piloto ou
onboarding.
Pilotos:
Período previsto nos cronogramas de implementação aplicado ao lançamento de novos produtos e/ou funcionalidades por participantes ativos do ecossistema. O não atingimento de qualquer um dos critérios até o fim do piloto terá as seguintes consequências:
Para consumidores de dados e serviços: não serão considerados aptos para disponibilizarem o produto para o público geral até atingimento de sucesso em todos os indicadores;
Para provedores de dados e serviços: as instituições consumidoras de dados e serviços terão a opção de não mostrar a marca com problemas em produção até que a situação seja regularizada
Onboarding
:
Processo de testes direcionado exclusivamente a novos entrantes no ecossistema ou participantes que queiram ofertar um produto adicional após o período de piloto desse produto.
Novos entrantes obrigatórios no Open Finance deverão obter sucesso em todos os indicadores monitorados até 6 semanas da data de entrada da instituição;
Novos entrantes voluntárias não possuem prazo para entrada em produção.
Restrição de usuários
Durante o período de testes em produção, os novos produtos, funcionalidades ou marcas deverão ser restritos para uma base de usuários variável. Essa restrição é de responsabilidade da instituição consumidora de dados, enquanto o provedor não deve impedir o acesso a nenhum usuário.
A Associação é responsável por coletar a lista de usuários testadores:
das instituições participantes (consumidores e provedores de dados e serviços)
geralmente, são recomendados cerca de 100 usuários por instituição, mas não é um critério obrigatório
do Banco Central
da Associação
de responsáveis por testes
Exceto em alguns casos, essa lista deverá conter apenas o CPF dos usuários e ser compartilhada com os consumidores de maneira anonimizada. Os consumidores são responsáveis por garantir que essa lista de usuários possa testar a funcionalidade.
Adicionalmente, a funcionalidade poderá ser disponibilizada para uma porcentagem da base de clientes, de maneira escalonada, a depender de aprovação em testes anteriores ou de tempo. Essa opção de liberar para base de clientes dependerá do produto sendo lançado, e poderá seguir o exemplo abaixo:
0% entre 01/01/20XX e 15/01/20XX;
No mínimo 1% ou 2.000.000 entre 16/01/20XX e 15/02/20XX;
No mínimo 5% ou 10.000.000 entre 16/02/20XX e 05/03/20XX;
No mínimo 10% ou 20.000.000 entre 06/03/20XX e 20/03/20XX;
No mínimo 50% ou 100.000.000 entre 21/03/20XX e 05/04/20XX;
100% a partir de 06/04/20XX (
fim do piloto
).
Critérios de sucesso dos testes em produção
Durante o período de testes em produção, a instituição participante será monitorada pela Associação Open Finance, e deverá obter sucesso nos indicadores específicos de cada modalidade. Estes indicadores são:
Item
Descrição
Item
Descrição
Comportamento funcional
Sucesso em módulos de teste da Ferramenta de Validação em Produção (FVP)
Jornada de experiência do usuário
Monitoramento simplificado da jornada de experiência do usuário
Integração com ferramentas do perímetro central
Pareamento de 95% das chamadas com a Plataforma de Coleta de Métricas (PCM) e envio de todos additionalInfos ou dados equivalentes do produto;
Para os participantes que tenham utilização obrigatória do Motor de Qualidade de Dados (MQD), não haver apontamentos relativos a não envio ou qualidade.
Testes bilaterais
Realização de testes bilaterais entre instituições participantes, respeitando critérios específicos de volumetria e representatividade
Incidentes bilaterais
Resolução de todos os chamados em aberto até a conclusão do processo
Consulta de organizações homologadas
Instituições de organizações aptas a disponibilizar um produto ou serviço aos seus clientes finais podem ser consultadas através do Diretório de Participantes, não podendo haver nenhuma
flag
ou metadado da Família de API indicando status de homologação do recurso.

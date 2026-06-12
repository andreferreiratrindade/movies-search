---
                            title: "Tipos de Versionamento - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "86835268_Tipos+de+Versionamento"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/86835268/Tipos+de+Versionamento"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Tipos de Versionamento - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            O controle de versão das especificações do Open Finance Brasil é composto pelos tipos de versionamento
major
,
minor
e
patch
. Os nomes e o formato de numeração utilizados pelos tipos de versionamento são idênticos aos utilizados no
semantic versioning
, no entanto, a definição utilizada diverge.
A seguir, as definições para cada um dos tipos de versionamento:
Major
:
Contempla alterações de especificações derivadas de grandes lançamentos planejados pelo GT baseados nas prioridades do ecossistema e do Banco Central;
Contêm grandes mudanças de arquitetura ou de escopo como inclusão de novos arranjos de pagamento e atualizações na máquina de estados;
Pode conter várias dessas mudanças agrupadas;
Não possui restrição quanto aos tipos de alterações existentes;
Permite todas as alterações não aceitas nos versionamentos
minor
e
patch
;
Exemplos: v
1
.0.0, v
2
.0.0
Minor
:
Permite alterações com quebra de contrato nos casos de correção de
bugs
que estejam impactando negativamente o ecossistema e adequações regulatórias que não podem aguardar o próximo versionamento
major
;
Permite adição de novas funcionalidades, desde que não haja quebra de contrato;
Para toda proposta de alteração
minor
, deve ser feita uma análise de risco/retorno pelo GT responsável, pois o versionamento
minor
subentende um processo de testes simplificado, se comparado à
major
;
Permite ajustes (adição, alteração, exclusão) para valores dos campos do tipo ENUM, mesmo que haja quebra de contrato, sendo necessário análise de risco/retorno pelo GT responsável;
Exemplos: v1.
1
.0, v1.
2
.0
Patch
:
Contempla alterações de documentação para promover esclarecimentos no texto ou correções feitas no
Swagger
que não impactam em nada na funcionalidade das APIs;
Permite alterações sem quebra de contrato no caso de correções de bugs ou cenários específicos que não demandem implementação por todos os participantes do ecossistema;
Exemplos: v1.1.
1
, v1.1.
2
Antes da publicação (
release
) da versão estável (
stable
) possuímos estágios em que a versão sendo construída é considerada instável (
unstable
). No estágio
unstable
, a versão é considerada não finalizada e, por isso, deve ser submetida a testes e avaliações por parte do ecossistema até que alcance a maturidade necessária para ser considerada
stable
. No Open Finance Brasil, vamos trabalhar com duas extensões
unstable
que dividem o estágio em duas partes:
Beta:
estágio suficientemente evoluído para avaliações e testes externos, ainda pode possuir mudanças significativas.
A primeira versão é publicada como (x+1).0.0-beta.1;
Pode sofrer atualizações decorrentes de tickets abertos pelo ecossistema;
A cada nova publicação de atualização, o contador será incrementado de modo que tenha-se, por exemplo: (x+1).0.0-beta.2, (x+1).0.0-beta.3, ...;
Corresponde ao estágio inicial do Swagger disponibilizado na Área do Desenvolvedor;
Estágio em que é iniciado o processo de maturação do motor de conformidade;
É nesse estágio que as instituições deverão iniciar o desenvolvimento das APIs;
Release candidate
(RC):
estágio quase pronto para lançamento final, sem novos aprimoramentos de recursos, limitando alterações a correções de
bugs
e questões de segurança. Estágio mais estruturado e próximo ao que será a versão estável.
A primeira versão é publicada como (x+1).0.0-rc.1;
A cada nova publicação de atualização, o contador será incrementado de modo que tenha-se, por exemplo: (x+1).0.0-rc.2, (x+1).0.0-rc.3, ...;
Esse estágio é iniciado após o marco de 50% de sucesso nos testes;
Esse estágio é finalizado após o marco de 100% de sucesso nos testes;
Estágio em que é iniciado o período de certificação após o atingimento da maturidade do motor de conformidade.
Após cada alteração de estágio, ou seja, na passagem de beta para RC ou de RC para
stable
, o ecossistema será comunicado através de Informa para o devido acompanhamento da evolução das especificações. Entretanto, cabe às instituições acompanharem na Área do Desenvolvedor as atualizações dentro do mesmo estágio, por exemplo, de 1.0.0-beta.1 para 1.0.0-beta.2.
Toda atualização de especificação deve vir acompanhada de
changelog
, por exemplo:
Dentro de um mesmo estágio: 1.0.0-beta.1 ➞ 1.0.0-beta.2;
Entre estágios :2.0.0-beta.4 ➞ 2.0.0-rc.1;
Entre versões: 4.0.0 ➞ 4.1.0.
Open
Definição sobre período de convivência de acordo com o tipo de versionamento
Versionamento
Restrições
Nova versão da API (Current)​
Versão anterior da API (Deprecated)
Possui data limite para implementação
Necessita certificação
Depreciação
(Deprecated)
Aposentadoria
(Retired)
Observação
Major
Não haverá mais do que duas versões em convivência
Fornecedores²: Sim, no início do período de convivência
Consumidores³: Sim, no final do período de convivência
Sim
90 dias contados a partir do início em produção da nova versão em casos em que não houver período de piloto.
Nos casos em que houver piloto, o período de convivência acontecerá durante o período do piloto, seja ele com duração
maior ou menor que os 90 dias
Acontecerá quando terminar o período de convivência, ficando vigente apenas a nova versão major
N/A
Minor Planejada
Não haverá breaking change
Fornecedores: Sim
Consumidores: Não
Sim, processo simplificado
Não haverá período de convivência
Aposentadoria imediata
Não há problemas de interoperabilidade
Minor Crítica Não Sincronizada¹
Necessidade de implementar o mais breve possível até a data limite estabelecida, porém os participantes não precisam sincronizar o momento do início em produção
Fornecedores: Sim
Consumidores: Sim
Sim, processo simplificado
Não haverá período de convivência
Aposentadoria imediata
Não gerar novos problemas de interoperabilidade para quem consome e a aplicação das soluções pelas instituições podem ocorrer até a data limite para implementação estabelecida em informa.
Minor Crítica Sincronizada
Necessidade de implementar o mais breve possível, porém os participantes devem sincronizar o momento do início em produção
Fornecedores: Sim
Consumidores: Sim
Sim, processo simplificado
Não haverá período de convivência
Aposentadoria imediata
Há riscos de novos problemas de interoperabilidade para quem consome e a implementação em produção deve ser sincronizada na data e hora estabelecida em informa
Patch
N/A
Fornecedores: Sim, deve ser implementada 7 dias úteis após a divulgação do Informa sobre a nova versão
Consumidores: Não
Não
Não haverá período de convivência
Aposentadoria imediata
N/A
Legenda:
1-
Sincronizada: Início em produção realizado ao mesmo tempo por todos os participantes;
2-
Fornecedores: Detentoras de conta e transmissoras de dados;
3-
Consumidores: Iniciadoras de pagamento e receptoras de dados.

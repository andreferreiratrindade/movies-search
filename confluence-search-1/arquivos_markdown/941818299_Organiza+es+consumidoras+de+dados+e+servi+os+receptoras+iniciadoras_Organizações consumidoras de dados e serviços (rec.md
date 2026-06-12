---
                            title: "Organizações consumidoras de dados e serviços (receptoras/iniciadoras) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "941818299_Organiza+es+consumidoras+de+dados+e+servi+os+receptoras+iniciadoras"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/941818299/Organiza+es+consumidoras+de+dados+e+servi+os+receptoras+iniciadoras"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Organizações consumidoras de dados e serviços (receptoras/iniciadoras) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Organizações que desejarem atuar como recebedoras de dados deverão publicar suas declarações de software para realizar o Dynamic Client Registration (DCR), ou registro dinâmico do cliente nos servidores de autorização dos provedores, e ter acessos aos dados e recursos das organizações provedoras de dados de acordo com o escopo de seu papel regulatório.
Para a declaração de software, é necessário que a organização adicione um certificado de transporte (BRCAC) emitido por Autoridades Certificadoras reconhecidas pela cadeia ICP Brasil. O diretório irá validar que o certificado possui UID em seu subject igual ao UID da declaração do software no caso do BRCAC.  É possível executar essa consulta avaliando se o UID do subject é igual ao UID apresentado no diretório, que pode ser obtido utilizando a ferramenta openssl com o seguinte commando: openssl x509 -in brcac.pem -noout -subject .
No ambiente sandbox, é possível a geração de certificados de transporte emitidos pelo próprio Diretório para uso exclusivo neste ambiente.
Após a criação da declaração de software, a organização deverá obter um software statement assertion (SSA). Uma Software Statements Assertion (SSA) é um JWT assinado do diretório que contém todas as informações sobre um aplicativo que existe em um determinado momento no diretório. Inclui a localização de todas as chaves públicas vinculadas a esta declaração de software e todos os outros metadados de que um banco precisa para validar a legitimidade do aplicativo.
A entrada em produção de instituições consumidora de dados e serviços só deverá ocorrer após a obtenção de certificação de segurança RP e a realização das devidas integrações com ferramentas do perímetro central. Instituições que atuarem na modalidade de iniciadoras de pagamento deverão realizar o processo de
onboarding
de ITPs.
Clique para conferir o passo a passo para criar uma declaração de software
Clique para conferir o passo a passo para vinculação do papel regulatório na declaração de software
Clique para conferir o passo a passo para registro de certificado de transporte    da declaração de software
Clique para conferir o passo a passo para obter o
software statement assertition
(SSA)
Clique para conferir o passo a passo para emissão de certificados no Diretório para uso exclusivo do ambiente sandbox
Clique para conferir as regras e obrigações das instituições participantes do Open Finance Brasil

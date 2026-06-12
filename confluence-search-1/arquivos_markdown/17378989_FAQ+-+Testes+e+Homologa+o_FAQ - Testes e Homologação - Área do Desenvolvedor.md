---
                            title: "FAQ - Testes e Homologação - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "17378989_FAQ+-+Testes+e+Homologa+o"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378989/FAQ+-+Testes+e+Homologa+o"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # FAQ - Testes e Homologação - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1. Quais certificações uma instituição precisa para entrar em produção?
Detentoras e transmissores de dados é necessário certificação funcional e de segurança, iniciadoras e receptoras é necessária certificação de segurança. Maiores informações sobre as certificações obrigatórias para cada modalidade estão disponíveis no documento “Orientações para certificação”, disponível em no link conforme item 21 desta FAQ.
2. Quando eu preciso obter as certificações funcionais e de segurança?
Novos entrantes:
Para entrada em produção de todas as APIs.
Certificações funcionais e de segurança:
Devem seguir as datas de acordo com sua participação no arranjo ou de adesão ao compartilhamento de dados.  Por exemplo, uma instituição que entre em operação restrita no Pix, possui 10 dias para entrar em produção pelo Open Finance, já com todas as certificações necessárias.
Participantes atuais:
Certificações funcionais:
Devem seguir as datas de
go live
do versionamento das APIs.
Certificações de segurança:
Via de regra, a certificação terá duração de 12 meses. As instruções e exceções estão disponíveis na política de renovação, conforme item 18 desta FAQ.
3. O que é a OIDF?
OpenID Foundation é uma organização sem fins lucrativos que promove tecnologias OpenID. No Open Finance, eles são os fornecedores das certificações de segurança.
4. O que é OP e RP, que aparecem nos nomes das certificações de segurança?
OP: OpenID Providers (detentoras e transmissoras)
RP: Relying Parties (receptoras e iniciadoras)
5. O que é CIBA e qual a exigência?
CIBA significa Client Initiated Backchannel Authentication.
A oferta de CIBA é opcional, porém, para todas as instituições que desejem disponibilizar essa modalidade, a certificação de CIBA da OIDF será obrigatória.
6. O que é a FVP e como ela funciona?
FVP significa Ferramenta de Validação em Produção. É uma ferramenta desenvolvida pelo ecossistema que executa parte dos testes de segurança e funcionais em ambiente produtivo.
A ferramenta busca averiguar se o comportamento das instituições se mantém consistente com as certificações e se os cadastros em produção estão feitos da maneira correta.
Maiores informações estão disponíveis em:
https://gitlab.com/obb1/certification/-/wikis/Automated-Production-Tests
7. As variações DCR e FAPI OP estão incluídas na taxa que cada instituição vai pagar para a certificação FAPI ?
FAPI OP, DCR e suas variações (private key e MTLS, com ou sem JARM) estarão inclusos na taxa de certificação paga     pela instituição, desde que as submissões sejam feitas juntas.
FAPI-CIBA e RP, não estão contempladas nas certificações acima, devendo ser pagas taxas adicionais para cada uma dessas  certificações.
8. Posso certificar diversos
authorisation servers
com uma única certificação?
Pela política do Open Finance a certificação deverá ser realizada em todas as implementações únicas, devendo a instituição garantir mesma tecnologia e configuração para todos os authorisation servers contemplados.
Conforme orientação da OIDF, entende-se por implementação única: “cada issuer presente no endpoint well-know do authorisation server". Dessa forma, a certificação deveria ser realizada ao nível do issuer no authorisation server, logo múltiplos servidores de autorização que compartilhem o mesmo issuer poderiam estar englobados numa só certificação.
9. Para diferentes marcas, posso realizar uma única certificação funcional para a mesma API?
Pela política do Open Finance a certificação deverá ser realizada em todas as implementações únicas, devendo a instituição garantir mesma tecnologia e configuração para a API certificada.
A única hipótese de se utilizar a mesma certificação funcional para mais de uma marca, é no caso destas marcas compartilharem a mesma infraestrutura.
10. Utilizo um provedor terceiro que já possui certificação funcional e/ou de segurança, preciso me “recertificar”?
A certificação deverá ser realizada ao nível do conglomerado prudencial, confederação ou instituição, sendo obrigatória a certificação independente da utilização de um provedor externo que já possua certificação.
11. É necessário se certificar na plataforma da OIDF para utilizar o motor de conformidade funcional?
A instituição precisará ter passado com sucesso no motor de segurança para executar o motor de conformidade funcional.
12. Como é feito o pagamento das certificações OIDF pelas instituições?
O pagamento deve ser realizado de acordo com orientações do Guia de Certificação, disponível no link conforme item 22 desta FAQ.
13. Instituições poderão aderir à OIDF como membro e pagar a taxa reduzida na certificação de segurança?
Sim, qualquer instituição que queira e consiga se associar como membro poderá realizar o pagamento da taxa reduzida na certificação de segurança de acordo com as políticas da OIDF.
Além disso, há condições especiais para renovações de certificações FAPI-OP e DCR com valor reduzido para solicitações feitas com antecedência. Maiores detalhes estão disponíveis no
Guia de Certificação, disponível no link conforme item 22 desta FAQ.
14. Existirá algum custo para realização da certificação funcional?
Não há custos para realização da certificação funcional.
15. Qual o ambiente deve ser utilizado para certificação?
Para qualquer certificação, deve ser utilizado o ambiente de testes da instituição e do Diretório (sandbox).
Validações em ambiente produtivo são realizados pela Ferramenta de Validação em Produção (FVP).
16. Como acesso o Sandbox do diretório de participantes?
O acesso pode ser realizado pelos administradores da instituição no ambiente de sandbox do Diretório de Participantes.
https://web.sandbox.directory.openbankingbrasil.org.br/
Os ambientes de produção e de sandbox do Diretório são desvinculados e ser administrador em um não confere poder de administrador no outro.
A adição de administradores pode ser realizada por qualquer administrador atual da instituição em sandbox, seguindo o  passo a passo para cadastro , que pode ser encontrado em:
Guia de Operação do Diretório Central
archived
Preview
17. Como  acesso o motor de conformidade segurança da OIDF?
O acesso a plataforma da OIDF é livre para todo o público.
O Motor de conformidade de segurança está disponível em:
https://www.certification.openid.net/
18. Como  acesso o motor de conformidade funcional do Open Finance Brasil?
O Acesso ao motor de conformidade funcional só poderá ser realizado pelos contatos técnicos e administradores das instituições cadastrados no diretório de participantes de sandbox.
O Motor de conformidade funcional, está disponível em:
https://web.conformance.directory.openbankingbrasil.org.br
19. Qual o critério para uma instituição fazer a certificação novamente? Depois de uma  major/minor/periodicidade trimestral?
Os critérios de expiração de certificação funcional e de segurança estão explicados no
Guia de Certificação
.
20. Será possível integrar os testes funcionais e de segurança com o
pipeline
de DevOps das instituições?
Os testes funcionais e de segurança são fornecidos em formato de código aberto, podendo a instituição implementar esses testes no ambiente da instituição. Vale notar que não está previsto suporte para que seja realizada essa integração e que, para fins de certificação, deverão ser utilizados logs de testes realizados no próprio motor de conformidade (versão web).
21. Uma instituição pode fazer testes usando
endpoints
públicos de outra instituição?
Testes entre instituições não estão no escopo da plataforma de certificação, mas as instituições podem combinar testes de integração entre si no ambiente de sandbox.
22. Onde posso encontrar o documento “Orientações para certificação”?
O documento está disponível em:
Orientações para Certificação
23. Como posso acessar o Guia de Conformidade?
O Guia de Conformidade está disponível em:
https://openfinancebrasil.atlassian.net/wiki/download/attachments/17378905/20220912_OpenFinance-Guia_Motor_De_Conformidade_V7.pdf?api=v2
24. Em qual versão preciso executar os testes para obter a certificação?
Para obter a certificação, é imprescindível realizar a execução dos testes na última versão estável do motor de conformidade, garantindo que eventuais novos requisitos e padrões necessários estejam sendo atendidos de forma consistente e confiável pelas instituições. A versão estável do motor será comunicada por Informa na abertura da certificação.
25. Como poderei enviar dúvidas adicionais?
Todas as dúvidas deverão ser enviadas para o service desk do Open Finance, acessível através do link:
https://servicedesk.openfinancebrasil.org.br

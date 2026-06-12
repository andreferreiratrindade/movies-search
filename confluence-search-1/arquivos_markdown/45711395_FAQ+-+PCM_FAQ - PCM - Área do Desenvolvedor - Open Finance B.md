---
                            title: "FAQ - PCM - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "45711395_FAQ+-+PCM"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/45711395/FAQ+-+PCM"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # FAQ - PCM - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            O que significa a sigla P.C.M.?
PCM significa Plataforma de Coleta de Métricas.
Onde podemos acessar a documentação da PCM?
A documentação está publicada na Área do Desenvolvedor dentro do portal Open Finance Brasil. Link direto:
Plataforma de Coleta de Métricas
Qual é o SLA para envio de reportes à PCM?
Diariamente é necessário enviar, até às 08:00 do dia seguinte (D+1) no horário padrão do Brasil (BRT), pelo menos 95% dos reportes referentes ao dia atual (D zero). Demais reportes devem ser enviados até “D+7” a partir do
timestamp
da transação. A PCM não aceitará reportes enviados após decorrido este prazo. A meta diária pode ser infringida em uma janela de 30 dias corridos por até 4 vezes, e em uma janela de 90 dias por até 10 vezes.
Preciso enviar dados da versão 1 da Fase 2?
Não. Esta versão está sendo depreciada.
Precisarei enviar dados referentes a futuras APIs em estado deprecated?
Sim. A única exceção é a versão 1.x.x da Fase 2.
Como faço para referenciar as marcas acionadas?
Atualmente os dados enviados à PCM não são diferenciados por marcas, estão à nível da organização (organization-org-id).
Havia um problema em minha integração e eu enviei um dado errado. Consigo corrigir?
Está previsto um método PUT para que o participante corrija algum dado de sua responsabilidade, entretanto o processo administrado de resolução de divergências será definido futuramente, após aprendizados baseados nos eventos observados no MVP.
Qual é o escopo de endpoints que a PCM vai receber?
São todas as APIs hoje disponíveis no Open Finance Brasil. Elas são separadas em duas categorias:
Private APIs:
que são as que possuem Dados de Cliente (fase 2), Serviços (fase 3) e Segurança (FAPI/OAUTH).
OpenData APIs
: que são as APIs não autenticadas, que respondem por Dados Abertos (fase 1).
Você encontra na especificação técnica da PCM uma lista detalhada com todos os endpoints e que quais papéis necessitam realizar envio quais tipos de telemetria. Saiba mais
Temos a necessidade de teste funcional ou certificação específica dos participantes para a PCM?
Não há pré-certificação. Está previsto para que a FVP (Ferramenta de Validação em Produção) envie telemetria à PCM sobre todas as requisições feitas, e, desta forma, será possível ter métricas relativas à conformidade da integração feita pelo participante em ambiente produtivo.
Podemos enviar dados de sandbox para a PCM?
Até 1/2/2023 será permitido o envio de dados não produtivos. Nós recomendamos que sejam enviados dados produtivos, a fim de se colaborar para testarmos a capacidade de pareamento real da plataforma.
Quais são os padrões de certificado de segurança que precisam ser adotados para se integrar à PCM?
A PCM utiliza o padrão de tokens OAuth2, na modalidade client_credentials. Deve-se utilizar, para tal, um certificado de transporte (mTLS) padrão Open Finance Brasil (BRCAC) atrelado a sua organização. Para detalhes, consulte a documentação técnica da PCM.
Minha instituição não possui BRCAC. Como faço para me integrar à PCM?
Você poderá utilizar o certificado emitido pelo Diretório de sandbox. Para sua plena operação e 1/2/23, uma alternativa está em definição pelo GT Arquitetura.
Qual é o prazo para se integrar à PCM?
Prazo estabelecido, conforme Open Finance Informa #282, para 1/Fev/2023.
Qual é o processo para correção de eventos com divergência de reportes com status PAIRED_INCONSISTENT ou UNPAIRED?
A PCM possui um métodos do tipo PUT, que deverão ser utilizados para a realização de reenvio de pontos de telemetria problemáticos e, desta forma, se aplique a correções. Neste momento, porém, não há definição de regras definidas sobre quais os casos em que o uso do PUT será permitido, pois o GT Arquitetura optou por elaborar tais regras baseado em estudo de casos reais, com dados reais, que ocorrerem em produção pós lançamento da plataforma.
Como é contabilizada a paginação?
Atualmente não é feita contabilização de paginações pela PCM. Será feito um estudo para adição do pagination-key como campo no additionalInfo.
Estou com uma dúvida que não está explicada nem na documentação neste FAQ. Como faço para fazer perguntas para especialistas em PCM?
Utilize o Service Desk. Uma nova categoria para centralizar as questões será disponibilizada nos próximos dias.
Não há incoerência entre falar para não criticar a criação do consentimento, e informar se é ou não é cliente?
Os impedimentos colocados na API de pagamentos dizem respeito ao que não informar ao iniciador no momento de criação de consentimento e, portanto, não se aplicam ao processo de reporte, que ocorre de forma assíncrona à criação do consentimento, e reporta-se ao perímetro central. Por este motivo, entendemos não haver incoerência entre as recomendações.
O consentimento é criado sem qualquer crítica e, depois, em tempo de reporte, eventuais críticas ou complementação de dados são executadas para enviar o reporte apenas ao perímetro central.

---
                            title: "Histórico - Estoque de Consentimentos Ativos  - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "937820214_Hist+rico+-+Estoque+de+Consentimentos+Ativos"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/937820214/Hist+rico+-+Estoque+de+Consentimentos+Ativos"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Histórico - Estoque de Consentimentos Ativos  - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Esta é a documentação legada, e deve ser consultada apenas para fins de histórico. A página atualizada pode ser encontrada aqui:
Estoque de Consentimentos Ativos
Objetivo
Disponibilização de uma nova API dedicada à obtenção de dados quantitativos de consentimentos ativos e únicos por tipo de cliente. Esta solução permite que as instituições realizem o autorreporte via PCM, garantindo precisão e conformidade com a IN 588, fornecendo uma perspectiva completa e transparente sobre o fluxo de dados e consentimentos para cada instituição.
Terminologia
Os termos abaixo estão no contexto da Plataforma de Coleta de Métricas, que por sua vez está no contexto do Open Finance Brasil.
Estoque de Consentimento
São os consentimentos que se encontram ativos e foram reportados por determinada organização, separados pelo tipo de pessoa (Física ou Jurídica), correspondentes aos dados dos clientes e transacionais (Fases 2 e 4b).
Client e Server
Em uma interação, a parte que solicita os dados é chamada de
client
, ao passo que a parte que devolve os dados é
server
. Portanto, supondo que A faça uma consulta em B pelos dados de uma conta, esses dados serão transmitidos por quem recebeu a solicitação, e recebidos por quem a fez. Neste caso, A é o
client
e B é o
server
.
Descrição funcional da API
CAMPO
DESCRIÇÃO
Data de Referência¹
Deve conter a data a que se referem os dados de consentimento enviados na mensagem. Formato: AAAA-MM-DD
organisationId¹
Organização de envio da mensagem referente ao papel do Transmissor ou Receptor, conforme
Role
, a ser preenchido a partir do Certificado
Papel (Role)¹
A ser preenchido com “CLIENT” ou “SERVER”
Escopo de Dados¹
A ser preenchido com a
Role
“DADOS”
Total de clientes únicos PF
A ser preenchido com o total de clientes PF com consentimentos ativos. Formato: numérico inteiro natural
Total de clientes únicos PJ
A ser preenchido com o total de clientes PJ com consentimentos ativos. Formato: numérico inteiro natural
Lista de Estoque de Consentimentos, composta pelos campos¹:
organisationId do CLIENT¹
Identificador da Organização de onde a chamada foi realizada
organisationId do SERVER¹
Identificador da Organização para onde a chamada foi realizada
Quantidade de consentimentos ativos¹
Estoque total de consentimentos ativos, correspondendo ao número de consentimentos totais válidos até a data de referência
¹ Campos com preenchimento obrigatório para que a mensagem seja considerada válida na ingestão
Detalhes operacionais
PARÂMETRO
REGRA
JUSTIFICATIVA
Frequência de envio
Diária
Alinha-se com a prática atual das instituições que enviam reportes diários
Proporciona dados mais atualizados e granulares
Facilita a detecção de tendências e anomalias
Período de Referência
Diário, das 00:00:00 às 23:59:59
Permite às instituições consolidar dados de um dia completo
Política de Deduplicação
Se uma instituição enviar dados com as mesmas quantidades dentro de um período de 24 horas, considerar apenas o primeiro envio
Permitir atualizações se houver alteração nos números
Evita duplicações acidentais
Permite correções em caso de erros no reporte inicial
Prazo Máximo de Reporte
Até 08h00 do próximo dia da Data de Referência
Garante que os dados sejam processados em um pipeline uniforme e respeitem a janela única de processamento
Regras de Validação
Verificar se o organisationId informado é válido
Garantir que a Data de Referência seja sempre anterior ou igual à Data de Envio
Assegurar que a quantidade de consentimentos únicos para PF/PJ não exceda a quantidade de consentimentos ativos
Confirmar que o envio dos dados relativos a uma Data de Referência ocorreu até D+1 às 08h00
Documentação da API
<
Documentação da API - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor
>

---
                            title: "Limites de tráfego - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "17989722_Limites+de+tr+fego"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17989722/Limites+de+tr+fego"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Limites de tráfego - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Limites por origem - TPM (Transações por minuto)
2
Limites globais - TPS (Transações por segundo)
Limites por origem - TPM (Transações por minuto)
Limites por origem - TPM (Transações por minuto)
Existem dois tipos de origem quando analisamos o tráfego de dados, desconsiderando o tráfego interno da instituição:
IP: aplicado aos endpoints que não demandam autenticação;
Instituição ou organizationId: aplicado aos endpoints autenticados.
Os limites, quando implementados, são definidos por
endpoint
e por origem como segue:
Alta frequência:
De acordo com o número de consentimentos possuídos por uma determinada instituição receptora de dados com uma determinada instituição transmissora de dados:
Quando a quantidade de consentimentos ativos for ≤ 6 milhões, aplica-se a tabela:
QCA | TPM
0 < QCA ≤ 1 000 000 → 2.500
1 000 000 < QCA ≤ 2 000 000 → 5.000
2 000 000 < QCA ≤ 3 000 000 → 8.000
3 000 000 < QCA ≤ 6 000 000 → 10.000
Para QCA > 6 000 000, o TPM é calculado em faixas de 2 milhões, somando-se 2.000 ao limite da faixa anterior (ex.: 6-8 MM → 12.000 TPM)
Média-alta frequência: 2.000 TPM
Média frequência: 1.500 TPM
Baixa frequência: 1.000 TPM
Para contabilização dos limites de tráfego, tanto transmissoras como receptoras, devem considerar minuto cheio, ou seja, é preciso zerar o contador a cada minuto. Assim, tipicamente, a contabilização deve começar no início do minuto (00s000ms) e terminar no final do minuto (59s999ms). Como por exemplo:
O servidor começa a receber requisições em 10h25m55s123ms. O servidor deve contabilizar até 10h25m59s999ms;
Deve-se contabilizar a cada minuto: 10h25m00s000ms até 10h25m59s999ms, depois zerar e contar 10h26m00s000ms até 10h26m59s999ms.
Nos casos abaixo não são aplicáveis limites por origem:
APIs de Segurança:
Token: consumo OAuth 2.0 (FAPI)
Token: DCR/DCM
APIs de Consentimento (
Consents
)
APIs de Recursos (
Resources
)
Grupo de APIs de Serviços
O erro HTTP
Status
Code
429 (
Too many requests
) passa a ser utilizado de forma exclusiva para pedidos de consumo que excedam os limites de TPM.
Por fim, as requisições que ultrapassarem os limites deverão ser desprezadas no cálculo do tempo de resposta das implementações das APIs.
Limites globais - TPS (Transações por segundo)
A infraestrutura das instituições provendo APIs no Open Finance (Dados Abertos, Dados Cadastrais e Transacionais, Serviços, Relatórios e Métricas, Segurança) deve ter a capacidade de, no mínimo, atender a 300 requisições simultâneas por segundo (TPS), desconsiderando chamadas internas.
Caso o limite de 300 TPS seja atingido, no contexto do Open Finance, a instituição deve ampliar sua capacidade de infraestrutura para possibilitar um acréscimo de 150 TPS ao limite anterior. Tal aumento deve ocorrer novamente a cada vez que o limite vigente na instituição for atingido. Cada instituição deve criar monitoramento preventivo, de acordo com critérios definidos; as evidências devem estar à disposição do Banco Central do Brasil por um período de doze meses.
Fica definida a utilização do código HTTP
Status
Code
529 (
Site is overloaded
) para retorno quando atingido o limite de TPS estabelecido.
Endpoints
criados dentro do conceito de extensibilidade, sejam dentro de novas APIs ou em APIs existentes, não podem ser considerados para controle do limite global de transações simultâneas.
Gatilho para ampliação do TPS
O aumento do limite deve ocorrer novamente, a cada vez que o limite vigente naquela instituição for atingido
Cada instituição precisará realizar este cálculo preventivamente
Caso a instituição tenha aumentado a sua infraestrutura para disponibilizar um TPS maior do que os 300, mas tenha elasticidade para diminuir de acordo com a demanda, poderá fazer isso até o limite mínimo de 300 TPS
Formato de cálculo para monitoramento:
Limite máximo de 10% de atingimento de 90% do TPS estabelecido por quinzena, em 3 quinzenas consecutivas
Cálculo de TPS a cada 1 segundo
Contador de segundos com TPS maior que 90% do regulamento atual (inicial 270 TPS)
Caso ao final da quinzena o contador atinja um número maior que 10%, a quinzena deve ser contabilizada
Caso a instituição contabilize 3 quinzenas consecutivas ultrapassando o limite percentual, o TPS deve ser acrescido em 150 TPS ao limite anterior
O tempo para adequação deve ser de no máximo 2 meses após a identificação do gatilho

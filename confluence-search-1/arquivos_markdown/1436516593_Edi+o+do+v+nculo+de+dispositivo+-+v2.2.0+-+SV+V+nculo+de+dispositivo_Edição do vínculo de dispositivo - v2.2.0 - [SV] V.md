---
                            title: "Edição do vínculo de dispositivo - v2.2.0 - [SV] Vínculo de dispositivo - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1436516593_Edi+o+do+v+nculo+de+dispositivo+-+v2.2.0+-+SV+V+nculo+de+dispositivo"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1436516593/Edi+o+do+v+nculo+de+dispositivo+-+v2.2.0+-+SV+V+nculo+de+dispositivo"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Edição do vínculo de dispositivo - v2.2.0 - [SV] Vínculo de dispositivo - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Campos passíveis de edição e suas condições:
O produto Vinculo de dispositivo possui características de edição de campos que podem ser realizadas em ambiente do detentor.
Nas tabelas abaixo foram listados os campos, o ambiente em que será editado, o tipo de mudança (ex. aumentar/reduzir valor), se o usuário precisará estar presente e ser redirecionado ou não para confirmar essa alteração. Apenas vínculos em estado AUTHORISED podem ser editados, independente do produto ao qual estão associados.
Campo
Presença do usuário
Anuência do usuário?
Quem edita?
Campo preenchido inicialmente?
Tipo de alteração
Exige redirecionamento?
Exemplo
Webhook
Campo
Presença do usuário
Anuência do usuário?
Quem edita?
Campo preenchido inicialmente?
Tipo de alteração
Exige redirecionamento?
Exemplo
Webhook
transactionLimit
Necessário
Sim
Usuário Pagador
Sim
Aumentar o valor
Não
Limite por transação vai de R$200 para R$300
Sim
transactionLimit
Necessário
Sim
Usuário Pagador
Sim
Reduzir o valor
Não
Limite por transação vai de R$200 para R$100
Sim
dailyLimit
Necessário
Sim
Usuário Pagador
Sim
Aumentar o valor
Não
Limite diário vai de R$200 para R$300
Sim
dailyLimit
Necessário
Sim
Usuário Pagador
Sim
Reduzir o valor
Não
Limite diário vai de R$200 para R$100
Sim
dailyLimit
Necessário
Sim
Usuário Pagador
Não
Definir valor
Não
Limite diário não definido passa a ser de R$200
Sim
dailyLimit
Necessário
Sim
Usuário Pagador
Sim
Indefinir valor
Não
Limite diário definido em R$200 passa a ser indefinido
Sim
expirationDateTime*
Necessário
Sim
Usuário Pagador
Sim
Aumentar o prazo de expiração
Não
Vinculo deixa de expirar em 01/01/2026 muda para 01/12/2026
Sim
expirationDateTime*
Necessário
Sim
Usuário Pagador
Sim
Reduzir o prazo de expiração
Não
Vinculo deixa de expirar em 01/12/2026 muda para 01/06/2026
Sim
expirationDateTime*
Necessário
Sim
Usuário Pagador
Não
Definir prazo
Não
Vinculo deixa de ter prazo indeterminado e passa a expirar em 01/12/2026
Sim
expirationDateTime*
Necessário
Sim
Usuário Pagador
Sim
Indefinir prazo
Não
Vinculo tem prazo determinado para expirar em 01/12/2026 e passa a ser indefinido
Sim
Legenda: * Possível de edição apenas para vínculos criados a partir da versão 2.2.0 da API Vinculo de dispositivos

---
                            title: "Jornada Otimizada - SV - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1275625473_Jornada+Otimizada+-+SV"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1275625473/Jornada+Otimizada+-+SV"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Jornada Otimizada - SV - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            v 1.01
Objetivo
Com o intuito de monitorar a Jornada Otimizada, faz-se necessária a inclusão de dois novos additionalInfo nos reportes da PCM, de forma a diferenciar consentimentos primários e secundários, e relacionar consentimentos vinculados.
Para consultar os detalhes técnicos da implementação destes additilnalInfo, por favor consultar a página
Documentação da API - PCM
journeyIsLinked
Descrição:
indica que o consentimento é vinculado a outro em uma Jornada Otimizada
Jornada Sem Redirecionamento (JSR)
⁠
Regra de preenchimento:
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.isLinked”, retornado após a chamada inicial na API “POST /enrollments” em caso de Jornada Otimizada.  Em casos em que a informação não está disponível espera-se o envio do valor FALSE.
Exemplo:
true
Roles:
CLIENT
Métodos:
POST e GET
Http Code:
Todos
endpoints:
/open-banking/enrollments/v2/enrollments
/open-banking/enrollments/v2/enrollments/{enrollmentId}
PIX Automático
⁠
Regra de preenchimento:
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.isLinked”, retornado após a chamada inicial na API “POST /consent” em caso de Jornada Otimizada. Em casos em que a informação não está disponível espera-se o envio do valor FALSE.
Exemplo:
true
Roles:
CLIENT
Métodos:
POST e GET
Http Code:
Todos menos 4xx e 5xx no POST
endpoints:
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
journeyLinkId
Descrição:
Identifica o consentimento de dados vinculado a uma Jornada Otimizada.
Jornada Sem Redirecionamento (JSR)
⁠
Regra de preenchimento:
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.linkId”, retornado após a chamada inicial na API “POST /enrollments” em caso de Jornada Otimizada. Deve ser enviado se journeyIsLinked for TRUE.
Roles:
CLIENT
Métodos:
POST e GET
Http Code:
Todos
endpoints:
/open-banking/enrollments/v2/enrollments
/open-banking/enrollments/v2/enrollments/{enrollmentId}
PIX Automático
⁠
Regra de preenchimento:
Deve ser preenchido com a mesma string enviada ou recebida no campo “.data.journey.linkId”, retornado após a chamada inicial na API “POST /consent” em caso de Jornada Otimizada. Deve ser enviado se journeyIsLinked for TRUE.
Roles:
CLIENT
Métodos:
POST e GET
Http Code:
Todos menos 4xx e 5xx no POST
endpoints:
/open-banking/automatic-payments/v2/recurring-consents
/open-banking/automatic-payments/v2/recurring-consents/{recurringConsentId}
Importante:
Para estes endpoints, caso se trate de uma Jornada Otimizada, em journeyIsLinked enviar TRUE; caso contrário, enviar FALSE. O campo journeyLinkId deve ser enviado caso journeyIsLinked seja TRUE.

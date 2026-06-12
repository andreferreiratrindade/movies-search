---
                            title: "Informações Gerais - [DA] Títulos de Capitalização - v2.1.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1719042170_Informa+es+Gerais+-+DA+T+tulos+de+Capitaliza+o+-+v2.1.0"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1719042170/Informa+es+Gerais+-+DA+T+tulos+de+Capitaliza+o+-+v2.1.0"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Informações Gerais - [DA] Títulos de Capitalização - v2.1.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Contexto sobre a API
​
2
Prefixo
​
3
Lista de Endpoints
4
Visão de alto nível
​
5
DE-PARA de campos
6
DE-PARA dos parâmetros
7
DE-PARA dos status code
Contexto sobre a API
​
A API Título de Capitalização fornece dados pertinente ao produto financeiro título de capitalização. As instituições participantes do OFB devem reportar este produto por meio desta API no endpoint /bonds. ​
Esta API interopera, via demanda regulatória do Banco Central na Resolução Conjunta n.º 5, Art. 1º, com a API Capitalization Title do ecossistema OPIN (Open Insurence), a qual é gerenciada e regulada pela SUSEP (Superintendência de Seguros Privados).​
No âmbito do OFB, a instituição é obrigada a divulgar todos os dados relacionados ao produto em questão, independentemente de ser de sua propriedade ou de uma empresa parceira. ​
Prefixo
​
- Prefixo do(s) endpoint(s): /opendata-capitalization/v2
Lista de Endpoints
- Lista de todos os títulos de capitalização de uma instituição: GET /bonds
Visão de alto nível
​
A estrutura base do endpoint disponibilizado nesta API é visualizada na Figura abaixo, onde as informações sobre os títulos de capitalizações comercializados pelas instituições participantes do OFB encontra-se no objeto products, abaixo de society​
Open
DE-PARA de campos
API Capitalization Bonds (Open Finance)
​
Endpoint /bonds
​
API Capitalization Title (Open Insurance)
​
Endpoint /capitalization-title
​
/data[]​
-​
/data[]/participant/brand​
-​
/data[]/participant/name​
-​
/data[]/participant/cnpjNumber​
-​
/data[]/participant/urlComplementaryList​
-​
/data[]/society/brand​
/data/brand/name​
/data[]/society/name​
/data/brand/companies/name​
/data[]/society/cnpjNumber​
/data/brand/companies/cnpjNumber​
/data[]/society/products/name​
/data/brand/companies/products/name​
/data[]/society/products/code​
/data/brand/companies/products/code​
/data[]/society/products/modality​
/data/brand/companies/products/modality​
/data[]/society/products/costType​
/data/brand/companies/products/costType​
/data[]/society/products/termsAndConditions/susepProcessNumber​
/data/brand/companies/products/termsAndConditions/susepProcessNumber​
/data[]/society/products/termsAndConditions/detail​
/data/brand/companies/products/termsAndConditions/termsRegulations​
/data[]/society/products/quotas[]/quota​
/data/brand/companies/products/quotas[]/quota​
/data[]/society/products/quotas[]/capitalizationQuota​
/data/brand/companies/products/quotas[]/capitalizationQuota​
/data[]/society/products/quotas[]/raffleQuota​
/data/brand/companies/products/quotas[]/raffleQuota​
/data[]/society/products/quotas[]/chargingQuota​
/data/brand/companies/products/quotas[]/chargingQuota​
/data[]/society/products/validity​
/data/brand/companies/products/validity​
/data[]/society/products/serieSize​
/data/brand/companies/products/serieSize​
/data[]/society/products/capitalizationPeriod/interestRate​
/data/brand/companies/products/capitalizationPeriod/interestRate​
/data[]/society/products/capitalizationPeriod/updateIndex​
/data/brand/companies/products/capitalizationPeriod/updateIndex​
/data[]/society/products/capitalizationPeriod/updateIndexAdditionalInfo​
/data/brand/companies/products/capitalizationPeriod/updateIndexOthers​
/data[]/society/products/capitalizationPeriod/contributionAmount[]/periodicity​
/data/brand/companies/products/capitalizationPeriod/contributionAmount/frequency​
/data[]/society/products/capitalizationPeriod/contributionAmount[]/periodicityAdditionalInfo​
-​
/data[]/society/products/capitalizationPeriod/contributionAmount[]/minimum​
/data/brand/companies/products/capitalizationPeriod/contributionAmount/minValue​
/data[]/society/products/capitalizationPeriod/contributionAmount[]/maximum​
/data/brand/companies/products/capitalizationPeriod/contributionAmount/maxValue​
/data[]/society/products/capitalizationPeriod/contributionAmount[]/allowedValue​
/data/brand/companies/products/capitalizationPeriod/contributionAmount/value​
/data[]/society/products/capitalizationPeriod/earlyRedemptions[]​
/data/brand/companies/products/capitalizationPeriod/earlyRedemption[]​
/data[]/society/products/capitalizationPeriod/redemptionPercentageEndTerm​
/data/brand/companies/products/capitalizationPeriod/redemptionPercentageEndTerm​
/data[]/society/products/capitalizationPeriod/gracePeriodRedemption​
/data/brand/companies/products/capitalizationPeriod/gracePeriodRedemption​
/data[]/society/products/latePayment/suspensionMonths​
/data/brand/companies/products/latePayment/suspensionPeriod​
/data[]/society/products/latePayment/periodExtensionOption​
/data/brand/companies/products/latePayment/termExtensionOption​
/data[]/society/products/contributionPayment/paymentMethod​
/data/brand/companies/products/contributionPayment/paymentMethod[]​
/data[]/society/products/contributionPayment/paymentMethodAdditionalInfo​
/data/brand/companies/products/contributionPayment/paymentDetail​
/data[]/society/products/contributionPayment/updateIndex​
/data/brand/companies/products/contributionPayment/updateIndex[]​
/data[]/society/products/contributionPayment/updateIndexAdditionalInfo​
/data/brand/companies/products/contributionPayment/updateIndexOthers[]​
/data[]/society/products/redemptionPercentageEndTerm​
/data/brand/companies/products/redemption/redemption​
/data[]/society/products/finalRedemptionRate​
/data/brand/companies[]/products[]/redemption/redemption​
/data[]/society/products/draws[]​
/data/brand/companies[]/products[]/raffle​
/data[]/society/products/draws[]/timeInterval​
/data/brand/companies/products/raffle/timeInterval[]​
/data[]/society/products/draws[]/timeIntervalAdditionalInfo​
/data/brand/companies/products/raffle/timeIntervalOthers​
/data[]/society/products/draws[]/quantity​
/data/brand/companies/products/raffle/raffleQty​
/data[]/society/products/draws[]/prizeMultiplier​
/data/brand/companies/products/raffle/raffleValue​
/data[]/society/products/draws[]/earlySettlementRaffle​
/data/brand/companies/products/raffle/earlySettlementRaffle​
/data[]/society/products/draws[]/mandatoryContemplation​
/data/brand/companies/products/raffle/mandatoryContemplation​
/data[]/society/products/draws[]/ruleDescription​
/data/brand/companies/products/raffle/ruleDescription​
/data[]/society/products/draws[]/minimumContemplationProbability​
/data/brand/companies/products/raffle/minimumContemplationProbability​
/data[]/society/products/additionalInfo​
/data/brand/companies/products/additionalDetails/additionalDetails​
/data[]/society/products/minimumRequirementDetails​
/data/brand/companies/products/minimumRequirements/minimumRequirementDetails​
/data[]/society/products/targetAudience​
/data/brand/companies/products/targetAudiences[]​
Legenda:
O caractere "-" indica que não existe correspondência do campo na API.
DE-PARA dos parâmetros
API Capitalization Bonds (Open Finance)
​
Endpoint /bonds
​
API Capitalization Title (Open Insurance)
​
Endpoint /capitalization-title
​
API Capitalization Bonds (Open Finance)
​
Endpoint /bonds
​
API Capitalization Title (Open Insurance)
​
Endpoint /capitalization-title
​
-​
parameters/cache-Control​
-​
parameters/cnpjNumber​
-​
parameters/content-Security-Policy​
-​
parameters/content-Type​
-​
parameters/strict-Transport-Security​
-​
parameters/x-Content-Type-Options​
-​
parameters/x-Frame-Options​
DE-PARA dos status code
API Capitalization Bonds (Open Finance)
​
Endpoint /bonds
​
API Capitalization Title (Open Insurance)
​
Endpoint /capitalization-title
​
API Capitalization Bonds (Open Finance)
​
Endpoint /bonds
​
API Capitalization Title (Open Insurance)
​
Endpoint /capitalization-title
​
-​
Status code: 401​
-​
Status code: 403​
-​
Status code: 406​
-​
Status code: default​
400 404 405 429 500 /meta/requestDateTime​
400 401 403 404 405 406 422 429 500 /erros/requestDateTime​

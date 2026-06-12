---
                            title: "Informações Gerais - [DA] Previdência - v2.1.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1719042436_Informa+es+Gerais+-+DA+Previd+ncia+-+v2.1.0"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1719042436/Informa+es+Gerais+-+DA+Previd+ncia+-+v2.1.0"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Informações Gerais - [DA] Previdência - v2.1.0 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Contexto sobre a API
2
Prefixo
3
Lista de Endpoints
4
Visão de alto nível
5
Tabela de correspondência das APIs de previdência do Open Finance e Open Insurance
6
DE-PARA de campos
7
DE-PARA dos Parâmetros
Contexto sobre a API
A API Previdência fornece dados pertinente ao produto previdência. As instituições participantes do OFB devem reportar este produto por meio desta API no endpoint
/risk-coverages
e
/survival-coverages
. Esta API interopera, via demanda regulatória do Banco Central na Resolução Conjunta n.º 5, Art. 1º, com a API Life-pension e API Pension-plan do ecossistema OPIN (Open Insurance), a qual é gerenciada e regulada pela SUSEP (Superintendência de Seguros Privados). No âmbito do OFB, a instituição é obrigada a divulgar todos os dados relacionados ao produto em questão, independentemente de ser de sua propriedade ou de uma empresa parceira.
Prefixo
Prefixo dos endpoints: /opendata-pension/v2
Lista de Endpoints
Lista de todas as informações de Previdência de Coberturas de Risco: GET /risk-coverages
Lista de todas as informações de Previdência de Coberturas de Sobrevivência.: GET /survival-coverages
Visão de alto nível
A estrutura base do endpoint disponibilizado nesta API é visualizada na Figura abaixo, onde as informações sobre previdências comercializados pelas instituições participantes do OFB encontra-se no objeto
products
, abaixo de
society
Open
Tabela de correspondência das APIs de previdência do Open Finance e Open Insurance
>>>>> OFB <<<<<
>>>>> OPIN <<<<<
>>>>> OFB <<<<<
>>>>> OPIN <<<<<
APIs
APIs
API pension, endpoint
/risk-coverages
API pension-plan
API pension, endpoint
/survival-coverages
API life-pension
DE-PARA de campos
API Previdência (Open Finance)
Endpoint
/risk-coverages
​
API Pension Plan (Open Insurance)
Endpoint
/pension-plan
​
/data[]​
-​
/data[]/participant​
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
/data/brand/companies/products/coverages[]/coveragesAttributes/modality​
/data[]/society/products/coverages[]/type​
/data/brand/companies/products/coverages[]/converage​
/data[]/society/products/coverages[]/typeAdditionalInfos[]​
-​
/data[]/society/products/coverages[]/attributes/minValue​
/data/brand/companies/products/coverages[]/coveragesAttributes/minValue​
/data[]/society/products/coverages[]/attributes/minValue/amount​
/data/brand/companies/products/coverages[]/coveragesAttributes/minValue/amount​
-​
/data/brand/companies/products/coverages[]/coveragesAttributes/minValue/unit​
​
/data/brand/companies/products/coverages[]/coveragesAttributes/minValue/unit/code​
​
/data/brand/companies/products/coverages[]/coveragesAttributes/minValue/unit/description​
/data[]/society/products/coverages[]/attributes/maxValue​
/data/brand/companies/products/coverages[]/coveragesAttributes/maxValue​
/data[]/society/products/coverages[]/attributes/maxValue/amount​
/data/brand/companies/products/coverages[]/coveragesAttributes/maxValue/amount​
-​
/data/brand/companies/products/coverages[]/coveragesAttributes/maxValue/unit​
​
/data/brand/companies/products/coverages[]/coveragesAttributes/maxValue/unit/code​
​
/data/brand/companies/products/coverages[]/coveragesAttributes/maxValue/unit/description​
/data[]/society/products/coverages[]/attributes/indemnifiablePeriod​
/data/brand/companies/products/coverages[]/coveragesAttributes/indemnifiablePeriod​
/data[]/society/products/coverages[]/attributes/indemnifiableDeadline​
/data/brand/companies/products/coverages[]/coveragesAttributes/indemnifiableDeadline​
/data[]/society/products/coverages[]/attributes/indemnityPaymentMethod​
/data/brand/companies/products/coverages[]/coveragesAttributes/indenizationPaymentMethod​
/data[]/society/products/coverages[]/attributes/gracePeriod​
/data/brand/companies/products/coverages[]/coveragesAttributes/gracePeriod​
/data[]/society/products/coverages[]/attributes/minValue/currency​
/data/brand/companies/products/coverages[]/coveragesAttibutes/currency​
/data[]/society/products/coverages[]/attributes/maxValue/currency​
/data/brand/companies/products/coverages[]/coveragesAttibutes/currency​
/data[]/society/products/coverages[]/attributes/gracePeriod/amount​
/data/brand/companies/products/coverages[]/coveragesAttributes/gracePeriod/amount​
/data[]/society/products/coverages[]/attributes/gracePeriod/unit​
/data/brand/companies/products/coverages[]/coveragesAttributes/gracePeriod/unit​
/data[]/society/products/coverages[]/attributes/excludedRisks[]​
/data/brand/companies/products/coverages[]/coveragesAttributes/excludedRisks[]​
/data[]/society/products/coverages[]/attributes/excludedRisksURL​
/data/brand/companies/products/coverages[]/coveragesAttributes/excludedRisksURL​
/data[]/society/products/coverages[]/attributes/profitModality​
-​
/data[]/society/products/assistanceTypes[]​
/data/brand/companies/products/assistanceTypes[]​
/data[]/society/products/assistanceTypesAdditionalInfos[]​
/data/brand/companies/products/assistanceTypeOthers[]​
/data[]/society/products/additional​
/data/brand/companies/products/additional​
/data[]/society/products/termsAndConditions[]/susepProcessNumber​
/data/brand/companies/products/termsAndConditions[]/susepProcessNumber​
/data[]/society/products/termsAndConditions[]/detail​
/data/brand/companies/products/termsAndConditions[]/definition​
/data[]/society/products/pmbacRemuneration/interestRate​
/data/brand/companies/products/updatePMBaC/interestRate​
/data[]/society/products/pmbacRemuneration/updateIndexes[]​
/data/brand/companies/products/updatePMBaC/updateIndex​
/data[]/society/products/premiumUpdateIndex[]​
/data/brand/companies/products/premiumUpdateIndex[]​
/data[]/society/products/ageAdjustment​
/data/brand/companies/products/ageReframing​
/data[]/society/products/ageAdjustment/criterias[]​
/data/brand/companies/products/ageReframing/reframingCriterion[]​
/data[]/society/products/ageAdjustment/frequency​
/data/brand/companies/products/ageReframing/reframingPeriodicity​
/data[]/society/products/financialRegimeContractType​
-​
/data[]/society/products/reclaim​
/data/brand/companies/products/reclaim​
/data[]/society/products/reclaim/table[]​
/data/brand/companies/products/reclaim/reclaimTable[]​
/data[]/society/products/reclaim/table[]/initialMonthRange​
/data/brand/companies/products/reclaim/reclaimTable[]/initialMonthRange​
/data[]/society/products/reclaim/table[]/finalMonthRange​
/data/brand/companies/products/coverages[]/coveragesAttributes/modality​
/data[]/society/products/reclaim/table[]/percentage​
/data/brand/companies/products/reclaim/reclaimTable[]/percentage​
-​
/data/brand/companies/products/reclaim/reclaimTable[]/differentiatedPercentage​
/data[]/society/products/reclaim/gracePeriod​
/data/brand/companies/products/reclaim/gracePeriod​
/data[]/society/products/reclaim/gracePeriod/amount​
/data/brand/companies/products/reclaim/gracePeriod/amount​
/data[]/society/products/reclaim/gracePeriod/unit​
/data/brand/companies/products/reclaim/gracePeriod/unit​
/data[]/society/products/reclaim/differenciatedPercentage​
-​
/data[]/society/products/otherGuaranteedValues​
/data/brand/companies/products/otherGuaranteedValues​
/data[]/society/products/contributionPayment​
/data/brand/companies/products/contributionPayment​
data[]/society/products/contributionTax​
data/brand/companies/products/contributionTax​
/data[]/society/products/contributionPayment/contributionPaymentMethod[]​
/data/brand/companies/products/contributionPayment/contributionPaymentMethod[]​
/data[]/society/products/contributionPayment/contributionPaymentMethodAdditionalInfo​
/data/brand/companies/products/contributionPayment/contributionPaymentDetail​
/data[]/society/products/contributionPayment/contributionPeriodicity[]​
/data/brand/companies/products/contributionPayment/contributionPeriodicity[]​
/data[]/society/products/contributionPayment/contributionPeriodicityAdditionalInfo​
/data/brand/companies/products/contributionPayment/contributionDetail​
-​
/data/brand/companies/products/contributionTax​
/data[]/society/products/minimumRequirement​
/data/brand/companies/products/minimumRequirements​
/data[]/society/products/minimumRequirement/contractType​
/data/brand/companies/products/minimumRequirements/contractMinRequirementsType​
/data[]/society/products/minimumRequirement/contractingMinRequirement​
/data/brand/companies/products/minimumRequirements/contractMinRequirements​
/data[]/society/products/targetAudience​
/data/brand/companies/products/targetAudience​
API Previdência (Open Finance)
Endpoint /survival-coverages
​
API Pension Plan (Open Insurance)
Endpoint /life-pension
​
/data[]​
-​
/data[]/participant​
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
/data[]/society/products[]/name​
/data/brand/companies/products/name​
/data[]/society/products[]/code​
/data/brand/companies/products/code​
/data[]/society/products[]/segment​
/data/brand/companies/products/segment​
/data[]/society/products[]/type​
/data/brand/companies/products/type​
/data[]/society/products[]/modality​
/data/brand/companies/products/modality​
/data[]/society/products[]/additionalInfo​
/data/brand/companies/products/optionalCoverage​
-​
/data/brand/companies/products/productDetails​
/data[]/society/products[]/termsAndConditions[]/susepProcessNumber​
/data/brand/companies/products/productDetails/susepProcessNumber​
/data[]/society/products[]/termsAndConditions[]/detail​
/data/brand/companies/products/productDetails/contractTermsConditions​
/data[]/society/products[]/defferalPeriod/interestRate​
/data/brand/companies/products/productDetails/defferalPeriod/interestRate​
/data[]/society/products[]/defferalPeriod/updateIndex​
/data/brand/companies/products/productDetails/defferalPeriod/updateIndex​
/data[]/society/products[]/defferalPeriod/otherMinimumPerformanceGarantees​
/data/brand/companies/products/productDetails/defferalPeriod/otherMinGuaranteesIndex​
data/society/products/defferalPeriod/otherMinGuaranteesPercentage​
data/brand/companies/products/defferalPeriod/otherMinGuaranteesPercentage​
-​
/data/brand/companies/products/productDetails/defferalPeriod/otherMinGuaranteesPercentage​
/data[]/society/products[]/defferalPeriod/reversalFinancialResults​
/data/brand/companies/products/productDetails/defferalPeriod/reversalFinancialResults​
/data[]/society/products[]/defferalPeriod/minimumPremiums[]​
/data/brand/companies/products/productDetails/defferalPeriod/minimumPremiumAmount[]​
/data[]/society/products[]/defferalPeriod/minimumPremiums[]/currency​
-​
/data[]/society/products[]/defferalPeriod/minimumPremiums[]/periodicity[]​
/data/brand/companies/products/productDetails/defferalPeriod/minimumPremiumAmount[]/minimumPremiumAmountDescription​
/data[]/society/products[]/defferalPeriod/minimumPremiums[]/amount​
/data/brand/companies/products/productDetails/defferalPeriod/minimumPremiumAmount[]/minimumPremiumAmountValue​
/data[]/society/products[]/defferalPeriod/premiumPaymentMethods[]​
/data/brand/companies/products/productDetails/defferalPeriod/premiumPaymentMethod[]​
-​
/data/brand/companies/products/productDetails/defferalPeriod/paymentDetail​
/data[]/society/products[]/defferalPeriod/permissionExtraordinaryContributions​
/data/brand/companies/products/productDetails/defferalPeriod/permissionExtraordinaryContributions​
/data[]/society/products[]/defferalPeriod/permissionScheduledFinancialPayments​
/data/brand/companies/products/productDetails/defferalPeriod/permissonScheduledFinancialPayments​
/data[]/society/products[]/defferalPeriod/gracePeriod/redemption​
/data/brand/companies/products/productDetails/defferalPeriod/gracePeriodRedemption​
/data[]/society/products[]/defferalPeriod/gracePeriod/betweenRedemptionRequests​
/data/brand/companies/products/productDetails/defferalPeriod/gracePeriodBetweenRedemptionRequests​
/data[]/society/products[]/defferalPeriod/portabilityPaymentTerm​
/data/brand/companies/products/productDetails/defferalPeriod/redemptionPaymentTerm​
/data[]/society/products[]/defferalPeriod/gracePeriod/portability​
/data/brand/companies/products/productDetails/defferalPeriod/gracePeriodPortability​
/data[]/society/products[]/defferalPeriod/gracePeriod/betweenPortabilityRequests​
/data/brand/companies/products/productDetails/defferalPeriod/gracePeriodBetweenPortabilityRequests​
/data[]/society/products[]/defferalPeriod/redemptionPaymentTerm​
/data/brand/companies/products/productDetails/defferalPeriod/portabilityPaymentTerm​
/data[]/society/products[]/defferalPeriod/investmentFunds[]/cnpjNumber​
/data/brand/companies/products/productDetails/defferalPeriod/investmentFunds/cnpjNumber​
/data[]/society/products[]/defferalPeriod/investmentFunds[]/name​
/data/brand/companies/products/productDetails/defferalPeriod/investmentFunds/companyName​
/data[]/society/products[]/defferalPeriod/investmentFunds[]/maximumAdministrationFee​
/data/brand/companies/products/productDetails/defferalPeriod/investmentFunds/maximumAdministrationFee​
/data[]/society/products[]/defferalPeriod/investmentFunds[]/eligibilityRule    ​
/data/brand/companies/products/productDetails/defferalPeriod/investmentFunds/eligibilityRule​
/data[]/society/products[]/defferalPeriod/investmentFunds[]/minimumContributionAmount​
/data/brand/companies/products/productDetails/defferalPeriod/investmentFunds/minimumContributionAmount​
data[]/society/products/defferalPeriod/investmentFunds/minimumContributionValue​
data/brand/companies/products/defferalPeriod/investmentFunds/minimumContributionValue​
data/society/products/grantPeriodBenefit/investmentFunds/minimumContributionValue​
data/brand/companies/products/grantPeriodBenefit/investmentFunds/minimumContributionValue​
-​
/data/brand/companies/products/productDetails/defferalPeriod/investmentFunds/minimumContributionValue​
/data[]/society/products[]/defferalPeriod/investmentFunds[]/minimumMathematicalProvisionAmount​
/data/brand/companies/products/productDetails/defferalPeriod/investmentFunds/minimumMathematicalProvisionAmount​
/data[]/society/products[]/defferalPeriod/investmentFunds[]/currency​
-​
/data[]/society/products[]/grantPeriodBenefit/incomeModalities[]​
/data/brand/companies/products/productDetails/grantPeriodBenefit/incomeModality[]​
/data[]/society/products[]/grantPeriodBenefit/biometricTable[]​
/data/brand/companies/products/productDetails/grantPeriodBenefit/biometricTable[]​
/data[]/society/products[]/grantPeriodBenefit/interestRate​
/data/brand/companies/products/productDetails/grantPeriodBenefit/interestRate​
/data[]/society/products[]/grantPeriodBenefit/updateIndex​
/data/brand/companies/products/productDetails/grantPeriodBenefit/updateIndex​
/data[]/society/products[]/grantPeriodBenefit/reversalFinancialResults​
/data/brand/companies/products/productDetails/grantPeriodBenefit/reversalResultsFinancial​
/data[]/society/products[]/grantPeriodBenefit/investmentFunds[]​
/data/brand/companies/products/productDetails/grantPeriodBenefit/investmentFunds[]​
/data[]/society/products[]/grantPeriodBenefit/investmentFunds[]/cnpjNumber​
/data/brand/companies/products/productDetails/grantPeriodBenefit/investmentFunds/cnpjNumber​
/data[]/society/products[]/grantPeriodBenefit/investmentFunds[]/name​
/data/brand/companies/products/productDetails/grantPeriodBenefit/investmentFunds/companyName​
/data[]/society/products[]/grantPeriodBenefit/investmentFunds[]/maximumAdministrationFee​
/data/brand/companies/products/productDetails/grantPeriodBenefit/investmentFunds/maximumAdministrationFee​
/data[]/society/products[]/grantPeriodBenefit/investmentFunds[]/typePerformanceFee​
/data/brand/companies/products/productDetails/grantPeriodBenefit/investmentFunds/typePerformanceFee[]​
/data[]/society/products[]/grantPeriodBenefit/investmentFunds[]/maximumPerformanceFee​
/data/brand/companies/products/productDetails/grantPeriodBenefit/investmentFunds/maximumPerformanceFee​
/data[]/society/products[]/grantPeriodBenefit/investmentFunds[]/eligibilityRule​

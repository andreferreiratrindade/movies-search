---
                            title: "Execução do Plano de testes de Pix Automático na FVP - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "958693401_Execu+o+do+Plano+de+testes+de+Pix+Autom+tico+na+FVP"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/958693401/Execu+o+do+Plano+de+testes+de+Pix+Autom+tico+na+FVP"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Execução do Plano de testes de Pix Automático na FVP - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Introdução
Esta página possui como intuito auxiliar as instituições para realizarem a devida configuração e execução da FVP Manual para os testes relacionados ao produto de Pix Automático.
Acessando e configurando a FVP
: Para as devidas instruções de acesso e configurações iniciais da ferramenta, é recomendado que sejam seguidas as etapas presentes no
Guia de Operação da FVP
, na etapa “Configurando e executando testes”;
Nome do Plano de Testes de Pix Automático
: Para execução dos testes de Pix Automático na FVP, o seguinte plano de testes na plataforma deve ser selecionado:
“
Production Functional Tests for Automatic Pix Payments - API Version 2.1”
Este plano de testes valida os fluxos funcionais da API Pagamentos Automáticos via Pix (versão 2.1) no ambiente de produção.
Preenchimento de Campos
Além dos campos padrão exigidos para a seleção do
Authorization Server
, o plano de testes de Pix Automático requer também o preenchimento de
campos adicionais obrigatórios
.
Esses campos simulam dados reais de usuários e contas, necessários para a execução adequada dos fluxos de Pix Automático.
Esses campos incluem:
Informações sobre o usuário autenticado (CPF ou CNPJ)
Informações do
devedor
presentes no consentimento (
debtor
)
Detalhes completos da conta do
credor
(
creditor
)
Nota:
O Pix Automático foi desenvolvido para pagamentos destinados a pessoas jurídicas (empresas). A conta a ser creditada deve ser corporativa (CNPJ). Pagamentos para pessoas físicas não são suportados.
Segue o detalhamento dos campos adicionais obrigatórios de preenchimento:
Dados do Usuário Autenticado (Pessoa Física ou Jurídica)
Campo
Descrição
Exemplo
Payment consent - Logged User CPF
CPF do usuário que está autorizando o consentimento
76109277673
brazilCpf
CPF utilizado durante a autenticação
76109277673
brazilCnpj
*
CNPJ utilizado durante a autenticação, caso o teste seja com um usuário pessoa jurídica
<seu CNPJ>
*Obrigatório apenas se o usuário autenticado for uma pessoa jurídica.
Informações do
Debtor
(dentro do consentimento)
Campo
Descrição
Exemplo
Recurring Payment consent - Contract Debtor Name
Nome do titular da conta responsável pelo pagamento
Ralph Bragg
Recurring Payment consent - Contract Debtor Identification
CPF ou CNPJ do titular da conta
76109277673
Creditor Account
(deve pertencer a uma entidade legal)
Campo
Descrição
Exemplo
Payment consent - Creditor Account Name
Nome da empresa que receberá os valores
Empresa Exemplo S.A.
Payment consent - Creditor Account CPF/CNPJ
CNPJ da empresa que receberá os valores
50685362006773
Payment consent - Business Entity CNPJ
CNPJ da pessoa jurídica recebedora
50685362006773
Payment consent - Creditor Account ISPB
Código ISPB da instituição financeira recebedora
99999004
Payment consent - Creditor Account Issuer
Código da agência da conta do recebedor
0001
Payment consent - Creditor Account Number
Número da conta do recebedor
11188222
Payment consent - Creditor Account Type
Tipo da conta (ver opções abaixo)
SVGS
Importante:
A conta recebedora deve, obrigatoriamente, pertencer a uma pessoa jurídica (CNPJ). Contas de pessoas físicas (CPF)
não são válidas
para fluxos de Pix Automático.
Sobre o campo
accountType
:
Indica o tipo de conta bancária utilizada pelo credor (recebedor). Este campo é obrigatório e deve ser consistente com os demais dados da conta (ISPB, agência, número).
Valores Permitidos (conforme versão 2.1.0 da API do Open Finance Brasil):
Valor
Descrição
CACC
Conta Corrente
SVGS
Conta Poupança
TRAN
Conta de Pagamento Pré-Paga
Nota
: Contas salário (SLRY) não são permitidas nessa API.
Modelo de Configuração FVP:
O modelo a seguir serve para instruir como construir uma configuração funcional para os planos de teste da FVP. Abaixo estão listados todos os campos que você deverá preencher no arquivo JSON de configuração para executar os módulos de teste da FVP:
{
"alias": "74e929d9-33b6-4d85-8ba7-c146c867a817",
"description": "mock",
"server": {
"discoveryUrl": "
https://auth.mockbank.poc.raidiam.io/.well-known/openid-configuration
",
"authorisationServerId": "xxxxx-xxxx-xxxx-xxxx-xxxxx"
},
"resource": {
"brazilOrganizationId": "xxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
"name": "John Doe",
"brazilCpf": "00000000000",
"loggedUserIdentification": "00000000000",
"paymentAmount": "0.00",
"creditorAccountIspb": "00000000",
"creditorAccountIssuer": "0000",
"creditorAccountNumber": "0000000000",
"creditorAccountAccountType": "CACC",
"creditorName": "John Doe",
"creditorCpfCnpj": "00000000000",
"creditorProxy": "00000000000",
"debtorAccountIspb": "00000000",
"debtorAccountNumber": "0000000",
"debtorAccountIssuer": "0000",
"debtorAccountType": "TRAN"
"contractDebtorName": "Example",
"contractDebtorIdentification": "00000000000"
},
"directory": {
"participants": "
https://data.example.directory/participants
",
"keystore": "
https://keystore.example.directory/
",
"apibase": "
https://api.example.directory/
",
"directoryRootsUri": "
https://data.example.directory/roots_directory.jwks
",
"discoveryUrl": "
https://auth.example.directory/.well-known/openid-configuration
"
}
}

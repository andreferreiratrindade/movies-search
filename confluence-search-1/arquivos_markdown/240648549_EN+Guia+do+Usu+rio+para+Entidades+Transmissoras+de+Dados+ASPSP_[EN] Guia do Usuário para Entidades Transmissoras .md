---
                            title: "[EN] Guia do Usuário para Entidades Transmissoras de Dados (ASPSP) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "240648549_EN+Guia+do+Usu+rio+para+Entidades+Transmissoras+de+Dados+ASPSP"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/240648549/EN+Guia+do+Usu+rio+para+Entidades+Transmissoras+de+Dados+ASPSP"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # [EN] Guia do Usuário para Entidades Transmissoras de Dados (ASPSP) - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
1. Registering a Bank
1.1
1.1. Directory Overview
1.2
1.2. Registering an Authorization Server and OpenID Provider
1.3
1.3. Registering Resources
2
2. Validating a client registration request
2.1
2.1. OpenID Connect Registration and OAuth 2.0 Dynamic Client Registration
2.2
2.2. Software Statement Assertion Processing
3
3. Validating an Authorization Request
1. Registering a Bank
1.1. Directory Overview
The trust framework services provided by Open Finance Brasil provide all of the discovery services necessary for a TPPs and ASPSPs to interact with each other without being required to validate the authenticity of each others Identity, Authorizations, Consumer Offerings (Apps), APIs or Credentials
An Authorization Server or AS as defined by
RFC 6749 - The OAuth 2.0 Authorization Framework
perform several functions in a Data Sharing ecosystem like Open Finance. Please read ensure that the concepts roles and responsibilities defined in the original RFC are well understood before proceeding. In addition please ensure that the concepts, roles and responsibilities defined in
OpenID Connect Core
and how they extended the concepts defined in RFC 6749 are equally as well understood.
1.2. Registering an Authorization Server and OpenID Provider
Banks, typically large banks, will not be a single entity from a technology operations point of view. They may have different brands, security and IT infrastructure for different customer segments or they may have some IT infrastructure that supports multiple brands or customer segments. This means that the technical ecosystem needs to be flexible enough to support a wide variety of Banks Infrastructure Deployments whilst ensuring that the necessary services are discoverable both Third Parties customers that need to interact with it.
A flexible model for advertising authentication/authorization services and the resources that are protected by the AuthN and AuthZ is supported by the Directory.
Customer Friendly Name
- This is will be displayed to customers by TPPs and should be recognisable by the Banks Customers Already.
Customer Friendly Logo
- This will be displayed to customers by TPPs to aid brand recognition.
Description
- This may be displayed to customers by TPPs to aid brand recognition.
Terms of Service
- This is a link to the Banks Terms of Service which may be included by TPPs.
Notification WebHook
- Authorization Servers can register a WebHook that will receive pushed updates regarding changes to participants, their software or certificates.
OpenID Well Known Document Uri
- Link to the Authorization Server’s Discovery Document.
A Bank may choose to have one Authorization Server or many provided that it can satisfy the following requirements.
A customer can recognise the Authorization Server as a place that they would normally Bank with.
The Authorization Server can issue tokens for the resource and services that a customer or TPP is looking for.
For transmiting/account holder institutions whose
Authorization Server
supports more than one brand, it must accept more than one registry (client_ids creation) for the same
software statement
. If your
Authorization Server
implementation does not supports this behaviour, it must be suitable to support multiple brands and the registration of brands in the directory must be annotated according to each brand.
1.3. Registering Resources
Once a Bank has registered an Authorization Server, it needs to advertise what resources, APIs or Services it can provide authorization for.
[Authorization Resources management image]
Auth Id
Auth Customer Friendly Name
Well Known
Resource
Version
Auth Id
Auth Customer Friendly Name
Well Known
Resource
Version
1
Amazing Business Banking
https://auth.business.amazingbank.org.br/.well-known/openid-configuration
consents
1
1
Amazing Business Banking
https://auth.business.amazingbank.org.br/.well-known/openid-configuration
business account information
1
1
Amazing Business Banking
https://auth.business.amazingbank.org.br/.well-known/openid-configuration
payments
1
2
Amazing Banking
https://auth.amazingbank.org.br/.well-known/openid-configuration
consents
1
2
Amazing Banking
https://auth.amazingbank.org.br/.well-known/openid-configuration
account information
1
2
Amazing Banking
https://auth.amazingbank.org.br/.well-known/openid-configuration
account information
2
3
Amazing Banking
https://auth.payments.amazingbank.org.br/.well-known/openid-configuration
payments consents
1
3
Amazing Banking
https://auth.payments.amazingbank.org.br/.well-known/openid-configuration
payments
1
In the above example, Amazing Banking is advertising two services that should be recognisable to customers. “Amazing Business Banking” and “Amazing Banking”. These
may or may not be
directly related to “Brands” as different Banks may need to advertise different authentication services even within a sub brand.
In addition the bank advertises what resources each of the Authorization Servers are protecting or offering. In the above example Amazing Banking is supporting both version 1 and version 2 of the account information API and that “Amazing Banking” has two separate authentication and authorization systems for Payments and Account Information .
Correctly advertising what resources are offered by each server is important to achieving the scale envisaged by Brasil Open Finance and critical for ensuring that customers can identify their banking service easily and that TPPs can route customers to the correct Authorization Service based on the resources that protected by each service.
2. Validating a client registration request
Using OpenID Connect Discovery and the Brasil Open Finance Dynamic Client Registration specification. A TPP can register their application at each of the Authorization Servers available in the ecosystem.
2.1. OpenID Connect Registration and OAuth 2.0 Dynamic Client Registration
Please see Open Finance Brasil Dynamic Client Registration Specification for more details:
[EN]  Open Finance Brasil Financial-grade API Dynamic Client Registration 1.0 Implementers Draft 3
2.2. Software Statement Assertion Processing
Please see Open Finance Brasil Dynamic Client Registration Specification for more details:
[EN]  Open Finance Brasil Financial-grade API Dynamic Client Registration 1.0 Implementers Draft 3
3. Validating an Authorization Request
Please see Open Finance Security Profile for more details:
[EN] Open Finance Brasil Financial-grade API Security Profile - v2.0.0

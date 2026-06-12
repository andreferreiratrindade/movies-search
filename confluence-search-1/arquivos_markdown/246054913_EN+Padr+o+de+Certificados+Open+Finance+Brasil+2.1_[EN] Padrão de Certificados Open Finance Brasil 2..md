---
                            title: "[EN] Padrão de Certificados Open Finance Brasil 2.1 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "246054913_EN+Padr+o+de+Certificados+Open+Finance+Brasil+2.1"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/246054913/EN+Padr+o+de+Certificados+Open+Finance+Brasil+2.1"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # [EN] Padrão de Certificados Open Finance Brasil 2.1 - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            1
Foreword
2
Objective
3
Notational Conventions
4
1. Scope
5
2. Normative refences
6
3. Terms and definitions
7
4. Glossary
8
5. Open Finance Brasil Certificate Standards
8.1
5.1. Introduction
8.2
5.2. ICP-Brasil Certificates
8.2.1
5.2.1. Server Certificate
8.2.2
5.2.2. Client Certificate
8.2.2.1
5.2.2.1. Open Finance Brasil Attributes
8.2.3
5.2.3. Signature Certificate
8.2.3.1
5.2.3.1. Open Finance Brasil Attributes Present in the Certificate
8.2.4
5.2.4. Front-End Certificates
8.2.5
5.2.5. About certificates for exchanging information between authorized institutions and partners (non-participating)
9
6. Acknowledgements
10
7. Notices
11
8. Appendix
11.1
8.1. Configuration Template for Client Certificate - OpenSSL - For certificates issued until August 31, 2022
11.2
8.2. Configuration Template for Client Certificate - OpenSSL - For certificates issued after August 31, 2022
11.3
8.3. Configuration Template for Signature Certificate - OpenSSL
11.4
8.4. Endpoints vs Certificate type and mTLS requirements
11.5
8.5. Guide for the exchange of Certification Authorities approved in the Open Finance Brazil ecosystem by institutions
11.5.1
8.5.1. Introduction
11.5.2
8.5.2. Responsibilities and Prerequisites
11.5.3
8.5.2.1 Responsibilities:
11.5.4
8.5.2.2. Prerequisites:
11.6
8.5.3. Digital Certificate Analysis
12
9. Open Finance Client Certificate Subject DN Pattern - After January 19, 2023 {#subjectDNtemplates}
12.1
9.1.1. JWKS with certificate’s information:
12.2
Example:
https://keystore.directory.openbankingbrasil.org.br/d7384bd0-842f-43c5-be02-9d2b2d5efc2c/bc97b8f0-cae0-4f2f-9978-d93f0e56a833/transport.jwks
12.3
9.1.2. Public Key Certificate Example:
12.4
9.2. Example Subject Distinguished Name of the Certificate - Human readable:
12.5
9.3. Relative Distinguished Name (RDN) - Human readable:
12.6
9.4. Relative Distinguished Name (RDN) using OID - ANS.1:
12.7
9.5. Subject DN in RDN - According to RFC4514 - Open Finance Brazil Ecosystem Standard:
12.8
9.6. Table with RDN and details of the OIDs and Encodings.
12.9
The table below presents the sequence in Relative Distinguished Name as per item 9.5. In order to check the sequential order of the subjectDN, refer to itens 9.2 and 5.2.2.1
Foreword
Este documento também está disponível em
português
.
The Open Finance Brasil Initial Structure is responsible for creating standards and specifications necessary to meet the requirements and obligations of the Brasil Open Finance Legislation as originally outlined by the
Brasil Central Bank
. There is a possibility that some of the elements of this document may be the subject to patent rights. OFBIS shall not be held responsible for identifying any or all such patent rights.
Objective
Specify the set of necessary certificates required by participating organizations in Open Finance Brasil to ensure interoperability for authentication, confidentiality, integrity and non-repudiation among participants, as well as for users and consumers of these entities. The audience of this specification are the entities participating in Open Finance Brasil that will issue certificates to authenticate themselves with other entities, as well as offering their customers a secure authentication channel.
Notational Conventions
The key words "shall", "shall not", "should", "should not", "may", and "can" in this document are to be interpreted as described in [ISO Directive Part 2][ISODIR2]. These key words are not to be used as lexicon terms such that any occurrence of them shall be interpreted as key words and are not to be interpreted with their natural language meanings.
1. Scope
This document specifies the types of certificates required for:
Mutually authenticate (MTLS - Mutual TLS) participants' applications;
Message Signature (JWS - JSON Web Signature) applications to ensure authenticity and non-repudiation of messages between participants;
Provide a safe and reliable channel for Open Finance Brasil customers;
Authenticate participants in the Open Finance Brasil Participant Directory.
2. Normative refences
The following referenced documents are indispensable for the application of this document. For dated references, only the edition cited applied. For undated references, the latest edition of the referenced document (including any amendments) applies.
[ISODIR2] - ISO/IEC Directives Part 2 [ISODIR2]:
ISO/IEC Directives, Part 2 — Principles and rules for the structure and drafting of ISO and IEC documents
[RFC5280] - Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile:
RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile
[RFC7519] - JSON Web Token (JWT) [RFC7519]:
RFC 7519: JSON Web Token (JWT)
[RFC7515] - JSON Web Signature (JWS) [RFC7515] :
RFC 7515: JSON Web Signature (JWS)
[RFC7591] - OAuth 2.0 Dynamic Client Registration Protocol [RFC7591]:
RFC 7591: OAuth 2.0 Dynamic Client Registration Protocol
[RFC7592] - OAuth 2.0 Dynamic Client Registration Management Protocol [RFC7592]:
RFC 7592: OAuth 2.0 Dynamic Client Registration Management Protocol
[BCP195] - Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS) [BCP195]:
BCP 195 subseries contains 2 RFCs | RFC Editor
[RFC8705] - OAuth 2.0 Mutual TLS Client Authentication and Certificate Bound Access Tokens [RFC8705]:
RFC 8705: OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens
[OFB-FAPI] - Open Finance Brasil Financial-grade API Security Profile 1.0 [OFB-FAPI]:
https://github.com/OpenBanking-Brasil/specs-seguranca/open-banking-brasil-financial-api-1_ID3.html
[OFB-FAPI-DCR] - Open Finance Brasil Financial-grade API Dynamic Client Registration Profile 1.0 [OFB-FAPI-DCR]:
[EN] Open Finance Brasil Financial-grade API Dynamic Client Registration 1.0 Implementers Draft 3
[DOC-ICP-01] - DECLARAÇÃO DE PRÁTICAS DE CERTIFICAÇÃO DA AUTORIDADE CERTIFICADORA RAIZ DA ICP-BRASIL:
https://www.gov.br/iti/pt-br/centrais-de-conteudo/doc-icp-01-v-5-2-dpc-da-ac-raiz-da-icp-brasil-pdf
[DOC-ICP-04] - REQUISITOS MÍNIMOS PARA AS POLÍTICAS DE CERTIFICADO NA ICP-BRASIL:
https://www.gov.br/iti/pt-br/assuntos/legislacao/resolucoes/resolucoes-old/resolucao179_doc-icp-04_compilada.pdf
[RFC6749] - The OAuth 2.0 Authorization Framework [RFC6749]:
RFC 6749: The OAuth 2.0 Authorization Framework
[BCB-IN134] - Manual de Segurança do Open Finance:
https://www.in.gov.br/web/dou/-/instrucao-normativa-bcb-n-134-de-22-de-julho-de-2021-3345585364
[RFC2818] - HTTP Over TLS:
RFC 2818: HTTP Over TLS
[RFC5246] - The Transport Layer Security (TLS) Protocol Version 1.2
https://www.rfc-editor.org/rfc/rfc5246.txt
3. Terms and definitions
For the purpose of this document, the terms defined in [RFC5280], [BCP195], [RFC8705], e ISO29100 apply.
4. Glossary
API
- Application Programming Interface
DCR
- Dynamic Client Registration
HTTP
- Hyper Text Transfer Protocol
ICP
- Infraestrutura de Chave Públicas Brasileira
SS
- Software Statement
SSA
- Software Statement Assertion
TLS
- Transport Layer Security
mTLS
- Mutual Transport Layer Security
5. Open Finance Brasil Certificate Standards
5.1. Introduction
The Open Finance Brazil ecosystem makes use of chains of certificates and TLS protocol to guarantee the confidentiality, authentication and integrity of the communication channel used by the APIs of the participating organizations, as well as the customers of each of the participants.
The certificates used by Open Finance Brasil are also required to authenticate applications through private_key_jwt, in addition to being used to perform the payload signature using JWS. Another important attribution of certificates is to authenticate and present a secure channel to the end user in the act of authentication and use of services provided by the participating organizations.
5.2. ICP-Brasil Certificates
Certificates issued by Certifying Authorities authorized by ICP-Brasil are only used for communication between entities participating in the Open Finance Brasil ecosystem.
The certificate issuing and revocation processes are responsibility of the Certifate Authorities themselves, being regulated by Certification Practice Statements, and supervised by the Management Committee of the Brazilian Public Key Infrastructure (Comitê Gestor da Infraestrutura de Chaves Públicas Brasileira).
The practices, processes, availability and values practiced by the Certification Authorities are not responsibility of the Initial Structure of Open Finance Brasil.
Name restrictions
Despite UTF8 support by the certificate attributes, this standard will adhere to name restrictions as outlined in the document: “REQUISITOS MÍNIMOS PARA AS POLÍTICAS DE CERTIFICADO NA ICP-BRASIL”, section 7.1.5, establishing the following name restrictions applicable to all ICP-BRASIL certificates:
shall not use punctuation signs, umlauts or cedilla;
in addition to alphanumeric characters, only the following special characters may be used:
Character
Code NBR9611 (hexadecimal)
Character
Code NBR9611 (hexadecimal)
White space
20
+
2B
!
21
,
2C
“
22
-
2D
#
23
.
2E
$
24
/
2F
%
25
:
3A
&
26
;
3B
‘
27
=
3D
(
28
?
3F
)
29
@
40
*
2A
\
5C
Algorithms
All certificates issued by ICP-Brasil must have the following characteristics:
Type A of ICP-Brasil;
Key Algorithms: RSA 2048 bits;
Message Digest: SHA 256 bits.
Participating Certificate Authorities
The following certifying authorities carried out the onboard process for Open Finance Brasil and are authorized to issue Open Finance Brasil certificates using the level 1 certificates listed here:
CertiSign
(Chain v5 e v10)
Serasa
(Chain v5 e v10)
Serpro
(Chain v5 e v10)
Soluti
(Chain v5 e v10)
Valid
(Chain v5 e v10)
Only the certificates indicated with "Situação: válido" (which mean "status: valid") in these ITI repositories referenced above, which are Chain v5 and v10, should be accepted by the servers of the Open Finance Brasil ecosystem.
5.2.1. Server Certificate
The Server Certificate must be issued to protect and authenticate the TLS channel used by the APIs that will be consumed by client applications of organizations participating in Open Finance.
The certificate standard used must follow the existing certificate issuing practices of "CERTIFICATE FOR WEB SERVER - ICP-Brasil".
The server certificate shall be sent with the intermediate chain, according to
RFC5246
.
5.2.2. Client Certificate
Client Application Certificates (Transport) are used to authenticate the mTLS channel and to authenticate the client application through private_key_jwt, according to the application registration performed by the Dynamic Client Registration process with the transmitting organization. Regarding mTLS, the client certificate shall be sent with the intermediate chain, according to
RFC5246
.
To issue a Client Certificate, the participating organization in Open Finance Brasil must register the application in the Directory Service through the Software Statement Assertion issue process, and thus have already obtained the Software Statement ID value.
5.2.2.1. Open Finance Brasil Attributes
serialNumber:
National Register of Legal Personnel (CNPJ) of the legal entity holding the certificate and associated with the UID attribute and Software Statement ID, during validation with the Directory Service of Open Finance Brasil;
organizationIdentifier:
Participant Code associated with the CNPJ listed in the Directory Service of Open Finance Brasil; For certificates issued until August 31 the field used for this information is organizationalUnitName.
UID:
Software Statement ID registered in the Directory Service of Open Finance Brasil and belonging to the CNPJ and Participant Code.
The Client Certificate must be issued through the V10 chain, and must contain the following attributes:
Distinguished Name, as per the sequence bellow (details available in section 9.2):
businessCategory (OID 2.5.4.15):
Type of business category, which must contain: "Private Organization" or "Government Entity" or "Business Entity" or "Non-Commercial Entity"
jurisdictionCountryName (OID: 1.3.6.1.4.1.311.60.2.1.3):
BR
serialNumber (OID 2.5.4.5):
CNPJ
countryName (OID 2.5.4.6):
BR
organizationName (OID 2.5.4.10):
Company Name
stateOrProvinceName (OID 2.5.4.8):
Federation unit of the certificate holder's physical address
localityName (OID 2.5.4.7):
City of the holder's physical address
organizationIdentifier (OID 2.5.4.97):
Participant Code associated with the CNPJ listed in the Directory Service of Open Finance Brasil. *For certificates issued until August 31: organizationalUnitName (OID 2.5.4.11): Participant Code associated with the CNPJ listed in the Directory Service of Open Finance Brasil*
UID (OID 0.9.2342.19200300.100.1.1):
Software Statement ID generated by Open Finance Brasil Directory
commonName (OID 2.5.4.3):
FQDN or Wildcard
Certificate Extensions
keyUsage:
critical,digitalSignature,keyEncipherment
extendedKeyUsage:
clientAuth
Subject Alternative Name
DNSName:
FQDN or Wildcard
5.2.3. Signature Certificate
Signature Certificates are used to perform payload signature through the use of JWS (JSON Web Signature).
5.2.3.1. Open Finance Brasil Attributes Present in the Certificate
UID:
Participant Code associated with the CNPJ listed in the Directory Service of Open Finance Brasil;
commonName:
Company Name registered in the Directory Service of Open Finance Brasil and belonging to the CNPJ and Participant Code.
The Signature Certificate must be issued through the V5 chain, and must contain the following attributes:
Distinguished Name
UID (OID 0.9.2342.19200300.100.1.1):
Participant Code associated with the CNPJ listed in the Directory Service of Open Finance Brazil
countryName (OID 2.5.4.6):
BR
organizationName (OID 2.5.4.10):
ICP-Brasil
organizationalUnitName (OID 2.5.4.11):
Certificate Authority Name
organizationalUnitName (OID 2.5.4.11):
CNPJ of the Registration Authority
organizationalUnitName (OID 2.5.4.11):
Type of identification used (in person, videoconference or digital certificate)
commonName (OID 2.5.4.3):
Company Name
Certificate Extensions
keyUsage:
critical,digitalSignature,nonRepudiation
Subject Alternative Name
otherName (OID 2.16.76.1.3.2 - ICP-Brasil):
Name of the person responsible for the certificate
otherName (OID 2.16.76.1.3.3 - ICP-Brasil):
National Register of Legal Entities (CNPJ) of the legal entity holding the certificate;
otherName (OID 2.16.76.1.3.4 - ICP-Brasil):
Responsible for the certificate of legal entity holding the certificate (date of birth, CPF, PIS/PASEP/CI, RG);
otherName (OID 2.16.76.1.3.7 - ICP-Brasil):
INSS Specific Registry Number (CEI) of the legal entity holding the certificate.
5.2.4. Front-End Certificates
Front-End certificates are utilized to make services available, generally web pages, using TLS, that are acessible by the end users. Due to their function, and in order to guarantee better interoperability, those certificates must be of the type EV (Extended Validation) and must be generated by a valid certificate authority, following definitions of RFC 5280 e RFC 2818, in conformance with WebTrust principles and criteria.
5.2.5. About certificates for exchanging information between authorized institutions and partners (non-participating)
According to section IV of Joint Resolution No. 1 of May 4, 2020, the establishment of bilateral partnerships between authorized institutions and partners is an arrangement provided for in the regulation which must observe, where applicable, the same standards and certificates requirements that are applicable to exchange of information between participating institutions.
In accordance with §2 of Art. 10 of Provisional Measure 2200-2 of August 24, 2001 and with the provisions of item 3.12 in BCB Normative Instruction No. 134, for bilateral communication between institutions and partners, the use is authorized, by mutual agreement between the parties, of a private PKI, provided that the requirements of this profile for security certificates are observed, including their formatting, algorithms and established attributes.
The values for filling in the attributes required in this specification, but not applicable to the partner, should be defined in common agreement between the authorized institution and the partner, which does not exempt the authorized institution from the responsibility for filling it in properly.
6. Acknowledgements
Thanks to all who have set the foundations for secure and safe data sharing through the formation of the OpenID Foundation FAPI Working Group, the Open Finance Brasil GT Security and to the pioneers who will stand on their shoulders.
The following people contributed to this document:
João Rodolfo Vieira (Itaú)
José Michael Dias (Grupo Pan)
Marcos Rodrigues (Itaú)
Nic Marcondes (Quanto)
Ralph Bragg (Raidiam)
7. Notices
Copyright (c) 2023 Open Finance Brasil Initial Structure.
The Open Finance Brasil Initial Structure (OFBIS) grants to any Contributor, developer, implementer, or other interested party a non-exclusive, royalty-free, worldwide copyright license to reproduce, prepare derivative works from, distribute, perform and display, this Implementers Draft or Final Specification solely for the purposes of (i) developing specifications, and (ii) implementing Implementers Drafts and Final Specifications based on such documents, provided that attribution be made to the OFBIS as the source of the material, but that such attribution does not indicate an endorsement by the OFBIS.
The technology described in this specification was made available from contributions from various sources, including members of the OpenID Foundation, the Open Finance Brasil GT Security Working Group and others. Although the Open Finance Brasil Initial Structure has taken steps to help ensure that the technology is available for distribution, it takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this specification or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any independent effort to identify any such rights. The Open Finance Brasil Initial Structure and the contributors to this specification make no (and hereby expressly disclaim any) warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to this specification, and the entire risk as to implementing this specification is assumed by the implementer. The Open Finance Brasil Intellectual Property Rights policy requires contributors to offer a patent promise not to assert certain patent claims against other contributors and against implementers. The Open Finance Brasil Initial Structure invites any interested party to bring to its attention any copyrights, patents, patent applications, or other proprietary rights that may cover technology that may be required to practice this specification.
8. Appendix
8.1. Configuration Template for Client Certificate - OpenSSL - For certificates issued until August 31, 2022
[req]
default_bits = 2048
default_md = sha256
encrypt_key = yes
prompt = no
string_mask = utf8
distinguished_name = client_distinguished_name
req_extensions = req_cert_extensions
[ client_distinguished_name ]
businessCategory = <type of organization>
jurisdictionCountryName = BR
serialNumber = <CNPJ>
countryName = BR
organizationName = <Company Name>
stateOrProvinceName = <UF>
localityName = <City>
organizationalUnitName = <Participant Code>
UID = <Software Statement ID issued by the Directory>
commonName = <FQDN|Wildcard>
[ req_cert_extensions ]
basicConstraints = CA:FALSE
subjectAltName = @alt_name
keyUsage = critical,digitalSignature,keyEncipherment
extendedKeyUsage = clientAuth
[ alt_name ]
DNS = <FQDN|Wildcard>
8.2. Configuration Template for Client Certificate - OpenSSL - For certificates issued after August 31, 2022
oid_section = OIDs
[req]
default_bits = 2048
default_md = sha256
encrypt_key = yes
prompt = no
string_mask = nombstr
distinguished_name = client_distinguished_name
req_extensions = req_cert_extensions
[ OIDs ]
organizationIdentifier = 2.5.4.97
[ client_distinguished_name ]
businessCategory = <type of organization>
jurisdictionCountryName = BR
serialNumber = <CNPJ>
countryName = BR
organizationName = <Company Name>
stateOrProvinceName = <UF>
localityName = <City>
organizationIdentifier = OFBBR-<Participant Code>
UID = <Software Statement ID issued by the Directory>
commonName = <FQDN|Wildcard>
[ req_cert_extensions ]
basicConstraints = CA:FALSE
subjectAltName = @alt_name
keyUsage = critical,digitalSignature,keyEncipherment
extendedKeyUsage = clientAuth
[ alt_name ]
DNS = <FQDN|Wildcard>
8.3. Configuration Template for Signature Certificate - OpenSSL
[req]
default_bits = 2048
default_md = sha256
encrypt_key = yes
prompt = no
string_mask = nombstr
distinguished_name = client_distinguished_name
req_extensions = req_cert_extensions
[ client_distinguished_name ]
UID = <Participant Code>
countryName = BR
organizationName = ICP-Brasil
0.organizationalUnitName = <Certificate Authority>
1.organizationalUnitName = <CNPJ of the Registration Authority>
2.organizationalUnitName = <Validation type>
commonName = <Company Name>
[ req_cert_extensions ]
basicConstraints = CA:FALSE
subjectAltName = @alt_name
keyUsage = critical,digitalSignature,nonRepudiation
[ alt_name ]
otherName.0 = 2.16.76.1.3.2;PRINTABLESTRING:<Name of the person responsible for the organization>
otherName.1 = 2.16.76.1.3.3;PRINTABLESTRING:<CNPJ>
otherName.2 = 2.16.76.1.3.4;PRINTABLESTRING:<CPF/PIS/RF of the responsible person>
otherName.3 = 2.16.76.1.3.7;PRINTABLESTRING:<INSS Number>
8.4. Endpoints vs Certificate type and mTLS requirements
Below we present which endpoints can be published utilizing the EV certificate as consent authentication and the endpoints of private/bussiness API authentication using the ICP certificate. You will also be able to check which endpoints must protect its connections using mTLS.
ASPSP may choose the certificate that should be adopted for Open Data endpoints, which, by nature, are publicly accessible.
Table 1
OFB Phase
group
endpoint
certificate type
mTLS
NA
OIDC
.well-known/openid-configuration
EV or ICP WEB SSL
NA
OIDC
jwks_uri
EV or ICP WEB SSL
NA
OIDC
authorization_endpoint
EV
NA
OIDC
token_endpoint
ICP WEB SSL
Required
NA
OIDC
userinfo_endpoint
ICP WEB SSL
Required
NA
OIDC
pushed_authorization_request_endpoint
ICP WEB SSL
Required
NA
DCR
registration_endpoint
ICP WEB SSL
Required
NA
OIDC
revocation_endpoint
ICP WEB SSL
Required
2
Consentimentos
/consents/*
ICP WEB SSL
Required
2
Resources
/resources/*
ICP WEB SSL
Required
2
Dados
/customers/*
ICP WEB SSL
Required
2
Cartão
/credit-cards-accounts/*
ICP WEB SSL
Required
2
Contas
/accounts/*
ICP WEB SSL
Required
2
Empréstimos
/loans/*
ICP WEB SSL
Required
2
Financiamentos
/financings/*
ICP WEB SSL
Required
2
Adiantamento
/unarranged-accounts-overdraft/*
ICP WEB SSL
Required
2
Direitos Creditórios
/invoice-financings/*
ICP WEB SSL
Required
3
Pagamentos
/payments/*
ICP WEB SSL
Required
3
Webhook
/webhook/*
ICP WEB SSL
Required
4
Câmbio
/exchanges/*
ICP WEB SSL
Required
4
Investimentos
/credit-fixed-incomes/*
ICP WEB SSL
Required
8.5. Guide for the exchange of Certification Authorities approved in the Open Finance Brazil ecosystem by institutions
8.5.1. Introduction
Open Finance is an initiative of the Brazil Central Bank whose main objectives are to bring innovation to the financial system, promote competition, and improve the offer of financial products and services to the end consumer. This guide aims to assist professionals involved in the management of digital certificates used in the scope of Open Finance services by presenting the necessary technical analyses for migrating from an approved certificate authority (CAs/PKIs) to another certificate authority.
An approved certificate issuer is understood to be a certification authority that is linked to ITI/ICP, meeting all requirements and current legislation related to ITI/ICP's public key infrastructure and that is duly registered by the Open Finance ecosystem as a certification authority able to issue digital certificates in ITI/ICP's Brasil (Management Committee of the Brazilian Public Key Infrastructure) V5 and V10 chains,  following all the requirements listed in the
Digital Certificate Standard.
You can find the list of approved organizations here:
Participating Certificate Authorities
.
8.5.2. Responsibilities and Prerequisites
8.5.2.1 Responsibilities:
The participating institutions, when hiring the new certificate issuance service provider, in addition to observing the technical standards and recommendations of the working groups, must observe the rules for contracting technological services and on digital certificates under their responsibility under the terms of the current regulations, especially, in the case of Open Finance, items 2.6 and 3.9 of IN BCB 305/2022:
Item 2.6 IN BCB 305

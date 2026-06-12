---
                            title: "Guia de Boas Práticas - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "301662235_Guia+de+Boas+Pr+ticas"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/301662235/Guia+de+Boas+Pr+ticas"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Guia de Boas Práticas - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            OCSP e cache
As respostas OCSP das ACs podem ser cacheadas pelo participante provedor do serviço de forma a permitir melhor performance na checagem necessária à conexão mTLS oriunda do consumidor do serviço, de acordo com a política de risco de cada instituição provedora.
JWKS e cache
As respostas JWKS do diretório obtidas pelos participantes podem ser cacheadas pelo participante de forma a evitar consultas recorrentes à Infraestrutura do diretório e permitir maior celeridade nas checagens de assinatura dos
payloads
melhorando, assim, o tempo de resposta a qual o participante está sujeito.
O participante pode utilizar duas estratégias para definir quando solicitar a atualização (
refresh)
de um objeto JWKS cacheado localmente:
Update on error
: Consulta o objeto JWKS vigente quando a checagem com o objeto JWKS cacheado não obtém êxito
Update on Webhook
: Consulta o objeto JWKS vigente quando recebe uma notificação de
Webhook
do diretório informando da mudança, conforme consta na documentação que pode ser acessada através do link
16. Configurando eventos de notificação no Diretório
archived
Preview
Captura do authorization code na receptora/iniciadora
As implementações responsáveis pela captura do
authorization code
nas URLs de
call back
devem ser as mais simples possíveis, de forma a minimizar o risco de quebra de dependência e não execução da funcionalidade pelo
user-agent
do usuário. Entre outras, deve-se evitar (em ordem decrescente de criticidade):
Dependências externas ao domínio da URL (exemplo:
captcha, analytics
);
Que o conteúdo da página seja cacheado no lado do usuário;
Dependências externas ao
host
da URL;
Páginas com várias imagens;
Demais implementações que possam não funcionar por alguma indisponibilidade de rede ou dependência a partir da máquina do usuário.
Após a captura do
authorization code
, realize as demais operações de UX necessárias.
Payload
de resposta e cache
Nas APIs de negócio, as respostas dos sistemas de negócio podem ser cacheadas no API
Gateway
, desde que a arquitetura do sistema invalide dinamicamente os registros em cache que não espelhem mais a realidade.

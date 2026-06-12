---
                            title: "Aderência das APIs das instituições participantes às especificações funcionais e de segurança - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "498500006_Ader+ncia+das+APIs+das+institui+es+participantes+s+especifica+es+funcionais+e+de+seguran+a"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/498500006/Ader+ncia+das+APIs+das+institui+es+participantes+s+especifica+es+funcionais+e+de+seguran+a"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Aderência das APIs das instituições participantes às especificações funcionais e de segurança - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            item 2.2 - vii
Controle de versão
Versão
Data
Resumo das alterações
1
May 23, 2024
Versão inicial
Introdução e Objetivos
Esta métrica visa garantir que as APIs das instituições participantes do Open Finance em ambiente produtivo estejam aderentes às especificações funcionais e de segurança estabelecidas. A Estrutura Responsável pela Governança do Open Finance verifica e exige essa conformidade para assegurar a integridade, segurança e eficiência do ecossistema do Open Finance.
Sobre a Métrica
A métrica consiste na avaliação das APIs em ambiente produtivo das instituições participantes que estejam cadastradas no Diretório de Participantes do Open Finance. Seu objetivo é identificar desconformidades, ou seja, divergências entre as APIs publicadas em ambiente produtivo e as especificações funcionais e de segurança. A análise ocorre tanto no aspecto funcional quanto no de segurança das APIs.
Especificações Funcionais
Verificação dos endpoints de Consents e Payments
Verifica se todos os endpoints das APIs publicadas têm todos os endpoints publicados.
Verifica se os endpoints de consents e payments estão acessíveis e conformes.
Verificação do logotipo
Verifica se foi registrado um logotipo válido.
Confirma se o logo é acessível.
Valida se o logo é do tipo .svg e possui dimensões de no mínimo 512 de altura e 512 de largura.
Verificação do endpoint de Well-Known
Verifica se o endpoint de well-known cadastrado no Diretório está válido e acessível em ambiente produtivo na instituição participante.
Verificação dos scopes suportados
Valida se os scopes suportados pela instituição são válidos e declarados no well-known.
Compara os scopes com os family types cadastrados no diretório pela organização.
Verificação de fluxos de DCR
Verifica se o servidor de autorização da instituição realiza o fluxo DCR com diferentes configurações e se rejeita o fluxo DCR em cenários de erro.
Metodologia Simplificada
Para fins de monitoramento deste item, o período de apuração será mensal, conforme orientado pelo Manual de Monitoramento do Open Finance Brasil. A avaliação envolverá:
Verificação das Especificações Funcionais
Chamada aos endpoints de consents e payments, validação se as chamadas foram aceitas e se a resposta é válida, e verificação de respostas esperadas ao chamar o endpoint de payments-consents com diferentes tipos de parâmetros.
Verificação do logotipo registrado, acessibilidade e conformidade com as especificações (.svg, dimensões mínimas de 512x512).
Verificação se o endpoint de well-known está válido e acessível em ambiente produtivo.
Verificação das Especificações de Segurança
Verificação do fluxo DCR com diferentes configurações, validação da cadeia de certificados, e rejeição do fluxo DCR em cenários de erro.
Validação dos scopes suportados e comparação com os family types cadastrados no diretório pela organização.
Interpretação dos Resultados
Os resultados da métrica serão interpretados para verificar se as instituições estão aderentes às especificações funcionais e de segurança das APIs em ambiente produtivo. A análise incluirá:
Especificações Funcionais
Verificação dos endpoints de Consents
Chamada aos endpoints de consents e validação se as chamadas foram aceitas e se a resposta é válida.
Verificação dos Endpoints de Payments
Chamada aos endpoints de payments, se disponíveis pela instituição, e validação se as chamadas foram aceitas e se a resposta é válida.
Chamadas ao endpoint de payments-consents com diferentes tipos de parâmetros, como payments type igual a BAD, person type igual a INVALID, currency igual a XXX, utilizando uma data do passado, entre outros, para verificar se as respostas estão de acordo com o esperado, como retornar o código de erro 422 ou 400.
Verificação do logotipo
Verificação se foi registrado um logotipo válido.
Confirmação se o logo é acessível.
Validação se o logo é do tipo .svg e possui dimensões de no mínimo 512 de altura e 512 de largura.
Verificação dos endpoints de Well-Known
Verificação se o endpoint de well-known cadastrado no Diretório está válido e acessível em ambiente produtivo na instituição participante.ante.
Especificações de Segurança
Verificação do fluxo DCR
Verificação se o servidor de autorização da instituição realiza o fluxo DCR com diferentes configurações, como:
Configurações básicas e sem campos adicionais.
Alterando a ordem do parâmetro grant_types e adicionando o parâmetro opcional scopes.
Com campo opcional scopes em ordem diferente.
Chamada ao endpoint de token para receber um token.
Verificação da Cadeia de Certificados
Verificação se a cadeia de certificados retornados pelos endpoints do servidor de autorização (token, registro) e endpoints funcionais estão de acordo com a RFC5246 - 7.4.2.
Verificação se a CA é aceita pelo Open Finance Brasil.
Validação se todas as certificações de segurança necessárias estão publicadas no diretório.
Verificação se, para o novo perfil único, a instituição deve ter publicado exclusivamente a certificação BR-OF Adv. OP com Private Key, PAR (FAPI-BR v2).
Rejeição do Fluxo DCR em Cenários de Erro
Utilizando Software Statement Assertion com assinatura inválida.
Sem enviar o Software Statement Assertion.
Sem adicionar os certificados TLS do cliente, verificando se as chamadas GET e DELETE são recusadas ao não utilizar os certificados TLS.
Adicionando um certificado TLS não confiável, verificando se as chamadas GET e DELETE são recusadas ao utilizar um certificado TLS não confiável.
Sem enviar o redirect_uri.
Com um jwks_uri não presente no diretório.
Enviando um jwks by_value.
Utilizando um certificado emitido pela PKI do Diretório de Participantes em ambiente de Sandbox.
Tentando registrar o DCR novamente, pois não devem ser permitidos múltiplos clients.
Utilizando um certificado revogado pela CA.
Após a deleção do client, executando as chamadas de GET e DELETE esperando a recusa às chamadas.
Nas chamadas de GET e DELETE ao utilizar um access token inválido.
Verificação dos scopes Suportados
Validação se os scopes suportados pela instituição são válidos e declarados no well-known.
Comparação dos scopes com os family types cadastrados no diretório pela organização.
Exemplo Ilustrativo
Considere uma instituição em que o servidor de autorização não rejeite o fluxo DCR ao utilizar um Software Statement Assertion com assinatura inválida. Mesmo que todos os outros critérios estejam em conformidade, a métrica consideraria a instituição em desconformidade devido a esse único item não atendido. Em caso de desconformidade com algum dos critérios, a métrica deverá destacar o item em questão como um ponto de atenção.
Dados e Fontes
Para o cálculo da métrica, utilizam-se os dados obtidos a partir do Diretório de Participantes e da Ferramenta de Validação de Produção (FVP). A FVP gera logs detalhados sobre o sucesso ou falha dos cenários de testes executados. Esses logs são consolidados na Plataforma Analítica de Dados (PAD), um repositório centralizado que serve como base para a análise e avaliação da métrica. A combinação dessas fontes de dados permite uma avaliação precisa da métrica e um monitoramento efetivo da conformidade regulatória no contexto do Open Finance.
Limitações e Considerações
Atualmente, não há visibilidade ou conhecimento de limitações ou considerações adicionais para esta métrica. A análise será continuamente revisada e aprimorada conforme novos dados e informações se tornem disponíveis.
Responsável pela Aprovação
Squad Sandbox

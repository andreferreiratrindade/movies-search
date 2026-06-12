---
                            title: "Certificação - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "86835297_Certifica+o"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/86835297/Certifica+o"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Certificação - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            Para a entrada segura e assertiva no ecossistema do Open Finance Brasil, a Estrutura de Governança disponibilizou um conjunto de ferramentas e infraestrutura para suportar o processo de testes e homologação dos produtos e serviços desenvolvidos pelas instituições participantes.
Lembramos que uma implementação de versão de API do Open Finance Brasil só poderá ser registrada no ambiente produtivo do Diretório caso tenha sido certificada nos testes de segurança e funcionais. Maiores detalhes sobre o processo de certificação estão disponíveis na página
Diretrizes Técnicas de Certificação
.
Neste documento são apresentados os impactos do motor de conformidade funcional no processo de versionamento das APIs do ecossistema do Open Finance Brasil e as regras de certificação. Regras estas que podem ser ajustadas para atender as particularidades de cada uma das especificações, fases ou produtos sendo discutidos.
O motor de conformidade funcional é a plataforma utilizada para a certificação das instituições participantes do Open Finance Brasil. Deste modo, uma instituição participante só estará apta a participar do Open Finance Brasil se passar em 100% dos testes obrigatórios e também nos condicionais que se aplicam à instituição. Para que o motor de conformidade funcional esteja pronto para realizar a certificação, é necessário que sejam realizadas as seguintes etapas:
Estimativa de tempo de desenvolvimento do motor de conformidade funcional;
Previamente ao encerramento da etapa de design, haverá um período (C) em que a especificação será submetida ao Squad Sandbox. Em conjunto com o GT Especificações, o Squad deverá estimar os prazos para implementação do motor de conformidade funcional (I), atingimento dos marcos de maturidade dos testes (P1, P2, P3 e P4) e o tempo de processamento das submissões das certificações (P5);
Desenvolvimento dos módulos de testes;
Os módulos devem ser desenvolvidos dentro da etapa implementing;
Disponibilização dos testes para o processo de maturidade;
Esse evento dará início à etapa certifying;
Acompanhamento do processo de maturidade junto ao ecossistema;
O processo de maturidade é dividido em 4 períodos: P1, P2, P3 e P4;
A duração de cada um dos períodos será definida pelo Squad Sandbox, a depender de cada especificação;
A duração de referência para cada um dos períodos será de duas semanas, sendo flexibilizada para mais ou para menos;
O período P1 deverá conter não somente o tempo apontado pelo Squad Sandbox para o atingimento de 25% de sucesso nos testes, mas também o tempo definido pelo GT Especificações, para que as instituições participantes possam fazer o desenvolvimento inicial das integrações;
Ao final da quarta etapa (P4), é esperado o atingimento de maturidade do motor de conformidade funcional;
Liberação do motor de conformidade funcional para que os participantes iniciem o processo de certificação das APIs;
Esse evento promoverá a versão das especificações das APIs de RC para stable;
Processamento da submissão das certificações;
O processo de submissão e processamento das certificações ocorrem no período P5;
A duração de referência para este período será de cinco semanas, sendo flexibilizada para mais ou para menos;
Ao final deste período, o ecossistema estará pronto para realizar a liberação da nova versão em produção.
Cada um dos períodos de maturidade contidos na tabela estabelece um percentual de sucesso para que ele seja considerado finalizado com êxito.
Open
C:
Período onde são definidas as datas de início dos períodos Px;
I:
Período para desenvolvimento do motor de conformidade pelo Squad Sandbox e início do desenvolvimento das APIs pelas instituições participantes após a
publicação da versão (x+1).0.0-beta.1;
P1:
Período para continuidade do desenvolvimento pelas instituições participantes que permita o atingimento de 25% de sucesso nos testes;
P2:
Período para atingimento de 50% de sucesso nos testes;
P3:
Período para atingimento de 75% de sucesso nos testes;
P4:
Período para atingimento de 100% de sucesso nos testes;
P5:
Período para certificação, submissão dos documentos e processamento das submissões.
Observação:
O atingimento da porcentagem de sucesso nos testes é considerada a partir do início de cada um dos períodos. Por exemplo, se houver 16 testes no início de P1, é necessário passar em 4 para atingir 25% de sucesso nos testes . Se for adicionado um teste extra entre P1 e P2, será necessário obter 50% de sucesso dos 17 testes existentes no P2 para atingir o sucesso nos testes correspondente a este período
Os testes específicos são um subconjunto dos testes que compõem o motor de conformidade funcional. O objetivo deles é validar as alterações ocorridas nas versões minor e patch. O propósito de homologar as alterações realizadas nas especificações, com o subconjunto apenas, é diminuir a quantidade e complexidade dos testes executados. Além disso, o processo de validação da minor e da patch diminui a burocracia do processo de certificação aplicado nas majors, através da supressão dos passos de submissão de documentos e processamento dos mesmos por parte do Squad Sandbox. No entanto, para um participante continuar apto a participar do Open Finance Brasil, ainda é necessário estar certificado e passar em 100% dos módulos de testes específicos obrigatórios e dos condicionais cabíveis do motor de certificação funcional.
Novos entrantes deverão entrar com as versões mais atuais vigentes, mas detalhes serão informados de acordo com o caso específico. As alterações minor ou patch podem ser classificadas segundo dois critérios de avaliação:
quebra de contrato:
uma alteração de especificação possui quebra de contrato, quando a sua adoção por uma determinada classe de participantes, seja iniciador de pagamento, detentor de conta, transmissor de dados ou receptor de dados; causa incompatibilidade técnica e/ou funcional na comunicação destes com seus pares; detentor de conta, iniciador de pagamento, receptor de dados ou transmissor de dados, respectivamente;
correção de bugs:
uma alteração de especificação pode ter como objetivo apenas a correção de erros que impossibilitem o correto funcionamento do ecossistema do Open Finance Brasil, ou pode incluir novas funcionalidades que objetivam trazer melhorias e/ou novos comportamentos desejáveis para o ecossistema.
Versionamento
Restrições
Necessita de certificação¹
Testes Específicos
Exemplos de situações
Versionamento
Restrições
Necessita de certificação¹
Testes Específicos
Exemplos de situações
Major
Não haverá mais do que duas versões em convivência
Sim
Processo completo de certificação funcional
Criação de uma nova API ou adição de novas funcionalidades com alterações nos endpoints já existentes
Minor Planejada
Não haverá quebra de contrato
Sim, processo simplificado
Avaliação do GT Especificação
Novas funcionalidades Ex: Webhook e Agendamento
Minor Crítica Não Sincronizada
Necessidade de implementar o mais breve possível, para correção de bugs, até a data limite estabelecida, porém os participantes não precisam sincronizar o momento do início em produção
Sim, processo simplificado
Testes específicos/Direcionado s e incorporados na próxima certificação planejada
Criação de plano de testes específicos para os cenários a serem avaliados. Ex.: Clarificação de regra de negócio que exigirá alteração por parte de organização do ecossistema. (Atualização da cadeia V3 dos certificados digitais)
Minor Crítica Sincronizada
Necessidade de implementar o mais breve possível, para correção de bugs, porém os participantes devem sincronizar o momento do início em produção
Sim, processo simplificado
Testes específicos/Direcionado s e incorporados na próxima certificação planejada
Criação de plano de testes específicos para os cenários a serem avaliados. Ex.: Alteração de regra de negócio de campo que pode impedir a execução da funcionalidade
Patch
Não haverá quebra de contrato
Não
Apenas na próxima certificação planejada
Ajustes para melhorar a descrição de um campo
Legenda:
1-
Em situações excepcionais, o Squad Sandbox e GT Especificações poderão decidir a melhor abordagem de testes.
Ex.: Prazos de construção dos testes não atendem a criticidade do problema.

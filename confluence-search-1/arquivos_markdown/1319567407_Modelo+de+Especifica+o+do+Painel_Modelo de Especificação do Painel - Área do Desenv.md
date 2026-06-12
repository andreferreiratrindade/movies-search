---
                            title: "Modelo de Especificação do Painel - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor"
                            paginaId: "1319567407_Modelo+de+Especifica+o+do+Painel"
                            url: "https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1319567407/Modelo+de+Especifica+o+do+Painel"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # Modelo de Especificação do Painel - Área do Desenvolvedor - Open Finance Brasil - Área do Desenvolvedor

                            #
Modelo de Especificação do Painel
## 1. Visão geral do Painel
### Informações do Painel
**Nome do Painel**: [Nome do Painel]
**ID/Código do Painel**: [Identificador Único]
**Versão**: [Número da Versão]
**Criado por**: [Nome do Autor]
**Data de Criação**: [YYYY-MM-DD]
**Última atualização**: [YYY-MM-DD]
**Status**: [Rascunho | Em Revisão | Aprovado | Produção]
### Propósito e Objetivos
**Propósito do Negócio**:
[Descreva o problema de negócios que este painel resolve]
**Perguntas-chave respondidas**:
[Pergunta 1]
[Pergunta 2]
[Pergunta 3]
**Público-alvo**:
[Quem usará este painel - por exemplo, Executivos, Equipe de Vendas, Operações]
**Frequência de atualização**:
[Tempo real | Horário | Daily | Semanal | Mensal]
---
## 2. Fontes de Dados
### Fonte de Dados 1
**Nome da Fonte**: [Nome da Fonte]
**Tipo de Fonte**: [Banco de Dados | API | Arquivo | [Data Warehouse]
**String/Caminho de Conexão**: [Detalhes de conexão ou caminho do arquivo]
**Banco de Dados/Esquema**: [Nome do banco de dados e do esquema]
**Tabelas/Vistas Principais**:
'table_name_1'
'table_name_2'
**Cronograma de Atualização**: [Quando os dados são atualizados]
**Proprietário dos Dados**: [Equipe/Pessoa responsável]
**Requisitos de Acesso**: [Credenciais, permissões necessárias]
### Fonte de Dados 2
**Nome da Fonte**: [Nome da Fonte]
**Tipo de Fonte**: [Banco de Dados | API | Arquivo | [Data Warehouse]
**String/Path de Conexão**: [Detalhes da Conexão]
**Banco de Dados/Esquema**: [Nome do banco de dados e do esquema]
**Tabelas/Vistas Principais**:
'table_name_1'
**Cronograma de Atualização**: [Quando os dados são atualizados]
**Proprietário dos Dados**: [Equipe/Pessoa responsável]
**Requisitos de Acesso**: [Credenciais, permissões necessárias]
## 3. Modelo de Dados e Relações
###
Principais Tabelas/Conjuntos de Dados
#### Conjunto de Dados 1: [Nome do Conjunto de Dados]
**Fonte**: Fonte de Dados 1
**Tabela/Consulta**: 'table_name' ou 'custom_query_name'
**Colunas Utilizadas**:
| Nome da Coluna | Tipo de Dado | Descrição | Valores de Exemplo |
|-------------|-----------|-------------|---------------|
| column_1 | VARCHAR | [Descrição] | "Valor1", "Valor2" |
| column_2 | INTEIRO | [Descrição] | 100, 200 |
| column_3 | DATA | [Descrição] | 01-01-2024 |
**Filtros Aplicados**:
Cláusula WHERE: 'status = 'ativo' E data >= '2024-01-01''
#### Conjunto de Dados 2: [Nome do Conjunto de Dados]
**Fonte**: Fonte de Dados 2
**Tabela/Consulta**: 'table_name'
**Colunas Utilizadas**:
| Nome da Coluna | Tipo de Dado | Descrição | Valores de Exemplo |
|-------------|-----------|-------------|---------------|
| column_1 | VARCHAR | [Descrição] | "Valor1" |
| column_2 | DECIMAL | [Descrição] | 99,99 |
### Relacionamentos/Unões
```
Dataset1.key_coluna → Dataset2.key_coluna (Many-to-One)
Dataset2.id
→ Dataset3.foreign_id (Um para Muitos)
```
---
## 4. Variáveis e Métricas Calculadas
### Variável Calculada 1: [Nome da Variável]
**Propósito**: [O que isso calcula e por quê]
**Fórmula**:
```
[campo1] * [campo2] / 100
```
**Tipo de Dado**: [Número | Percentual | Moeda | Texto]
**Formato**: [ex., #,##0,00 ou 0,00%]
**Exemplo**:
Entrada: campo1 = 1000, campo2 = 25
Saída: 250,00
---
### Variável Calculada 2: [Nome da Variável]
**Propósito**: [O que isso calcula e por quê]
**Fórmula**:
```
SE([status] = "Concluído",
[actual_value],
[estimated_value])
```
**Tipo de Dado**: Número
**Formato**: Moeda ($#,##0.00)
---
### Variável Calculada 3: [Nome da Variável]
**Propósito**: [O que isso calcula e por quê]
**Fórmula**:
'''sql
SOMA([RECEITA]) / CONTAGEM(DISTINTA [customer_id])
```
**Tipo de Dado**: Número
**Formato**: Moeda
**Agregação**: Média
**Dependências**: Requer campos 'receita' e 'customer_id'
---
### Variável Calculada 4: [Crescimento Ano a Ano]
**Objetivo**: Calcular a variação percentual em relação ao ano anterior
**Fórmula**:
```
((SUM([current_year_sales]) - SUM([previous_year_sales]))
/ SUM([previous_year_sales])) * 100
```
**Tipo de Dado**: Porcentagem
**Formato**: 0,0%
**Contexto do Filtro**: Aplicado em nível de ano
---
### Variável Calculada 5: [Total Contínuo]
**Propósito**: Soma acumulada ao longo do período
**Fórmula**:
```
WINDOW_SUM(SUM([vendas]),
FIRST(),
0,
'PEDIDO POR [DATA]')
```
**Tipo de Dado**: Número
**Formato**: #,##0
**Partição**: Por categoria
**Ordem**: Por Data ascendente
---
## 5. Componentes do Painel
### Componente 1: [Nome do Componente]
**Tipo de Componente**: [Cartão de KPI | Gráfico de barras | Gráfico de Linhas | Gráfico de Pizza | Tabela | Mapa | Medidor]
**Posição**: [Linha 1, Coluna 1 | Canto superior esquerdo | etc.]
**Tamanho**: [Largura x Altura ou unidades de grade]
**Configuração de Dados**:
**Conjunto de Dados**: Conjunto de Dados 1
-**Dimensões**:
[dimension_field_1]
[dimension_field_2]
-**Métricas**:
[metric_field_1]: Agregação = SUM
[metric_field_2]: Agregação = média média
**Campos Calculados Utilizados**:
[calculated_variable_1]
**Filtros**:
Faixa de Datas: Últimos 90 dias
Status: Apenas Ativo
**Classificação**:
[metric_field_1] DESC
Limite: Top 10
**Formatação**:
Esquema de Cores: [Gradiente azul | Personalizado: #1f77b4]
Rótulos do Programa: Sim
Lenda do Show: Sim
Formato do eixo: [Formato numérico]
**Interatividade**:
Ação de Clique: [Filtrar outros componentes | Vamos nos detalhes | Link para a URL]
Dica de Deslize: Mostrar [campo1], [campo2], [calculated_field]
---
### Componente 2: [Nome do Componente]
**Tipo de Componente**: Gráfico de Linhas de Séries Temporais
**Posição**: Fila 1, Coluna 2-4
**Tamanho**: 3x2 unidades de grade
**Configuração de Dados**:
**Conjunto de Dados**: Conjunto de Dados 1
**Eixo X**: [date_field] (Granularidade: Diária)
-**Eixo y**:
[SUM(sales)] - Eixo Primário
[COUNT(ordens)] - Eixo Secundário
**Série/Análise**: [category_field]
**Campos Calculados**: [calculated_variable_2]
**Filtros**:
Faixa de Datas: Dinâmica - Últimos 12 meses
Região: Todos
**Formatação**:
Estilo de Linha: Liso
Marcadores de Pontos: Ativados
Paleta de cores: categórica
Formato do eixo Y: Moeda
**Formatação Condicional**:
Se [vendas] < [alvo]: Vermelho - Se [vendas] >= [alvo]: Verde
---
### Componente 3: [Tabela de Dados]
**Tipo de Componente**: Tabela de Dados
**Posição**: Fileira 2, largura total
**Tamanho**: largura total x 400px
**Colunas**:
| Cabeçalho da Coluna | Campo Fonte | Agregação | Formato | Largura |
|---------------|--------------|-------------|---------|-------|
| Nome do Cliente | [customer_name] | Nenhum | Texto | 200px |
| Vendas Totais | [vendas] | SUM | Moeda | 120px |
| Contagem de Ordens | [order_id] | CONDE | Número | 100px |
| Valor Médio da Ordem | [calculated_variable_3] | - | Moeda | 120px |
| Status | [status] | Nenhum | Texto | 100px |
**Filtros**: [Filtros aplicados]
**Ordenação**: Ordenação padrão por DESC de Vendas Totais
**Paginação**: 25 linhas por página
**Exportar**: Ativado (CSV, Excel)
---
### Componente 4: [Cartão de KPI]
**Tipo de Componente**: KPI/Cartão de Métrica
**Posição**: Fileira de cima, Posição 1
**Tamanho**: 1x1
**Métrica Primária**:
**Valor**: SOM([receita])
**Rótulo**: "Receita Total"
**Formato**: $#,##0
**Métrica de Comparação**:
**Valor**: [calculated_variable_4] (Crescimento Ano Ano %)
**Rótulo**: "vs. Ano Passado"
**Formato**: +0,0%;-0,0%
**Cor Condicional**:
Verde se > 0
Vermelho se < 0
**Sparkline**:
Tendência do programa: Últimos 30 dias
Métrica: Receita diária
---
## 6. Filtros e Parâmetros do Painel
### Filtros Globais
(Aplicado a todos ou múltiplos componentes)
#### Filtro 1: Faixa de Datas
**Tipo**: Seletor de Intervalo de Datas
**Valor Padrão**: Últimos 90 dias
**Opções**: [Últimos 7 dias | Últimos 30 dias | Últimos 90 dias | YTD | Personalizado]
**Aplica-se a**: Todos os componentes
#### Filtro 2: [Região]
**Tipo**: Menu suspenso Multi-Select
**Campo Fonte**: [region_field]
**Valor Padrão**: Todos
**Opções**: Dinâmica a partir dos dados
**Aplica-se a**: [Componente 1, Componente 2, Componente 3]
#### Filtro 3: [Categoria]
**Tipo**: Menu suspenso de seleção única
**Campo Fonte**: [category_field]
**Valor Padrão**: Todas as Categorias
**Aplica-se a**: Todos os componentes
### Filtros Específicos de Componente
**Componente 2**: Filtro adicional para [product_line] = "Premium"
### Parâmetros
| Nome do Parâmetro | Tipo | Valor Padrão | Usado em | Propósito |
|----------------|------|---------------|---------|---------|
| target_value | Número | 100000 | Variável Calculada 2 | Comparação de gols |
| currency_conversion | Número | 1.0 | Múltiplos | Taxa de conversão de moeda |
---
## 7. Layout e Design
### Layout da Grade
```
+----------+----------+----------+----------+
| KPI 1 | KPI 2 | KPI 3 | KPI 4 |
| (1x1) | (1x1) | (1x1) | (1x1) |
+----------+----------+----------+----------+
| Gráfico 1 | Gráfico 2 |
| (2x2) | (2x2) |
| | |
+-------------------+----------------------+
| Tabela 1 (Largura Total) |
| (4x2) |
+------------------------------------------+
| Gráfico 3 | Gráfico 4 |
| (2x2) | (2x2) |
+-------------------+----------------------+
```
### Especificações de Design
-**Paleta de cores**:
Primária: #1f77b4
Secundária: #ff7f0e
Sotaque: #2ca02c
Contexto: #ffffff
Texto: #333333
-**Tipografia**:
Fonte do título: [Nome da fonte], 24px, negrito
Cabeçalhos componentes: [nome da fonte], 18px, semi-negrito
Texto principal: [Nome da Fonte], 14px, Regular
Rótulos: [Nome da Fonte], 12px, Regular
-**Espaçamento**:
Enchimento de componentes: 16px
Margem de Componente: 12px
Gap de grade: 8px
---
## 8. Otimização de Desempenho
### Otimização de Dados
**Nível de Agregação**: Pré-agregado para nível [diário | mensal]
**Faixa de Dados**: Limite para durar [X] meses/anos
**Indexação**: Garantir índices em [campo1, campo2, date_field]
**Particionamento**: Dados particionados por [data | região]
### Estratégia de Cache
**Duração do Cache**: [15 minutos | 1 hora | 4 horas]
**Chave de Cache**: Baseada em [valores de filtro, intervalo de datas]
**Pré-cache**: Agendar para [tempo] antes do uso de pico
### Otimização de Consultas
**Limite de linhas**: Limite em [10.000 | 50.000] linhas por consulta
**Visualizações Materializadas**: Use 'mv_sales_summary' em vez de tabelas brutas
**Atualização Incremental**: Só atualiza os dados dos últimos [7 dias]
---
## 9. Acesso e permissões
### Níveis de Acesso do Usuário
| Função | Nível de Acesso | Permissões |
|------|-------------|-------------|
| Executivo | Apenas visualização | Acesso completo ao painel |
| Técnico | Visualizar & Exportar | Pode exportar dados |
| Admin | Acesso Total | Editar dashboard, gerenciar acesso |
### Segurança em Nível de Fileira
**Equipe de Vendas**: Filtrar ONDE [sales_rep_id] = CURRENT_USER_ID
**Gerentes Regionais**: Filtrar ONDE [região] = USER_REGION
### Compartilhamento & Distribuição
**Link de Compartilhamento**: [Ativado | Desativado]
**Embed*: [Permitido | Não Permitido]
**Relatórios Programados**:
Frequência: [Semanalmente às segundas-feiras às 8h]
Destinatários: [lista de e-mails]
Formato: PDF
---
## 10. Testes e Validação
### Validação de Dados
[ ] Verificar se os totais correspondem ao sistema de origem
[ ] Verifique valores nulos/ausentes
[ ] Valide que os intervalos de data estão corretos
[ ] Confirme que campos calculados produzem resultados esperados
[ ] Teste com casos extremos (valores zero, números negativos, nulos)
### Testes Funcionais
[ ] Todos os filtros funcionam corretamente
[ ] Função de detalhamento/ações de clique
[ ] Funcionalidades de exportação
[ ] Layout móvel/responsivo exibe corretamente
[ ] Desempenho atende aos requisitos (
### Teste de Aceitação do Usuário
[ ] O painel atende aos requisitos do negócio
[ ] Métricas alinhadas com as expectativas dos stakeholders
[ ] Design visual aprovado
[ ] Treinamento do usuário concluído
---
## 11. Documentação e Suporte
### Dicionário de Dados
Link para o dicionário completo de dados: [URL ou caminho]
### Problemas e Limitações Conhecidos
[Problema 1]: [Descrição e solução alternativa]
[Edição 2]: [Descrição e solução alternativa]
### Melhorias Futuras
[ ] Adicionar componente de análise preditiva
[ ] Integrar alertas em tempo real
[ ] Adicionar o drill-through ao detalhe da transação
### Contatos de Apoio
**Proprietário do Painel**: [Nome, e-mail]
**Suporte Técnico**: [Nome da equipe, email]
**Administrador de Dados**: [Nome, e-mail]

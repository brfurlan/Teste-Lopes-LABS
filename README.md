
### a. Como foi a deﬁnição da sua estratégia de modelagem?

<p align="justified"> 
Inicialmente, foi feita uma comparação dos três métodos de correlação: de Pearson, de Spearmen e  de Kendall. Assim,  foram destacadas as variáveis com maior módulo de correlação. Como o método de Kendall apresentou menor correlação das variáveis em comparação com os outros métodos, especialmente na variável álcool (que apresenta menor correlação em comparação com os demais métodos). Este não foi utilizado na modelagem da qualidade. Assim, foram comarados os métodos de Spearman e Pearson.</p>

<p align="justified"> Para para a modelagem nos dois métodos foram utilizados os valores máximo e mínimo das seguintes variáveis, além da variável de qualidade (utilizada para validar o modelo):</p>

1. Álcool;
2. Volatilidade da acidez;
3. Cloretos;
4. Densidade;
   
    
<p align="justified"> Para o método de Pearson foram utilizadas as variáveis álcool, volatilidade de acidez e cloretos enquanto que para o método de Spearman foram utilizadas as variáveis álcool, densidade e cloretos. Para cada uma destas variáveis, foram dados conceitos de qualidade de 0 a 10 (para correlação positiva) e de 10 a 0 (para correlação negativa). Como o valor máximo de qualidade encontrado foi de 9 e o mínimo foi de 3, foram feitos os seguintes métodos para a estimação dos conceitos das variáveis:</p>


* Foi feita a subtração do menor valor para o maior valor de cada uma das váriáveis, pelo menor valor e este foi dividido por 6 (intervalo entre o maior e o menor valor da variável qualidade) para determinar o tamanho do intervalo de dados que receberia cada conceito;
* Com o tamanho do intervalo de dados para cada variável, foram feitas as divisões de intervalos para variável e atribuidos conceitos para cada variável:de 3 a 9 para correlações positivas e de 9 a 3 para correlações negativas;
* Com a utilização de cada intervalo de dados, foram estimados os possíveis intervalos para os conceitos de 0,1,2,3 e 10;


<p align="justified">Assim, foram estimados os seguintes intervalos e conceitos para cada variável</p>

1. Álcool;

| Intervalo |       | Conceito |
|-----------|-------|----------|
| Início    | Fim   |          |
| 0         | 5,7   | 0        |
| 5,7       | 6,85  | 1        |
| 6,85      | 8     | 2        |
| 8         | 9,15  | 3        |
| 9,15      | 10,3  | 4        |
| 10,3      | 11,45 | 5        |
| 11,45     | 12,6  | 6        |
| 12,6      | 13,75 | 7        |
| 13,75     | 14,9  | 8        |
| 14,9      | 16,05 | 9        |
| <= 16,05  |       | 10       |

2. Volatilidade da acidez;

| Intervalo |      | Conceito |
|-----------|------|----------|
| Início    | Fim  |          |
| 0         | 0,08 | 10       |
| 0,08      | 0,33 | 9        |
| 0,33      | 0,58 | 8        |
| 0,58      | 0,83 | 7        |
| 0,83      | 1,08 | 6        |
| 1,08      | 1,33 | 5        |
| 1,33      | 1,58 | 4        |
| 1,58      | 1,83 | 3        |
| 1,83      | 2,08 | 2        |
| 2,08      | 2,33 | 1        |
| <= 2,33   |      | 0        |

3. Cloretos;

| Intervalo |        | Conceito |
|-----------|--------|----------|
| Início    | Fim    |          |
| 0,0000    | 0,0090 | 10       |
| 0,0090    | 0,1093 | 9        |
| 0,1093    | 0,2097 | 8        |
| 0,2097    | 0,3100 | 7        |
| 0,3100    | 0,4103 | 6        |
| 0,4103    | 0,5107 | 5        |
| 0,5107    | 0,6110 | 4        |
| 0,6110    | 0,7113 | 3        |
| 0,7113    | 0,8117 | 2        |
| 0,8117    | 0,9120 | 1        |
| <= 0,9120 |        | 0        |

4. Densidade;

| Intervalo |          | Conceito |
|-----------|----------|----------|
| Início    | Fim      |          |
| 0,0000    | 0,9871   | 10       |
| 0,9871    | 18,1389  | 9        |
| 18,1389   | 35,2907  | 8        |
| 35,2907   | 52,4426  | 7        |
| 52,4426   | 69,5944  | 6        |
| 69,5944   | 86,7462  | 5        |
| 86,7462   | 103,8980 | 4        |
| 103,8980  | 121,0498 | 3        |
| 121,0498  | 138,2016 | 2        |
| 138,2016  | 155,3534 | 1        |
| <= 155,353|          | 0        |


<p align="justified">* O final de cada intervalo é aberto</p>
<p align="justified"> Em seguida, foi feita uma cópia do banco de dados para cada método, sendo calculados os conceitos para cada variável em cada vinho e foi também feita sua qualidade estimada. O cálculo da qualidade estimada, foi feito  pela média ponderada, multiplicando cada conceito de cada variável pelo módulo da correlação da mesma e dividindo pela soma do módulo das correlações. </p>

<p align="justified"> O erro de estimação também foi calculado para cada vinho, sendo este o módulo da diferença da qualidade no banco da dados e da qualidade estimada no modelo. Assim, para a determinação do modelo mais eficaz foi considerado o que apresentou menor média de erro de estimação dentre os dois métodos e por tipo de vinho.</p>

### b. Como foi deﬁnida a função de custo utilizada?

<p align="justified"> A qualidade estimada foi definida desta maneira, pois as três variáveis com maior correlação com a variável qualidade poderiam ser mais adequadas para a modelagem. Desta forma, seria necessária uma ponderação para compensar as diferenças entre as correlações de cada variável. Por esse motivo, se optou por fazer uma média ponderada para a estimação da qualidade. </p>

### c. Qual foi o critério utilizado na seleção do modelo ﬁnal?

<p align="justified"> Assim, para a determinação do modelo com o método mais eficaz foi considerado o que apresentou menor média de erro de estimação dentre os dois métodos e por tipo de vinho.</p>

### d. Qual foi o critério utilizado para validação do modelo? Por que escolheu utilizar este método?

<p align="justified"> O erro de estimação também foi calculado para cada vinho, sendo este o módulo da diferença da qualidade no banco da dados e da qualidade estimada no modelo. Este método foi escolhido por ser simples de ser calculado e por evidenciar a diferença entre o modelo e a qualidade mostrada no banco de dados.</p>

### e. Quais evidências você possui de que seu modelo é suﬁcientemente bom?

<p align="justified"> Pois é um modelo que apresenta poucas variáveis para a estimação de um determinado modelo, embora  erro médio tenha sido coniderável, este é resultado da comparação de diferentes métodos de correlação, sendo este o que mais se adequou à proposta do que foi pedido no desafio.</p>

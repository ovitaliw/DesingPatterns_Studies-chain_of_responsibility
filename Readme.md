# Aplicação prática do Chain of Responsability #

Umas das partes mais difícies da aplicação de padrões de projeto é saber quando e 
onde cada padrão pode ser utilizado. 

Nesta série estou trazendo exemplos de problemas comuns e como utilizar algum 
padrão de projeto para resolver este problema. 

#### Validadores ####

É bastante comum passarmos por situação onde precisamos submenter algo a uma 
série de validações, onde o resultado de cada etapa da validação pode gerar 
um retorno diferente. 

Por exemplo, o pagamento de uma conta em banco precisa realizar as seguintes validações:

- A conta pode ser paga neste banco?
- A conta está no prazo ou vencida?
- Existe saldo na sua conta para pagar esta conta?

Note que para cada uma destas validações o retorno será diferente.

É estratamente comum encontramos longas listas de 'if's para resolver estes tipos de situação.
O que é horrível para qualquer sistema.

#### FizzBuzz Test ####

Para ilustrar melhor o problema e como resolve-lo vamos usar o 'FizzBuzz Test'.

O FizzBuzz é um desafio comumente utilizado em exames de entrevistas que básicamente 
consiste em dato uma lista de n número inteiros, deve-se retornar 'Fizz', 'Buzz', 'FizzBuzz' ou o 
próprio valor de acordo com as seguintes regras. 

- Para número multiplos de 3 e 5 deve-se imprimir 'FizzBuzz'
- Para multiplos de 3 deve-se imprimir 'Fizz'
- Para multiplos de 5 deve-se imprimir 'Buzz'
- Para valores não multiplos de 3 ou 5 imprimir o próprio número

Vamos ver isso em código da maneira mais simples e direta possivel [v1.0](https://github.com/ovitaliw/DesingPatterns_Studies-chain_of_responsibility/blob/1.0/fizzbuzz.py)

Note que é um algoritmo bem simples mas que reflete um problema bem comum.
Diversos 'if's encadeados para realizar uma validação sobre algo, aqui temos apenas 4 caminhos, 
mas imagine que seja necessários adicionar novas regras a esta validação, logo este método ficará 
péssimo para realizar a manutenção e entender o que realmente esta sendo feito.    
 
E é ai que entram os padrões de projetos para ajudar nas resoluções de problemas e sem 
gerar alta complexidade ciclomática para o método.   


#### Chain of responsability ####

Chain of responsability, ou CoR é um padrão de projeto comportamental onde você passa um objeto, valor, algo qualquer, 
para uma série de manipuladores ou validadores, comumente chamados de *Handlers*, encadeados que decidem se devem 
realizar o processamento do objeto ou encaminhar para o proximo handler da corrente.

Este padrão se encaixa perfeitamente para solução deste problema apresentado. 

Vamos refatorar o código anterior para utilizar este padrão.

Primeiramente vamos escrever um teste unitário simples para garantir a nossa refatoração.  



Para mais detalhes sobre o padrão recomendo ler o artigo sobre o CoR do site [Refactoring Guru](https://refactoring.guru/pt-br/design-patterns/chain-of-responsibility)
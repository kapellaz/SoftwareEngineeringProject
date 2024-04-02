# EDITAR QUIZ

`User Story #8` - Como criador, quero poder editar um quiz reprovado para que este possa ser reavaliado

### Testes:

    * Testar quando o quiz ainda não foi reprovado por pelo menos 3 revisores
    * Testar quando não existem quizzes reprovados
    * Testar quando um quiz reprovado já foi editado
    * Testar quando um quiz já está aprovado
<br/>


`Caso de Uso #1 -` Editar cada um dos detalhes de um quizz



__Ator Primário:__  Criador

__Nível:__ Objetivo do utilizador 

__Stakeholders e Interesses:__
* Criador - Quer que o seu quiz seja aprovado
* Revisor - Quer que o quiz que rejeitou seja corrigido

__Pré-condição:__ Estar logado e ser utilizador criador

__Garantia de sucesso:__ O criador consegue editar o/os quiz(zes) de forma a corrigir os erros indicados pelos revisores

__Cenário de Sucesso Principal:__

1. O utilizador criador abre a pagina onde aparecem os quizzes que criou

2. O sistema apresenta os quizzes rejeitados pelos revisores

3. O utilizador criador edita o/os quiz(zes) rejeitados

4. O utilizador criador submete para aprovação o/os quiz(zes) já editados.

5. O sistema aprova/rejeita a submissão.

__Extensões:__ 

1.a. O utilizador criador ainda não criou nenhum quiz

1a1- O sistema apresenta uma mensagem a indicar que ainda não criou nenhum quiz

2.a. O utilizador criador não tem quizzes rejeitados

2a1- O sistema apresenta uma mensagem a indicar que não tem quizzes para editar

2.b. Todos os quizzes rejeitados já foram editados

2.b.1. - O sistema apresenta uma mensagem a indicar que não tem quizzes para editar

4.a.- O utilizador criador submete um quiz para aprovação sem ter feito mudanças

4.a.1. - O sistema mostra um aviso a indicar que o quiz não pode ser submetido para aprovação se não existirem mudanças.





Grupo 4 - Escrito por Bruno Sequeira

`User Story #11` - Como revisor, quero poder aprovar/rever quizzes para poder corrigir quizzes

### Testes

_Cenário:_  Utilizador com sessão iniciada, na página de Rever Quizes

1. Testar com um utilizador que não tenha criado nenhum quiz.
2. Testar com um utilizador que não tenha permissão de revisor.
3. Testar com um revisor não fazer um comentário final acerca do quiz.
4. Testar aprovar um quiz.
4. Testar reprovar um quiz.


-----------------------------Caso de Uso-----------------------------


Caso de Uso : Rever quizzes(aprovar ou rejeitar)
Ator Primário: revisor
Nível: Objetivo do utilizador
Stakeholders e Interesses:
    revisor - Quer poder rever/aprovar quizzes.
    Pré-condição: Estar logado.
Garantia de Sucesso: O aprovador pode aprovar/rejeitar quizzes
Cenário Principal de Sucesso:
1. O sistema mostra todos os quizzes por aprovar.
2. O Utilizador aprovador clica em Rever o quiz que deseja.
3. O sistema mostra as respostas.
4. O revisor comenta todas as respostas.
5. O revisor submete o veredicto e o seu comentário final.
6. Se o quiz for aprovado e se for o 3º aprovado pelo criador este recebe a permissão de revisor.


Extensões:
2a. O utilizador não é um revisor.

    2a2. O site informa o utilizador que este não pode aprovar/rever um quiz se este não tiver colocado um quiz/(sem permissão).

5a. O utilizador não insere nenhuma justificação.

    5a1. O site informa o utilizador que não justificou a sua ação ou não comentou todas as perguntas.
    
    5a2. O utilizador vai colocar a sua justificação até todas estiverem completas.

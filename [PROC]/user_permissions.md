# Permissões de utilizadores

## Verificação de permissões

* Para verificar se um utilizador tem uma permissão específica (para ter acesso a uma certa *view*), faz-se:
    - No terminal, na pasta kahucsite (\DEV\kahucsite), para executar o script para criar os grupos, faz-se
  ```
  py manage.py shell
  exec(open('create_kahuc_groups.py').read())
  ```
    - No ficheiro das *views* ```from django.contrib.auth.decorators import permission_required```
    - Na linha acima da *view* em que se pretende verificar a permissão, adiciona-se o *
      decorator* ```@permission_required('users.{permissão}', raise_exception=True)```
    - Onde está {permissão}, insere-se a permissão que se adequa à situação:
        1. can_create_quiz
        2. can_review_quiz
        3. can_create_test
        4. can_solve_test

## Verificação de autenticação

* Para verificar se um utilizador iniciou sessão (para ter acesso a uma *view*), faz-se:
    - ```from django.contrib.auth.decorators import login_required```
    - Na linha acima da *view* em causa, adicionar o seguinte *decorator* ```@login_required```

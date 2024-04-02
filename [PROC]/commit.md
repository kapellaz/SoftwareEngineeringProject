# Práticas de commit
### As mensagens de commit devem:

* Ser escritas em **português**
* Completar sucintamente a idea "Se aplicado, este commit irá..." usando um verbo **imperativo ou **infinitivo**
* Ser curtas (50 caracteres)
* Conter o número do *issue* a qual pertencem (se aplicável) **no corpo do commit**

* Começar com "[código]", se não relacionado com desenvolvimento
	- [PROC] - alterações aos processos
	- [ARCH] - ficheiros do desenho da arquitetura
	- [DES] - ficheiros do design gráfico
	- [PM] - gestão do projeto
	- [QA] - desenvolvimento de funcionalidades de Quality Assurance
	- [REQ] - trabalho sobre os requisitos

* Se relacionado com desenvolvimento, começar com um dos seguintes tipos de commit:
	- wip:      Work in progress
	- docs:     Mudanças de documentação
	- feat:     Uma nova funcionalidade
	- fix:      Arranjou-se um bug
	- perf:     Uma mudança no código que aumenta a performance
	- refactor: Uma mudança no código que nem arranja um bug nem adiciona uma funcionalidade
	- test:     Adicionar testes ou corrigir testes existentes

* Utilizar o corpo do commit para detalhar as alterações (caso necessário)
* Referir apenas alterações da mesma área (cada commit deve ser limitado a uma área de alterações)

---

Exemplo 1:
[PM] atualiza tarefas do grupo 2  

#168

--- 

Exemplo 2:
feat: Escolhe teste para resolver

Clica no teste e redireciona para pagina do teste
...
#Issue nº REQ_6.1


## Observações
Commits atómicos - Alterações relacionadas devem ser condensadas no mesmo commit!
**Se fizerem demasiados commits seguidos relativos à mesma área, realizem um "squash commit"** 

##  Exemplos de **MÁS** mensagens de commit
* corrige erros (deve indicar quais erros foram corrigidos no corpo)
* atualiza testes de codigo (especificar quais os testes no corpo)
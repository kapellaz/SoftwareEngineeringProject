# Práticas de issues

## Template dos issues
Os issues devem ser escritos em **português**.

O título deve começar por um indicador de tema aplicável:
- [PROC] - alterações aos processos
- [ARCH] - tarefas relativas ao desenho da arquitetura
- [DES] - tarefas relativas ao design gráfico
- [DEV] - desenvolvimento do código
- [PM] - gestão do projeto
- [QA] - desenvolvimento de funcionalidades de Quality Assurance
- [REQ] - trabalho sobre os requisitos

O corpo do issue deve assumir a seguinte template, desenvolvendo os 
objetivos com detalhe suficiente e sumariando a Definition of Done em formato de checklist:
```
## Objetivos:
- tarefa detalhada
- tarefa detalhada
- ...

## DOD:
- condição final explicada sucintamente
- condição final explicada ...
- ...
```

Todos os issues devem ter as seguintes labels ao ser criados:
- `Sprint#`
- `grupo#`
- `to-do`

Uma deadline deve ser definida no campo _Due date_.

## Comportamento dos Desenvolvedores
Devem colocar uma estimativa do tempo a gastar com o comando `/estimate` nos comentários do issue.

A atividade deve ser documentada nos comentários do issue, acompanhando o progresso e atualizando regularmente o tempo gasto com o comando `/spend`.

O desenvolvedor deve pedir ao PM do seu grupo para abrir o issue com o respetivo título e DoD definidas pelo desenvolvedor e deve marcar o issue com a tag: `waiting-to-be-reviewed` quando acabar o trabalho.

## Abrir e fechar issues
A criação de cada issue é feita pelo PM do respetivo grupo.

O issue é fechado pelo deployer do respetivo grupo após revisão.

O perfil do desenvolvedor é atualizado pelos respetivos *project managers* e *deployers* colocando o # sob `Assigned` ou `Finished` (ou `Not completed` no caso de reatribuição do issue)

## Procedimento de verificação

Os *deployers* são os principais responsáveis por garantir a qualidade do trabalho desenvolvido. 

Um *deployer* **não deve** verificar os seus próprios issues. Um colega do seu grupo deverá confirmar o seu código.

## Procedimento de refactoring

Caso se verifique que :
- A funcionalidade não cumpre a DOD
- Falta de compatibilidade com o resto do programa
- Não ser possível entender claramente como usar a funcionalidade

ou no caso do código:

- Não estar devidademente documentado
- Não seguir os [padrões de linguagem](language_stds.md) definidos neste repositório

o issue será marcado com a *tag* `requires-refactoring` e o desenvolvedor terá que documentar, reformatar ou arranjar o código. O issue permanece aberto.

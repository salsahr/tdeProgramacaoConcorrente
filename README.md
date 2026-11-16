# tdeProgramacaoConcorrente

Nome do Grupo: TDE2 20

Nome dos integrantes:
Eric Tan Hui Zhen
Guilherme Hoshino Rouver
Otávio Costa Dallo

Linguagem escolhida: Python

Instrução de execução do código do Jantar dos filósofos:

Para rodar com o deadlock:
1. entrar na pasta parte1-filosofos
2. cd .\JantarFilosofoDeadlock\
3. python main.py

Para rodar sem o deadlock:
1. entrar na pasta parte1-filosofos
2. cd .\JantarFilosofosSemDeadlock\
3. python main.py

Relatório curto Jantar dos filósofos:

A dinâmica do problema do jantar dos filósofos é baseada na premissa em que tem uma mesa de jantar com um prato grande de macarrão no centro da mesa, ao redor da mesa há 5 filósofos com pratos menores e 5 garfos.
Para eles conseguirem comer a condição é que eles peguem tanto o garfo posicionado em sua esquerda quanto o garfo da direita. E é nesse momento em que surge o impasse, como existem apenas 5 garfos, se todos pegarem
ao mesmo tempo por exemplo, o garfo da esquerda, não irá sobrar nenhum garfo na direita de ninguém, logo ninguém consegue comer e todos ficam esperando. A condição de Coffman que será negada na nossa solução proposta 
é a de condição de espera circular.

Fluxograma está dentro da pasta parte1-filosofos



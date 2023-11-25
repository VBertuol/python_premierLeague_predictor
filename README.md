Para o seminário final da matéria de Sistemas Inteligentes, resolvi criar um preditor de
desempenho de um time do campeonato inglês de futebol: Premier League. A predição é feita
baseando-se nas estatísticas atuais do clube e na base de dados disponíveis do campeonato.

A minha inspiração foi o meu trabalho realizado na Atividade 3 da matéria: “Árvore
do Conhecimento do Bem e do Mal”, onde utilizei o método de árvore de decisão de
aprendizado supervisionado.

Na atividade 3, o objetivo era o algoritmo receber um filme e suas informações
relevantes e responder se aquele filme pode ser considerado um filme “bom” ou “ruim”
baseado no banco de dados de filmes assistidos por mim.

O banco de dados possuía na Atividade 3 um campo dedicado a receber minhas notas
pessoais para cada filme assistido, assim um novo campo binário era criado para classificar os
filmes como “bom” ou “ruim” a partir de uma nota arbitrária usada como fronteira de decisão.

No algoritmo criado para a Premier League o objetivo é ter como resultado final um
intervalo que representa as possíveis posições finais de um time baseando-se nas principais
estatísticas do clube em determinada rodada do campeonato.# python_premierLeague_predictor

Preditor de desempenho de um time do campeonato inglês de futebol: Premier League. A predição é feita baseando-se nas estatísticas atuais do clube e na base de dados disponíveis do campeonato. 

# natural-language-patent-classification
Classificação de resumos de patentes sobre o bioplástico PLA utilizando o Natural Language Classifier da IBM Watson. 

O desafio abordado neste projeto é a classificação de grande quantidade de patentes sobre o biolplástico Polylactic Acid (PLA) em três categorias: produto, aplicação e processo de fabricação do polímero.

- Aplicação: quando ocorre a menção à alguma aplicação possível com o desenvolvimento do objeto da patente. (ex: cápsulas com PLA para liberação controlada de medicamentos na corrente sanguínea). 
- Produto: não é citada uma aplicação específica, normalmente, relacionado ao desenvolvimento de alguma material com propriedades específicas (ex: micropartículas utilizando PLA e lisossomos em sua superfície).
- Processo de fabricação do polímero: o tema principal da patente é o processo de fabricação do polímero contendo PLA (ex: processo catalítico para produção de PLA em forma de anéis).

Como uma grande quantidade de dados está envolvida (Big Data), utilizou-se o serviço "Natural Language Classifier" da IBM Watson para interpretar e classificar o conteúdo dos resumos das patentes, após treinamento prévio (arquivo com os dados de treinamento estão neste repositório). 

Para mais informações, acesse: [https://www.ibm.com/watson/services/natural-language-classifier](https://www.ibm.com/watson/services/natural-language-classifier)

Este projeto faz parte de um trabalho maior sobre Mapeamento de Redes Sociais e Econômicas em Bioplásticos, que tem como objetivo mapear as relações entre os distintos atores no mercado mundial de Bioplásticos, utilizando a Teoria de Redes (Network Theory) e Perspectiva de Multinível (Multi-level Perspective).



# AI-number-prediction

Deploy de uma aplicação de IA em Flask que identifica dígitos de 0-9 escritos a mão. A aplicação está hospedada no Heroku.

<div>
  <a href = 'https://flask.palletsprojects.com/en/1.1.x/' target="_blank"> 
    <img alt="Flask" src="https://img.shields.io/badge/flask%20-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white"/>
  </a>
  <a href = 'https://heroku.com/' target="_blank"> 
    <img alt="Heroku" src="https://img.shields.io/badge/heroku%20-%23430098.svg?&style=for-the-badge&logo=heroku&logoColor=white"/>
  </a>
<div>

- https://ai-number-identification.herokuapp.com/

<p align="center">
  <a href = 'https://ai-number-identification.herokuapp.com/' target="_blank">
  <img width="460" height="300" src="https://github.com/gomeslucasm/AI-number-prediction/blob/master/site_img.gif">
  </a>
</p>


## Rede neural

Rede neural artificial estilo perceptron, utilizando o algoritmo de backpropagation para identificar
os dígitos escritos a mão. Para treinamento e validação, é utilizado a base de dados MNIST <a> http://yann.lecun.com/exdb/mnist/ </a>.

- <a href = "https://github.com/gomeslucasm/Deep-Learning/blob/master/Exerc_Backprop_MNIST_Lucas_Gomes.ipynb" >Notebook com o código de treinamento e validação </a>


<p align="center">
  Exemplo:
</p>

<p align="center">
  <img width="100" height="100" src="https://user-images.githubusercontent.com/44169749/96166004-c7641980-0ef3-11eb-93ec-8cfa12578646.PNG">
</p>

## To-do

- [ ] Treinamento e deploy de uma rede convolucional para comparação.

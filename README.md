# Sorting Service Challenge
Esse projeto implementa a resolução do desafio requisitado para a vaga de Estagiário de Desenvolvimento Full Stack na SumOne. Foi requisitado um sistema que ordene uma lista de livros baseado em atributos passados através de um arquivo de configuração. O repositório que descreve o desafio pode ser encontrado clicando [aqui](https://github.com/sumoners/s1-programming-challenges/tree/master/v2).

## Requisitos
+ Python 3.5.3
+ configparser 3.5.0

## Instalação de dependencias
Os pacotes necessários para a execução do código podem ser instalados utilizando um gerenciador de pacotes, como o [pip](https://pip.pypa.io/en/stable/installing/). Os pacotes estão presentes no arquivo de dependências [requirements.txt](https://github.com/JoaoFagundes/sorting-service/blob/master/requirements.txt) e portanto uma execução do comando `pip install -r requirements.txt`, do diretório raiz do repositório é o suficiente para instalá-los. Após isso, para rodar o programa o usuário basta executar o arquivo Main.py através de uma chamada simples:
```
  python Main.py
```

O usuário também pode, se quiser evitar possíveis problemas quanto às dependências, utilizar um ambiente isolado do Python, como o virtualenv.

Os livros a serem utilizados no sistema de ordenação são os presentes no arquivo [books_list.json](https://github.com/JoaoFagundes/sorting-service/blob/master/books_list.json) e caso o usuário deseje adicionar ou remover um livro, deve fazer alterando o arquivo mencionado seguindo o mesmo padrão lá presente.

## Parâmetros de ordenação
Os parâmetros para ordenação do sistema devem ser inseridos utilizando o arquivo [.config](https://github.com/JoaoFagundes/sorting-service/blob/master/.config). O arquivo possui comentários descrevendo como os atributos devem ser preenchidos, mas o padrão que segue é:
```
  params = <Atributo>_<Direção>, ...
```

sendo que Atributo pode ser:
+ Title;
+ Author;
+ Edition;

e Direção pode ser:
+ ASC;
+ DSC;

sendo que o uso de letras minúsculas ou maiúsculas não interefere no resultado.
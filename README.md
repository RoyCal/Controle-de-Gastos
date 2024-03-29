# Sistema de controle de gastos
O sistema tem como finalidade auxiliar no controle mensal de gastos. Ele possui funcionalidades que permitem ajustar a renda mensal e adicionar ou remover um gasto. A fim de praticar o roteamento de páginas, foi criada uma segunda página que permite apenas mudar
o nome do usuário.

<div align="center"> 
  <img width="500em" src="page_1.png"/>
  <img width="500em" src="page_2.png"/>
</div>

## Front-end
- Tkinter
- [Tkinter Designer][tkdesigner]
  - Tkinter Designer é um código em Python feito pela comunidade que converte automaticamente um design do Figma em código Python, utilizando a biblioteca Tkinter para design gráfico.
- [Figma][figma]

## Back-end
- Python
- MySQL

## Requirements
- Python 3.10.4
- PyMySql 1.1.0
- MySQL 8.0.34
- Dentro do MySQL você deve:
  - Criar um banco de dados com o nome "controle_gastos". Use o comando: ```CREATE DATABASE controle_gastos;```
  - Criar 3 tabelas específicas. Use os comandos a seguir: ```CREATE TABLE `controle_gastos`.`gastos` (`IdGasto` INT, `Nome` VARCHAR(45), `Valor` FLOAT, PRIMARY KEY (`IdGasto`));```, ```CREATE TABLE `controle_gastos`.`renda_mensal` (
  `renda_mensal` FLOAT);``` e ```CREATE TABLE `controle_gastos`.`user` (
  `user` VARCHAR(50));```.
  - Se esses passos não forem seguidos corretamente, o programa corre o risco de quebrar. Note que os nomes das tabelas e do banco de dados devem ser exatamente como estão nos comandos, caso contrário, serão necessárias mudanças ou no código Python, ou nos nomes em si.
- No Python você deve:
  - Se certificar de mudar a senha do seu MySQL no arquivo ```database.py```. A mudança deve ser realizada na variável iniciada na 5ª linha.
  - Se a senha não corresponder à sua senha de acesso ao MySQL, o programa não consegue se conectar ao banco de dados e quebra.

[tkdesigner]: https://github.com/ParthJadhav/Tkinter-Designer
[figma]: https://www.figma.com/

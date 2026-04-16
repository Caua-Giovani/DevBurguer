CREATE DATABASE IF NOT EXISTS DevBurguer;

USE DevBurguer;

CREATE TABLE IF NOT EXISTS hamburguers (
 codigo INTEGER auto_increment PRIMARY KEY,
 produto VARCHAR(100) NOT NULL,
 descricao VARCHAR(1000) NOT NULL,
 preco DOUBLE NOT NULL,
 destaque BOOLEAN NOT NULL,
 foto VARCHAR(1000) NOT NULL,
 disponibilidade BOOLEAN NOT NULL
);

INSERT INTO `DevBurguer`.`hamburguers`(`produto`,`descricao`,`preco`,`destaque`,`foto`,`disponibilidade`)
VALUES
("Classic Dev","Pão brioche, carne suculenta e queijo derretido.",25.00,0,"https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600",1),
("Double Stack","Dois hambúrgueres, bacon crocante e molho especial.",38.00,1,"https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=600",1),
("Veggie Script","Hambúrguer de grão de bico com salada fresca.",30.00,0,"https://images.pexels.com/photos/3219483/pexels-photo-3219483.jpeg?auto=compress&cs=tinysrgb&w=600",1),
("Java Chicken","Frango empanado crocante com alface e maionese.",28.00,1,"https://images.pexels.com/photos/12034622/pexels-photo-12034622.jpeg",1),
("Python Onion","Anéis de cebola, barbecue e queijo cheddar.",33.00,1,"https://images.pexels.com/photos/70497/pexels-photo-70497.jpeg?auto=compress&cs=tinysrgb&w=600",1),
("React Salad","Uma opção leve e reativa para o seu almoço.",27.00,0,"https://images.pexels.com/photos/1199957/pexels-photo-1199957.jpeg?auto=compress&cs=tinysrgb&w=600",1);

CREATE TABLE IF NOT EXISTS usuarios (
	codigo INTEGER auto_increment PRIMARY KEY,
    login VARCHAR(100) NOT NULL,
    senha VARCHAR(200) NOT NULL
);

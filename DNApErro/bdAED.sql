-- drop database adrian;

create database adrian;
use adrian;

-- Tabela cliente

create table Cliente(
 id int null primary key,
 nome varchar(50) not null,
 endereco varchar(100) not null,
 fornecedor varchar(50),
 email varchar(50) not null
);

-- Tabela os

create table Os(
	os int not null primary key,
    data_os timestamp not null,
    equipamento varchar(150) not null,
    defeito varchar(150) not null,
    servico varchar(150),
    tecnico varchar(30),
    valor decimal(10,2),
    idCliente int,
    foreign key (idCliente) references Cliente(id)
);


-- tabela de usuarios

create table Usuarios(
	id int not null primary key auto_increment,
    usuario varchar(50),
    fone varchar(15),
    login varchar(15),
    senha varchar(15)
);


insert into Usuarios values('',"Teste","Nao sei","testes","123");
select * from Usuarios;


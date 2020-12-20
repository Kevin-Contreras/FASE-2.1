USE proyecto;
create table administrador(
usuario varchar(40) not null,
contrasenia varchar(50) not null,
primary key (usuario)
);
insert into administrador(usuario,contrasenia) value('usuario1','123');
insert into administrador(usuario,contrasenia) value('usuario13','12e3');

select * from administrador;
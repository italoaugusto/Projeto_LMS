create table usuario (
id int identity,
login varchar(100) not null,
senha varchar(100) not null,
dt_expiracao date default '19000101',
constraint pk_usuario primary key (id),
constraint uq_login_usuario unique (login)
);
go

create table coordenador(
id int identity,
id_usuario int not null,
nome varchar(100) not null,
email varchar(100) not null,
celular varchar(60) not null,
constraint pk_coordenador primary key(id),
constraint fk_usuario_coordenador foreign key (id) references usuario(id),
constraint uq_email_coordenador unique (email),
constraint uq_celular_coordenador unique (celular)
);
go

create table aluno
(
    id int identity
    ,id_usuario int not null
    ,nome varchar(100) not null
    ,email varchar(100) not null
    ,celular varchar(100) not null
    ,ra varchar(100) not null
    ,foto varchar(200)
    ,constraint pk_aluno primary key(id)
    ,constraint fk_usuario_aluno foreign key(id) references usuario(id)
    ,constraint uq_email_aluno unique (email)
    ,constraint uq_celular_aluno unique (celular)
);
go

create table professor(
id int identity,
id_usuario int not null,
email varchar(100) not null,
celular varchar(60) not null,
apelido varchar(100) not null,
constraint pk_professor primary key(id),
constraint fk_usuario_professor foreign key (id) references usuario(id),
constraint uq_email_professor unique (email),
constraint uq_celular_professor unique (celular),
);
go

create table curso
(
id int identity
,nome varchar(100) not null
,constraint PK_curso primary key(id)
,constraint UQ_nome_curso unique(nome)
);
go

create  table disciplina(
id int identity,
nome varchar(100) not null,
data date not null constraint df_data_disciplina default (getdate()),
status varchar(7) not null constraint df_status_disciplina default ('ABERTA'),
plano_ensino varchar (255) NOT NULL,
carga_horaria int not null,
competencias varchar(100)not null,
habilidades varchar(100)not null,
ementa varchar(255) not null,
conteudo_programatico varchar(255) not null,
bibliografiabasica varchar(255)not null,
bibliografia_Complementar varchar(255)not null,
percentual_pratico tinyint not null,
percentual_teorico tinyint not null,
id_coordenador int not null,
constraint pk_disciplina primary key(id),
constraint fk_coordenador_disciplina foreign key (id_coordenador) references coordenador(id),
constraint uq_nome_disciplina unique (nome),
constraint ck_carga_horaria check(carga_horaria = 40 or carga_horaria = 80),
constraint ck_status_disciplina check(status = 'Aberta' or status = 'Fechada'),
constraint ck_percentual_teorico_disciplina check(percentual_teorico between 0 and 100),
constraint ck_percentual_pratico_disciplina check(percentual_pratico between 0 and 100)
);
go

create table disciplina_ofertada
(
	id int identity
	,id_coordenador int  not null
	,dt_inicio_matricula date
	,dt_fim_matricula date
	,id_disciplina int not null
	,id_curso int not null
	,ano date not null
	,semestre smallint not null
	,turma char(1) not null
	,id_professor int
	,metodologia varchar(255)
	,recursos varchar(255)
	,criterios_avalicao varchar(255)
	,plano_aulas varchar(255)
	,constraint pk_disciplina_ofertada primary key(id)
	,constraint fk_coordenador_disciplina_ofertada foreign key(id_coordenador) references coordenador(id)
	,constraint fk_disciplina_disciplina_ofertada foreign key(id_disciplina) references disciplina(id)
	,constraint fk_curso_disciplina_ofertada foreign key (id_curso) references curso(id)
	,constraint ck_ano check(ano between '19000101' and '21001231')
    ,constraint ck_semestre check (semestre like '[1-2]')
    ,constraint ck_turma check (turma like '[A-Z]')
    ,constraint fk_professor_disciplina_ofertada foreign key(id_professor) references professor(id)
    );
go

create table atividade
(
id int identity
,titulo varchar(255) not null
,descricao varchar(255) 
,conteudo varchar(255) not null
,tipo varchar(15) not null
,extras varchar(255) 
,id_professor int not null
,constraint pk_atividade primary key (id)
,constraint uq_titulo unique (titulo)
,constraint ck_tipo check (tipo = 'Resposta Aberta' or tipo = 'Teste')
,constraint fk_atividade_professor foreign key (id_professor) references professor(id)
);
go


create table atividade_vinculada
(
id  int identity
,id_atividade int not null
,id_professor int not null
,id_disciplina_ofertada int not null
,rotulo varchar(100) not null
,status varchar(15) not null
,dt_inicio_respostas date not null
,dt_fim_respostas date not null
,constraint PK_atividade_vinculada primary key(id)
,constraint FK_atividade foreign key(id_atividade) references atividade(id)
,constraint FK_professor_vinculado_atividade foreign key(id_professor) references professor(id)
,constraint FK_disciplina_ofertada_vinculada foreign key(id_disciplina_ofertada) references disciplina_ofertada(id)
,constraint ck_status_atividade check (status = 'Disponibilizada' or status = 'Aberta' or status = 'Fechada' or status = 'Encerrada' or status ='Prorrogada')
);
go

create table solicitacao_matricula(
id int identity,
id_aluno int not null,
id_disciplina_ofertada int not null,
dt_solicitacao date not null constraint df_dt_solicitacao default (getdate()),
id_coordenador int  not null,
status int not null constraint df_solicitacao_status default ('solicitada'), 
constraint pk_solicitacao_matricula primary key(id),
constraint fk_disciplina_ofertada_solicitacao foreign key (id_disciplina_ofertada) references disciplina_ofertada(id),
constraint fk_solicitacao_matricula_id_coordenador foreign key (id_coordenador) references coordenador(id),
constraint ck_solicitacao_status check(status = 'Solicitada' or status = 'Aprovada' or status = 'Rejeitada' or status = 'Cancelada') 
);
go

create table entrega(
id int identity,
id_aluno int not null,
id_atividade_vinculada int not null,
titulo  varchar(150) not null,
resposta varchar(1000)not null,
dt_entrega date not null constraint df_dt_entrega default (getdate()),
status varchar(9) not null constraint df_status_entrega default ('Entregue'),
id_professor int,
nota decimal(3,2),
dt_avaliacao date,
obs varchar(255),
constraint pk_entrega primary key(id),
constraint fk_aluno_entrega foreign key (id_aluno) references aluno(id),
constraint fk_atividade_entrega foreign key (id_atividade_vinculada) references atividade_vinculada(id),
constraint fk_professor_entrega foreign key (id_professor) references professor(id),
constraint ck_status check(status = 'Entregue' or status = 'Corrigido'),
constraint ck_nota check(nota between 0.00 and 10.00)
);
go

create table mensagem(
id int identity,
id_aluno  int not null,
id_professor int not null,
assunto varchar (100) not null,
referencia varchar (255)not null,
conteudo varchar (500)not null,
status varchar(10)not null constraint df_status_msg default ('Enviado'),
dt_envio datetime not null constraint df_dt_envio_msg default (getdate()),
resposta varchar (500),
dt_resposta datetime,
constraint pk_mensagem primary key(id),
constraint fk_aluno_mensagem foreign key (id_aluno) references aluno(id),
constraint fk_professor_mensagem foreign key (id_professor) references professor(id),
constraint ck_status_mensagem check(status = 'Enviado' or status = 'Lido' or status = 'Respondido')
);
go
## ADS 2E
## GABRIEL ALMEIDA DA SILVA - RA 1601551
## ORIVALDO FRANCISCO DEITOS JUNIOR - RA 1800885
## BRUNO CORREA FALANGA - RA 1800789
## WILKER GULYTH TORRES LOPES - RA 1801024
## ELAINE CRISTINA DOS SANTOS PAIVA - RA 1801149
## ITALO AUGUSTO NASCIMENTO DA ROCHA - RA 1801071

class Usuario:
    def __init(self, _login, _senha, _id):
        self.id = _id
        self.login = _login
        self.senha = _senha
        self.dtExpiracao = '19000101'

class Coordenador:
    def __init__(self, _idUsuario, _nome, _email, _celular, _id):
        self.id = _id
        self.nome = _nome
        self.email = _email
        self.celular = _celular
        self.idUsuario = _idUsuario

class Aluno:
    def __init__(self, _idUsuario, _nome, _email, _celular, _ra, _foto, _id):
        self.id = _id
        self.idUsuario = _idUsuario
        self.nome = _nome
        self.email = _email
        self.celular = _celular
        self.ra = _ra
        self.foto = None

class Professor:
    def __init__(self, _idUsuario, _email, _celular, _apelido, _id):
        self.id = _id
        self.idUsuario = _idUsuario
        self.apelido = _apelido
        self.email = _email
        self.celular = _celular

class Disciplina:
    def __init__(self, id, nome, plano_de_Ensino,carga_horaria,competencias,habilidades,ementa,conteúdo_programático,bibliografia_basica,bibliografia_complementar,percentual_pratico,percentual_teorico):
        self.id = id
        self.nome= nome
        self.plano_de_Ensino =plano_de_Ensino
        self.competencias = competencias
        self.habilidades = habilidades 
        self.ementa=ementa
        self.conteúdo_programático =conteúdo_programático
        self.bibliografia_basica = bibliografia_basica
        self.bibliografia_complementar= bibliografia_complementar
        self.percentual_pratico = percentual_pratico
        self.percentual_teorico =percentual_teorico 
        if carga_horaria >= 40 or carga_horaria <= 80:
            self.carga_horaria = carga_horaria
        else:
            self.carga_horaria =None 

class DisciplinaOfertada:
    def __init__ (self, curso, ano, semestre, turma, idCoordenador, idDisciplina, id):
        self.id = id
        self.curso = curso
        self.turma = turma
        self.idCoordenador = idCoordenador
        self.idDisciplina = idDisciplina
        self.idCurso = idCurso
        self.idProfessor = None
        self.DtInicioMatricula = None 
        self.DtFimMatricula = None
        self.Metodologia = None
        self.Recursos = None
        self.CriteriosAvaliacao = None
        self.PlanoDeAula = None
        if ano >= 1900 and ano <= 2100:
            self.ano = ano
        else:
            self.ano = None
        if semestre >= 1 or semestre <= 2:
            self.semestre = semestre
        else:
            self.semestre = None
            
class Curso:
    def __init__ (self, id, nome):
        self.id = id
        self.nome = nome

class SolicitacaoMatricula:
    def __init__(self, _idAluno, _idDisciplinaOfertada, _dtSolicitacao, _id):
        self.id = _id
        self.idAluno = _idAluno
        self.idDisciplinaOfertada = _idDisciplinaOfertada
        self.dtSolicitacao = _dtSolicitacao
        self.idCoordenador = None
        self.status = None

class Atividade:
    def __init__(self,ID,Titulo,conteudo,Tipo,idprofessor):
    self.ID = ID
    self.Titulo = Titulo
    self.Descricao = None
    self.conteudo = conteudo
    self.Tipo = Tipo
    self.Extras = None
    self.idprofessor = idprofessor

class AtividadeVinculada:
    def __init__(self,ID,IdAtividade,IdProfessor,idDisciplinaOfertada,rotulo,status,DtinicioRespostas,dtfimRespostas):
        self.ID = ID
        self.IdAtividade = IdAtividade
        self.IdProfessor = IdProfessor
        self.idDisciplinaOfertada = idDisciplinaOfertada
        self.rotulo = rotulo
        self.status = status
        self.DtinicioRespostas = DtinicioRespostas
        self.dtfimRespostas = dtfimRespostas

class Entrega:
    def __init__(self,id,Resposta,DataEntrega,Semestre,Titulo,Status, idAluno, idAtividadeVinculada):
        self.id = id
        self.idAluno = idAluno
        self.idAtividadeVinculada = idAtividadeVinculada
        self.Titulo = Titulo
        self.Resposta = Resposta
        self.DataEntrega = DataEntrega 
        self.Status = Status 
        self.idProfessor = None
        self.nota = None
        self.DtAvaliacao = None
        self.obs = None

class Mensagem:
    def __init__(self, _id, _idAluno, _idProfessor, _assunto, _ref, _conteudo, _status, _dtEnvio):
        self.id = _id
        self.idAluno = _idAluno
        self.idProfessor = _idProfessor
        self.assunto = _assunto
        self.ref = _ref
        self.conteudo = _conteudo
        self.status = _status
        self.dtEnvio = _dtEnvio
        self.dtResposta = None
        self.resposta = None
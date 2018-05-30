"""
Tabela 5 - Informacoes de uma amostra de alunos da UTFPR
Pagina 26
"""

from enum import Enum, unique

@unique
class EstadoCivilEnum(Enum):
    SOLTEIRO = 1
    CASADO = 2

@unique
class SexoEnum(Enum):
    MASCULINO = 1
    FEMININO = 2

@unique
class ReligiaoEnum(Enum):
    CATOLICA = 1
    ESPIRITA = 2
    BATISTA = 3

class Item:

    def __init__(self, estadoCivil, sexo, religiao, estaturaCm, idade):
        self.estadoCivil = estadoCivil
        self.sexo = sexo
        self.religiao = religiao
        self.estatura = estaturaCm
        self.idade = idade

def createTabela():
    item1 = Item(EstadoCivilEnum.SOLTEIRO, SexoEnum.FEMININO, ReligiaoEnum.CATOLICA, 163, 20)

    item2 = Item(EstadoCivilEnum.SOLTEIRO, SexoEnum.FEMININO, ReligiaoEnum.CATOLICA, 159, 25)

    item3 = Item(EstadoCivilEnum.CASADO, SexoEnum.MASCULINO, ReligiaoEnum.CATOLICA, 175, 19)

    item4 = Item(EstadoCivilEnum.SOLTEIRO, SexoEnum.FEMININO, ReligiaoEnum.ESPIRITA, 166, 21)

    item5 = Item(EstadoCivilEnum.SOLTEIRO, SexoEnum.MASCULINO, ReligiaoEnum.CATOLICA, 180, 23)

    item6 = Item(EstadoCivilEnum.SOLTEIRO, SexoEnum.MASCULINO, ReligiaoEnum.CATOLICA, 165, 19)

    item7 = Item(EstadoCivilEnum.CASADO, SexoEnum.FEMININO, ReligiaoEnum.BATISTA, 160, 35)

    item8 = Item(EstadoCivilEnum.SOLTEIRO, SexoEnum.FEMININO, ReligiaoEnum.CATOLICA, 156, 23)

    item9 = Item(EstadoCivilEnum.SOLTEIRO, SexoEnum.MASCULINO, ReligiaoEnum.CATOLICA, 167, 24)

    item10 = Item(EstadoCivilEnum.SOLTEIRO, SexoEnum.FEMININO, ReligiaoEnum.CATOLICA, 169, 20)

    item11 = Item(EstadoCivilEnum.CASADO, SexoEnum.MASCULINO, ReligiaoEnum.ESPIRITA, 175, 28)

    item12 = Item(EstadoCivilEnum.SOLTEIRO, SexoEnum.MASCULINO, ReligiaoEnum.CATOLICA, 173, 22)

    return [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12]

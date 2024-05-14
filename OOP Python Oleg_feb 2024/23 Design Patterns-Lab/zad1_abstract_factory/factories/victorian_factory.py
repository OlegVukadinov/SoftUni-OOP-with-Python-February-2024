from zad1_abstract_factory.factories.abstract_furniture_factory import AbstractFactory
from zad1_abstract_factory.furnitures.chair import Chair
from zad1_abstract_factory.furnitures.sofa import Sofa
from zad1_abstract_factory.furnitures.table import Table


class VictorianFactory(AbstractFactory):

    def create_sofa(self):
        return Sofa("Victorian")

    def create_chair(self):
        return Chair("Victorian")

    def create_table(self):
        return Table("Victorian")

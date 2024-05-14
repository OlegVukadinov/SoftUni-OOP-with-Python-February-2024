from zad1_abstract_factory.factories.modern_factory import ModernFactory
from zad1_abstract_factory.factories.victorian_factory import VictorianFactory

factory = VictorianFactory()

print(factory.create_sofa())
print(factory.create_table())
print(factory.create_sofa())

modern_factory = ModernFactory()
print(modern_factory.create_table())

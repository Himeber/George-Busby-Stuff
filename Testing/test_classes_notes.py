from classes_notes import Animal
def test_name():
    aminals = Animal()
    name = aminals.getname()
    assert name == "Bob"
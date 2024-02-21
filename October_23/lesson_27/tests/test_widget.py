from Hellel.October_23.lesson_25.widgets.components import ExpandableTreeElement, Button


class TestWidgets:
    def test_1(self):
        x = ExpandableTreeElement()
        y = Button()
        assert x.type_of() == "ExpandableTreeElement"
        assert y.type_of() == "Button"
# Magiya
class Element:
    combinations = {}

    def __add__(self, other):
        if not isinstance(other, Element):
            return None

        name1 = self.__class__.__name__
        name2 = other.__class__.__name__

        key = name1 + name2
        reverse_key = name2 + name1

        result = self.combinations.get(key) or self.combinations.get(reverse_key)
        return result() if result else None


class Voda(Element):
    pass


class Vozduh(Element):
    pass


class Ogon(Element):
    pass


class Zemlya(Element):
    pass


class Shtorm(Element):
    pass


class Par(Element):
    pass


class Gryaz(Element):
    pass


class Molniya(Element):
    pass


class Pyl(Element):
    pass


class Lava(Element):
    pass


class Energiya(Element):
    pass


class Plazma(Element):
    pass


Element.combinations = {
    "VodaVozduh": Shtorm,
    "VodaOgon": Par,
    "VodaZemlya": Gryaz,
    "VozduhOgon": Molniya,
    "VozduhZemlya": Pyl,
    "OgonZemlya": Lava,
    "OgonEnergiya": Plazma,
    "VozduhEnergiya": Molniya,
    "VodaEnergiya": Par,
    "ZemlyaEnergiya": Lava,
}


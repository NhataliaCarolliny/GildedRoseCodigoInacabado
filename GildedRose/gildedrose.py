import logging
logger = logging.getLogger("gildedRose")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
))

logger.addHandler(handler)

class Item:
    def __init__(self, nome: str, validade: int, qualidade: int):
        self.nome = nome
        self.validade = validade
        self.qualidade = qualidade

    def __repr__(self):
        return f"{self.nome}, {self.validade}, {self.qualidade}"           

class ItemComum:
    def atualizar_item_comum(self, item):
        item.validade -= 1

        if item.validade < 0:
            item.qualidade = max(0, item.qualidade - 2)
        else:
            item.qualidade = max(0, item.qualidade - 1)

        if item.qualidade > 50:
            item.qualidade = 50

class AgedBrie: 
    def agedBrie_excecoes(self, item):
        item.validade -= 1
        if item.validade > 0:
            item.qualidade = max(0, item.qualidade + 1)
        else:
            item.qualidade = max(0, item.qualidade + 2)
        
        if item.qualidade > 50:
            item.qualidade = 50

class Sulfuras:
    def sulfuras_excecoes(self, item):
        item.qualidade = 80

class BackstagePasses:
    def backstagePasses_excecoes(self, item):
        item.validade -= 1
        if item.validade >= 11:
            item.qualidade = max(0, item.qualidade + 1)
        elif item.validade >= 6 and item.validade <= 10:
            item.qualidade = max(0, item.qualidade + 2)
        elif item.validade >= 0 and item.validade <= 5:
            item.qualidade = max(0, item.qualidade + 3)
        else:
            item.qualidade = 0

        if item.qualidade > 50:
            item.qualidade = 50

class Conjurado:  
    def conjurado_excesoes(self, item):
        item.validade -= 1
        if item.validade > 0:
            item.qualidade = max(0, item.qualidade - 2)
        else:
            item.qualidade = max(0, item.qualidade - 4)
        
        if item.qualidade > 50:
            item.qualidade = 50
            
class GildedRose:
    def __init__(self, itens: list[Item]):
        self.itens = itens
        self.itemComum = ItemComum()
        self.agedBrie = AgedBrie()
        self.sulfuras = Sulfuras()
        self.backstagePasses = BackstagePasses()
        self.conjurado = Conjurado()

    def atualiza_itens(self):
        for item in self.itens:
            if item.nome == "Aged Brie":
                self.agedBrie.agedBrie_excecoes(item)
            
            elif item.nome == "Sulfuras" or item.nome == "Sulfuras vencido":
                self.sulfuras.sulfuras_excecoes(item)
            
            elif item.nome == "Backstage passes":
                self.backstagePasses.backstagePasses_excecoes(item)
            
            elif item.nome == "Conjurado":
                self.conjurado.conjurado_excesoes(item)
            
            else:
                self.itemComum.atualizar_item_comum(item)

if __name__ == "__main__":
    itens = [
        Item("Espada normal", validade=10, qualidade=20),
        Item("Aged Brie", validade=2, qualidade=0),
        Item("Espada vencida", validade=0, qualidade=7),
        Item("Sulfuras", validade=0, qualidade=80),
        Item("Sulfuras vencido", validade=-1, qualidade=80),
        Item("Backstage passes", validade=15, qualidade=20),
        Item("Backstage passes", validade=10, qualidade=49),
        Item("Backstage passes", validade=5, qualidade=49),
        Item("Conjurado", validade=-2, qualidade=5)
    ]
    rose = GildedRose(itens)
    logger.info("Dia 0:")
    for item in rose.itens:
        logger.info(f"{item}")
    rose.atualiza_itens()
    logger.info("\nDia 1:")
    for item in rose.itens:
        logger.info(f"{item}")

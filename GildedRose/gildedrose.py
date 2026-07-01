"""
Projeto Final - Gilded Rose Refactoring Kata (versão completa)

Você é responsável pela manutenção do sistema de uma loja chamada
"Gilded Rose". A loja vende todo tipo de itens, e o sistema precisa
atualizar a qualidade e validade dos itens diariamente.

O dono da loja, Allison, escreveu uma especificação (em REGRAS_DE_NEGOCIO.md)
e um código que funciona, mas é difícil de manter. Allison quer adicionar
um novo tipo de item ("Conjurado"), mas tem medo de quebrar tudo.

Sua missão completa está em INSTRUCOES_PROJETO_FINAL.md.

NÃO modifique a classe Item nem suas propriedades, Allison não tem
permissão (a classe é da empresa Goblin que fornece o pacote).
"""
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
        """ Faz alterações nos itens que não tem exceções.

        Args:
            item (string): Identifica o objeto que vai ser alterado.
        
        Returns:
            O item atualizado, alterando a validade e a qualidade.
            Item comum tem a validade dimunuída todos os dias, e quando a validade está vencida(<0) tem a qualidade diminuida em -2, e quando a validade é maior que 0 a qualidade é diminuida em -1.
            A qualidade nunca é negativa e nem maior que 50.
        """
        item.validade -= 1

        if item.validade < 0:
            item.qualidade = max(0, item.qualidade - 2)
        else:
            item.qualidade = max(0, item.qualidade - 1)

        if item.qualidade > 50:
            item.qualidade = 50

class AgedBrie: 
    def agedBrie_excecoes(self, item):
        """ Faz alterações no item Aged Brie com suas respectivas exceções.

        Args:
            item (string): Identifica o objeto que vai ser alterado.
        
        Returns:
            O item atualizado, alterando a validade e a qualidade.
            Aged Brie tem a validade dimunuída todos os dias, quando a validade é maior que 0 a qualidade aumenta +1, e quando a validade é menor que 0 a qualidade aumenta +2.
            A qualidade nunca é negativa e nem maior que 50.
        """
        item.validade -= 1
        if item.validade > 0:
            item.qualidade = max(0, item.qualidade + 1)
        else:
            item.qualidade = max(0, item.qualidade + 2)
        
        if item.qualidade > 50:
            item.qualidade = 50

class Sulfuras:
    def sulfuras_excecoes(self, item):
        """ Faz alterações no item Sulfuras/Sulfuras vencido com suas respectivas exceções.

        Args:
            item (string): Identifica o objeto que vai ser alterado.
        
        Returns:
            O item mantem a validade e a qualidade sem alterações.
            Tem qualidade fixa em 80.
        """
        item.qualidade = 80

class BackstagePasses:
    def backstagePasses_excecoes(self, item):
        """ Faz alterações no item Backstage Passes com suas respectivas exceções.

        Args:
            item (string): Identifica o objeto que vai ser alterado.
        
        Returns:
            O item atualizado, alterando a validade e a qualidade.
            Backstage Passes tem a validade dimunuída todos os dias, quando a validade está vencida (<0) a qualidade é igual a 0, 
            quando a validade é entre 5 e 0 a qualidade é aumentada em +3, 
            quando a validade é entre 10 e 6 a qualidade é aumentada em +2 
            e quando a validade é maior que 11 a qualidade é aumentada em +1.
            A qualidade nunca é negativa e nem maior que 50.
        """
        item.validade -= 1
        if item.validade < 0:
            item.qualidade = 0
        elif item.validade < 5:
            item.qualidade = max(0, item.qualidade + 3)
        elif item.validade < 10:
            item.qualidade = max(0, item.qualidade + 2)
        else:
            item.qualidade = max(0, item.qualidade + 1)

        if item.qualidade > 50:
            item.qualidade = 50

class Conjurado:  
    def conjurado_excesoes(self, item):
        """ Faz alterações no item Conjurado com suas respectivas exceções.

        Args:
            item (string): Identifica o objeto que vai ser alterado.
        
        Returns:
            O item atualizado, alterando a validade e a qualidade.
            Conjurado tem a validade dimunuída todos os dias, quando a validade é maior que 0 a qualidade é diminuída em -2,
            e quando a validade está vencida (<0) a qualidade é diminuída em -4.
            A qualidade nunca é negativa e nem maior que 50.
        """
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
        """ Faz a escolha do item e direciona para a classe/função correspondente
        
        Returns:
            De acordo com o item escolhido pode direcionar para a classe/função AgedBrie(agedBrie_excecoes), Sulfuras(sulfuras_excecoes), BackstagePasses(backstagePasses_excecoes), Conjurado(conjurado_excesoes) e ItemComum(atualizar_item_comum)
        """
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

# Code Smells do código anterior
# Magic Number: Número "solto" no código sem explicação, por exemplo "<50", ">0", "<6", "+1"
# Long Parameter List: Função com muitos parâmetros

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

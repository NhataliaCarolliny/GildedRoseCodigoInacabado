import pytest
from gilded_rose_completo import GildedRose, Item

def test_regras_gerais_de_qualidade_e_validade_dos_itens():
    # Arrange(prepara)
    itens = [
        Item("Espada normal", validade=10, qualidade=20), 
        Item("Espada vencida", validade=-1, qualidade=4)
        #A qualidade de um item nunca é negativa e nunca é maior que 50.
    ]
    rose = GildedRose(itens)

    # Act (executa)
    rose.atualiza_itens()

    #Assert (verifica)
    assert itens[0].validade == 9
    assert itens[0].qualidade == 19
    assert itens[1].validade == -2 # Após o vencimento a
    assert itens[1].qualidade == 2 # qualidade degrada duas vezes mais rápido.
    #Ao final de cada dia, o sistema diminui ambos os valores (validade e qualidade) de cada item.

def test_excecoes_item_Aged_Brie():
    # Arrange(prepara)
    itens = [
        Item("Aged Brie", validade=2, qualidade=0),
        Item("Aged Brie", validade=-1, qualidade=2)
    ]
    rose = GildedRose(itens)

    # Act (executa)
    rose.atualiza_itens()

    #Assert (verifica)
    assert itens[0].validade == 1
    assert itens[0].qualidade == 1 #Aumenta sua qualidade quanto mais velho fica
    assert itens[1].validade == -2
    assert itens[1].qualidade == 4 #Após o vencimento, aumenta o dobro

def test_excecoes_item_sulfuras():
    # Arrange(prepara)
    itens = [
        Item("Sulfuras", validade=1, qualidade=80)
        #Sua qualidade é fixa em 80
    ]
    rose = GildedRose(itens)

    # Act (executa)
    rose.atualiza_itens()

    #Assert (verifica)
    assert itens[0].validade == 1
    assert itens[0].qualidade == 80
    #Nunca diminui qualidade nem validade

def test_excecoes_item_backstage_passes():
    # Arrange(prepara)
    itens = [
        Item("Backstage passes", validade=20, qualidade=1),
        Item("Backstage passes", validade=9, qualidade=2),
        Item("Backstage passes", validade=4, qualidade=3),
        Item("Backstage passes", validade=0, qualidade=4)
    ]
    rose = GildedRose(itens)

    # Act (executa)
    rose.atualiza_itens()

    #Assert (verifica)
    #Aumenta a qualidade conforme a data do show se aproxima
    assert itens[0].validade == 19
    assert itens[0].qualidade == 2 #11 ou mais dias antes: ganha 1 de qualidade por dia.
    assert itens[1].validade == 8
    assert itens[1].qualidade == 4 #10 a 6 dias antes: ganha 2 de qualidade por dia.
    assert itens[2].validade == 3
    assert itens[2].qualidade == 6 #5 a 0 dias antes: ganha 3 de qualidade por dia.
    assert itens[3].validade == -1
    assert itens[3].qualidade == 0 #Após o show (validade < 0): qualidade vira 0.

def test_excecao_item_conjurado():
    # Arrange(prepara)
    itens = [
        Item("Conjurado", validade=3, qualidade=10),
        Item("Conjurado", validade=-1, qualidade=5)
    ]
    rose = GildedRose(itens)

    # Act (executa)
    rose.atualiza_itens()

    #Assert (verifica)
    assert itens[0].validade == 2
    assert itens[0].qualidade == 8 #Antes do vencimento: perdem 2 de qualidade por dia.
    assert itens[1].validade == -2
    assert itens[1].qualidade == 1 #Após o vencimento: perdem 4 de qualidade por dia.
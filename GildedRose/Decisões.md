# Projeto Gilded Rose
## Decisões importantes

- **Implementação dos testes:**
    
    Foi feito testes para todos os itens do código de acordo com as Regras de Negócio.

    *Teste unitário* :
    ```bash
    python -m pytest -v
    ```
    ```bash
    test_regras_gerais_de_qualidade_e_validade_dos_itens PASSED [20%]

    test_excecoes_item_Aged_Brie PASSED [40%]

    test_excecoes_item_sulfuras PASSED [60%]

    test_excecoes_item_backstage_passes PASSED [80%]

    test_excecao_item_conjurado PASSED [100%]
    ```
    *Teste de cobertura* :
    ```bash
    python -m pytest --cov
    ```
    ```bash
    Name                      Stmts   Miss  Cover
    ---------------------------------------------
    gilded_rose_completo.py     81     14    83%
    tests\test_gilded_rose.py   44      0   100%
    ---------------------------------------------
    TOTAL                      125     14    89%
    ```
- **Identificação de Code Smells:**

    Foi encontrado dois tipos de code smells (Magic Number e Long Parameter List).

    *Magic Number* : Número "solto" no código sem explicação, por exemplo "<50", ">0", "<6", "+1"
    
    *Long Parameter List* : Função com muitos parâmetros

- **Adicionado Logging:**

    O *logger.info* foi colocado para exibir os itens. Confirmando que as coisas estão funcionando como esperado no fluxo normal do programa.
    
    Exemplo:
    ```python
    logger.info("Dia 0:")
    logger.info(f"{item}")
    ```

- **Refatoração:**

    A refatoração foi feita para facilitar o entendimento do código, retirando o aninhamento de *if - else*. O polimorfismo foi colocado em prática.
    
    Foram criadas novas classes e funções para cada item, onde os itens normais (que não tem exceções) são representados pela classe *ItemComum* e função *atualizar_item_comum* e os itens com exceções (Aged Brie, Sulfuras, Backstage Passes e Conjurado) foram colocados em classes e funções separadas.
    ```python
    class ItemComum:
        def atualizar_item_comum(self, item):

    class AgedBrie: 
        def agedBrie_excecoes(self, item):

    class Sulfuras:
        def sulfuras_excecoes(self, item):
    
    class BackstagePasses:
        def backstagePasses_excecoes(self, item):

    class Conjurado:  
        def conjurado_excesoes(self, item):
    ```
    Uma classe/função foi criada para escolher a destinação dos itens para sua função correspondente

    ```python
    class GildedRose:
        def __init__(self, itens: list[Item]):
            self.itens = itens
            self.itemComum = ItemComum()
            self.agedBrie = AgedBrie()
            self.sulfuras = Sulfuras()
            self.backstagePasses = BackstagePasses()
            self.conjurado = Conjurado()

        def atualiza_itens(self):
    ```

- **Adicionado o item "Conjurado":**

    Nas Regras de Negócio foi exigida a adição de um novo item com suas respectivas especificações, que foi colocado no código e também feito o teste para esse item.

    ```python
    class Conjurado:  
        def conjurado_excesoes(self, item):
    ```
    ```python
    def test_excecao_item_conjurado():
    ```

# Exemplo de estratégia de Divisão e Conquista

def merge_sort(unsorted: list) -> list:
    """
    Função que que recebe uma lista não ordenada, então
    usando o conceito de "divisão e conquista" fará
    a divisão da lista em sublistas, até que reste
    somente 1 elemento na lista. Ao mesmo tempo fica
    responsável por invocar a função merge, que irá
    juntar os elementos de forma ordenada.
    """

    ...

def merge(first: list, second: list):
    """
    Função que junta as listas de forma ordenada"
    """
    index1 = index2 = 0
    elements = []

    while index1 < len(first) and index2 < len(second):
        if first[index1] < second[index2]:
            elements.append(first[index1])

unsorted = [10,1,20,3,5,2,18,0]
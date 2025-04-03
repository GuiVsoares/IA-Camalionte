# Busca Binária

def search(array, start, end, key):
    while start  <= end:
        # dividir o array no meio
        mid = start + (end - start) // 2
        
        # verificar se o elemento foi encontrado
        if array[mid] == key:
            return mid

        elif array[mid] < key:
            start = mid + 1

        else:
            end = mid - 1

    return "Elemento não encontrado"

array = [4,6,9,13,14,18,21,24,38]
key = 18

result = search(array, 0, len(array ) -1 , key)
print(result)
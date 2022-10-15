import sys

from collections import Counter, OrderedDict
from numpy import sort

def main() -> int:
    lista = { "item 1" : 1.23, 
              "item 2" : 361.23, 
              "item 3" : 414.23, 
              "item 4" : 5461.2243, 
              "item 5" : 2213.23, 
              "item 6" : 1332.23, 
              "item 7" : 431.23, 
              "item 8" : 13.22, 
              "item 9" : 2.94,
              "item 10" : 7.301 }
        
    lista_primeiro_digito = sort(list(map(lambda valor: str(valor)[0], lista.values())))
    lista_contagem_primeiro_digito = dict(OrderedDict(Counter(lista_primeiro_digito)))
    itens_lista = len(lista_primeiro_digito)
    
    print("Dicionário: %s" % (lista))
    print("Primeiros dígitos dos valores do dicionário: %s" % (lista_primeiro_digito))
    print("Contagem dos primeiros dígitos: %s" % (lista_contagem_primeiro_digito))
    print("Total de itens no dicionário: %s" % (itens_lista))
    
    resultado_analise = {}
    
    for digito in lista_contagem_primeiro_digito:
        resultado_analise[digito[0]] = lista_contagem_primeiro_digito.get(digito[0]) / itens_lista
        
    print("Resultado da análise do dicionário: %s" % (resultado_analise))
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

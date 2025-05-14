"""
Proje
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""
from collections.abc import Iterable

# Aşağıdaki işlem hem dış listenin hem de iç içe listelerin her seviyedeki elemanlarının tersine çevrilmesini gerektirir. Yani işlem hem derin hem de yüzeysel bir tersine çevirme işlemi yapar.

def deep_reverse(lst):
    result = []
    for item in reversed(lst):
        if isinstance(item, list):
            result.append(deep_reverse(item))
        else:
            result.append(item)
    return result

# Aşağıdaki işlem  iç içe listeleri açarak tüm elemanları tek bir liste  haline getirir.

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


# Aşağıdaki işlem verilen bir yapıyı flatten etmek; içinde ne varsa (liste, tuple, string, dict, set…) tüm iç içe yapıları açarak tek bir düz liste haline getirmek.

def flatten(data):
    result = []
    
    if isinstance(data, dict):
        # Sadece dict'in değerlerini flatten ediyoruz (anahtarları da isterseniz ekleyebilirim)
        for value in data.values():
            result.extend(flatten(value))
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            result.extend(flatten(item))
    elif isinstance(data, str):
        for char in data:
            result.append(char)
    elif isinstance(data, Iterable) and not isinstance(data, (str, bytes)):
        for item in data:
            result.extend(flatten(item))
    else:
        result.append(data)
    
    return result

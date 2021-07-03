# Declaración de un diccionario
diccionario = dict()

# Devuelve el numero de elementos que tiene el diccionario
len(dict)

# Compara el número de elementos distintos que tienen los dos 
cmp (dict1,dict2)

# Devuelve una lista con las claves del diccionario
dict.keys()

# Devuelve una lista con los valores del diccionario
dict.values()

# Devuelve el valor del elemento con clave key. Sino devuelve default
dict.get(key, default=None)

# Inserta un elemento en el diccionario clave:valor. Si la clave existe no lo inserta
dict.setdefault(key, default=None)

# Insertamos un elemento en el diccionario con su clave:valor
dict['key'] = 'value'

# Eliminamos el elemento del diccionario con clave key
dict.pop('key',None)

# Devuleve la copia de un diccionario dict2 = dict.copy()
dict.copy()

# Elimina todos los elementos de un diccionario
dict.clear()

# Crea un nuevo diccionario poniendo como claves las que hay en la lista y los valores por defecto si se les pasa
dict.fromkeys(list, defaultValue)

# Devuelve true si existe la clave. Sino devuelve false
dict.has_key(key)

# devuelve un lista de tuplas formadas por los pares clave:valor
dict.items()

# Añade los elementos de un diccionario a otro
dict.update(dict2)

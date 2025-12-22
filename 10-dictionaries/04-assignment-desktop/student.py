def desktop(catalog, components):

    total_price=0

    for item in components:
        if item in catalog:
            total_price+=catalog[item]
        else:
            raise ValueError("not in list hoe")
    return total_price

catalog = {
    'Intel Core i7 13700K': 439,
    'Intel Core i5 13600K': 331,
    'Gigabyte Z790 AORUS ELITE AX': 261,
    'MSI MAG Z790 TOMAHAWK WIFI': 279,
    'Corsair DDR5 Vengeance 2x16GB 5600': 95,
    'Corsair DDR5 Vengeance 2x32GB 5600': 165,
    'MSI GeForce RTX 4070 VENTUS 3X 12G OC GPU': 659,
    'Gigabyte GeForce RTX 4090 GAMING OC 24G GPU': 1849,
}
    
components = [
     'Intel Core i7 13700K',
     'Gigabyte GeForce RTX 4090 GAMING OC 24G GPU',
     'Corsair DDR5 Vengeance 2x32GB 5600',
]

print(desktop(catalog,components))
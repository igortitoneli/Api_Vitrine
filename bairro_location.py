import geopy

bairros_list = [
        "Boa Vista",
        "Bom Pastor",
        "Centro",
        "Granbery",
        "Jardim Glória",
        "Santa Helena",
        "São Mateus",
        "Teixeiras",
        "Bairu",
        "Bonfim",
        "Botanágua",
        "Centenário",
        "Cesário Alvim",
        "Grajaú",
        "Linhares",
        "Manoel Honório",
        "Marumbi",
        "Nossa Senhora Aparecida",
        "Progresso",
        "Santa Rita",
        "Santa Cândida",
        "São Benedito",
        "São Bernardo",
        "Vitorino Braga",
        "Eldorado",
        "Granjas Betânea",
        "Jardim Bom Clima",
        "Mariano Procópio",
        "Grama",
        "Jardim Emaús",
        "Parque Independência",
        "Santa Therezinha",
        "Filgueiras",
        "Vale dos Bandeirantes",
        "Barbosa Lage",
        "Barreira do Triunfo",
        "Benfica",
        "Milho Branco",
        "Carlos Chagas",
        "Cerâmica",
        "Esplanada",
        "Francisco Bernardino",
        "Industrial",
        "Jardim Natal",
        "Jóquei Clube",
        "Nova Era",
        "Paula Lima",
        "Remonta",
        "Represa",
        "Santa Cruz",
        "São Dimas",
        "Vila Esperança",
        "Aeroporto",
        "Borboleta",
        "Cruzeiro Santo Antônio",
        "Martelos",
        "Morro do Imperador",
        "Nova Califórnia",
        "Novo Horizonte",
        "São Pedro",
        "Serro Azul",
        "Barão do Retiro",
        "Floresta",
        "Nossa Senhora de Lourdes",
        "Santo Antônio",
        "Vila Furtado de Menezes",
        "Vila Olavo Costa",
        "Niterói",
        "Costa Carvalho",
        "Bomba de Fogo",
        "Cascatinha",
        "Graminha",
        "Ipiranga",
        "Jardim Laranjeiras",
        "Sagrado Coração de Jesus",
        "Salvaterra",
        "Santa Efigênia",
        "Santa Luzia",
        "São Geraldo",
      ]

location_dict = {}

for bairro in bairros_list:
    geolocator = geopy.geocoders.Nominatim(user_agent="geolocalização")
    location = geolocator.geocode(bairro + ', Juiz de Fora - MG')
    
    try:
        lat = location.latitude
        lon = location.longitude
        location_dict[bairro]={
            'latitude': lat,
            'logitude': lon,
        }
        print(bairro + ', Juiz de Fora - MG.')

    except:
        print(bairro + ', não funciona.')


print(location_dict)
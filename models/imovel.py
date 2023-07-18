class ImovelModel:
    
    def __init__(self, tipo, preco, m2, quatos, banheiros, vagas, condominio, iptu, latitude, longitude):
        self.tipo = tipo
        self.preco = preco
        self.m2 = m2
        self.quatos = quatos
        self.banheiros = banheiros
        self.vagas = vagas
        self.condominio = condominio
        self.iptu = iptu
        self.latitude = latitude
        self.longitude = longitude

    def json(self):
        return {
            'tipo': self.tipo,
            'preco': self.preco,
            'm2': self.m2,
            'quatos': self.quatos,
            'banheiros': self.banheiros,
            'vagas': self.vagas,
            'condominio': self.condominio,
            'iptu': self.iptu,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

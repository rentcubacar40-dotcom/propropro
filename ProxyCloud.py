def parse(text):
    """
    Compatibilidad: Devuelve string si es string, dict si es necesario
    """
    if not text:
        return None
    
    # Si ya es string usable
    if isinstance(text, str):
        text = text.strip()
        if not text:
            return None
        
        # Si ya tiene protocolo, devolver string directo
        if text.startswith(('socks4://', 'socks5://', 'http://', 'https://')):
            return text  # ← ¡STRING, no dict!
        
        # Si no tiene protocolo, agregar socks5://
        return f'socks5://{text}'
    
    # Si es dict, mantenerlo (para compatibilidad)
    if isinstance(text, dict):
        return text
    
    # Cualquier otro caso
    return str(text) if text else None


class ProxyCloud:
    def __init__(self, ip, port, type='socks5'):
        self.ip = ip
        self.port = port
        self.type = type
    
    @staticmethod
    def parse(text):
        return parse(text)
    
    def as_dict_proxy(self):
        return {
            'http': f'{self.type}://{self.ip}:{self.port}',
            'https': f'{self.type}://{self.ip}:{self.port}'
        }

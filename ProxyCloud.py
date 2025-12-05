"""
ProxyCloud.py - Módulo para manejar proxies en el bot de Moodle
Versión simplificada sin encriptación
"""

def parse(text):
    """
    Convierte string de proxy a formato requests
    
    Ejemplos de entrada:
      "socks5://190.6.65.2:1080"
      "http://45.61.139.148:8080"
      "190.6.65.2:1080"  (asume socks5)
      "" o None  (devuelve None)
    
    Salida:
      {'http': 'socks5://190.6.65.2:1080', 'https': 'socks5://190.6.65.2:1080'}
      o None si no hay proxy
    """
    # 1. Verificar si hay contenido
    if text is None:
        return None
    
    # 2. Convertir a string y limpiar
    proxy_str = str(text).strip()
    
    # 3. Si está vacío, devolver None
    if not proxy_str:
        return None
    
    # 4. Si ya es un dict, devolverlo (compatibilidad)
    if isinstance(text, dict):
        return text
    
    # 5. Asegurar que tiene protocolo
    # Lista de protocolos válidos
    valid_protocols = ['socks4://', 'socks5://', 'http://', 'https://']
    
    has_protocol = any(proxy_str.startswith(p) for p in valid_protocols)
    
    if not has_protocol:
        # No tiene protocolo, agregar socks5:// por defecto
        proxy_str = f'socks5://{proxy_str}'
    
    # 6. Devolver dict para requests
    return {
        'http': proxy_str,
        'https': proxy_str
    }


# Clase para compatibilidad (si algún código la usa)
class ProxyCloud:
    def __init__(self, ip, port, type='socks5'):
        self.ip = ip
        self.port = port
        self.type = type
    
    @staticmethod
    def parse(text):
        """Método estático compatible"""
        return parse(text)
    
    def as_dict_proxy(self):
        """Convierte objeto a dict"""
        return {
            'http': f'{self.type}://{self.ip}:{self.port}',
            'https': f'{self.type}://{self.ip}:{self.port}'
        }

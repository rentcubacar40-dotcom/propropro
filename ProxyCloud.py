class ProxyCloud(object):
    def __init__(self, ip, port, type='socks5'):
        self.ip = ip
        self.port = port
        self.type = type
    
    def as_dict_proxy(self):
        return {
            'http': f'{self.type}://{self.ip}:{self.port}',
            'https': f'{self.type}://{self.ip}:{self.port}'
        }


def parse(text):
    """
    VERSIÓN QUE SÍ FUNCIONA - Devuelve DICT directamente
    Compatible con AMBOS: main.py y MoodleClient
    """
    if not text:
        return None
    
    try:
        text_str = str(text).strip()
        if not text_str:
            return None
        
        print(f"[ProxyCloud] Parseando: '{text_str}'")
        
        # Si YA es dict, devolverlo (compatibilidad)
        if isinstance(text, dict):
            return text
        
        # Si YA es objeto ProxyCloud, convertirlo a dict
        if hasattr(text, 'as_dict_proxy'):
            return text.as_dict_proxy()
        
        # Determinar protocolo
        if text_str.startswith('socks4://'):
            protocol = 'socks4'
            rest = text_str[9:]  # Quitar "socks4://"
        elif text_str.startswith('socks5://'):
            protocol = 'socks5'
            rest = text_str[9:]  # Quitar "socks5://"
        elif text_str.startswith('http://'):
            protocol = 'http'
            rest = text_str[7:]  # Quitar "http://"
        elif text_str.startswith('https://'):
            protocol = 'https'
            rest = text_str[8:]  # Quitar "https://"
        else:
            protocol = 'socks5'
            rest = text_str
        
        # Extraer IP:puerto SIN intentar desencriptar
        if ':' in rest:
            ip, port_str = rest.split(':', 1)
            try:
                port = int(port_str)
            except:
                port = 1080
        else:
            ip = rest
            port = 1080
        
        # ✅ DEVOLVER DICT (lo que MoodleClient necesita)
        result = {
            'http': f'{protocol}://{ip}:{port}',
            'https': f'{protocol}://{ip}:{port}'
        }
        
        print(f"[ProxyCloud] Resultado: {result}")
        return result
        
    except Exception as e:
        print(f"[ProxyCloud] Error: {e}")
        # Fallback: si todo falla, devolver string como dict
        if text and isinstance(text, str):
            return {'http': text, 'https': text}
    
    return None

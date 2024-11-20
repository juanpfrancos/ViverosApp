import requests
import json
from typing import Dict, List

class TrelloAutomation:
    def __init__(self, api_key: str, token: str):
        self.api_key = api_key
        self.token = token
        self.base_url = "https://api.trello.com/1"
        
    def create_card(self, list_id: str, name: str, desc: str, labels: List[str] = None) -> Dict:
        """
        Crea una tarjeta en Trello
        """
        url = f"{self.base_url}/cards"
        params = {
            'key': self.api_key,
            'token': self.token,
            'idList': list_id,
            'name': name,
            'desc': desc
        }
        
        if labels:
            params['idLabels'] = labels
            
        response = requests.post(url, params=params)
        return response.json()

def main():
    # Reemplazar con tus credenciales de Trello
    API_KEY = "80b3706914e1de82766c153be3851d74"
    TOKEN = "4455db36fe82683ccc03edc350b9eca66d240c7cf29baf2ef4b47d112f98b8d3"
    LIST_ID = "ID_DE_LA_LISTA"  # ID de la lista donde quieres crear las tarjetas
    
    trello = TrelloAutomation(API_KEY, TOKEN)
    
    # Estructura de las historias de usuario y sus commits
    historias = {
        "Gestión de Productores": {
            "descripcion": """Como administrador, quiero registrar y gestionar los datos de los Productores para tener información detallada y actualizada de cada uno.
            
Rama: feature/gestion-productores

Commits:
- Inicializar módulo para la gestión de Productores
- Crear modelo de datos para Productores
- Implementar formulario para registrar y editar Productores
- Añadir servicio para manejo de Productores
- Implementar interfaz para listar y buscar Productores""",
        },
        "Gestión de Fincas y Viveros": {
            "descripcion": """Como administrador, quiero registrar y asociar Fincas y Viveros a los Productores para tener una estructura jerárquica y organizada de los datos.
            
Rama: feature/gestion-fincas-viveros

Commits:
- Inicializar módulo para la gestión de Fincas y Viveros
- Crear modelo de datos para Fincas y Viveros
- Implementar formulario para registrar y editar Fincas y Viveros
- Añadir lógica para asociar Fincas y Viveros con un Productor
- Implementar vista para listar Fincas y sus Viveros asociados""",
        },
        "Registro de Labores en Viveros": {
            "descripcion": """Como administrador, quiero registrar las Labores realizadas en cada Vivero, con sus descripciones y fechas, para llevar un seguimiento detallado de las actividades agrícolas.
            
Rama: feature/registro-labores

Commits:
- Inicializar módulo para la gestión de Labores
- Crear modelo de datos para Labores
- Implementar formulario para registrar Labores en un Vivero
- Añadir lógica para listar y filtrar Labores por Vivero
- Implementar validaciones en las fechas de registro de las Labores""",
        },
        "Gestión de Productos de Control": {
            "descripcion": """Como administrador, quiero registrar y gestionar los Productos de Control asociados a las Labores para garantizar un adecuado seguimiento y cumplimiento de regulaciones.
            
Rama: feature/gestion-productos-control

Commits:
- Crear modelos de datos para los Productos de Control
- Añadir lógica específica según el tipo de producto
- Implementar formulario para registrar y editar Productos de Control
- Vincular Productos de Control con las Labores
- Implementar vista para listar y detallar Productos de Control registrados""",
        }
    }
    
    # Crear tarjetas para cada historia
    for titulo, datos in historias.items():
        trello.create_card(
            list_id=LIST_ID,
            name=titulo,
            desc=datos["descripcion"]
        )
        print(f"Tarjeta creada: {titulo}")

if __name__ == "__main__":
    main()
import json
import os

FILE_PATH = "products.json"


def _load_data():
    """Carga productos desde JSON"""
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)


def _save_data(data):
    """Guarda productos en JSON"""
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)


def create_product(product):
    """Crear producto"""
    data = _load_data()
    data.append(product)
    _save_data(data)
    return product


def read_products():
    """Leer productos"""
    return _load_data()


def update_product(product_id, new_data):
    """Actualizar producto"""
    data = _load_data()

    for product in data:
        if product.get("id") == product_id:
            product.update(new_data)
            _save_data(data)
            return product

    return None


def delete_product(product_id):
    """Eliminar producto"""
    data = _load_data()

    new_data = [p for p in data if p.get("id") != product_id]

    if len(new_data) == len(data):
        return False

    _save_data(new_data)
    return True
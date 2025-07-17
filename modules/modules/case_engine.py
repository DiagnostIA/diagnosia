import json

def load_case(filepath):
    """Charge le fichier JSON contenant le cas clinique"""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def get_node(case_data, node_key):
    """Retourne le nœud actuel du scénario"""
    return case_data.get(node_key, None)

import json


# ==============================================================================
# Funções Auxiliares
# ==============================================================================

def load_json_file(filepath):
    """Carrega um arquivo JSON e retorna seu conteúdo como um dicionário Python."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERRO: Arquivo não encontrado em '{filepath}'")
        return None
    except json.JSONDecodeError:
        print(f"ERRO: O arquivo '{filepath}' não é um JSON válido.")
        return None


def find_element_by_id(elements, id_short):
    """
    Encontra um submodelo recursivamente em uma lista de elementos pelo seu idShort.
    """
    for element in elements:
        if element.get('idShort') == id_short:
            return element
        # Se for uma coleção, busca recursivamente dentro dela
        if element.get('modelType') == 'SubmodelElementCollection':
            found = find_element_by_id(element.get('value', []), id_short)
            if found:
                return found
    return None


# ==============================================================================
# Funções de Lógica Principal
# ==============================================================================

def check_service_compatibility(requester_data, provider_data):
    """
    Verifica a compatibilidade entre requisitante e provedor.
    Retorna True se compatível, False caso contrário.
    """
    try:
        requester_elements = requester_data.get('submodelElements', [])
        provider_elements = provider_data.get('submodelElements', [])

        # 1. Validação de Profundidade (Depth)
        req_depth_val = float(find_element_by_id(requester_elements, 'RequiredDepth')['value'])
        prov_min_depth_val = float(find_element_by_id(provider_elements, 'MinDepth')['value'])
        prov_max_depth_val = float(find_element_by_id(provider_elements, 'MaxDepth')['value'])
        if not (prov_min_depth_val <= req_depth_val <= prov_max_depth_val):
            return False

        # 2. Validação de Torque
        req_torque_val = float(find_element_by_id(requester_elements, 'RequiredTorque')['value'])
        prov_min_torque_val = float(find_element_by_id(provider_elements, 'MinTorque')['value'])
        prov_max_torque_val = float(find_element_by_id(provider_elements, 'MaxTorque')['value'])
        if not (prov_min_torque_val <= req_torque_val <= prov_max_torque_val):
            return False

        # 3. Validação das Coordenadas
        screwing_points = find_element_by_id(requester_elements, 'ScrewingPoints')['value']
        limits = {
            'X': (float(find_element_by_id(provider_elements, 'MinLimitX')['value']),
                  float(find_element_by_id(provider_elements, 'MaxLimitX')['value'])),
            'Y': (float(find_element_by_id(provider_elements, 'MinLimitY')['value']),
                  float(find_element_by_id(provider_elements, 'MaxLimitY')['value'])),
            'Z': (float(find_element_by_id(provider_elements, 'MinLimitZ')['value']),
                  float(find_element_by_id(provider_elements, 'MaxLimitZ')['value'])),
        }
        for point in screwing_points:
            point_coords = {
                'X': float(find_element_by_id(point['value'], 'ScrewingCoordX')['value']),
                'Y': float(find_element_by_id(point['value'], 'ScrewingCoordY')['value']),
                'Z': float(find_element_by_id(point['value'], 'ScrewingCoordZ')['value']),
            }
            for axis, coord in point_coords.items():
                min_limit, max_limit = limits[axis]
                if not (min_limit <= coord <= max_limit):
                    return False

        # Se todas as verificações passaram
        return True
    except (TypeError, KeyError) as e:
        print(f"ERRO: Chave ou elemento não encontrado no JSON durante a verificação de compatibilidade. Detalhe: {e}")
        return False


def validate_ai_response(ai_response_data, expected_capability):
    """
    Valida se a resposta da IA corresponde à realidade calculada.
    """
    print("\n--- Validando a Resposta da IA ---")

    ai_result = ai_response_data.get("result", {})
    ai_is_capable = ai_result.get("capable")

    if ai_is_capable is None:
        print("FALHA: Não foi possível encontrar a chave 'capable' no JSON de resposta da IA.")
        return False

    print(f"Resultado real da compatibilidade: {expected_capability}")
    print(f"Resultado reportado pela IA:      {ai_is_capable}")

    if expected_capability == ai_is_capable:
        print(f"SUCESSO: A resposta da IA corresponde à realidade.")
        return True
    else:
        print(f"FALHA: A resposta da IA contradiz a realidade.")
        return False


# ==============================================================================
# Bloco de Execução Principal
# ==============================================================================
if __name__ == "__main__":
    # Nomes dos arquivos de entrada
    requester_file = 'requester-base.json'
    provider_file = 'provider-base.json'
    ai_response_file = 'ai-response.json'

    # Carregar todos os arquivos JSON
    requester_json = load_json_file(requester_file)
    provider_json = load_json_file(provider_file)
    ai_response_json = load_json_file(ai_response_file)

    # Executar a lógica apenas se todos os arquivos forem carregados com sucesso
    if requester_json and provider_json and ai_response_json:

        # 1. Calcular a verdade absoluta (Ground Truth)
        print("--- Calculando a Compatibilidade Real (Ground Truth) ---")
        is_truly_compatible = check_service_compatibility(requester_json, provider_json)

        # 2. Validar a resposta da IA contra a verdade absoluta
        validation_passed = validate_ai_response(ai_response_json, is_truly_compatible)

        print("\n--- Teste de Metavalidação Finalizado ---")
        if validation_passed:
            print("Resultado Final: A IA avaliou a situação CORRETAMENTE.")
        else:
            print("Resultado Final: A IA avaliou a situação INCORRETAMENTE.")
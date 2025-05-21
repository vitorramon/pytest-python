import pytest
from database_manager import DatabaseManager, Cliente

"""
Desenvolva os 3 casos de teste propostos:

Teste para verificar se a inclusão falha com dados inválidos

Teste para verificar se cliente existe no banco de dados

Teste para testar a função de atualização de clientes

Utilize uma fixture com a conexão com o banco de dados!

Estudar o código e entende-lo faz parte da atividade!

Boa atividade!
"""

"""
Perguntas dessa tarefa
Por que utilizamos testes parametrizados para a função de inclusão de clientes e como eles contribuem para a eficácia dos testes automatizados?

Como a fixture poderia ser implementada para configurar o caminho do banco de dados nos testes, e quais são os benefícios de usar essa abordagem? Que tipo de fixture seria mais adequada?

No teste de atualização de cliente, como você garantiria que a atualização foi realmente efetiva no banco de dados e não apenas na camada de abstração da aplicação?
"""

@pytest.fixture
def db_connection():
    try:
        db_connection = DatabaseManager(db_file='users.db')
        db_connection.create_connection()
        yield db_connection
        db_connection.conn.close()
    except Exception as e:
        print(f"Erro ao criar a conexão com o banco de dados: {e}")
        pytest.fail("Falha na configuração da fixture de conexão com o banco de dados.")
    finally:
        db_connection.conn.close()
        print("Conexão com o banco de dados fechada.")

# Teste para verificar se a inclusão falha com dados inválidos

@pytest.mark.parametrize("cliente_invalido", [
    Cliente(
        nome=5,
        email="email_invalido",
        telefone="telefone_invalido",
        endereco="endereco_invalido",
        cidade="cidade_invalida",
        estado="estado_invalido",
        cep="cep_invalido",
        datacadastro="2023-10-01",
        datanascimento="2023-10-01"
    )])
def test_incluir_cliente_invalido(db_connection, cliente_invalido):
    cliente = cliente_invalido
    resultado = db_connection.incluir_cliente(cliente)
    assert resultado == "Falha na validação dos dados do cliente.", "A inclusão de cliente inválido não falhou como esperado."
    print("Teste de inclusão de cliente inválido passou com sucesso.")

# Teste para verificar se cliente existe no banco de dados
@pytest.mark.parametrize("cliente_valido", [
    Cliente("John Doe" \
    "", "johndoe@example.com", "1234567890", "1234 Elm Street", "Springfield", "SP", "12345-678", "2023-03-15", "1990-01-01")])
def test_verificar_cliente_existe(db_connection, cliente_valido):
    # Adiciona o cliente ao banco de dados
    db_connection.incluir_cliente(cliente_valido)
    
    # Verifica se o cliente existe
    id_cliente = 1
    cliente_encontrado = db_connection.verificar_cliente(id_cliente)
    assert cliente_encontrado is not None, "Cliente não encontrado no banco de dados."
    assert cliente_encontrado[1] == cliente_valido.nome, "O nome do cliente encontrado não corresponde ao esperado."
    print("Teste de verificação de cliente existente passou com sucesso.")

# Teste para testar a função de atualização de clientes
@pytest.mark.parametrize("cliente_existente", [
    Cliente("John Doe" \
    "", "johndoe@example.com", "1234567890", "1234 Elm Street", "Springfield", "SP", "12345-678", "2023-03-15", "1990-01-01")])
def test_atualizar_cliente(db_connection, cliente_existente):
    # Adiciona o cliente ao banco de dados
    db_connection.incluir_cliente(cliente_existente)
    
    # Atualiza o cliente
    id_cliente = 1
    campo_atualizar = "nome"
    novo_valor = "John Smith"
    resultado = db_connection.atualizar_cliente(id_cliente, campo_atualizar, novo_valor)
    assert resultado is not None, "Erro ao atualizar o cliente."
    # Verifica se a atualização foi efetiva
    cliente_atualizado = db_connection.verificar_cliente(id_cliente)
    assert cliente_atualizado[1] == novo_valor, "O nome do cliente atualizado não corresponde ao esperado."
    print("Teste de atualização de cliente passou com sucesso.")
    
    
"""
Por que utilizamos testes parametrizados para a função de inclusão de clientes e como eles contribuem para a eficácia dos testes automatizados?

Os testes parametrizados são utilizados para executar uma função de teste múltiplas vezes com diferentes conjuntos de dados. No caso da função de inclusão de clientes, o uso de testes parametrizados permite verificar a robustez da função incluir_cliente em várias situações inválidas sem a necessidade de escrever múltiplos testes individuais. Isso aumenta a cobertura dos testes, assegurando que a função se comporta conforme esperado em uma variedade de cenários inválidos, como dados nulos, e-mails mal formatados ou datas inválidas. Ao identificar falhas específicas em potencial nos dados de entrada, esses testes ajudam a garantir que a aplicação se mantenha estável e confiável diante de entradas incorretas.

Como a fixture poderia ser implementada para configurar o caminho do banco de dados nos testes, e quais são os benefícios de usar essa abordagem? Que tipo de fixture seria mais adequada?

As fixtures no pytest são utilizadas para configurar um ambiente de teste; elas podem ser configuradas para executar código antes e depois dos testes, proporcionando um contexto necessário para os testes serem executados. Implementar uma fixture de módulo para configurar o caminho do banco de dados ajudaria a centralizar a configuração do banco de dados em um único lugar, tornando os testes mais limpos e fáceis de manter. Além disso, essa abordagem beneficia a reutilização de código e a separação de preocupações, já que a configuração do banco de dados é mantida separadamente dos casos de teste, permitindo que os testes se concentrem na lógica que está sendo testada. As fixtures podem ser usadas para criar um novo banco de dados antes de cada teste e destruí-lo depois, garantindo que cada teste seja executado em um ambiente isolado e consistente.

No teste de atualização de cliente, como você garantiria que a atualização foi realmente efetiva no banco de dados e não apenas na camada de abstração da aplicação?

Para garantir que a atualização foi efetiva no banco de dados, é importante não apenas confiar no valor de retorno da função de atualização, mas também verificar o estado atual do banco de dados após a execução do teste. Após chamar o método atualizar_cliente, podemos executar uma nova consulta ao banco de dados para recuperar o cliente atualizado e verificar se os campos relevantes foram modificados conforme esperado. Isso pode ser feito através da execução de uma função de consulta direta após a atualização ou reutilizando o método verificar_cliente para obter os dados atualizados do cliente. Comparando os valores recuperados com os valores esperados, podemos confirmar que a atualização teve efeito no banco de dados, validando assim a eficácia do teste de atualização.
    """
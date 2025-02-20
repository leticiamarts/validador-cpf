# Validador de CPF em Python

## Descrição
Este projeto implementa uma função para validação de CPF em Python, garantindo que o CPF fornecido atenda aos seguintes critérios:

- Deve ser uma string.
- Deve conter apenas dígitos numéricos.
- Deve ter exatamente 11 dígitos.

Além disso, o projeto inclui testes automatizados utilizando **pytest** para validar o funcionamento da função.

## Estrutura do Projeto
```
/
|-- modules/
|   |-- cpf.py  # Implementação da função validar_cpf
|-- tests/
|   |-- test_cpf.py  # Testes unitários usando pytest
|-- README.md  # Documentação do projeto
|-- requirements.txt  # Dependências do projeto
```

## Instalação
1. Clone o repositório:
```sh
git clone https://github.com/leticiamarts/validador-cpf.git
cd validador-cpf
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```sh
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```sh
pip install -r requirements.txt
```

## Uso
O arquivo `cpf.py` contém a função **`validar_cpf(cpf: str) -> bool`** que pode ser utilizada da seguinte forma:

```python
from modules.cpf import validar_cpf

cpf = "12345678901"
if validar_cpf(cpf):
    print("CPF válido!")
```

## Testes
Os testes unitários foram escritos seguindo a estrutura **Arrange, Act e Assert**. Para executá-los, basta rodar:
```sh
pytest tests/
```

Se todos os testes passarem, você verá uma saída semelhante a:
```
==================== test session starts ====================
collected 6 items

tests/test_cpf.py ......                                     [100%]

==================== 6 passed in 0.12s ====================
```

## Exemplo de Teste
Aqui está um exemplo de um dos testes presentes no projeto:
```python
import pytest
from modules.cpf import validar_cpf

def test_validarCpf_quandoCpfValido_retornaSucesso():
    """Testa um CPF válido com 11 dígitos numéricos."""
    # Arrange
    cpf = "12345678901"
    
    # Act
    resultado = validar_cpf(cpf)
    
    # Assert
    assert resultado is True
```

## Contribuição
Sinta-se à vontade para abrir **issues** ou enviar **pull requests** para melhorias e correções.



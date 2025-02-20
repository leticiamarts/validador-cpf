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

def test_validarCpf_quandoCpfContemLetras_retornaValueError():
    """Testa um CPF contendo letras, esperando um ValueError."""
    # Arrange
    cpf = "1234A678901"

    # Act & Assert
    with pytest.raises(ValueError, match="O CPF deve conter apenas números."):
        validar_cpf(cpf)

def test_validarCpf_quandoCpfCurto_retornaValueError():
    """Testa um CPF muito curto (menos de 11 dígitos), esperando um ValueError."""
    # Arrange
    cpf = "12345"

    # Act & Assert
    with pytest.raises(ValueError, match="O CPF deve conter exatamente 11 dígitos."):
        validar_cpf(cpf)

def test_validarCpf_quandoCpfLongo_retornaValueError():
    """Testa um CPF muito longo (mais de 11 dígitos), esperando um ValueError."""
    # Arrange
    cpf = "123456789012345"

    # Act & Assert
    with pytest.raises(ValueError, match="O CPF deve conter exatamente 11 dígitos."):
        validar_cpf(cpf)

def test_validarCpf_quandoCpfNaoString_retornaTypeError():
    """Testa um CPF que não é string, esperando um TypeError."""
    # Arrange
    cpf = 12345678901  # Número inteiro em vez de string

    # Act & Assert
    with pytest.raises(TypeError, match="O CPF deve ser uma string."):
        validar_cpf(cpf)

def test_validarCpf_quandoCpfContemCaracteresEspeciais_retornaValueError():
    """Testa um CPF formatado com caracteres especiais, esperando um ValueError."""
    # Arrange
    cpf = "123.456.789-01"

    # Act & Assert
    with pytest.raises(ValueError, match="O CPF deve conter apenas números."):
        validar_cpf(cpf)


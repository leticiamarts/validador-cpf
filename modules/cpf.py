def validar_cpf(cpf: str) -> bool:
    """Verifica se um CPF contém exatamente 11 dígitos numéricos.
    
    Args:
        cpf (str): O CPF a ser validado.

    Returns:
        bool: True se o CPF for válido, caso contrário, levanta uma exceção.

    Raises:
        TypeError: Se o CPF não for uma string.
        ValueError: Se o CPF não contiver apenas números ou não tiver exatamente 11 dígitos.
    """
    if not isinstance(cpf, str):
        raise TypeError("O CPF deve ser uma string.")
    
    if not cpf.isdigit():
        raise ValueError("O CPF deve conter apenas números.")
    
    if len(cpf) != 11:
        raise ValueError("O CPF deve conter exatamente 11 dígitos.")
    
    return True


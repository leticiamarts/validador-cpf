def validar_cpf(cpf: str) -> bool:
    """Verifica se um CPF contém exatamente 11 dígitos numéricos."""
    if not isinstance(cpf, str):
        raise TypeError("O CPF deve ser uma string.")
    
    if not cpf.isdigit():
        raise ValueError("O CPF deve conter apenas números.")
    
    if len(cpf) != 11:
        raise ValueError("O CPF deve conter exatamente 11 dígitos.")
    
    return True


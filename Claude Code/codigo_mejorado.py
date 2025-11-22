def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.
    
    Args:
        notas (list): Lista de valores numéricos
        
    Returns:
        float: El promedio de las notas
        
    Raises:
        ValueError: Si la lista está vacía o contiene valores no numéricos
    """
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía")
    
    if not all(isinstance(n, (int, float)) for n in notas):
        raise ValueError("Todas las notas deben ser números")
    
    return sum(notas) / len(notas)


if __name__ == "__main__":
    notas = [3.5, 4.0, 2.8, 3.9]
    print(f"Promedio: {calcular_promedio(notas):.2f}")
def add(a, b):
    """Sabira dva broja."""
    return a + b

def subtract(a, b):
    """Oduzima b od a."""
    return a - b

def multiply(a, b):
    """Množi dva broja."""
    return a * b

def divide(a, b):
    """Deli a sa b."""
    if b == 0:
        raise ValueError("Deljenje sa nulom nije dozvoljeno.")
    return a / b

def power(a, b):
    """Računa a na stepen b."""
    return a ** b 
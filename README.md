# Python Calculator

Jednostavna Python biblioteka za osnovne matematičke operacije koja demonstrira CI/CD pipeline.

## Funkcionalnosti

- Sabiranje (`add`)
- Oduzimanje (`subtract`)
- Množenje (`multiply`)
- Deljenje (`divide`)
- Stepenovanje (`power`)

## Instalacija

```bash
git clone https://github.com/YOUR_USERNAME/ci-pipeline-test.git
cd ci-pipeline-test
pip install -r requirements.txt
```

## Korišćenje

```python
from calculator import add, subtract, multiply, divide, power

# Sabiranje
result = add(5, 3)  # Rezultat: 8

# Oduzimanje
result = subtract(10, 4)  # Rezultat: 6

# Množenje
result = multiply(3, 4)  # Rezultat: 12

# Deljenje
result = divide(8, 2)  # Rezultat: 4

# Stepenovanje
result = power(2, 3)  # Rezultat: 8
```

## Testiranje

Pokrenite testove korišćenjem `pytest`:

```bash
pytest
```

## CI/CD Pipeline

Ovaj projekat koristi GitHub Actions za implementaciju CI/CD pipeline-a sa sljedećim koracima:

1. **Test** - Pokreće linting i testove
   - Linting sa flake8
   - Testovi sa pytest
2. **Build** - Simulira proces izgradnje (build)
3. **Deploy** - Simulira deployment u staging okruženje

GitHub Actions workflow je definisan u `.github/workflows/main.yml`.

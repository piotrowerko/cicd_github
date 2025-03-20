# CI/CD Example with GitHub Actions

Ten projekt pokazuje podstawowe użycie GitHub Actions w celu automatycznego
uruchamiania testów jednostkowych w Pythonie.

## Pliki

- **hello.py** - Moduł z funkcją `greet`.
- **test_hello.py** - Testy jednostkowe korzystające z `unittest`.
- **.github/workflows/ci.yml** - Konfiguracja GitHub Actions, uruchamiająca testy po każdym pushu lub w pull requestach.

## Uruchomienie testów lokalnie

```bash
pip install -r requirements.txt
python -m unittest discover -v


ci-cd-example/
├── .github/
│   └── workflows/
│       └── ci.yml
├── hello.py
├── test_hello.py
├── requirements.txt
└── README.md


---

### 5. `ci.yml` (w katalogu `.github/workflows/`)

który:

1. Uruchamia się przy każdym `push` i `pull_request` na branchu `main`.
2. Klonuje repozytorium na maszynie wirtualnej.
3. Instaluje Pythona 3.11 (możesz zmienić wersję na inną).
4. Instaluje zależności z `requirements.txt`.
5. Uruchamia testy wykorzystując `unittest`.
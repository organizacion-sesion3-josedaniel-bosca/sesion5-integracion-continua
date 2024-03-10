# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import par

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestParClass:

    # Test para la operación suma
    def test_par(self):
        assert par(1) == 1
        assert par(2) == 0

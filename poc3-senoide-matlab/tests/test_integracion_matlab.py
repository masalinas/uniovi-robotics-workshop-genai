import pytest
from senoide_matlab.puente_matlab import generar_senoide_via_matlab, cerrar_engine

@pytest.fixture(scope="module", autouse=True)
def teardown_matlab():
    # Asegura que el engine se cierre al terminar los tests
    yield
    cerrar_engine()

@pytest.mark.matlab
def test_generacion_real_matlab():
    t, y = generar_senoide_via_matlab(amplitud=1.0, frecuencia=1.0, color='r', mostrar_grafico=False)
    
    assert len(t) == 1000
    assert len(y) == 1000
    # y[0] debe ser 0 porque sin(0) = 0
    assert abs(y[0]) < 1e-10

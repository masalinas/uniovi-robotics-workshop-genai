from unittest.mock import MagicMock, patch
import pytest

# Usamos patch para evitar que el import falle si no hay matlabengine
@patch("senoide_matlab.puente_matlab.get_engine")
def test_llama_a_generar_senoide_con_los_parametros_correctos(mock_get_engine):
    mock_engine = MagicMock()
    mock_get_engine.return_value = mock_engine
    
    # Simulamos el valor de retorno de MATLAB (vectores de 1xN)
    mock_engine.generar_senoide.return_value = ([0.0, 0.1, 0.2], [0.0, 1.0, 0.0])

    from senoide_matlab.puente_matlab import generar_senoide_via_matlab
    
    t, y = generar_senoide_via_matlab(amplitud=2.0, frecuencia=1.0, color="r", mostrar_grafico=False)

    # Verificamos que se llamó a MATLAB con los tipos correctos
    mock_engine.generar_senoide.assert_called_once_with(2.0, 1.0, "r", False, nargout=2)
    
    assert t == [0.0, 0.1, 0.2]
    assert y == [0.0, 1.0, 0.0]

@patch("senoide_matlab.puente_matlab.get_engine")
def test_traduce_errores_matlab(mock_get_engine):
    mock_engine = MagicMock()
    mock_get_engine.return_value = mock_engine
    
    # Simulamos un error genérico
    mock_engine.generar_senoide.side_effect = Exception("MATLAB error")
    
    from senoide_matlab.puente_matlab import generar_senoide_via_matlab, MatlabExecutionError
    
    with pytest.raises(MatlabExecutionError, match="Fallo al ejecutar generar_senoide en MATLAB: MATLAB error"):
        generar_senoide_via_matlab(amplitud=2.0, frecuencia=1.0, color="r")

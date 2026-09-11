import logging
import os
import sys

# La dependencia de MATLAB se encapsula aquí.
try:
    import matlab.engine
except ImportError:
    matlab = None

class MatlabExecutionError(Exception):
    """Excepción lanzada cuando ocurre un error dentro de la ejecución de MATLAB."""
    pass

_engine = None

def get_engine():
    """
    Arranca el engine de MATLAB de forma perezosa (solo cuando se necesita)
    y lo reutiliza en llamadas posteriores.
    
    Arrancar el engine toma varios segundos, por lo que no debe hacerse por cada llamada.
    """
    global _engine
    if matlab is None:
        raise RuntimeError("El paquete 'matlabengine' no está instalado. No se puede arrancar el engine.")
        
    if _engine is None:
        logging.info("Arrancando MATLAB Engine (esto puede tardar unos segundos)...")
        _engine = matlab.engine.start_matlab()
        
        # Añadir la carpeta 'matlab' al path de MATLAB para que encuentre nuestra función
        matlab_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "matlab")
        _engine.addpath(matlab_dir, nargout=0)
        logging.info("MATLAB Engine listo.")
        
    return _engine

def cerrar_engine():
    """Cierra la instancia actual del engine de MATLAB."""
    global _engine
    if _engine is not None:
        _engine.quit()
        _engine = None

def generar_senoide_via_matlab(amplitud: float, frecuencia: float, color: str, mostrar_grafico: bool = False) -> tuple[list[float], list[float]]:
    """
    Delega a MATLAB la generación de los puntos de la señal senoidal.
    
    Args:
        amplitud: Amplitud de la señal.
        frecuencia: Frecuencia de la señal.
        color: Color para la gráfica.
        mostrar_grafico: Indica si MATLAB debe mostrar la figura.
        
    Returns:
        Una tupla (t, y) con las listas de tiempo y amplitud, respectivamente.
        
    Raises:
        MatlabExecutionError: Si hay un error en la ejecución dentro de MATLAB.
    """
    # En un caso real, aquí primero llamaríamos a validar_parametros
    eng = get_engine()
    
    try:
        # Llamar a la función generar_senoide en MATLAB
        # nargout=2 indica que esperamos dos valores de retorno (t, y)
        t, y = eng.generar_senoide(float(amplitud), float(frecuencia), color, bool(mostrar_grafico), nargout=2)
        
        # t y y pueden ser arrays de MATLAB. Los convertimos a listas anidadas
        # y extraemos la primera fila (ya que MATLAB devuelve vectores fila o columna 2D).
        t_lista = t[0] if isinstance(t, matlab.double) else t
        y_lista = y[0] if isinstance(y, matlab.double) else y
        
        return list(t_lista), list(y_lista)
        
    except Exception as e:
        # Capturamos el error críptico de matlabengine y lo relanzamos con contexto
        raise MatlabExecutionError(f"Fallo al ejecutar generar_senoide en MATLAB: {e}") from e

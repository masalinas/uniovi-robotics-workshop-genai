import argparse
import sys
import logging
from senoide_matlab.parametros import validar_parametros
from senoide_matlab.puente_matlab import generar_senoide_via_matlab, cerrar_engine, MatlabExecutionError

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main():
    parser = argparse.ArgumentParser(description="Generador de Señal Senoidal usando MATLAB")
    parser.add_argument("--amplitud", type=float, default=2.5, help="Amplitud de la señal")
    parser.add_argument("--frecuencia", type=float, default=1.0, help="Frecuencia de la señal (Hz)")
    parser.add_argument("--color", type=str, default="r", help="Color de la línea en MATLAB (ej: r, g, b)")
    parser.add_argument("--no-grafico", action="store_true", help="Si se especifica, no se muestra la gráfica en MATLAB")

    args = parser.parse_args()

    try:
        # 1. Validar parámetros en Python puro
        validar_parametros(args.amplitud, args.frecuencia, args.color)
        
        # 2. Llamar a MATLAB para calcular y opcionalmente dibujar
        mostrar = not args.no_grafico
        logging.info(f"Generando senoide: amplitud={args.amplitud}, frecuencia={args.frecuencia}, color='{args.color}'")
        
        t, y = generar_senoide_via_matlab(args.amplitud, args.frecuencia, args.color, mostrar_grafico=mostrar)
        
        logging.info(f"Señal generada con éxito. {len(t)} puntos calculados.")
        
        if mostrar:
            logging.info("La figura se está mostrando en MATLAB. Presiona ENTER para salir y cerrar el motor...")
            input()
            
    except ValueError as e:
        logging.error(f"Error de validación: {e}")
        sys.exit(1)
    except MatlabExecutionError as e:
        logging.error(f"Error en MATLAB: {e}")
        sys.exit(1)
    finally:
        # 3. Cerrar el engine de MATLAB de forma segura
        cerrar_engine()

if __name__ == "__main__":
    main()

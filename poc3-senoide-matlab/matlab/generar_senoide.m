function [t, y] = generar_senoide(amplitud, frecuencia, color, mostrarGrafico)
% GENERAR_SENOIDE Genera los vectores de tiempo y amplitud para una onda senoidal.
% 
% [t, y] = generar_senoide(amplitud, frecuencia, color, mostrarGrafico)
% 
% Entradas:
%   amplitud       - Amplitud de la señal (escalar > 0)
%   frecuencia     - Frecuencia de la señal (escalar > 0)
%   color          - Carácter con el color de la señal (e.g., 'r', 'b')
%   mostrarGrafico - Valor lógico (true/false) para dibujar la señal
%
% Salidas:
%   t - Vector de tiempo (1 fila, 1000 columnas)
%   y - Vector con los valores de la onda (1 fila, 1000 columnas)
%
% Ejemplo de uso:
%   [t, y] = generar_senoide(2.5, 1.0, 'r', true);

    % Generar el vector de tiempo de 0 a 2*pi (1000 puntos para resolución)
    numPuntos = 1000;
    t = linspace(0, 2*pi, numPuntos);
    
    % Calcular los valores de la función seno
    y = amplitud * sin(2 * pi * frecuencia * t);
    
    % Dibujar si se solicita
    if mostrarGrafico
        figure;
        plot(t, y, color, 'LineWidth', 1.5);
        title(sprintf('Señal Senoidal (Amplitud: %.1f, Frecuencia: %.1f Hz)', amplitud, frecuencia));
        xlabel('Tiempo (s)');
        ylabel('Amplitud');
        grid on;
        
        % Forzar el dibujado inmediato para que se vea si es llamado desde engine
        drawnow;
    end
end

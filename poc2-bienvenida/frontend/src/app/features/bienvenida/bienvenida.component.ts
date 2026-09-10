import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { BienvenidaService } from '../../core/services/bienvenida.service';

@Component({
  selector: 'app-bienvenida',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './bienvenida.component.html',
  styleUrl: './bienvenida.component.scss',
})
export class BienvenidaComponent {
  private bienvenidaService = inject(BienvenidaService);

  // Signals para gestionar el estado del componente
  nombre = signal<string>('');
  mensaje = signal<string>('');
  estado = signal<'inicial' | 'cargando' | 'error'>('inicial');

  enviar() {
    if (!this.nombre().trim()) {
      return;
    }

    this.estado.set('cargando');
    this.mensaje.set('');

    this.bienvenidaService.saludar({ nombre: this.nombre() }).subscribe({
      next: (response) => {
        this.mensaje.set(response.mensaje);
        this.estado.set('inicial');
      },
      error: () => {
        this.estado.set('error');
      },
    });
  }
}

import { Component } from '@angular/core';
import { BienvenidaComponent } from './features/bienvenida/bienvenida.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [BienvenidaComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'frontend';
}

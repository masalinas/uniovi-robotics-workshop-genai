import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BienvenidaComponent } from './bienvenida.component';
import { BienvenidaService } from '../../core/services/bienvenida.service';
import { of, throwError } from 'rxjs';

describe('BienvenidaComponent', () => {
  let component: BienvenidaComponent;
  let fixture: ComponentFixture<BienvenidaComponent>;
  let mockBienvenidaService: jasmine.SpyObj<BienvenidaService>;

  beforeEach(async () => {
    mockBienvenidaService = jasmine.createSpyObj('BienvenidaService', [
      'saludar',
    ]);

    await TestBed.configureTestingModule({
      imports: [BienvenidaComponent],
      providers: [
        { provide: BienvenidaService, useValue: mockBienvenidaService },
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(BienvenidaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('debería crearse correctamente', () => {
    expect(component).toBeTruthy();
  });

  it('debería mostrar el mensaje de éxito tras llamar al servicio', () => {
    mockBienvenidaService.saludar.and.returnValue(
      of({ mensaje: 'Respuesta simulada' }),
    );

    component.nombre.set('Usuario');
    component.enviar();

    expect(component.estado()).toBe('inicial');
    expect(component.mensaje()).toBe('Respuesta simulada');
  });

  it('debería manejar el error si falla la petición', () => {
    mockBienvenidaService.saludar.and.returnValue(
      throwError(() => new Error('API Error')),
    );

    component.nombre.set('Usuario');
    component.enviar();

    expect(component.estado()).toBe('error');
    expect(component.mensaje()).toBe('');
  });
});

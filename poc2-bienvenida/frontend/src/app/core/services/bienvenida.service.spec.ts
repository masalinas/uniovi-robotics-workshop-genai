import { TestBed } from '@angular/core/testing';
import {
  HttpTestingController,
  provideHttpClientTesting,
} from '@angular/common/http/testing';
import { provideHttpClient } from '@angular/common/http';
import { BienvenidaService } from './bienvenida.service';
import { BienvenidaResponse } from '../models/bienvenida.model';

describe('BienvenidaService', () => {
  let service: BienvenidaService;
  let httpTestingController: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [provideHttpClient(), provideHttpClientTesting()],
    });
    service = TestBed.inject(BienvenidaService);
    httpTestingController = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpTestingController.verify();
  });

  it('debería enviar una petición POST para saludar', () => {
    const mockResponse: BienvenidaResponse = {
      mensaje: '¡Hola, Test! Bienvenido a la PoC2.',
    };

    service.saludar({ nombre: 'Test' }).subscribe((response) => {
      expect(response).toEqual(mockResponse);
    });

    const req = httpTestingController.expectOne((request) =>
      request.url.endsWith('/bienvenida'),
    );
    expect(req.request.method).toBe('POST');
    expect(req.request.body).toEqual({ nombre: 'Test' });
    req.flush(mockResponse);
  });
});

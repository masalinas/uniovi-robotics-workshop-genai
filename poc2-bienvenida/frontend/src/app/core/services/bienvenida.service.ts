import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {
  BienvenidaRequest,
  BienvenidaResponse,
} from '../models/bienvenida.model';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class BienvenidaService {
  private http = inject(HttpClient);
  private apiUrl = `${environment.apiUrl}/bienvenida`;

  saludar(request: BienvenidaRequest): Observable<BienvenidaResponse> {
    return this.http.post<BienvenidaResponse>(this.apiUrl, request);
  }
}

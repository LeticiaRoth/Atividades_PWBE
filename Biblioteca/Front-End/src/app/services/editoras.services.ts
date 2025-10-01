import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Editora } from '../models/editora';
import { enviroment } from '../../enviroments/enviroments';

@Injectable({ providedIn: 'root' }) // Serviço disponível em toda a aplicação
export class EditorasService {
  private http = inject(HttpClient); // Injeta HttpClient para fazer requisições HTTP
  private base = enviroment.apiBase; // URL base da API

  // Lista todas as editoras
  listar(): Observable<Editora[]> {
    const url = `${this.base}api/Editoras/`; // Monta a URL completa
    return this.http.get<Editora[]>(url); // Faz GET e retorna um array de editoras
  }

  // Busca 1 editora pelo id
  buscarPorId(id: number): Observable<Editora> {
    const url = `${this.base}api/Editoras/${id}/`; // URL específica da editora
    return this.http.get<Editora>(url); // Faz GET e retorna a editora
  }
}

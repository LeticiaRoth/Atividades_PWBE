import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Livro } from '../models/livro';
import { enviroment } from '../../enviroments/enviroments';

@Injectable({ providedIn: 'root' }) // Serviço disponível globalmente
export class LivrosService {
  private http = inject(HttpClient); // Injeta HttpClient para usar dentro do serviço
  private base = enviroment.apiBase; // URL base da API

  // Lista todos os livros
  listar(): Observable<Livro[]> {
    const url = `${this.base}api/Livros/`; // Monta a URL completa
    return this.http.get<Livro[]>(url); // Faz GET e retorna um array de livros
  }

  // Busca 1 livro pelo id
  buscarPorId(id: number): Observable<Livro> {
    const url = `${this.base}api/Livros/${id}/`; // URL específica do livro
    return this.http.get<Livro>(url); // Faz GET e retorna o livro
  }
}

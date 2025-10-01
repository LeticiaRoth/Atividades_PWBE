import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Autor } from '../models/autor';
import { enviroment } from '../../enviroments/enviroments';

@Injectable({providedIn: 'root'})
export class AutoresServices {
  private http = inject(HttpClient);
  private base = enviroment.apiBase

  listar(): Observable<Autor[]>{
    const url = `${this.base}api/Autores/`
    return this.http.get<Autor[]>(url)
  }
}

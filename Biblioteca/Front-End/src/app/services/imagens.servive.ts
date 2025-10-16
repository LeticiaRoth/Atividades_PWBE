import { Injectable, inject } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from "rxjs";
import { enviroment } from "../../enviroments/enviroments";

export type Imagem = {
    id: number;
    imagem: string;
    url: string;
    criado_em: string;
}

@Injectable({providedIn: 'root'})
export class ImagemService{
    private http = inject(HttpClient)
    private base = `${enviroment.apiBase}api/imagens/`

    private headers(): HttpHeaders{
        const token = localStorage.getItem('access')
        return token ? new HttpHeaders({Authorization: `Bearer ${token}`}) : new HttpHeaders()
    }

    listar(): Observable<Imagem[]>{
        return this.http.get<Imagem[]>(this.base, {headers: this.headers()})
    }
    
    enviar(file: File): Observable<Imagem>{
        const form =new FormData()
        form.append('imagem', file)
        return this.http.post<Imagem>(this.base, form, {headers: this.headers()})
    }

    deletar(id: number){
        return this.http.delete(`${this.base}${id}/`, {headers: this.headers()})
    }
}
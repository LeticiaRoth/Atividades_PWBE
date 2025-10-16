import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AutoresServices } from '../../services/autores.services';
import { Autor } from '../../models/autor';
import { AuthService } from '../../services/auth.services';

@Component({
  standalone: true,
  imports: [RouterLink],
  templateUrl: './authors.component.html'
})
export class AutoresComponent {
  private svc = inject(AutoresServices);
  private auth = inject(AuthService);   //Ver o token
  autores = signal<Autor[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  constructor() {
    console.log("Token de acesso: ", this.auth.token());
    
    this.svc.listar().subscribe({
      next: (data) => { this.autores.set(data); this.carregando.set(false); },
      error: () => { this.erro.set('Falha ao carregar autores'); this.carregando.set(false); }
    });
  }
}
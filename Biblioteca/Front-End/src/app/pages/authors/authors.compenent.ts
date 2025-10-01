import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AutoresServices } from '../../services/autores.services';
import { Autor } from '../../models/autor';
import { AuthService } from '../../services/auth.services';

@Component({
  standalone: true,
  imports: [RouterLink],
  template: `
    <section style="max-width:900px;margin:2rem auto;padding:0 1rem">
      <h1>Autores</h1>

      @if (carregando()) {
        <p>Carregando…</p>
      } @else if (erro()) {
        <p style="color:#c62828">{{ erro() }}</p>
      } @else {
        <ul style="padding-left:1.25rem">
          @for (a of autores(); track a.id) {
            <li style="margin:.25rem 0">
              <strong>{{ a.nome }} {{ a.sobrenome }}</strong>
              @if (a.nacionalidade) { — <em style="color:#666">{{ a.nacionalidade }}</em> }
              @if (a.data_nascimento) { • {{ a.data_nascimento }} }
              @if (a.biografia) { <div style="color:#555">{{ a.biografia }}</div> }
            </li>
          }
        </ul>
      }

      <nav style="margin-top:1rem">
        <a routerLink="/">Voltar ao início</a>
      </nav>
    </section>
  `
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
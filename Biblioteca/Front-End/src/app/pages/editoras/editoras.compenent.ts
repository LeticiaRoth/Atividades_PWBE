import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { EditorasService } from '../../services/editoras.services';
import { Editora } from '../../models/editora';
import { AuthService } from '../../services/auth.services';

@Component({
  standalone: true,
  imports: [RouterLink],
  template: `
    <section style="max-width:900px;margin:2rem auto;padding:0 1rem">
      <h1>Editoras</h1>

      @if (carregando()) {
        <p>Carregando…</p>
      } @else if (erro()) {
        <p style="color:#c62828">{{ erro() }}</p>
      } @else {
        <ul style="padding-left:1.25rem">
          @for (e of editoras(); track e.id) {
            <li style="margin:.25rem 0">
              <strong>{{ e.editora }}</strong>
              @if (e.cnpj) { — <em>{{ e.cnpj }}</em> }
              @if (e.endereco) { • {{ e.endereco }} }
              @if (e.telefone) { • {{ e.telefone }} }
              @if (e.email) { • {{ e.email }} }
              @if (e.site) { <div><a href="{{ e.site }}" target="_blank">{{ e.site }}</a></div> }
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
export class EditorasComponent {
  private svc = inject(EditorasService);
  auth = inject(AuthService);

  editoras = signal<Editora[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  constructor() {
    // Faz a requisição para listar todos as editoras
    this.svc.listar().subscribe({
      // Quando os dados chegarem com sucesso
      next: (data) => { 
        this.editoras.set(data); // Atualiza a signal 'editoras' com os dados recebidos
        this.carregando.set(false); 
      },
      error: () => { 
        this.erro.set('Falha ao carregar editoras');
        this.carregando.set(false);  // Marca o carregamento como concluído mesmo com erro
      }
    });
  }
}
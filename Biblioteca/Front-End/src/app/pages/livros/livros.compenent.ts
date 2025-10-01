import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { LivrosService } from '../../services/livros.services';
import { Livro } from '../../models/livro';
import { AuthService } from '../../services/auth.services';

@Component({
  standalone: true,
  imports: [RouterLink],
  template: `
    <section style="max-width:900px;margin:2rem auto;padding:0 1rem">
      <h1>Livros</h1>

      @if (carregando()) {
        <p>Carregando…</p>
      } @else if (erro()) {
        <p style="color:#c62828">{{ erro() }}</p>
      } @else {
        <ul style="padding-left:1.25rem">
          @for (l of livros(); track l.id) {
            <li style="margin:.75rem 0">
              <strong>{{ l.titulo }}</strong>
              @if (l.subtitulo) { — <em>{{ l.subtitulo }}</em> }
              <div style="color:#555">Autor: {{ l.autor }} • Editora: {{ l.editor }}</div>
              <div>ISBN: {{ l.isbn }}</div>
              <div>Idioma: {{ l.idioma }} | Ano: {{ l.ano_publicacao }}</div>
              <div>Páginas: {{ l.paginas }} | Preço: R$ {{ l.preco }}</div>
              @if (l.descricao) { <div>Descrição: {{ l.descricao }}</div> }
              <div>Estoque: {{ l.estoque }} | Disponível: {{ l.disponivel ? 'Sim' : 'Não' }}</div>
              <div>Dimensões: {{ l.dimensoes }} | Peso: {{ l.peso }} kg</div>
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
export class LivrosComponent {
  private svc = inject(LivrosService);
  auth = inject(AuthService);

  livros = signal<Livro[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  constructor() {
    // Faz a requisição para listar todos os livros
    this.svc.listar().subscribe({
      // Quando os dados chegarem com sucesso
      next: (data) => { 
        this.livros.set(data); // Atualiza a signal 'livros' com os dados recebidos
        this.carregando.set(false); 
      },
      error: () => { 
        this.erro.set('Falha ao carregar livros');
        this.carregando.set(false);  // Marca o carregamento como concluído mesmo com erro
      }
    });
  }
}

import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { LivrosService } from '../../services/livros.services';
import { Livro } from '../../models/livro';
import { AuthService } from '../../services/auth.services';

@Component({
  standalone: true,
  imports: [RouterLink],
  templateUrl: './livros.component.html'
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

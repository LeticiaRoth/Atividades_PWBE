import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { EditorasService } from '../../services/editoras.services';
import { Editora } from '../../models/editora';
import { AuthService } from '../../services/auth.services';

@Component({
  selector: 'app-publisher.component',
  imports: [RouterLink],
  templateUrl: './publisher.component.html',
})
export class PublisherComponent {
  private svc = inject(EditorasService);
  private auth = inject(AuthService);
  editoras = signal<Editora[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  token = this.auth.token

  constructor() {
      this.svc.listar().subscribe({
      next: (data) => { 
        this.editoras.set(data); 
        this.carregando.set(false); 
        console.log("Token do Lindo: ", this.token());
        
      },
      error: () => { this.erro.set('Falha ao carregar editoras'); this.carregando.set(false); }
    });
  }
}

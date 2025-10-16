import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImagemService } from '../../services/imagens.servive';
import { enviroment } from '../../../enviroments/enviroments';


export interface Imagem {
  id: number;
  url: string;
}

@Component({
  standalone: true,
  selector: 'app-imagens',
  imports: [CommonModule],
  templateUrl: './images.component.html',
})
export class ImagensComponent {
  private svc = inject(ImagemService);

  // Agora o TypeScript sabe o que é 'Imagem', e o erro some.
  imagens = signal<Imagem[]>([]);

  // <-- MELHORIA: Usar 'signal' para estados reativos é a prática moderna
  status = signal('');
  preview = signal<string | null>(null);

  arquivo: File | null = null;
  apiBase = enviroment.apiBase;

  // <-- CORREÇÃO 4: Adicionado o constructor para carregar os dados ao iniciar
  constructor() {
    this.carregar();
  }

  carregar() {
    this.status.set('Carregando imagens...');
    this.svc.listar().subscribe({
      next: (data: Imagem[]) => { // <-- MELHORIA: Tipagem mais forte
        this.imagens.set(Array.isArray(data) ? data : (data as any).results ?? []);
        this.status.set(''); // Limpa o status em caso de sucesso
      },
      error: () => this.status.set('Falha ao carregar imagens.'),
    });
  }

  onFile(e: Event) {
    const input = e.target as HTMLInputElement;
    this.arquivo = input.files?.[0] ?? null;

    if (this.arquivo) {
      const reader = new FileReader();
      reader.onload = () => this.preview.set(reader.result as string);
      reader.readAsDataURL(this.arquivo);
    } else {
      this.preview.set(null);
    }
  }

  onSubmit(ev: Event) {
    ev.preventDefault();
    if (!this.arquivo) return;
    this.status.set('Enviando...');

    this.svc.enviar(this.arquivo).subscribe({
      next: (img: Imagem) => { // <-- MELHORIA: Tipagem mais forte
        this.status.set('Imagem enviada com sucesso!');
        this.arquivo = null;
        this.preview.set(null);
        this.imagens.update((arr) => [img, ...arr]);
      },
      error: (err: any) => {
        console.error(err);
        this.status.set('Falha ao enviar imagem.');
      },
    });
  }

  remover(id: number) {
    if (!confirm('Tem certeza que deseja remover esta imagem?')) return;

    this.svc.deletar(id).subscribe({
      next: () => {
        this.imagens.update((arr) => arr.filter((i) => i.id !== id));
      },
      error: () => this.status.set('Falha ao remover a imagem.'),
    });
  }
}
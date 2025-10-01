import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AutoresComponent } from './pages/authors/authors.compenent';
import { EditorasComponent } from './pages/editoras/editoras.compenent';
import { LivrosComponent } from './pages/livros/livros.compenent';

export const routes: Routes = [
    {path: '', component: HomeComponent},
    {path: 'home', component: HomeComponent},
    {path: 'autores', component: AutoresComponent},
    {path: 'editoras', component: EditorasComponent},
    {path: 'livros', component: LivrosComponent}
];

import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AutoresComponent } from './pages/authors/authors.component';
import { EditorasComponent } from './pages/editoras/editoras.compenent';
import { LivrosComponent } from './pages/livros/livros.component';
import { LoginComponent } from './pages/login/login.component';

export const routes: Routes = [
    {path: '', component: HomeComponent},
    {path: 'home', component: HomeComponent},
    {path: 'autores', component: AutoresComponent},
    {path: 'editoras', component: EditorasComponent},
    {path: 'livros', component: LivrosComponent},
    {path: 'login', component:LoginComponent}
];

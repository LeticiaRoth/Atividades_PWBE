import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AutoresComponent } from './pages/authors/authors.component';
import { EditorasComponent } from './pages/editoras/editoras.compenent';
import { LivrosComponent } from './pages/livros/livros.component';
import { LoginComponent } from './pages/login/login.component';
import { ImagensComponent } from './pages/image/images.component';
import { PublisherComponent } from './pages/publisher/publisher.component';
import { authGuard } from './auth.guard';


export const routes: Routes = [
    {path: '', component: LoginComponent},
    {path: 'login', component: LoginComponent},
    {path: 'home', component: HomeComponent},
    {path: 'autores', component: AutoresComponent, canActivate: [authGuard]},
    {path: 'editoras', component: PublisherComponent, canActivate: [authGuard]},
    {path: 'livros', component: LivrosComponent, canActivate: [authGuard]},
    {path: 'imagens', component: LivrosComponent}
];

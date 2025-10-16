import { Component, inject, signal } from '@angular/core'
import { RouterLink, Router } from '@angular/router'
import { ReactiveFormsModule, FormBuilder, Validators} from '@angular/forms'
import { AuthService } from '../../services/auth.services'

@Component({
  selector: 'app-login.component',
  standalone: true,
  imports: [RouterLink, ReactiveFormsModule],
  templateUrl: './login.component.html',
})
export class LoginComponent {
  private fb = inject(FormBuilder)
  private auth = inject(AuthService)
  private router = inject(Router)
  
  loading = signal(false)
  error =signal<string | null>(null)

  form = this.fb.group({
    username: ['', [Validators.required]],
    password: ['', [Validators.required]],
  })

  onSubmit(){
    if (this.form.invalid) return

    this.loading.set(true)
    this.error.set(null)

    const {username, password} = this.form.value as {username: string, password: string}
    
    this.auth.login(username, password).subscribe({
      next: () => {
        this.loading.set(false)
        this.router.navigateByUrl('/home')
      },
      error: (e) => {
        this.loading.set(false)
        this.error.set("Usuário ou senha inválido...")
        console.log("O erro é ", e);
        
      }
    })

  }
}

import { Injectable, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from 'rxjs';
import { enviroment } from '../../enviroments/enviroments';

type TokenPair = { access: string; refresh?: string };

const storage = {
  get: (k: string) => (typeof localStorage !== 'undefined' ? localStorage.getItem(k) : null),
  set: (k: string, v: string) => { if (typeof localStorage !== 'undefined') localStorage.setItem(k, v); },
  del: (k: string) => { if (typeof localStorage !== 'undefined') localStorage.removeItem(k); },
};

@Injectable({ providedIn: 'root' })
export class AuthService {
  private _access = signal<string | null>(storage.get('access'));
  private _refresh = signal<string | null>(storage.get('refresh'));
  private base = enviroment.apiBase;

  constructor(private http: HttpClient) {}

  isAuthenticated = () => !!this._access();

  token = () => this._access();

  login(username: string, password: string): Observable<TokenPair> {
    const AUTH_URL = `${this.base}/token/`;
    
    
    return this.http.post<TokenPair>(AUTH_URL, { username, password }).pipe(
      tap(tokens => {
        if (tokens.access) { this._access.set(tokens.access); storage.set('access', tokens.access); }
        if (tokens.refresh) { this._refresh.set(tokens.refresh); storage.set('refresh', tokens.refresh); }
      })
      
    );
  }
  
  refresh(): Observable<{ access: string }> {
    const REFRESH_URL = `${this.base}/refresh/`;
    const refresh = this._refresh();
    return this.http.post<{ access: string }>(REFRESH_URL, { refresh }).pipe(
      tap(t => { this._access.set(t.access); storage.set('access', t.access); })
    );
  }

  logout() {
    this._access.set(null); this._refresh.set(null);
    storage.del('access'); storage.del('refresh');
  }
}

import { inject } from "@angular/core";
import { HttpInterceptorFn } from "@angular/common/http";
import { AuthService } from "./services/auth.services";

export const authInterceptor: HttpInterceptorFn = (req, next) => {
    const auth = inject(AuthService)
    const token = auth.token()
    if (token){
        req = req.clone({setHeaders: {Authorization: `Bearer ${token}`}})
        
    }
    return next(req)
}

#lang racket


(define empty-env
  (lambda ()
    (lambda (y)
      (error 'value-of "unbound identifier"))))
 
(define empty-k
  (lambda ()
    (lambda (v)
      v)))


(define value-of-cps
  (lambda (expr env k)
    (match expr
      [`(const ,expr) (k expr)]
      [`(mult ,x1 ,x2) (value-of-cps x1 env (lambda (v)
                                              (value-of-cps x2 env (lambda (u)
                                                                     (k (* v u))))))]
      [`(sub1 ,x) (value-of-cps x env (lambda (v)
                                        (k (sub1 v))))]
      [`(zero ,x) (value-of-cps x env (lambda (v)
                                    (k (zero? v))))]
      [`(if ,test ,conseq ,alt) (value-of-cps test env (lambda (v)
                                                         (if v
                                                             (value-of-cps conseq env (lambda (u)
                                                                                        (k u)))
                                                             (value-of-cps alt env (lambda (u)
                                                                                     (k u))))))]
      [`(letcc ,body) (value-of-cps body (lambda (y k^) (if (zero? y) (k^ k) (env (sub1 y) k^))) k)]
      [`(throw ,k-exp ,v-exp) (value-of-cps k-exp env (lambda (v)
                                                        (value-of-cps v-exp env (lambda (u)
                                                                                  (v u)))))]
      [`(let ,e ,body) (value-of-cps e env (lambda (v)
                                             (value-of-cps body (lambda (y k^) (if (zero? y) (k^ v) (env (sub1 y) k^))) k)))]
      [`(var ,y) (env y k)]
      [`(lambda ,body) (k (lambda (a k) (value-of-cps body (lambda (y k^) (if (zero? y) (k^ a) (env (sub1 y) k^))) k)))]
      [`(app ,rator ,rand) (value-of-cps rator env (lambda (v)
                                                     (value-of-cps rand env (lambda (u)
                                                                              (v u k)))))])))




(value-of-cps '(mult (sub1 (const 4)) (const 3)) (empty-env) (empty-k))
(value-of-cps '(app (lambda (var 0)) (const 2)) (empty-env) (empty-k))
(value-of-cps '(if (zero (const 9))
                   (const 1)
                   (const 2))
              (empty-env)
              (empty-k))
(value-of-cps '(letcc (throw (app (lambda (var 0)) (var 0)) (mult (const 5) (const 5)))) (empty-env) (empty-k))
;;25
(value-of-cps '(letcc (sub1 (throw (var 0) (const 5)))) (empty-env) (empty-k))
;;5
(value-of-cps '(letcc (throw (throw (var 0) (const 5)) (const 6))) (empty-env) (empty-k))
;;5
(value-of-cps '(letcc (throw (const 5) (throw (var 0) (const 5)))) (empty-env) (empty-k))
;;5
(value-of-cps '(mult (const 3) (letcc (throw (const 5) (throw (var 0) (const 5))))) (empty-env) (empty-k))
;;15
(value-of-cps '(if (zero (const 5)) (app (lambda (app (var 0) (var 0))) (lambda (app (var 0) (var 0)))) (const 4))
              (empty-env)
              (empty-k))
;;4
(value-of-cps '(if (zero (const 0)) (const 4) (app (lambda (app (var 0) (var 0))) (lambda (app (var 0) (var 0)))))
              (empty-env)
              (empty-k))
;;4
(value-of-cps '(app (lambda (app (app (var 0) (var 0)) (const 2)))
                             (lambda
                               (lambda 
                                 (if (zero (var 0))  
                                     (const 1)
                                     (app (app (var 1) (var 1)) (sub1 (var 0)))))))
                       (empty-env)
                       (empty-k))
;;1
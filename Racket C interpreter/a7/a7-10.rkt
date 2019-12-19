#lang racket


(define empty-env
  (λ ()
    '()))
 
(define empty-k
  (λ ()
    (λ (v)
      v)))


(define value-of-cps
  (lambda (expr env k)
    (match expr
      [`(const ,expr) (k expr)]
      [`(mult ,x1 ,x2) (value-of-cps x1 env (k-mult-outside x2 env k))]
      [`(sub1 ,x) (value-of-cps x env (k-sub1 k))]
      [`(zero ,x) (value-of-cps x env (k-zero k))]
      [`(if ,test ,conseq ,alt) (value-of-cps test env (k-if conseq alt env k))]
      [`(letcc ,body) (value-of-cps body (extend-env k env) k)] ;; no continuation abstraction
      [`(throw ,k-exp ,v-exp) (value-of-cps k-exp env (k-throw-outside v-exp env))] 
      [`(let ,e ,body) (value-of-cps e env (k-let body env k))]
      [`(var ,y) (apply-env env y k)]
      [`(lambda ,body) (apply-k k (make-closure body env))]
      [`(app ,rator ,rand) (value-of-cps rator env (k-rator-outside rand env k))])))

;; part 9 continuation helpers
(define k-rator-outside
  (λ (rand^ env^ k^)
    (lambda (v)
      (value-of-cps rand^ env^ (k-rator-inside v k^)))))

(define k-rator-inside
  (λ (v^ k^)
    (lambda (u)
      (apply-closure v^ u k^))))

(define k-let
  (λ (body env^ k^)
    (lambda (v)
      (value-of-cps body (extend-env v env^) k^))))

(define k-sub1
  (λ (k^)
    (lambda (v)
      (apply-k k^ (sub1 v)))))

(define k-zero
  (λ (k^)
    (lambda (v)
      (apply-k k^ (zero? v)))))

(define k-mult-inside
  (λ (v^ k^)
    (lambda (u)
      (apply-k k^ (* v^ u)))))

(define k-mult-outside
  (λ (x2^ env^ k^)
    (λ(v)
      (value-of-cps x2^ env^ (k-mult-inside v k^)))))

(define k-throw-inside
  (λ (v^)
    (lambda (u)
      (v^ u))))

(define k-throw-outside
  (λ (v-exp^ env^)
    (lambda (v)
      (value-of-cps v-exp^ env^ (k-throw-inside v)))))


(define k-if
  (λ (conseq^ alt^ env^ k^)
    (λ (v)
      (if v
          (value-of-cps conseq^ env^ k^)
          (value-of-cps alt^ env^ k^)))))






;; tag a closure with caltic, my student id
(define make-closure
  (λ (body env)
    `(caltic ,body ,env)))

(define apply-closure
  (λ (v u k)
    (match v
      [`(caltic ,body ,env)
       (value-of-cps body (extend-env u env) k)])))

(define extend-env
  (λ (x env)
    `(,x . ,env)))

(define apply-env
  (λ (env y k)
    (match env
      ['() (error "you fucked up")]
      [else (if (zero? y) (apply-k k (car env)) 
                (apply-env (cdr env) (sub1 y) k))])))

(define apply-k
  (λ (k v)
    (k v)))


;; variables needed:  body env a k
#|
(define make-closure-fn
  (λ (body env)
    (lambda (u k)
      (value-of-cps body (extend-env u env) k))))

(define apply-closure-fn
  (λ (v u k)
    (v u k)))
|#




(value-of-cps '(mult (sub1 (const 4)) (const 3)) (empty-env) (empty-k))
(value-of-cps '(app (lambda (var 0)) (const 2)) (empty-env) (empty-k))
(value-of-cps '(if (zero (const 9))
                   (const 1)
                   (const 2))
              (empty-env)
              (empty-k))
(value-of-cps '(let (const 69) (var 0)) (empty-env) (empty-k))
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


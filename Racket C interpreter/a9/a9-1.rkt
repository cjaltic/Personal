#lang racket
(require "parenthec.rkt")

;; part 1

(define empty-env
  (λ ()
    '()))
 
(define empty-k
  (λ ()
    '(empto)))


(define-union expr
  (const cexp)
  (var n)
  (if test conseq alt)
  (mult nexp1 nexp2)
  (sub1 nexp)
  (zero nexp)
  (letcc body)
  (throw kexp vexp)
  (let exp body)              
  (lambda body)
  (app rator rand))


(define value-of-cps
  (lambda (ex env k)
    (union-case ex expr
      [(const ex) (apply-k k ex)] 
      [(mult x1 x2) (value-of-cps x1 env (k-mult-outside x2 env k))]
      [(sub1 x) (value-of-cps x env (k-sub1 k))]
      [(zero x) (value-of-cps x env (k-zero k))]
      [(if test conseq alt) (value-of-cps test env  (k-if-inside conseq alt env k))]
      [(letcc body) (value-of-cps body (extend-env k env) k)] ;; no continuation abstraction
      [(throw k-exp v-exp) (value-of-cps k-exp env (k-throw v-exp env))] 
      [(let e body) (value-of-cps e env (k-let body env k))]
      [(var y) (apply-env env y k)]
      [(lambda body) (apply-k k (make-closure body env))]
      [(app rator rand) (value-of-cps rator env (k-rator-outside rand env k))])))

;; part 11 ds continuations
(define k-sub1
  (λ (k^)
    `(k-sub1 ,k^)))
(define k-zero
  (λ (k^)
    `(k-zero ,k^)))
(define k-mult-inside
  (λ (v^ k^)
    `(k-mult-inside ,v^ ,k^)))
(define k-mult-outside
  (λ (x2^ env^ k^)
    `(k-mult-outside ,x2^ ,env^ ,k^)))
(define k-if-inside
  (λ(conseq^ alt^ env^ k^)
    `(k-if-inside ,conseq^ ,alt^  ,env^ ,k^)))
(define k-throw
  (λ (v-exp^ env^)
    `(k-throw ,v-exp^ ,env^)))
(define k-let
  (λ (body^ env^ k^)
    `(k-let ,body^ ,env^ ,k^)))
(define k-rator-inside
  (λ (v^ k^)
    `(k-rator-inside ,v^ ,k^)))
(define k-rator-outside
  (λ (rand^ env^ k^)
    `(k-rator-outside ,rand^ ,env^ ,k^)))

(define apply-k
  (λ (k v)
    (match k
      [`(empto) v]
      [`,y #:when(symbol? y) (y v)]
      [`(k-sub1 ,k)
       (apply-k k (sub1 v))]
      [`(k-zero ,k)
       (apply-k k (zero? v))]
      [`(k-mult-inside ,u ,k)
       (apply-k k (* u v))] 
      [`(k-mult-outside ,x2 ,env ,k)
       (value-of-cps x2 env (k-mult-inside v k))]
      [`(k-if-inside ,conseq^ ,alt^  ,env^ ,k^)  (if v
                                                     (value-of-cps conseq^ env^ k^)
                                                     (value-of-cps alt^ env^ k^))]
      [`(k-throw ,v-exp ,env)
       (value-of-cps v-exp env v)]
      [`(k-let ,body ,env ,k)
       (value-of-cps body (extend-env v env) k)]
      [`(k-rator-inside ,v^ ,k^)
       (apply-closure v^ v k^)]
      [`(k-rator-outside ,rand ,env ,k)
       (value-of-cps rand env (k-rator-inside v k))]
      [else (k v)]))) 


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


(define main 
  (lambda ()
    (value-of-cps 
     (expr_let 
      (expr_lambda
       (expr_lambda 
        (expr_if
         (expr_zero (expr_var 0))
         (expr_const 1)
         (expr_mult (expr_var 0) (expr_app (expr_app (expr_var 1) (expr_var 1)) (expr_sub1 (expr_var 0)))))))
      (expr_mult
       (expr_letcc
        (expr_app
         (expr_app (expr_var 1) (expr_var 1))
         (expr_throw (expr_var 0) (expr_app (expr_app (expr_var 1) (expr_var 1)) (expr_const 4)))))
       (expr_const 5)))
     (empty-env)
     (empty-k))))



(main)

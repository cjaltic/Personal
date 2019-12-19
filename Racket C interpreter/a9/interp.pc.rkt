;#lang racket
;(require "parenthec.rkt")



#|
(define empty-env
  (λ ()
    (umwelt_empty)))
 
(define empty-k
  (λ ()
    (continue_empty)))
|#

;; step 7 program counter
(define-program-counter count)


(define-registers
  k
  v
  var
  exp
  env
  rator
  rest)

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
  (app rator rest))

(define-union umwelt
  (empty)
  (extend-env v env))

(define-union continue
  (empty dismount)
  (k-sub1 k)
  (k-zero k)
  (k-mult-inside v k)
  (k-mult-outside env-cps x k)
  (k-if-inside env-cps conseq alt k)
  (k-let env-cps body k)
  (k-throw-outside env-cps k-exp)
  (k-throw-inside v env-cps)
  (k-rator-inside v k)
  (k-rator-outside env-cps rest k))

(define-label value-of-cps
 ;; (lambda ()
  (union-case exp expr
              [(const ex)
               (begin (set! v ex) (set! count apply-k))]
              [(mult x1 x2)
               (begin (set! exp x1) (set! k (continue_k-mult-outside env x2 k))
                 (set! count value-of-cps))]
              [(sub1 n)
               (begin (set! exp n) (set! k (continue_k-sub1 k))
                 (set! count value-of-cps))]
              [(zero n)
               (begin
                 (set! exp n)(set! k (continue_k-zero k))(set! count value-of-cps))]
              [(if test conseq alt)
               (begin (set! exp test)(set! k (continue_k-if-inside env conseq alt k))
                 (set! count value-of-cps))]
              [(letcc body)
               (begin (set! exp body)(set! env (umwelt_extend-env k env))
                 (set! k k)(set! count value-of-cps))]
              [(throw k-exp v-exp)
               (begin (set! exp k-exp)(set! k (continue_k-throw-outside env v-exp))
                 (set! count value-of-cps))]
              [(let e body)
               (begin
                 (set! exp e)(set! k (continue_k-let env body k))
                 (set! count value-of-cps))]
              [(var y)
               (begin (set! var y) (set! count apply-env))]
              [(lambda body)
               (begin (set! exp exp) (set! v (schluss_caltic body env)) 
                 (set! count apply-k))]
              [(app rator rest)
               (begin
                 (set! exp rator) (set! k (continue_k-rator-outside env rest k))
                 (set! count value-of-cps))]))



(define-label apply-k
  ;;(lambda ()
  (union-case k continue
      [(empty dismount) (dismount-trampoline dismount)]
      [(k-sub1 k^)
       (begin (set! v (sub1 v))(set! k k^)
         (set! count apply-k))]
      [(k-zero k^)
       (begin(set! v (zero? v))(set! k k^)
         (set! count apply-k))]
      [(k-mult-outside env^ x k^)
       (begin
         (set! exp x)(set! env env^)
         (set! k (continue_k-mult-inside v k^))(set! count value-of-cps))]
      [(k-mult-inside u^ k^)
       (begin(set! k k^)(set! v (* u^ v))
         (set! count apply-k))]
      [(k-if-inside env^ conseq alt k^)
       (if v
           (begin(set! env env^)(set! exp conseq)(set! k k^)
             (set! count value-of-cps))
           (begin(set! exp alt)(set! env env^)
             (set! k k^)(set! count value-of-cps)))]
      [(k-throw-outside env^ k^)
       (begin
         (set! exp k^)(set! env env^)
         (set! k (continue_k-throw-inside v env))(set! count value-of-cps))]
      [(k-throw-inside v env^)
       (begin(set! exp exp)(set! env env)
         (set! k v)(set! count apply-k))]
      [(k-let env^ body k^)
       (begin(set! exp body)(set! k k^)(set! env (umwelt_extend-env v env^))
         (set! count value-of-cps))]
      [(k-rator-outside env^ rest k^)
       (begin(set! exp rest)(set! env env^)
         (set! k (continue_k-rator-inside v k^))(set! count value-of-cps))]
      [(k-rator-inside v^ k^)
       (begin(set! rest v)(set! k k^)
         (set! exp exp)(set! env env)
         (set! rator v^)(set! count apply-closure))]))


;; a9 step 2 define closure union 
(define-union schluss
  (caltic body env-cps))
;; new apply-closure using union
(define-label apply-closure
  ;;(lambda ()
    (union-case rator schluss
                [(caltic body env^)
                 (begin (set! k k) (set! env (umwelt_extend-env rest env^))
                   (set! exp body)
                   (set! count value-of-cps))]))




(define-label apply-env
 ;; (lambda ()
    (union-case env umwelt
                [(empty) (error "you fucked up")]
                [(extend-env v^ env^)
                 (if (zero? var)
                     (begin (set! v v^) (set! k k)
                       (set! count apply-k))
                     (begin (set! env env^)(set! var (sub1 var))
                       (set! k k)(set! count apply-env)))]))


	(define-label main
	  (begin 
	      (set! exp (expr_let 
	                 (expr_lambda
	                  (expr_lambda 
	                   (expr_if
	                    (expr_zero (expr_var 0))
	                    (expr_const 1)
	                    (expr_mult (expr_var 0)
	                               (expr_app (expr_app (expr_var 1) (expr_var 1))
	                                         (expr_sub1 (expr_var 0)))))))
	                 (expr_mult
	                  (expr_letcc
	                   (expr_app
	                    (expr_app (expr_var 1) (expr_var 1))
	                    (expr_throw (expr_var 0)
	                                (expr_app (expr_app (expr_var 1)
	                                                    (expr_var 1)) (expr_const 4)))))
	                  (expr_const 5))))             
(set! env (umwelt_empty))
(set! count value-of-cps)
(mount-trampoline continue_empty k count)
(printf "Fact 5: ~s\n" v)))

#|
;; tag a closure with caltic, my student id
(define-label make-closure
  (λ (body env)
    `(caltic ,body ,env)))

(define apply-closure
  (λ (v u k)
    (match v
      [`(caltic ,body ,env)
       (value-of-cps body (extend-env u env) k)]))) |#
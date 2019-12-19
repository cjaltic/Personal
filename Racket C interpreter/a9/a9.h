void (*count)();

void *k, *v, *var, *exp, *env, *rator, *rest;

struct expr;
typedef struct expr expr;
struct expr {
  enum {
    _const_expr,
    _var_expr,
    _if_expr,
    _mult_expr,
    _subr1_expr,
    _zero_expr,
    _letcc_expr,
    _throw_expr,
    _let_expr,
    _lambda_expr,
    _app_expr
  } tag;
  union {
    struct { void *_cexp; } _const;
    struct { void *_n; } _var;
    struct { void *_test; void *_conseq; void *_alt; } _if;
    struct { void *_nexpr1; void *_nexpr2; } _mult;
    struct { void *_nexp; } _subr1;
    struct { void *_nexp; } _zero;
    struct { void *_body; } _letcc;
    struct { void *_kexp; void *_vexp; } _throw;
    struct { void *_exp; void *_body; } _let;
    struct { void *_body; } _lambda;
    struct { void *_rator; void *_rest; } _app;
  } u;
};

void *exprr_const(void *cexp);
void *exprr_var(void *n);
void *exprr_if(void *test, void *conseq, void *alt);
void *exprr_mult(void *nexpr1, void *nexpr2);
void *exprr_subr1(void *nexp);
void *exprr_zero(void *nexp);
void *exprr_letcc(void *body);
void *exprr_throw(void *kexp, void *vexp);
void *exprr_let(void *exp, void *body);
void *exprr_lambda(void *body);
void *exprr_app(void *rator, void *rest);

struct umwelt;
typedef struct umwelt umwelt;
struct umwelt {
  enum {
    _empty_umwelt,
    _extendr__m__env_umwelt
  } tag;
  union {
    struct { char dummy; } _empty;
    struct { void *_v; void *_env; } _extendr__m__env;
  } u;
};

void *umweltr_empty();
void *umweltr_extendr__m__env(void *v, void *env);

struct continue;
typedef struct continue continue;
struct continue {
  enum {
    _empty_continue,
    _kr__m__subr1_continue,
    _kr__m__zero_continue,
    _kr__m__multr__m__inside_continue,
    _kr__m__multr__m__outside_continue,
    _kr__m__ifr__m__inside_continue,
    _kr__m__let_continue,
    _kr__m__throwr__m__outside_continue,
    _kr__m__throwr__m__inside_continue,
    _kr__m__ratorr__m__inside_continue,
    _kr__m__ratorr__m__outside_continue
  } tag;
  union {
    struct { void *_dismount; } _empty;
    struct { void *_k; } _kr__m__subr1;
    struct { void *_k; } _kr__m__zero;
    struct { void *_v; void *_k; } _kr__m__multr__m__inside;
    struct { void *_envr__m__cps; void *_x; void *_k; } _kr__m__multr__m__outside;
    struct { void *_envr__m__cps; void *_conseq; void *_alt; void *_k; } _kr__m__ifr__m__inside;
    struct { void *_envr__m__cps; void *_body; void *_k; } _kr__m__let;
    struct { void *_envr__m__cps; void *_kr__m__exp; } _kr__m__throwr__m__outside;
    struct { void *_v; void *_envr__m__cps; } _kr__m__throwr__m__inside;
    struct { void *_v; void *_k; } _kr__m__ratorr__m__inside;
    struct { void *_envr__m__cps; void *_rest; void *_k; } _kr__m__ratorr__m__outside;
  } u;
};

void *continuer_empty(void *dismount);
void *continuer_kr__m__subr1(void *k);
void *continuer_kr__m__zero(void *k);
void *continuer_kr__m__multr__m__inside(void *v, void *k);
void *continuer_kr__m__multr__m__outside(void *envr__m__cps, void *x, void *k);
void *continuer_kr__m__ifr__m__inside(void *envr__m__cps, void *conseq, void *alt, void *k);
void *continuer_kr__m__let(void *envr__m__cps, void *body, void *k);
void *continuer_kr__m__throwr__m__outside(void *envr__m__cps, void *kr__m__exp);
void *continuer_kr__m__throwr__m__inside(void *v, void *envr__m__cps);
void *continuer_kr__m__ratorr__m__inside(void *v, void *k);
void *continuer_kr__m__ratorr__m__outside(void *envr__m__cps, void *rest, void *k);

void valuer__m__ofr__m__cps();
void applyr__m__k();
struct schluss;
typedef struct schluss schluss;
struct schluss {
  enum {
    _caltic_schluss
  } tag;
  union {
    struct { void *_body; void *_envr__m__cps; } _caltic;
  } u;
};

void *schlussr_caltic(void *body, void *envr__m__cps);

void applyr__m__closure();
void applyr__m__env();
int main();
int mount_tram();

struct _trstr;
typedef struct _trstr _trstr;
struct _trstr {
  jmp_buf *jmpbuf;
  int value;
};


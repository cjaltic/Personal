#include <setjmp.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "a9.h"

void *schlussr_caltic(void *body, void *envr__m__cps) {
schluss* _data = (schluss*)malloc(sizeof(schluss));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _caltic_schluss;
  _data->u._caltic._body = body;
  _data->u._caltic._envr__m__cps = envr__m__cps;
  return (void *)_data;
}

void *continuer_empty(void *dismount) {
continue* _data = (continue*)malloc(sizeof(continue));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _empty_continue;
  _data->u._empty._dismount = dismount;
  return (void *)_data;
}

void *continuer_kr__m__subr1(void *k) {
continue* _data = (continue*)malloc(sizeof(continue));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _kr__m__subr1_continue;
  _data->u._kr__m__subr1._k = k;
  return (void *)_data;
}

void *continuer_kr__m__zero(void *k) {
continue* _data = (continue*)malloc(sizeof(continue));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _kr__m__zero_continue;
  _data->u._kr__m__zero._k = k;
  return (void *)_data;
}

void *continuer_kr__m__multr__m__inside(void *v, void *k) {
continue* _data = (continue*)malloc(sizeof(continue));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _kr__m__multr__m__inside_continue;
  _data->u._kr__m__multr__m__inside._v = v;
  _data->u._kr__m__multr__m__inside._k = k;
  return (void *)_data;
}

void *continuer_kr__m__multr__m__outside(void *envr__m__cps, void *x, void *k) {
continue* _data = (continue*)malloc(sizeof(continue));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _kr__m__multr__m__outside_continue;
  _data->u._kr__m__multr__m__outside._envr__m__cps = envr__m__cps;
  _data->u._kr__m__multr__m__outside._x = x;
  _data->u._kr__m__multr__m__outside._k = k;
  return (void *)_data;
}

void *continuer_kr__m__ifr__m__inside(void *envr__m__cps, void *conseq, void *alt, void *k) {
continue* _data = (continue*)malloc(sizeof(continue));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _kr__m__ifr__m__inside_continue;
  _data->u._kr__m__ifr__m__inside._envr__m__cps = envr__m__cps;
  _data->u._kr__m__ifr__m__inside._conseq = conseq;
  _data->u._kr__m__ifr__m__inside._alt = alt;
  _data->u._kr__m__ifr__m__inside._k = k;
  return (void *)_data;
}

void *continuer_kr__m__let(void *envr__m__cps, void *body, void *k) {
continue* _data = (continue*)malloc(sizeof(continue));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _kr__m__let_continue;
  _data->u._kr__m__let._envr__m__cps = envr__m__cps;
  _data->u._kr__m__let._body = body;
  _data->u._kr__m__let._k = k;
  return (void *)_data;
}

void *continuer_kr__m__throwr__m__outside(void *envr__m__cps, void *kr__m__exp) {
continue* _data = (continue*)malloc(sizeof(continue));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _kr__m__throwr__m__outside_continue;
  _data->u._kr__m__throwr__m__outside._envr__m__cps = envr__m__cps;
  _data->u._kr__m__throwr__m__outside._kr__m__exp = kr__m__exp;
  return (void *)_data;
}

void *continuer_kr__m__throwr__m__inside(void *v, void *envr__m__cps) {
continue* _data = (continue*)malloc(sizeof(continue));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _kr__m__throwr__m__inside_continue;
  _data->u._kr__m__throwr__m__inside._v = v;
  _data->u._kr__m__throwr__m__inside._envr__m__cps = envr__m__cps;
  return (void *)_data;
}

void *continuer_kr__m__ratorr__m__inside(void *v, void *k) {
continue* _data = (continue*)malloc(sizeof(continue));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _kr__m__ratorr__m__inside_continue;
  _data->u._kr__m__ratorr__m__inside._v = v;
  _data->u._kr__m__ratorr__m__inside._k = k;
  return (void *)_data;
}

void *continuer_kr__m__ratorr__m__outside(void *envr__m__cps, void *rest, void *k) {
continue* _data = (continue*)malloc(sizeof(continue));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _kr__m__ratorr__m__outside_continue;
  _data->u._kr__m__ratorr__m__outside._envr__m__cps = envr__m__cps;
  _data->u._kr__m__ratorr__m__outside._rest = rest;
  _data->u._kr__m__ratorr__m__outside._k = k;
  return (void *)_data;
}

void *umweltr_empty() {
umwelt* _data = (umwelt*)malloc(sizeof(umwelt));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _empty_umwelt;
  return (void *)_data;
}

void *umweltr_extendr__m__env(void *v, void *env) {
umwelt* _data = (umwelt*)malloc(sizeof(umwelt));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _extendr__m__env_umwelt;
  _data->u._extendr__m__env._v = v;
  _data->u._extendr__m__env._env = env;
  return (void *)_data;
}

void *exprr_const(void *cexp) {
expr* _data = (expr*)malloc(sizeof(expr));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _const_expr;
  _data->u._const._cexp = cexp;
  return (void *)_data;
}

void *exprr_var(void *n) {
expr* _data = (expr*)malloc(sizeof(expr));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _var_expr;
  _data->u._var._n = n;
  return (void *)_data;
}

void *exprr_if(void *test, void *conseq, void *alt) {
expr* _data = (expr*)malloc(sizeof(expr));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _if_expr;
  _data->u._if._test = test;
  _data->u._if._conseq = conseq;
  _data->u._if._alt = alt;
  return (void *)_data;
}

void *exprr_mult(void *nexpr1, void *nexpr2) {
expr* _data = (expr*)malloc(sizeof(expr));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _mult_expr;
  _data->u._mult._nexpr1 = nexpr1;
  _data->u._mult._nexpr2 = nexpr2;
  return (void *)_data;
}

void *exprr_subr1(void *nexp) {
expr* _data = (expr*)malloc(sizeof(expr));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _subr1_expr;
  _data->u._subr1._nexp = nexp;
  return (void *)_data;
}

void *exprr_zero(void *nexp) {
expr* _data = (expr*)malloc(sizeof(expr));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _zero_expr;
  _data->u._zero._nexp = nexp;
  return (void *)_data;
}

void *exprr_letcc(void *body) {
expr* _data = (expr*)malloc(sizeof(expr));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _letcc_expr;
  _data->u._letcc._body = body;
  return (void *)_data;
}

void *exprr_throw(void *kexp, void *vexp) {
expr* _data = (expr*)malloc(sizeof(expr));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _throw_expr;
  _data->u._throw._kexp = kexp;
  _data->u._throw._vexp = vexp;
  return (void *)_data;
}

void *exprr_let(void *exp, void *body) {
expr* _data = (expr*)malloc(sizeof(expr));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _let_expr;
  _data->u._let._exp = exp;
  _data->u._let._body = body;
  return (void *)_data;
}

void *exprr_lambda(void *body) {
expr* _data = (expr*)malloc(sizeof(expr));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _lambda_expr;
  _data->u._lambda._body = body;
  return (void *)_data;
}

void *exprr_app(void *rator, void *rest) {
expr* _data = (expr*)malloc(sizeof(expr));
if(!_data) {
  fprintf(stderr, "Out of memory\n");
  exit(1);
}
  _data->tag = _app_expr;
  _data->u._app._rator = rator;
  _data->u._app._rest = rest;
  return (void *)_data;
}

int main()
{
exp = (void *)exprr_let(exprr_lambda(exprr_lambda(exprr_if(exprr_zero(exprr_var((void *)0)),exprr_const((void *)1),exprr_mult(exprr_var((void *)0),exprr_app(exprr_app(exprr_var((void *)1),exprr_var((void *)1)),exprr_subr1(exprr_var((void *)0))))))),exprr_mult(exprr_letcc(exprr_app(exprr_app(exprr_var((void *)1),exprr_var((void *)1)),exprr_throw(exprr_var((void *)0),exprr_app(exprr_app(exprr_var((void *)1),exprr_var((void *)1)),exprr_const((void *)4))))),exprr_const((void *)5)));
env = (void *)umweltr_empty();
count = &valuer__m__ofr__m__cps;
mount_tram();
printf("Fact 5: %d\n", (int)v);}

void applyr__m__env()
{
umwelt* _c = (umwelt*)env;
switch (_c->tag) {
case _empty_umwelt: {
fprintf(stderr, "YOU FUCKED UP");
 exit(1);
break; }
case _extendr__m__env_umwelt: {
void *vr__ex__ = _c->u._extendr__m__env._v;
void *envr__ex__ = _c->u._extendr__m__env._env;
if((var == 0)) {
  v = (void *)vr__ex__;
count = &applyr__m__k;

} else {
  env = (void *)envr__ex__;
var = (void *)(void *)((int)var - 1);
count = &applyr__m__env;

}
break; }
}
}

void applyr__m__closure()
{
schluss* _c = (schluss*)rator;
switch (_c->tag) {
case _caltic_schluss: {
void *body = _c->u._caltic._body;
void *envr__ex__ = _c->u._caltic._envr__m__cps;
env = (void *)umweltr_extendr__m__env(rest,envr__ex__);
exp = (void *)body;
count = &valuer__m__ofr__m__cps;
break; }
}
}

void applyr__m__k()
{
continue* _c = (continue*)k;
switch (_c->tag) {
case _empty_continue: {
void *dismount = _c->u._empty._dismount;
_trstr *trstr = (_trstr *)dismount;
longjmp(*trstr->jmpbuf, 1);
break; }
case _kr__m__subr1_continue: {
void *kr__ex__ = _c->u._kr__m__subr1._k;
v = (void *)(void *)((int)v - 1);
k = (void *)kr__ex__;
count = &applyr__m__k;
break; }
case _kr__m__zero_continue: {
void *kr__ex__ = _c->u._kr__m__zero._k;
v = (void *)(v == 0);
k = (void *)kr__ex__;
count = &applyr__m__k;
break; }
case _kr__m__multr__m__outside_continue: {
void *envr__ex__ = _c->u._kr__m__multr__m__outside._envr__m__cps;
void *x = _c->u._kr__m__multr__m__outside._x;
void *kr__ex__ = _c->u._kr__m__multr__m__outside._k;
exp = (void *)x;
env = (void *)envr__ex__;
k = (void *)continuer_kr__m__multr__m__inside(v,kr__ex__);
count = &valuer__m__ofr__m__cps;
break; }
case _kr__m__multr__m__inside_continue: {
void *ur__ex__ = _c->u._kr__m__multr__m__inside._v;
void *kr__ex__ = _c->u._kr__m__multr__m__inside._k;
k = (void *)kr__ex__;
v = (void *)(void *)((int)ur__ex__ * (int)v);
count = &applyr__m__k;
break; }
case _kr__m__ifr__m__inside_continue: {
void *envr__ex__ = _c->u._kr__m__ifr__m__inside._envr__m__cps;
void *conseq = _c->u._kr__m__ifr__m__inside._conseq;
void *alt = _c->u._kr__m__ifr__m__inside._alt;
void *kr__ex__ = _c->u._kr__m__ifr__m__inside._k;
if(v) {
  env = (void *)envr__ex__;
exp = (void *)conseq;
k = (void *)kr__ex__;
count = &valuer__m__ofr__m__cps;

} else {
  exp = (void *)alt;
env = (void *)envr__ex__;
k = (void *)kr__ex__;
count = &valuer__m__ofr__m__cps;

}
break; }
case _kr__m__throwr__m__outside_continue: {
void *envr__ex__ = _c->u._kr__m__throwr__m__outside._envr__m__cps;
void *kr__ex__ = _c->u._kr__m__throwr__m__outside._kr__m__exp;
exp = (void *)kr__ex__;
env = (void *)envr__ex__;
k = (void *)continuer_kr__m__throwr__m__inside(v,env);
count = &valuer__m__ofr__m__cps;
break; }
case _kr__m__throwr__m__inside_continue: {
void *v = _c->u._kr__m__throwr__m__inside._v;
void *envr__ex__ = _c->u._kr__m__throwr__m__inside._envr__m__cps;
k = (void *)v;
count = &applyr__m__k;
break; }
case _kr__m__let_continue: {
void *envr__ex__ = _c->u._kr__m__let._envr__m__cps;
void *body = _c->u._kr__m__let._body;
void *kr__ex__ = _c->u._kr__m__let._k;
exp = (void *)body;
k = (void *)kr__ex__;
env = (void *)umweltr_extendr__m__env(v,envr__ex__);
count = &valuer__m__ofr__m__cps;
break; }
case _kr__m__ratorr__m__outside_continue: {
void *envr__ex__ = _c->u._kr__m__ratorr__m__outside._envr__m__cps;
void *rest = _c->u._kr__m__ratorr__m__outside._rest;
void *kr__ex__ = _c->u._kr__m__ratorr__m__outside._k;
exp = (void *)rest;
env = (void *)envr__ex__;
k = (void *)continuer_kr__m__ratorr__m__inside(v,kr__ex__);
count = &valuer__m__ofr__m__cps;
break; }
case _kr__m__ratorr__m__inside_continue: {
void *vr__ex__ = _c->u._kr__m__ratorr__m__inside._v;
void *kr__ex__ = _c->u._kr__m__ratorr__m__inside._k;
rest = (void *)v;
k = (void *)kr__ex__;
rator = (void *)vr__ex__;
count = &applyr__m__closure;
break; }
}
}

void valuer__m__ofr__m__cps()
{
expr* _c = (expr*)exp;
switch (_c->tag) {
case _const_expr: {
void *ex = _c->u._const._cexp;
v = (void *)ex;
count = &applyr__m__k;
break; }
case _mult_expr: {
void *xr1 = _c->u._mult._nexpr1;
void *xr2 = _c->u._mult._nexpr2;
exp = (void *)xr1;
k = (void *)continuer_kr__m__multr__m__outside(env,xr2,k);
count = &valuer__m__ofr__m__cps;
break; }
case _subr1_expr: {
void *n = _c->u._subr1._nexp;
exp = (void *)n;
k = (void *)continuer_kr__m__subr1(k);
count = &valuer__m__ofr__m__cps;
break; }
case _zero_expr: {
void *n = _c->u._zero._nexp;
exp = (void *)n;
k = (void *)continuer_kr__m__zero(k);
count = &valuer__m__ofr__m__cps;
break; }
case _if_expr: {
void *test = _c->u._if._test;
void *conseq = _c->u._if._conseq;
void *alt = _c->u._if._alt;
exp = (void *)test;
k = (void *)continuer_kr__m__ifr__m__inside(env,conseq,alt,k);
count = &valuer__m__ofr__m__cps;
break; }
case _letcc_expr: {
void *body = _c->u._letcc._body;
exp = (void *)body;
env = (void *)umweltr_extendr__m__env(k,env);
count = &valuer__m__ofr__m__cps;
break; }
case _throw_expr: {
void *kr__m__exp = _c->u._throw._kexp;
void *vr__m__exp = _c->u._throw._vexp;
exp = (void *)kr__m__exp;
k = (void *)continuer_kr__m__throwr__m__outside(env,vr__m__exp);
count = &valuer__m__ofr__m__cps;
break; }
case _let_expr: {
void *e = _c->u._let._exp;
void *body = _c->u._let._body;
exp = (void *)e;
k = (void *)continuer_kr__m__let(env,body,k);
count = &valuer__m__ofr__m__cps;
break; }
case _var_expr: {
void *y = _c->u._var._n;
var = (void *)y;
count = &applyr__m__env;
break; }
case _lambda_expr: {
void *body = _c->u._lambda._body;
v = (void *)schlussr_caltic(body,env);
count = &applyr__m__k;
break; }
case _app_expr: {
void *rator = _c->u._app._rator;
void *rest = _c->u._app._rest;
exp = (void *)rator;
k = (void *)continuer_kr__m__ratorr__m__outside(env,rest,k);
count = &valuer__m__ofr__m__cps;
break; }
}
}

int mount_tram ()
{
srand (time (NULL));
jmp_buf jb;
_trstr trstr;
void *dismount;
int _status = setjmp(jb);
trstr.jmpbuf = &jb;
dismount = &trstr;
if(!_status) {
k= (void *)continuer_empty(dismount);
for(;;) {
count();
}
}
return 0;
}

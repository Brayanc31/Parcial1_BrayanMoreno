%{
#include <stdio.h>
#include <math.h>
extern FILE *yyin;
void yyerror(const char *s);
int yylex(void);
double raiz_newton(double a);
%}

%union {
    double num;
}
%token <num> NUM
%token MAS MENOS POR DIV PARI PARD SQRT
%type <num> expr termino factor

%left MAS MENOS
%left POR DIV
%nonassoc SQRT
%right UMENOS   /* precedencia más alta para el menos unario */

%%

input: /* vacío */ | input linea ;
linea: expr '\n'               { printf("Resultado: %lf\n", $1); }
     | error '\n'               { yyerror("Error en expresión"); }
     ;

expr: termino
    | expr MAS termino          { $$ = $1 + $3; }
    | expr MENOS termino        { $$ = $1 - $3; }
    ;

termino: factor
       | termino POR factor     { $$ = $1 * $3; }
       | termino DIV factor     { $$ = $1 / $3; }
       ;

factor: NUM                     { $$ = $1; }
      | PARI expr PARD          { $$ = $2; }
      | SQRT PARI expr PARD     { $$ = raiz_newton($3); }
      | MENOS factor %prec UMENOS { $$ = -$2; }  /* menos unario */
      ;

%%

double raiz_newton(double a) {
    if (a < 0) {
        fprintf(stderr, "Error: raíz cuadrada de número negativo\n");
        return 0;
    }
    if (a == 0) return 0;
    double x = a / 2.0;
    double tol = 1e-10;
    int max_iter = 100, iter = 0;
    double error;
    do {
        double x_nuevo = (x + a/x) / 2.0;
        error = fabs(x_nuevo - x);
        x = x_nuevo;
        iter++;
    } while (error > tol && iter < max_iter);
    return x;
}

void yyerror(const char *s) {
    fprintf(stderr, "Error sintáctico: %s\n", s);
}

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *f = fopen(argv[1], "r");
        if (!f) {
            perror(argv[1]);
            return 1;
        }
        yyin = f;
    }
    yyparse();
    return 0;
}

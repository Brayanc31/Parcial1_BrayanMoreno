%{
#include "calculadora.tab.h"
#include <stdlib.h>
%}

%%

[0-9]+(\.[0-9]+)?   { yylval.num = atof(yytext); return NUM; }
"sqrt"              { return SQRT; }
"+"                 { return MAS; }
"-"                 { return MENOS; }
"*"                 { return POR; }
"/"                 { return DIV; }
"("                 { return PARI; }
")"                 { return PARD; }
[ \t]+              { /* ignorar espacios */ }
\n                  { return *yytext; }   
.                   { return *yytext; }   

%%

int yywrap() { return 1; }

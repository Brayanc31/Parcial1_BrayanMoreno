grammar Fibonacci;

// Regla principal: el programa consiste en un comando FIBO
prog: comando EOF ;

// Comando FIBO: la palabra 'FIBO' seguida de paréntesis con un número entero
comando: FIBO '(' INT ')' ;

// Tokens (reglas léxicas)
FIBO: 'FIBO' ;
INT : [0-9]+ ;                // uno o más dígitos
WS  : [ \t\r\n]+ -> skip ;    // ignorar espacios, tabs, saltos de línea

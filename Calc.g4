grammar Calc;


expr 
    : fator              
        (PLUS fator      
        | MINUS fator    
        )*
    ;

fator
    : termo 
        (TIMES termo    
        | DIVIDE termo   
        )*
    ;

termo
    : MINUS termo     
    | LPAR expr RPAR
    | INTEGER      
    | FLOAT  
    ;

LPAR    : '(' ;
RPAR    : ')' ;
PLUS    : '+' ;
MINUS   : '-' ;
TIMES   : '*' ;
DIVIDE  : '/' ;

fragment DIGIT  : [0-9] ;

INTEGER : DIGIT+ ;

FLOAT   : DIGIT+ '.' DIGIT* ([eE] (PLUS | MINUS) DIGIT+)?
        | '.' DIGIT+ ([eE] (PLUS | MINUS) DIGIT+)?
        ;

WS      : [ \t\n\r] -> skip;

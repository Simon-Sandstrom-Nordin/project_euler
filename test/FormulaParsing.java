package test;

public class FormulaParsing {

    public static void main(String []args) {



    }

}

// Looks a lot like recursive descent.
// Given:
// <Formel> ::= <Uttryck>  <Operator> <Uttryck>
// <Operator> ::= + | - | *
// <Uttryck> ::= <Tal> | "(" <Formel> ")"
// <Tal> ::= <Siffra> | <Siffra><Siffra>
// <Siffra> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

// recursive descent parser. This'll be used for
// molecular syntax analysis in Python aswell, so pay attention.

// Rude strangers on the internet (well, not all rude) tell me
// the fields of syntax analysis and parsing are my friends in this.
// Parsing Cares.

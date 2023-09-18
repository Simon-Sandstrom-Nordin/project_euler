package test;

import java.util.Scanner;

public class AIcheat {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ange en aritmetisk formel: ");
        String formula = scanner.nextLine();

        try {
            int result = evalueraFormel(formula);
            System.out.println("Resultat: " + result);
        } catch (IllegalArgumentException e) {
            System.out.println("Ogiltig formel: " + e.getMessage());
        }
    }

    public static int evalueraFormel(String formula) {
        formula = formula.replaceAll("\\s+", ""); // Ta bort alla mellanslag
        return evalueraUttryck(formula);
    }

    private static int evalueraUttryck(String expression) {
        if (expression.matches("\\d+")) {   // bara siffror
            return Integer.parseInt(expression);
        } else if (expression.startsWith("(") && expression.endsWith(")")) {    // utvärdera uttryck inom parantesen rekursivt
            return evalueraUttryck(expression.substring(1, expression.length() - 1));   // skapa delsträng och anropa metoden evalueraUttryck
        } else {
            int operatorIndex = hittaOperatorIndex(expression);
            if (operatorIndex == -1) {  // då blir det inget tal men heller inget riktigt uttryck
                throw new IllegalArgumentException("Ogiltigt uttryck: " + expression);
            }

            String operator = expression.substring(operatorIndex, operatorIndex + 1);   // plocka ut operatorn
            String leftExpression = expression.substring(0, operatorIndex);     // plocka ut vänstra halvan
            String rightExpression = expression.substring(operatorIndex + 1);   // plocka ut högra halvan

            int leftValue = evalueraUttryck(leftExpression);    // anropa för vänsterdelen
            int rightValue = evalueraUttryck(rightExpression);  // anropa för högerdelen

            return switch (operator) { // räkna ihop dessa med rätt operator
                case "+" -> leftValue + rightValue;
                case "-" -> leftValue - rightValue;
                case "*" -> leftValue * rightValue;
                default -> throw new IllegalArgumentException("Ogiltig operator: " + operator);
            // notering: Switch är som if-else fast lite coolare (det finns andra anledningar:
                // snabbare ibland, läsbarhet, vi hanterar inga booleans utan snarare strängar i jämför)

            };
        }
    }

    private static int hittaOperatorIndex(String expression) {
        int operatorIndex = -1;
        int parenthesesCount = 0;

        for (int i = 0; i < expression.length(); i++) {
            char c = expression.charAt(i);

            if (c == '(') {
                parenthesesCount++;
            } else if (c == ')') {
                parenthesesCount--;
            } else if (parenthesesCount == 0 && (c == '+' || c == '-' || c == '*')) {
                operatorIndex = i;  // kommer från vänster läsa in första operatorn som inte är i en parantes
                break;
            }
        }

        return operatorIndex;
    }
}

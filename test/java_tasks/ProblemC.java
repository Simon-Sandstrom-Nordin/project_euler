package test.test.java_tasks;
import java.util.Scanner;

public class ProblemC {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String formula = scanner.nextLine();

        try {
            long result = evalueraFormel(formula);
            System.out.println(result);
        } catch (IllegalArgumentException e) {
            System.out.println("Ogiltig formel: " + e.getMessage());
        }
    }

    public static long evalueraFormel(String formula) {
        formula = formula.replaceAll("\\s+", ""); // Ta bort alla mellanslag

        // Ta bort mellanslag runt parenteser
        formula = formula.replaceAll("\\(\\s*", "(");
        formula = formula.replaceAll("\\s*\\)", ")");

        return evalueraUttryck(formula);
    }

    private static boolean parenthesisValidity(String expression) { //special method for determining if surrounding parenthesis should be removed or not
        int counter = 0;    // 0 if we're looking for "(", 1 otherwise

        for (int i = 1; i < expression.length()-1; i++) {
            char c = expression.charAt(i);
            if (c == '(') {
                counter += 1;
            } else if (c==')') {
                counter -= 1;
            }
            if (counter<0) {
                return false;
            }
        }
        return true;

    }

    private static long evalueraUttryck(String expression) {
        // System.out.println(expression);
        // System.out.println(parenthesisValidity(expression));
        if (expression.matches("\\d+")) {
            return Integer.parseInt(expression);
        } else if ((expression.startsWith("(")) && (expression.endsWith(")")) && parenthesisValidity(expression)) {
            return evalueraUttryck(expression.substring(1, expression.length() - 1));
        } else {
            int parenthesesCount = 0;
            int operatorIndex = -1;

            for (int i = 0; i < expression.length(); i++) {
                char c = expression.charAt(i);
                if (c == '(') {
                    parenthesesCount++;
                } else if (c == ')') {
                    parenthesesCount--;
                } else if (parenthesesCount == 0 && (c == '+' || c == '-' || c == '*')) {
                    operatorIndex = i;
                    break;
                }
            }

            if (operatorIndex == -1) {
                throw new IllegalArgumentException("Ogiltigt uttryck: " + expression);
            }

            String operator = expression.substring(operatorIndex, operatorIndex + 1);
            String leftExpression = expression.substring(0, operatorIndex).trim();
            String rightExpression = expression.substring(operatorIndex + 1).trim();

            long leftValue = evalueraUttryck(leftExpression);
            long rightValue = evalueraUttryck(rightExpression);

            if (operator.equals("+")) {
                return leftValue + rightValue;
            } else if (operator.equals("-")) {
                return leftValue - rightValue;
            } else if (operator.equals("*")) {
                return leftValue * rightValue;
            } else {
                throw new IllegalArgumentException("Ogiltig operator: " + operator);
            }
        }
    }

}


// fuska med AIn... försökte iallafall förstå de rekursiva metoderna...
// se AIcheat.java i directoriet över

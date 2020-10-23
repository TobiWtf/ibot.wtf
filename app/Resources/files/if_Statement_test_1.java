import java.util.Random; // Imports tools
import java.util.Arrays;
class main {
    public static void print(String args) { // Easy print function
        System.out.println(args);
    }

    public static String stringify(int args) { // stringify function
        final String result = "" + args + "";
        return result;
    }

    public static void if_statement(Boolean args) { // If else funtion
        if (args == true) { // if (condition) {} else {}
            System.out.println(args); // True
        }
        else {
            print("No"); // False
        }
    }

    public static void start() { // starts this script
        Boolean var = true; // Checks if true cond
        if_statement(var);
        var = false; // Checks if false cond
        if_statement(var);
    }

    public static void main(String[] args) {

        start(); // Calls on start object

    }
}


// This is a test for
// conditional if_statements
// within java, this is
// day two of java And
// i feel less comfortable
// than i did with python
// but i feel good about
// this otherwise.

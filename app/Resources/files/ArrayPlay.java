import java.util.Random; // Imports random
import java.util.Arrays; // Imports array tools
class main {

    public static void print(String args) { // Declares a function
        System.out.println(args); // Prints arguments (args)
    }

    public static String stringify(int args) { // Declares a funtion
        final String result = "" + args + ""; // int arg as string
        return result; // returns the string
    }

    public static int[] range(int Amount) { // Declares a function requiring a
        int start = 0; // Start int         // a array of integers
        int finish = Amount; // Finish int

        int Range[] = new int[Amount]; // Declares an array allocating
                                       // finish ammount memory

        while (start < finish) { // While (condition) brackets to iterate
            Range[start] = start; // iter-i = start\iter
            start += 1; // start\iter + 1
        }
        return Range; // Returns new array of integers
    }

    public static void main(String[] args) { // Declares main function

        final int max = 10; // sets max int
        final int upperbound = 15; // upperbound fo random int
        int min = 0; // sets minimum int (to be changed)

        while (min < max) { // While (condition) brackets to iterate
              Random rand = new Random(); // Declares random object as rand
              final int Value = rand.nextInt(upperbound); // Gets a random int
              System.out.println(Arrays.toString(range(Value))); //Prints
                                                                 // range of
                                                                 // The integer
              min += 1; // changes value of min by one
        }

    }
}

// This is a test while
// i learn how object
// iteration works in
// java, this is day
// 3 of using the
// language and i feel
// more confortable with
// the syntax although it
// is definitely not the
// easiest language

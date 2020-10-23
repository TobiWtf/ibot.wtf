import java.util.Random; // Importd tools

class main {

    public static void print(String args) { // Easy print
        System.out.println(args);
    }

    public static String stringify(int args) { // stringify result
        final String result = "" + args + ""; // string + int + string = string
        return result;
    }

    public static void generate() { // start method

        Random rand = new Random(); // random object

        int done = 0;
        final int max = 100;
        final int upperbound = 25; // Upper for random integer generation

        while (done < max){ // iteration over max and done
            done += 1;
            int int_random = rand.nextInt(upperbound);
            System.out.println(int_random); // prints result od generation
          }

    }


    public static void main(String[] args) {
        generate(); // calls start method
    }
}

// This program puts my new
// skills having learned
// iterating and importing
// it creates a random
// and iterates a while
// loop until finished

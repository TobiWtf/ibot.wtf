class main {

    public static void test_for() { // Start method

      int[] arr = new int[]{ 1,2,3,4,5,6,7,8,9,10 }; // array of integers

      int max = 5;

      for (int i = 0; i < arr.length; i++) // iterates over the items in the
          {                                // array and prints if the item
            if (i < max)                   // is greater than max values
              {                            // (int this case, 5)
                System.out.println(i);     // prints result
              }
            }
    }

    public static void main(String[] args) {
        test_for(); // calls start method
    }
}

// This iterates over
// an array of integers
// and if it is less than
// max, it prints the number

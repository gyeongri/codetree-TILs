import java.io.*;

public class Main {
    public static void print(int n) {
        if (n == 0) {
            return;
        }
        print(n - 1);
        System.out.println("HelloWorld");
    }

    public static void main(String[] args) {
        try {
            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
            int n = Integer.parseInt(bf.readLine().trim());

            if (n < 0) {
                System.out.println("Error: n should be a non-negative integer.");
                return;
            }

            print(n);
        } catch (IOException e) {
            System.out.println("Error: An IOException occurred.");
        } catch (NumberFormatException e) {
            System.out.println("Error: Please enter a valid integer.");
        }
    }
}
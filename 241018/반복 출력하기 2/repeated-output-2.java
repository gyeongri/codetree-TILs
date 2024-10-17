import java.io.*;

public class Main {
    static StringBuilder sb = new StringBuilder();
    public static void print(int n) {
        if (n == 0) {
            return;
        }
        print(n - 1);
        sb.append("HelloWorld\n");
    }

    public static void main(String[] args) throws Exception{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());
        print(n);
        System.out.println(sb);

    }
}
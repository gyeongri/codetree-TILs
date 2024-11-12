import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader bf= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(bf.readLine());
        Integer[] arr = new Integer[n];

        st = new StringTokenizer(bf.readLine());
        for(int i=0; i<n; ++i){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        for(int i=0; i<n; ++i)
            sb.append(arr[i]).append(" ");
        sb.append("\n");
        Arrays.sort(arr, Collections.reverseOrder());
                for(int i=0; i<n; ++i)
            sb.append(arr[i]).append(" ");
        System.out.print(sb);
    }
}
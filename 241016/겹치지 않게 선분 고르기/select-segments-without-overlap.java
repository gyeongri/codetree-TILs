import java.io.*;
import java.util.*;
public class Main {
    static int n, maxCnt;
    static List<int[]> selectedLines = new ArrayList<>();
    static int[][] lines;
    static boolean isOverlapped(int[] cur){//겹치는지 확인
        for(int[] line: selectedLines){
            if ((cur[0]>= line[0] && cur[0]<=line[1]) || (cur[1]>= line[0] && cur[1]<=line[1])) {
                return true;
            }
        }
        return false;
    }

    static void dfs(int depth){
        
        int len = selectedLines.size();
        maxCnt = Math.max(maxCnt, len);

        for(int i=len; i<n; ++i){
            if(isOverlapped(lines[i])) continue;
            selectedLines.add(lines[i]);
            dfs(depth+1);
            selectedLines.remove(lines[i]);
        }

    }

    public static void main(String[] args) throws Exception {
        StringBuilder sb = new StringBuilder();
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(bf.readLine());
       
        lines = new int[n][2];

        for(int i=0; i<n; ++i){
            st = new StringTokenizer(bf.readLine());
            lines[i][0] = Integer.parseInt(st.nextToken());
            lines[i][1] = Integer.parseInt(st.nextToken());
       
        }

        dfs(0);
        sb.append(maxCnt);
        System.out.println(sb);
    }
}
import java.io.*;
import java.util.*;
public class Main {
    static int n, maxCnt;
    static List<int[]> selectedLines = new ArrayList<>();
    static int[][] lines;
    static boolean isOverlapped(int[] line2){//겹치는지 확인
        for(int[] line1: selectedLines){
           if (!(line1[1] < line2[0] || line2[1] < line1[0])) {
            return true;
            }
        }
        return false;
    }

    static void dfs(int depth){
        
        int len = selectedLines.size();
        maxCnt = Math.max(maxCnt, len);

        for(int i=depth; i<n; ++i){
            if(isOverlapped(lines[i])) continue;
            selectedLines.add(lines[i]);
            dfs(i+1);
            selectedLines.remove(selectedLines.size() - 1);
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
        
        // 오른쪽 끝점 기준으로 선분 정렬 (최대한 겹치지 않게 탐색)
        Arrays.sort(lines, Comparator.comparingInt(a -> a[1]));

        dfs(0);
        sb.append(maxCnt);
        System.out.println(sb);
    }
}
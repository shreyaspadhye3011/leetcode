import java.util.*;

class Solution {
    public static void main (String[] args) throws java.lang.Exception {
            Scanner sc = new Scanner(System.in);
            String str = sc.next();
            int n = str.length(); 
            for (int i = 0; i < n; i++) { 

            // Count occurrences of current character 
            int count = 1; 
            while (i < n - 1 && str.charAt(i) == str.charAt(i + 1)) { 
                count++; 
                i++; 
            } 

            // Print character and its count 
            System.out.print(str.charAt(i)); 
            if (count > 1) 
                System.out.print(count); 

            sc.close();
        } 
    }
}
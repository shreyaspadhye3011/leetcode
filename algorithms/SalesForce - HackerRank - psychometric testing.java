// PRoblem: scores is an int array. Return a `count` array such that each element 'i' of the count array is such that  lower[i] <= count[i] <= upper[i]

class Solution {
    public static int[] main(int[] scores, int[] lowerLimits, int[] upperLimits) {
        //java code
        int[] res = new int[lowerLimits.length];
        int n = scores.length;
        
        for(int i = 0; i < lowerLimits.length; i++) {
            int count = 0; 
            count = upperIndex(scores, n, upperLimits[i]) -  
                    lowerIndex(scores, n, lowerLimits[i]) + 1; 
            res[i] = count;
        }
        
        return res; 
    }

    static int lowerIndex(int arr[], int n, int x) 
    { 
        int l = 0, h = n - 1; 
        while (l <= h)  
        { 
            int mid = (l + h) / 2; 
            if (arr[mid] >= x) 
                h = mid - 1; 
            else
                l = mid + 1; 
        } 
        return l; 
    } 
        
    // function to find last index <= y 
    static int upperIndex(int arr[], int n, int y) 
    { 
        int l = 0, h = n - 1; 
        while (l <= h)  
        { 
            int mid = (l + h) / 2; 
            if (arr[mid] <= y) 
                l = mid + 1; 
            else
                h = mid - 1; 
        } 
        return h; 
    }
}
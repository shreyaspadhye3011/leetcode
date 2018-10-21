
import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

class Solution {
  
 static class TreeNode{
    int val;
    TreeNode left, right, parent;
    
    public TreeNode(int val, TreeNode parent){
      this.val = val;
      this.left = null;
      this.right = null;
      this.parent = parent;
    }
  }
  
  static TreeNode root;
  
  public static void main(String[] args) {
    String workDays = "08??840";
    int hours = 24;
    int maxHoursPerDay = 4;
    /*printCombination(workDays, hours, maxHoursPerDay);
    
    root = new TreeNode(5);
    root.left = new TreeNode(2);
    root.right = new TreeNode(8);
    root.left.left = new TreeNode(1);
    root.left.right = new TreeNode(3);
    root.right.left = new TreeNode(6);
    root.right.right = new TreeNode(10);
    root.right.right.right = new TreeNode(15);
    
    System.out.println(listOfDepthsRecursive(root));
    System.out.println(listOfDepthsIterative(root));
    
    System.out.println(checkBSTusingInOrder(root));
    System.out.println(checkBSTusingMinMax(root));*/
    
    // root = new TreeNode(5, null);
    // root.left = new TreeNode(3, root);
    // root.right = new TreeNode(8, root);
    // root.left.left = new TreeNode(1, root.left);
    // root.left.right = new TreeNode(4, root.left);
    // root.left.right.right = new TreeNode(9, root.left.right);
    // root.right.left = new TreeNode(6, root.right);
    // root.right.right = new TreeNode(10, root.right);
    // root.right.right.right = new TreeNode(15, root.right.right);
    
    root = new TreeNode(1, null);
    root.left = new TreeNode(2, root);
    root.right = new TreeNode(3, root);
    root.left.left = new TreeNode(4, root.left);
    // root.left.right = new TreeNode(4, root.left);
    // root.left.right.right = new TreeNode(9, root.left.right);
    // root.right.left = new TreeNode(6, root.right);
    root.right.right = new TreeNode(5, root.right);
    // root.right.right.right = new TreeNode(15, root.right.right);
    
    /*System.out.print("Preorder: ");
    preOrder(root);
    System.out.println("");
    
    //System.out.println(preOrderSuccessor().val);
    //System.out.println(preOrderPredeseccor().val);
    
    System.out.println("");
    System.out.print("Inorder: ");
    inOrder(root);
    System.out.println("");
    
    System.out.println("Inorder Successor of 10 :"+inOrderSuccessor(root.right.right).val);
    System.out.println("Inorder Predeseccor of 6 :"+inOrderPredeseccor(root.right.left).val);
    */
    
    System.out.println("");
    System.out.print("Postorder: ");
    postOrder(root);
    
    System.out.println("Successor of ");
    System.out.println(postOrderSuccessor(root.right.right).val);
    //System.out.println(postOrderPredeseccor().val);
  }
  
  public static TreeNode postOrderSuccessor(TreeNode succToCheck){
     if(succToCheck == null || succToCheck == root)
      return null;
    
    if(succToCheck.parent.right == null || succToCheck == succToCheck.parent.right)
      return succToCheck.parent;
    
    else 
      //if(succToCheck.parent.right != null && succToCheck == succToCheck.parent.left) {
       return findNode(succToCheck.parent.right, succToCheck.parent);
    //}
  }
  
  public static TreeNode findNode(TreeNode parentRight, TreeNode parent){
    if(parentRight == null) return parent;
    
    System.out.println("------"+parentRight.val);
    boolean explored = false;
    
    TreeNode temp = parentRight;
    while(temp.left != null) {
         explored = true;
         temp = temp.left;
    }
    
    if(temp.left == null && !explored)
      return findNode(parentRight.right, parentRight);
    else
      return temp;
  }
  
  public static TreeNode inOrderPredeseccor(TreeNode predeToCheck){
     if(predeToCheck == null)
      return null;
    
    if(predeToCheck.left != null){
      return findMax(predeToCheck.left); 
    } else  {
      
      TreeNode parent = predeToCheck.parent;
      while(parent != null && predeToCheck == parent.left){
        predeToCheck  = parent;
        parent = predeToCheck.parent;
      }
      
      return parent;
    } 
    
  }
  
  public static TreeNode findMax(TreeNode predeToCheck){
    if(predeToCheck == null)
      return null;
    
    while(predeToCheck.right  != null)
      predeToCheck = predeToCheck.right;
    
    return predeToCheck;
  }
  
  public static TreeNode inOrderSuccessor(TreeNode succToCheck){
    if(succToCheck == null)
      return null;
    
    if(succToCheck.right != null){
      return findMin(succToCheck.right); 
    } else {
      
      TreeNode parent = succToCheck.parent;
      while(parent != null && parent.right == succToCheck){
         succToCheck = parent;
         parent = succToCheck.parent;
      }
      
      return parent;
    }
  }
  
  public static TreeNode findMin(TreeNode succToCheck){
    if(succToCheck == null)
      return null;
    
    while(succToCheck.left != null)
      succToCheck = succToCheck.left;
    
    return succToCheck;
  }
  
  public static void preOrder(TreeNode root){
    if(root == null) return;
    System.out.print(root.val+" ");
    preOrder(root.left);
    preOrder(root.right);
  }
  
  public static void inOrder(TreeNode root){
    if(root == null) return;
    inOrder(root.left);
    System.out.print(root.val+" ");
    inOrder(root.right);
  }
  
  public static void postOrder(TreeNode root){
    if(root == null) return;
    postOrder(root.left);
    postOrder(root.right);
    System.out.print(root.val+" ");
  }
  
  public static boolean checkBSTusingMinMax(TreeNode root){
     if(root == null)
       return true;
    
    return checkBSTusingMinMaxHelper(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
  }
  
  public static boolean checkBSTusingMinMaxHelper(TreeNode root, int min, int max){
    if(root == null) return true;
      
    int currVal = root.val;
    if(currVal < min || currVal > max)
      return false;
    
    return checkBSTusingMinMaxHelper(root.left, min, currVal - 1) &&
           checkBSTusingMinMaxHelper(root.right, currVal + 1, max) ;
  }
  
  public static boolean checkBSTusingInOrder(TreeNode root){
    if(root == null)
       return true;
    
   /* List<Integer> res = new ArrayList<>();
    Stack<TreeNode> st = new Stack<>();
    
    while(!st.isEmpty() || root != null){
      if(root != null) {
        
        st.push(root);
        root = root.left;

      } else {
                
        root = st.pop();
        res.add(root.val);
        root = root.right;
        
      }
    }
     System.out.println(res);*/
    
    //write a code to check list is sorted or not
    
    int last = Integer.MIN_VALUE;
    Stack<TreeNode> st = new Stack<>();
    
    while(!st.isEmpty() || root != null){
      if(root != null) {
        
        st.push(root);
        root = root.left;

      } else {
                
        root = st.pop();
        
        System.out.println(last+" "+root.val);
        if(last <= root.val)
          last = root.val;
        else
          return false;
        root = root.right;
      }
    }
   
    return true;
  }
  
  public static List<List<Integer>> listOfDepthsRecursive(TreeNode root){
     List<List<Integer>> res = new ArrayList<>();
     listOfDepthsRecursiveHelper(root, res, 0);
     return res;
  }
  
  public static void listOfDepthsRecursiveHelper(TreeNode root, List<List<Integer>> res, int level) {
    if(root == null) return;
    
    List<Integer> currListData;
    if(res.size() == level)  {
      currListData = new ArrayList<>();
      res.add(currListData);
    } else {
      currListData = res.get(level);
      
    }
    currListData.add(root.val);
  
    listOfDepthsRecursiveHelper(root.left, res, level + 1);
    listOfDepthsRecursiveHelper(root.right, res, level + 1);
  }
  
  public static List<List<Integer>> listOfDepthsIterative(TreeNode root){
     List<List<Integer>> res = new ArrayList<>();
     Stack<TreeNode> st = new Stack<>();
     st.push(root);
     
     while(!st.isEmpty()) {
       List<Integer> tmp = new ArrayList<>();
       Stack<TreeNode> tmpStack = new Stack<>();
       
       while(!st.isEmpty()) {
          TreeNode curr = st.pop();
          tmp.add(curr.val);
          
         if(curr.left != null)
            tmpStack.push(curr.left);
         
         if(curr.right != null)
            tmpStack.push(curr.right);
       }
       
       res.add(tmp);
       st = tmpStack;
     }
     
     return res;
  }
  
  public static void printCombination(String workDays, int hours, int maxHoursPerDay){
     int unknownDays = 0;
     char[] workDaysDatas = workDays.toCharArray();
     for(char workDaysData : workDaysDatas){
       if(workDaysData == '?')
         unknownDays++;
       else
         hours -= workDaysData - '0';
     }
    
    System.out.println("hours.."+hours);
    
     List<Integer> chosen = new ArrayList<>();
     if(unknownDays > 0)
         printCombinationHelper(hours, unknownDays, maxHoursPerDay, chosen);
  }
  
  public static void printCombinationHelper(int remainHours, int unKnownDays, int maxHoursPerDay, List<Integer> chosen) {
     if(unKnownDays == 0){   
       
       if(remainHours > 0)
         return;
       
       StringBuilder sOut = new StringBuilder();
       //sOut.append("1 4 "); 
        for(int chooseVal: chosen){
          if(chooseVal > maxHoursPerDay)
            return;
          
          sOut.append(chooseVal+" ");
        }
       //sOut.append("4 5"); 
       System.out.println(sOut.toString());
       return;
     }
    
     for(int i=0; i<=remainHours; i++){
        chosen.add(i);
        printCombinationHelper(remainHours - i, unKnownDays - 1, maxHoursPerDay, chosen);
        chosen.remove(chosen.size() - 1);
     }
  }
}
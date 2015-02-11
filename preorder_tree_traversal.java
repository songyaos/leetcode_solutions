/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> mylist = new ArrayList<Integer>();
        traverse(root, mylist);
        return  mylist;
    }
    
    public void traverse(TreeNode node, List<Integer> mylist){
        if (node == null){return;}
        mylist.add(node.val);
        traverse(node.left,mylist);
        traverse(node.right,mylist);
        
    }
}
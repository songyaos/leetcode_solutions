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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> mylist =new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode node = root;
        while(!stack.isEmpty() || node!=null){
            if(node !=null){
                stack.push(node);
                node = node.left;
            }
            else{
                node = stack.pop();
                mylist.add(node.val);
                node = node.right;
            }
        }
        return mylist;
    }
}
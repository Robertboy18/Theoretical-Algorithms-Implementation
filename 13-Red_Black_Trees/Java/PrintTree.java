import java.util.LinkedList;

/**
 * Just a helper class to print the binary tree in tree format
 */
public class PrintTree {

  /**
   * This is a helper method to just print the binary tree on console thats why uses an inbuilt LinkedList of java
   * @param root
   */
  public static void printBinaryTree(RBNode root)
  {
    LinkedList<RBNode> treeLevel = new LinkedList<RBNode>();
    treeLevel.add(root);
    LinkedList<RBNode> temp = new LinkedList<RBNode>();
    int counter = 0;
    int height = heightOfTree(root) - 1;
    double numberOfElements
            = (Math.pow(2, (height + 1)) - 1);
    while (counter <= height) {
      RBNode removed = treeLevel.removeFirst();
      if (temp.isEmpty()) {
        printSpace(numberOfElements
                        / Math.pow(2, counter + 1),
                removed);
      }
      else {
        printSpace(numberOfElements
                        / Math.pow(2, counter),
                removed);
      }
      if (removed == null) {
        temp.add(null);
        temp.add(null);
      }
      else {
        temp.add(removed.left);
        temp.add(removed.right);
      }

      if (treeLevel.isEmpty()) {
        System.out.println("");
        System.out.println("");
        treeLevel = temp;
        temp = new LinkedList<>();
        counter++;
      }
    }
  }

  public static void printSpace(double n, RBNode removed)
  {
    for (; n > 0; n--) {
      System.out.print("\t");
    }
    if (removed == null) {
      System.out.print(" ");
    }
    else {
      System.out.print(removed.value + " (" + removed.color.getSymbol() + ")");
    }
  }

  public static int heightOfTree(RBNode root)
  {
    if (root == null) {
      return 0;
    }
    return 1
            + Math.max(heightOfTree(root.left),
            heightOfTree(root.right));
  }
}

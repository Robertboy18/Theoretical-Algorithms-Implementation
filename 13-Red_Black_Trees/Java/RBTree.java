import java.util.Scanner;

public class RBTree {
  public RBNode root;

  public RBTree(int[] nums) {
    root = new RBNode(nums[0]);
    root.color = Color.BLACK;

    for (int i = 1; i < nums.length; i++) {
      insert(nums[i], this);
    }
  }

  public static void insert(int value, RBTree tree) {
    RBNode z = new RBNode(value);
    RBNode y = null;
    RBNode x = tree.root;
    while (x != null) {
      y = x;
      if (z.value < x.value) {
        x = x.left;
      } else {
        x = x.right;
      }
    }

    z.parent = y;
    if (y == null) {
      tree.root = z;
    } else if (z.value < y.value) {
      y.left = z;
    } else {
      y.right = z;
    }
    insertFixup(tree, z);
  }

  public static void insertFixup(RBTree tree, RBNode z) {
    while (z.parent != null && z.parent.color == Color.RED) {
      if (z.parent.parent != null) {
        if (z.parent == z.parent.parent.left) {
          RBNode y = z.parent.parent.right;
          if (y != null && y.color == Color.RED) {
            z.parent.color = Color.BLACK;
            y.color = Color.BLACK;
            z.parent.parent.color = Color.RED;
            z = z.parent.parent;
          } else {
            if (z == z.parent.right) {
              z = z.parent;
              leftRotate(tree, z);
            }
            z.parent.color = Color.BLACK;
            z.parent.parent.color = Color.RED;
            rightRotate(tree, z.parent.parent);
          }
        } else {
          RBNode y = z.parent.parent.left;
          if (y != null && y.color == Color.RED) {
            z.parent.color = Color.BLACK;
            y.color = Color.BLACK;
            z.parent.parent.color = Color.RED;
            z = z.parent.parent;
          } else {
            if (z == z.parent.left) {
              z = z.parent;
              rightRotate(tree, z);
            }
            z.parent.color = Color.BLACK;
            z.parent.parent.color = Color.RED;
            leftRotate(tree, z.parent.parent);
          }
        }
        tree.root.color = Color.BLACK;
      }
    }
  }

  public static void leftRotate(RBTree tree, RBNode x) {
    RBNode y = x.right;
    x.right = y.left;
    if (y.left != null) {
      y.left.parent = x;
    }
    y.parent = x.parent;
    if (x.parent == null) {
      tree.root = y;
    } else if (x == x.parent.left) {
      x.parent.left = y;
    } else {
      x.parent.right = y;
    }
    y.left = x;
    x.parent = y;
  }

  public static void rightRotate(RBTree tree, RBNode x) {
    RBNode y = x.left;
    x.left = y.right;
    if (y.right != null) {
      y.right.parent = x;
    }
    y.parent = x.parent;
    if (x.parent == null) {
      tree.root = y;
    } else if (x == x.parent.right) {
      x.parent.right = y;
    } else {
      x.parent.left = y;
    }
    y.right = x;
    x.parent = y;
  }

  public static RBNode search(RBNode root, int value) {
    if (root == null) {
      return null;
    }
    if (value == root.value) {
      return root;
    }

    if (value < root.value) {
      return search(root.left, value);
    } else {
      return search(root.right, value);
    }
  }

  public static int minimum(RBNode root) {
    RBNode temp = root;
    while (temp.left != null) {
      temp = temp.left;
    }
    return temp.value;
  }

  public static int maximum(RBNode root) {
    RBNode temp = root;
    while (temp.right != null) {
      temp = temp.right;
    }
    return temp.value;
  }

  public static int successor(RBNode node) {
    RBNode x = node;
    if (x.right != null) {
      return minimum(x.right);
    }
    RBNode y = x.parent;
    while (y != null && x == y.right) {
      x = y;
      y = y.parent;
    }
    if (y == null) {
      System.out.println("No successor found");
      return -1;
    }
    return y.value;
  }

  public static int predecessor(RBNode node) {
    RBNode x = node;
    if (x.left != null) {
      return maximum(x.left);
    }
    RBNode y = x.parent;
    while (y != null && x == y.left) {
      x = y;
      y = y.parent;
    }
    if (y == null) {
      System.out.println("No predecessor found");
      return -1;
    }
    return y.value;
  }

  public static void inorder(RBNode node) {
    if (node != null) {
      inorder(node.left);
      System.out.println(node.value);
      inorder(node.right);
    }
  }

  public static void transplant(RBTree tree, RBNode u, RBNode v) {
    if (u.parent == null) {
      tree.root = v;
    } else if (u == u.parent.left) {
      u.parent.left = v;
    } else {
      u.parent.right = v;
    }
    if (v != null) {
      v.parent = u.parent;
    }
  }

  public static void delete(RBTree tree, RBNode z) {
    if (z.left == null) {
      transplant(tree, z, z.right);
    } else if (z.right == null) {
      transplant(tree, z, z.left);
    } else {
      RBNode y = search(tree.root, minimum(z.right));
      if (y.parent != z) {
        transplant(tree, y, y.right);
        y.right = z.right;
        y.right.parent = y;
      }
      transplant(tree, z, y);
      y.left = z.left;
      y.left.parent = y;
    }
  }

  /**
   * Randomly tests the created Red black tree.
   * @param args
   */
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int[] nums = new int[] {2, 5, 6, 78, 79, 80, 91, 92, 93, 94, 23, 24, 25, 26};
    RBTree tree = new RBTree(nums);
    PrintTree.printBinaryTree(tree.root);

    while (true) {
      System.out.println("Enter your operation ");
      String input = scanner.nextLine();

      String[] split = input.split(" ");
      if (split[0].equals("insert")) {
        int value = Integer.parseInt(split[1]);
        System.out.println("Inserting " + value);
        insert(value, tree);
        PrintTree.printBinaryTree(tree.root);

      } else if (split[0].equals("search")) {
        int value = Integer.parseInt(split[1]);
        RBNode found = search(tree.root, value);
        System.out.println("Searching " + value);

        if (found != null) {
          System.out.println("Found");
        } else {
          System.out.println("Not found");
        }

      } else if (split[0].equalsIgnoreCase("sort")) {
        System.out.println("Inorder traversal is ");
        inorder(tree.root);
      } else if (split[0].equalsIgnoreCase("min")) {
        System.out.println("Finding minimum");
        System.out.println(minimum(tree.root));
      } else if (split[0].equalsIgnoreCase("max")) {
        System.out.println("Finding maximum");
        System.out.println(maximum(tree.root));
      } else if (split[0].equalsIgnoreCase("successor")) {
        int value = Integer.parseInt(split[1]);
        RBNode node = search(tree.root, value);

        if (node != null) {
          System.out.println("Finding successor of " + value);
          System.out.println(successor(node));
        } else {
          System.out.println("Node not found");
        }

      } else if (split[0].equalsIgnoreCase("predecessor")) {

        int value = Integer.parseInt(split[1]);
        RBNode node = search(tree.root, value);

        if (node != null) {
          System.out.println("Finding predecessor of " + value);
          System.out.println(predecessor(node));
        } else {
          System.out.println("Node not found");
        }

      } else if (split[0].equalsIgnoreCase("delete")) {
        int value = Integer.parseInt(split[1]);
        RBNode node = search(tree.root, value);
        if (node != null) {
          delete(tree, node);
          PrintTree.printBinaryTree(tree.root);
        } else {
          System.out.println("Value not found");
        }
      } else {
        System.out.println("Unsupported operation");
        return;
      }

    }
  }

}

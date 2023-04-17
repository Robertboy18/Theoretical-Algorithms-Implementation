public class RBNode {
  public int value;
  public RBNode left;
  public RBNode right;
  public RBNode parent;
  public Color color;

  public RBNode(int value) {
    this.value = value;
    this.color = Color.RED;
  }
}

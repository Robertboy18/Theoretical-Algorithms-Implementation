public enum Color {
  RED("R"), BLACK("B");

  final String symbol;
  Color(String symbol) {
    this.symbol = symbol;
  }

  public String getSymbol() {
    return symbol;
  }
}

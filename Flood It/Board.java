import java.awt.*;
import java.util.Iterator;

public class Board {
  List<Tile> inside, outside;
  private List<Tile> perimeter;
  private int size;

  /**
   * Constructs a square game board of the given size, initializes the list of
   * inside tiles to include just the tile in the upper left corner, and puts
   * all the other tiles in the outside list.
   */

  public Board(int size) {
    // A tile is either inside or outside the current flooded region.
    inside = new DoublyLinkedList<>();
    outside = new DoublyLinkedList<>();
    this.size = size;
    for (int y = 0; y < size; y++)
      for (int x = 0; x < size; x++) {
        Coord coord = new Coord(x, y);
        outside.add(new Tile(coord));
      }
    // Move the corner tile into the flooded region.
    Tile corner = get(Coord.ORIGIN);
    outside.remove(corner);
    inside.add(corner);
  }


  public Tile get(Coord coord) {
    if(!coord.onBoard(getSize())){ // check to make sure the given coord is on the board
      throw new CoordOutOfBoundsException();
    }
    for(Tile t : outside){
      if(t.getCoord().equals(coord))  // Outside is normally the shorter list so this solution is ooptimal
        return t;
    }
    for(Tile t : inside){
      if(t.getCoord().equals(coord))
        return t;
    }

    throw new CoordOutOfBoundsException();
  }

  /**
   * Returns the size of this board.
   */

  public int getSize() {
    return size;
  }

  public boolean fullyFlooded() {
    if(outside.size() == 0)  // check if outside is empty
      return true;
    return false;
  }


  public boolean floodHelpOther(){   // irrelevent method
    List<Coord> tempList;
    perimeter = new DoublyLinkedList<>();  // for suggest
    boolean returnValue = false;  // how we know when to stop updating
    tempList = new DoublyLinkedList<>();
    tempList = inside.get(0).getCoord().neighbors(getSize());
    for(Coord c : tempList){
      Tile tempTile = get(c);
      if(tempTile.getColor() == inside.get(0).getColor()){
        outside.remove(tempTile);
        inside.add(tempTile);
        returnValue = true;
      }
    }
    return returnValue;
  }


  public void flood(WaterColor color){
    if(color == inside.get(0).getColor())  // save a little time
      return;
    assert(inside.size() + outside.size() == getSize() * getSize());
    perimeter = new DoublyLinkedList<>();   // refresh the perimeter list
    floodHelp(color, inside);  // call help, first on the inside tiles
    //System.out.println(inside.size() + "  " + outside.size());
    /*for(Tile t : inside) {
      System.out.println(t.getColor());
      System.out.println(t.getCoord());
    }*/

  }


  public void floodHelp(WaterColor color, List<Tile> edge){
    List<Tile> edgeList;
    edgeList = new DoublyLinkedList<>();  // these are the next tiles, whose neighbors we will be checking
    boolean returnValue = false;
    for(Tile t : edge){
      t.setColor(color);
      List<Coord> neighbors = t.getCoord().neighbors(getSize());
      for(Coord pair : neighbors){
        if(outside.contains(new Tile(pair, color))){
          Tile temp = get(pair);//new Tile(pair, color);
          outside.remove(temp);
          edgeList.add(temp);
          returnValue = true;
        }
      }
    }
    for(Tile t : edgeList){
      perimeter.add(t);
      inside.add(t);  // add to inside outside of the iterator for first case
    }

    if(returnValue){
      floodHelp(color, edgeList);  // keep going when changes are made
    }
  }

  /**
   public void flood(WaterColor color) {
   boolean keepGoing = true;
   do{
   keepGoing = floodHelp(color);
   System.out.println(keepGoing);
   }while(keepGoing);
   }

   public boolean floodHelp(WaterColor color) {
   boolean returnValue = false;
   for (Tile t : inside) {
   t.setColor(color);
   List<Coord> neighbors;
   neighbors = t.getCoord().neighbors(getSize());
   for (Coord set : neighbors) {
   if (outside.contains(new Tile(set, color))) {
   System.out.println("In" + inside.size() + "Out " + outside.size());
   returnValue = true;
   Tile tempTile = get(set);
   outside.remove(tempTile);
   inside.add(tempTile);

   }
   }
   }return returnValue;
   }
   **/

  public WaterColor suggest() {       // my suggest method takes Board's updated list of the perimeter.  It checks the colors of all the neighbors of the perimeter tallies them up to find the mode.  i think this is the best way to solve suggest because it has the best immediete impact. Although this method does not work properly I figured you would rather see my idea than an effortless solution. If I were to legimetly find the best next move I would generate a tree of all possible games for the next n remaining moves.  I would search the tree for the nearest solved board, then return the next step in the path towards that board. This method, however would be tremendously slow
    List<WaterColor> tempList;
    List<Integer> tempList2;
    List<Coord> tempList3;
    tempList = new DoublyLinkedList<>();
    tempList2 = new DoublyLinkedList<>();
    tempList3 = new DoublyLinkedList<>();
    for(Tile t : perimeter){
      tempList3 = t.getCoord().neighbors(getSize());
      for(Coord u : tempList3)
        tempList.add(get(u).getColor());
    }
    int pink, yellow, blue, red, cyan;
    pink = yellow = blue = red = cyan = 0;
    for(WaterColor w : tempList){
      switch(w){
        case PINK: pink++;
          break;
        case YELLOW: yellow++;
          break;
        case BLUE: blue++;
          break;
        case RED: red++;
          break;
        case CYAN: cyan++;
          break;
      }
    }
    tempList2.add(pink);
    tempList2.add(yellow);
    tempList2.add(blue);   // avoid using arrays
    tempList2.add(red);
    tempList2.add(cyan);
    WaterColor mode;
    if(WaterColor.PINK.equals(inside.get(0).getColor()))  //SLOW
      mode = WaterColor.YELLOW;
    else
      mode = WaterColor.PINK;
    int modeCount = -1;
    int index = 0;
    for(Integer i : tempList2){
      if(i > modeCount) {
        modeCount = i;
        switch(index){
          case 0:  mode = WaterColor.PINK;
            break;
          case 1:  mode = WaterColor.YELLOW;
            break;
          case 2: mode = WaterColor.BLUE;
            break;
          case 3:  mode = WaterColor.RED;
            break;
          case 4: mode = WaterColor.CYAN;
            break;

        }
        ++index;
      }
    }
    return mode;
  }


  /**
   * Returns a string representation of this board. Tiles are given as their
   * color names, with those inside the flooded region written in uppercase.
   */

  public String toString() {
    StringBuilder ans = new StringBuilder();
    for (int y = 0; y < size; y++) {
      for (int x = 0; x < size; x++) {
        Tile curr = get(new Coord(x, y));
        WaterColor color = curr.getColor();
        ans.append(String.format("%-8s",
                inside.contains(curr) ?
                        color.toString().toUpperCase() :
                        color));
      }
      ans.append("\n");
    }
    return ans.toString();
  }

  /**
   * Simple testing.
   */
  public static void main(String... args) {
    // Print out boards of size 1, 2, ..., 5
    int n = 5;
    for (int size = 1; size <= n; size++) {
      Board someBoard = new Board(size);
      System.out.println(someBoard);
    }
  }
}

class CoordOutOfBoundsException extends IndexOutOfBoundsException {

}


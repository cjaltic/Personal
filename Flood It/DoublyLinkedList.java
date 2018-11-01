import java.util.Iterator;
import java.util.ConcurrentModificationException;
import java.util.NoSuchElementException;

interface List<T> extends Iterable<T> {
  void add(T x);  // simple add
  boolean remove(T removeData);
  T remove(int i);
  T get(int i);
  boolean contains(T x);
  int size();
  default boolean isEmpty() {
    return size() == 0;
  }
}

public class DoublyLinkedList<T> implements List<T> {

  /**
   * Node is a pair containing a data field and pointers to
   * the previous and next nodes in the list.
   */

  class Node {
    T data;
    Node next, prev;

    Node(T data) {
      this(data, null, null);
    }

    Node(T data, Node prev, Node next) {
      this.data = data;
      this.prev = prev;
      this.next = next;
    }
  }

  final Node head; // always points to the headnode for this list
  int n;           // the number of nodes in this list, initially 0
  int modCount;

  /**
   * Creates the empty list.
   */

  public DoublyLinkedList() {
    // TODO: Create the headnode.
    // Note that the prev and next fields in the headnode should
    // point back to the headnode.
    head = new Node(null);
    head.prev = head.next = head;
    modCount = 0;
    n = 0;
  }

  /**
   * Inserts the value x at the end of this list.
   */

  public void add(T x) {
    // TODO: This must run in O(1) time.
    Node t = new Node(x, head.prev, head);
    head.prev.next = head.prev = t;
    modCount++;
    n++;
  }

  /**
   * Removes the element at index i from this list.
   * @return the data in the removed node.
   * @throw IndexOutOfBoundsException iff i is out of range for this list.
   */

  public boolean remove(T removeData){
    int c = 0;
    Node t = head.next; // skip over head node
    while(c < n){
      if(t.data.equals(removeData)){
        t.prev.next = t.next;
        t.next.prev = t.prev;
        modCount++;
        n--;
        return true;
      }
      else{
        t = t.next;
        c++;
      }
    }
    return false;
  }

  public T remove(int i) {
    if (i < 0 || i >= size())
      throw new IndexOutOfBoundsException();
    // TODO: Don't forget to skip over the headnode.
    int c = 0;
    Node t = head.next;
    while(c < i){
      t = t.next;
      c++;}
    t.prev.next = t.next;
    t.next.prev = t.prev;
    modCount--;
    n--;
    return t.data;
  }

  /**
   * Returns the i-th element from this list, where i is a zero-based
   * index.
   * @throw IndexOutOfBoundsException iff i is out of range for this list.
   */

  public T get(int i) {
    if (i < 0 || i >= size())
      throw new IndexOutOfBoundsException();
    // TODO: Don't forget to skip over the headnode.
    int c = 0;
    Node t = head.next; // skipping over head node
    while(t != null){
      if(i == c){
        return t.data;
      }
      t = t.next;
      c++;
    }
    return null; // should be unreachable
  }

  /**
   * Returns true iff the value x appears somewhere in this list.
   */

  public boolean contains(T x) {
    // TODO: Don't forget to skip over the headnode.
    Node t = head.next; // skipping over head node
    if(x == null)
      return false;
    while(t != head){
      if(x.equals(t.data)){
        return true;
      }
      t = t.next;
    }
    return false;
  }

  /**
   * Returns the number of elements in this list.
   */

  public int size() {
    return n;
  }

  /**
   * Returns an iterator for this list.
   */

  public Iterator<T> iterator() {
    return new Iterator<T>() {
      int savedModCount = modCount;
      public boolean removable = false;
      Node t = head.next; // skipp over head node

      public boolean hasNext() {
        return t != head;
      }

      public T next() {
        //  first check if we need to throw exceptions
        if(!hasNext()){
          throw new NoSuchElementException();
        }
        if(modCount != savedModCount){
          throw new ConcurrentModificationException();
        }

        T returnData = t.data;
        t = t.next;
        removable = true;
        return returnData;

      }

      public void remove() {
        // TODO: This must run in O(1) time.  This method can be
        // called only once per call to next().
        // Throw an Illegal StateException if next() has not yet been
        // called, or remove() has already been called after the last
        // call to next().

        // first check for exception
        if(!removable){
          throw new IllegalStateException();
        }
        t.prev.prev.next = t;
        t.prev = t.prev.prev;
        modCount++;
        savedModCount++;
        n--;
        removable = false;
      }
    };
  }

  /**
   * Returns a string representing this list (resembling a Racket list).
   */

  public String toString() {
    if (isEmpty())
      return "()";
    Iterator<T> it = iterator();
    StringBuilder ans = new StringBuilder("(").append(it.next());
    while (it.hasNext())
      ans.append(" ").append(it.next());
    return ans.append(")").toString();
  }

  /**
   * Simple testing to get you started. Add more tests of your own!
   */

  public static void main(String... args) {
    List<Integer> xs = new DoublyLinkedList<>();
    int[] a = new int[] { 4, 3, 6, 5, 7, 8 };
    for (int x : a)
      xs.add(x);
    assert 6 == xs.size();
    for (int i = 0; i < a.length; i++)
      assert xs.get(i) == a[i];
    assert !xs.contains(null);
    for (int x : a)
      assert xs.contains(x);
    assert "(4 3 6 5 7 8)".equals(xs.toString());
    assert xs.remove(0) == 4;
    assert xs.remove(1) == 6;
    assert 4 == xs.size();
    assert "(3 5 7 8)".equals(xs.toString());
    while (!xs.isEmpty())
      xs.remove(xs.size() - 1);
    assert 0 == xs.size();
    assert "()".equals(xs.toString());
    for (int x : a)
      xs.add(x);
    assert "(4 3 6 5 7 8)".equals(xs.toString());
    for (int x : xs)
      assert xs.contains(x);
    Iterator<Integer> it = xs.iterator();
    try {
      it.remove();
      assert false;
    }
    catch (IllegalStateException ex) {
    }
    assert "(4 3 6 5 7 8)".equals(xs.toString());
    assert it.hasNext();
    assert 4 == it.next();
    it.remove();
    assert "(3 6 5 7 8)".equals(xs.toString());
    try {
      it.remove();
      assert false;
    }
    catch (IllegalStateException ex) {
    }
    int x;
    it = xs.iterator();
    while (it.hasNext())
      if (it.next() % 2 == 0)
        it.remove();
    assert 3 == xs.size();
    assert "(3 5 7)".equals(xs.toString());
    try {
      for (Integer i : xs) {
        if (i != 3)
          xs.remove(0);
      }
      assert false;
    }
    catch (ConcurrentModificationException ex) {
    }
    assert "(5 7)".equals(xs.toString());
    try {
      for (Integer i : xs)
        xs.add(i);
      assert false;
    }
    catch (ConcurrentModificationException ex) {
    }
    assert "(5 7 5)".equals(xs.toString());
    System.out.println("All tests passed...");
  }
}
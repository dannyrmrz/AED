package HDT7;

public class BSTNode<K extends Comparable<K>, V> {
    K key;
    V value;
    BSTNode<K, V> left, right;

    public BSTNode(K key, V value) {
        this.key = key;
        this.value = value;
        left = right = null;
    }
}

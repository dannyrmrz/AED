package HDT7;

public class BinaryTree<K extends Comparable<K>, V> {
    private BSTNode<K, V> root;

    public BinaryTree() {
        root = null;
    }

    public void insert(K key, V value) {
        root = insertRec(root, key, value);
    }

    private BSTNode<K, V> insertRec(BSTNode<K, V> node, K key, V value) {
        if (node == null) {
            node = new BSTNode<>(key, value);
            return node;
        }

        if (key.compareTo(node.key) < 0)
            node.left = insertRec(node.left, key, value);
        else if (key.compareTo(node.key) > 0)
            node.right = insertRec(node.right, key, value);

        return node;
    }

    // Método para recorrer el árbol en inOrder y imprimir valores
    public void inOrder() {
        inOrderRec(root);
    }

    private void inOrderRec(BSTNode<K, V> node) {
        if (node != null) {
            inOrderRec(node.left);
            System.out.println(node.key + " - " + node.value);
            inOrderRec(node.right);
        }
    }

    // Método de búsqueda
    public V search(K key) {
        BSTNode<K, V> result = searchRec(root, key);
        if (result != null) {
            return result.value;
        } else {
            return null;
        }
    }

    private BSTNode<K, V> searchRec(BSTNode<K, V> node, K key) {
        if (node == null || node.key.equals(key))
            return node;

        if (node.key.compareTo(key) > 0)
            return searchRec(node.left, key);

        return searchRec(node.right, key);
    }
}


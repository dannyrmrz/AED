package HDT7;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class BSTNodeTest {

    @Test
    public void testBSTNodeInitialization() {
        // Arrange
        Integer key = 10;
        String value = "value";
        
        // Act
        BSTNode<Integer, String> node = new BSTNode<>(key, value);
        
        // Assert
        assertEquals(key, node.key);
        assertEquals(value, node.value);
        assertEquals(null, node.left);
        assertEquals(null, node.right);
    }

    @Test
    public void testBSTNodeWithLeftAndRightChild() {
        // Arrange
        Integer key1 = 10;
        String value1 = "value1";
        Integer key2 = 5;
        String value2 = "value2";
        Integer key3 = 15;
        String value3 = "value3";

        // Act
        BSTNode<Integer, String> rootNode = new BSTNode<>(key1, value1);
        rootNode.left = new BSTNode<>(key2, value2);
        rootNode.right = new BSTNode<>(key3, value3);

        // Assert
        assertEquals(key1, rootNode.key);
        assertEquals(value1, rootNode.value);
        assertEquals(key2, rootNode.left.key);
        assertEquals(value2, rootNode.left.value);
        assertEquals(key3, rootNode.right.key);
        assertEquals(value3, rootNode.right.value);
    }
}

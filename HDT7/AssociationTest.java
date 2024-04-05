package HDT7;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class AssociationTest {

    @Test
    public void testAssociationInitialization() {
        // Arrange
        Integer key = 1;
        String value = "value";
        
        // Act
        Association<Integer, String> association = new Association<>(key, value);
        
        // Assert
        assertEquals(key, association.getKey());
        assertEquals(value, association.getValue());
    }
}

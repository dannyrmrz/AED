package HDT7;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class DictionaryTranslatorTest {
    
    @Test
    public void testDetectLanguage_English() {
        BinaryTree<String, Association<String, String>> englishBST = new BinaryTree<>();
        BinaryTree<String, Association<String, String>> spanishBST = new BinaryTree<>();
        BinaryTree<String, Association<String, String>> frenchBST = new BinaryTree<>();
        
        Scanner scanner = new Scanner("Hello world");
        
        String detectedLanguage = DictionaryTranslator.detectLanguage(scanner, englishBST, spanishBST, frenchBST);
        
        assertEquals("English", detectedLanguage);
    }
    
    @Test
    public void testTranslateWord_EnglishToSpanish() {
        BinaryTree<String, Association<String, String>> englishBST = new BinaryTree<>();
        BinaryTree<String, Association<String, String>> spanishBST = new BinaryTree<>();
        BinaryTree<String, Association<String, String>> frenchBST = new BinaryTree<>();
        
        englishBST.insert("hello", new Association<>("hello", "hola"));
        englishBST.insert("world", new Association<>("world", "mundo"));
        
        String translatedWord = DictionaryTranslator.translateWord("hello", "English", englishBST, spanishBST, frenchBST);
        
        assertEquals("hola", translatedWord);
    }
    
    @Test
    public void testTranslateWord_SpanishToEnglish() {
        BinaryTree<String, Association<String, String>> englishBST = new BinaryTree<>();
        BinaryTree<String, Association<String, String>> spanishBST = new BinaryTree<>();
        BinaryTree<String, Association<String, String>> frenchBST = new BinaryTree<>();
        
        spanishBST.insert("hola", new Association<>("hola", "hello"));
        spanishBST.insert("mundo", new Association<>("mundo", "world"));
        
        String translatedWord = DictionaryTranslator.translateWord("hola", "Spanish", englishBST, spanishBST, frenchBST);
        
        assertEquals("hello", translatedWord);
    }
}

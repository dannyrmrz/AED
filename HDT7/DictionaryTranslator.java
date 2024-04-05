package HDT7;

import java.io.File;
import java.util.HashMap;
import java.util.Scanner;

public class DictionaryTranslator {
    private static BinaryTree<String, Association<String, String>> englishBST = new BinaryTree<>();
    private static BinaryTree<String, Association<String, String>> spanishBST = new BinaryTree<>();
    private static BinaryTree<String, Association<String, String>> frenchBST = new BinaryTree<>();

    public static void main(String[] args) {
        // La inicialización de BSTs y la carga del diccionario se asumen completadas aquí

        try {
            // Procesar el archivo texto.txt para detectar el idioma
            File textFile = new File("texto.txt");
            Scanner textScanner = new Scanner(textFile);
            String language = detectLanguage(textScanner, englishBST, spanishBST, frenchBST);

            System.out.println("Idioma detectado: " + language);
            
            // Reset scanner para empezar la traducción desde el principio del archivo
            textScanner = new Scanner(textFile);
            while (textScanner.hasNext()) {
                String word = textScanner.next();
                String translatedWord = translateWord(word, language, englishBST, spanishBST, frenchBST);
                System.out.print(translatedWord + " ");
            }
            textScanner.close();

        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    // Método para detectar el idioma del texto
    private static String detectLanguage(Scanner scanner, BinaryTree<String, Association<String, String>> englishBST, BinaryTree<String, Association<String, String>> spanishBST, BinaryTree<String, Association<String, String>> frenchBST) {
        int englishCount = 0, spanishCount = 0, frenchCount = 0;
        
        while (scanner.hasNext()) {
            String word = scanner.next();
            if (englishBST.search(word) != null) englishCount++;
            if (spanishBST.search(word) != null) spanishCount++;
            if (frenchBST.search(word) != null) frenchCount++;
        }
        
        if (englishCount >= spanishCount && englishCount >= frenchCount) return "English";
        if (spanishCount >= englishCount && spanishCount >= frenchCount) return "Spanish";
        return "French";
    }

    // Método para traducir una palabra basada en el idioma detectado
    private static String translateWord(String word, String language, BinaryTree<String, Association<String, String>> englishBST, BinaryTree<String, Association<String, String>> spanishBST, BinaryTree<String, Association<String, String>> frenchBST) {
        Association<String, String> association;
        switch (language) {
            case "English":
                association = spanishBST.search(word);
                break;
            case "Spanish":
                association = englishBST.search(word);
                break;
            case "French":
                association = englishBST.search(word); // Asumiendo que queremos traducir a inglés por defecto
                break;
            default:
                return "*" + word + "*";
        }
        return (association == null) ? ("*" + word + "*") : association.getValue();
    }
}

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

  public static void main() {
    ArrayList<Character> res = new ArrayList<>();
    try (BufferedReader br = new BufferedReader(new FileReader("input.txt"))) {
      String line;
      while ((line = br.readLine()) != null) {
        int first = -1, last = -1;
        for (int i = 0; i < line.length(); i++) {
          if (Character.isDigit(line.charAt(i))) {
            System.out.println("Hello");
          }
        }
      }
    } catch (IOException e) {
      System.out.println("An error has occured");
    }
  }
}

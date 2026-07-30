//Abraham Sharum
//September 4, 2024 11:00PM
//PS1
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.regex.*;

public class UAStringParser {
    public static void main(String[] args) throws IOException {
        int matchingTokens = 0;
        
        if(args.length != 2) {
            System.out.println("Please inculde two command line arguments: \n 1: Input file \n 2: Regular Expression");
            System.exit(0);
        }

        //Create a string from the contents of the file.
        Path filePath = Path.of(args[0]);
        String content = Files.readString(filePath);

        Pattern p;

        try {
            p = Pattern.compile(args[1]);
        } catch (PatternSyntaxException exception) {
            System.out.println("The regular expression used contains incorrect syntax: " + args[1]);
            return;
        }

        //Create an array of tokens split by whitespace and newlines
        String[] tokens = content.split("\\s+");

        //Evaluate regex
        ArrayList<String> matching = new ArrayList<>();

        for (String t : tokens) {
            Matcher m = p.matcher(t);

            if (m.find()) {
                matchingTokens++;
                matching.add(t);
                System.out.println(t);
            }
        }

        //Output
        System.out.printf("Number of matching tokens: %-5d\n",matchingTokens);
        System.out.printf("Total tokens: %d \n",tokens.length);

    }

}
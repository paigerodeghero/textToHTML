import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class textToHtml {
    public static void main(String[] args) {
        try {
            Scanner scanner = new Scanner(new File("src/templateText.txt")) ;
            convertToHtml(scanner);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void convertToHtml(Scanner scanner) throws IOException {
        FileWriter myWriter = new FileWriter("index.html");
        try {
            myWriter.write("<!DOCTYPE html>\n" +
                    "<html>\n" +
                    "    <head>\n" +
                    "        <title>Project for Grad Students (Paige Rodeghero's CPSC 6720) </title>\n" +
                    "    </head>\n" +
                    "    <body>\n" +
                    "        <p>Project for Grad Students (Paige Rodeghero's CPSC 6720)</p>\n");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        boolean flag1 = false, flag2= false;
        int count=0;
        while(scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if(line.indexOf("Category: ")!=-1) {
                if (flag1){
                    myWriter.write("        </ul>\n");
                    flag1=false;
                }
                myWriter.write("       <h1>"+line.substring(line.indexOf(": ")+2)+"</h1>\n");
                count=1;
            }
            else if (line.indexOf("[")!=-1){
                if (count==1){
                    myWriter.write("        <ul>\n");
                    count=0;
                    flag2=true;
                }
                myWriter.write("            <li><a href=\""+line.substring(line.indexOf("(")+1, line.indexOf(")"))+"\">"
                +line.substring(line.indexOf("[")+1, line.indexOf("]"))+"</a></li>\n");
                flag1=true;
            }
        }
        if (flag2){
            myWriter.write("        </ul>\n");
        }
        myWriter.write("</body>\n" +
                "</html>");
        myWriter.close();
        System.out.println("Successfully wrote to the file.");
    }
}

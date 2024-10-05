import java.io.*;
import java.time.LocalDate;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        LocalDate today = LocalDate.now();
        
        bw.write(today.toString());

        bw.flush();
        bw.close();
    }
}
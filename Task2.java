package dataMaining;

import java.io.*;
import java.util.*;

public class Task2 {

    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();

        // reading transactions.csv with purchasing power calculation
        try (BufferedReader reader = new BufferedReader(new FileReader("src/dataMaining/transactions.csv"))) {
            while (reader.ready()) {
                String[] line = reader.readLine().split(";");
                String PROD_CODE = line[0];
                map.putIfAbsent(PROD_CODE, 0);
                map.put(PROD_CODE, map.get(PROD_CODE) + 1);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

//        // sorting the map by values when saving
//        // the specified key match and writing to a file
//        try (BufferedWriter writer = new BufferedWriter(new FileWriter("src/dataMaining/out.csv"))) {
//            List<Map.Entry<String, Integer>> toSort = new ArrayList<>(map.entrySet());
//            toSort.sort(Map.Entry.comparingByValue(Comparator.naturalOrder()));
//            for (Map.Entry<String, Integer> entry : toSort) {
//                writer.write(entry.getKey() + ";" + entry.getValue() + "\n");
//            }
//        } catch (IOException e) {
//            e.printStackTrace();
//        }

        // Creating an offer for the buyer of the most popular products.
        // The buyer will be offered 10 products with the highest purchasing power.
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("src/dataMaining/offers.csv"))) {
            List<Map.Entry<String, Integer>> toSort = new ArrayList<>(map.entrySet());
            toSort.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));
            int topCount = 0;
            for (Map.Entry<String, Integer> entry : toSort) {
                writer.write(entry.getKey() + ";" + entry.getValue() + "\n");
                if (++topCount == 10) break;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.Scanner;

public final class AppDataCounter {
  public static void main(String[] args) throws Exception {
    new AppDataCounter();
  }

  private int amountPythonFiles;
  private int amountPackages;
  private int amountDefinitions;
  private int amountClasses;
  private int amountLinesOfCode;
  private int amountImages;

  private AppDataCounter() throws Exception {
    Path path = Paths.get("C:\\Users\\ialfa\\PycharmProjects\\BoatWars\\boat-wars\\src");
    if (!Files.exists(path)) {
      throw new InvalidPathException("Missing:", "Could not find " + path);
    }

    Files.walkFileTree(path, new SimpleFileVisitor<Path>() {
      @Override
      public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs) throws IOException {
        String directoryName = dir.getFileName().toString();
        if (!directoryName.equals("__pycache__")) {
          incrementPackage();
        }

        return FileVisitResult.CONTINUE;
      }

      @Override
      public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
        String fileName = file.getFileName().toString();
        if (fileName.endsWith(".py")) {
          try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNext()) {
              String line = scanner.nextLine();
              if (line.startsWith("class")) {
                incrementClass();
              } else if (line.contains("def ")) {
                incrementDefinition();
              }

              incrementLineOfCode();
            }
          }

          incrementPythonFile();
        } else if (fileName.endsWith(".png") || fileName.endsWith(".jpg")) {
          incrementImage();
        }

        return FileVisitResult.CONTINUE;
      }
    });

    System.out.println(amountPackages + " packages");
    System.out.println(amountPythonFiles + " python files");
    System.out.println(amountLinesOfCode + " lines of python code");
    System.out.println(amountDefinitions + " function/method definitions");
    System.out.println(amountClasses + " classes");
    System.out.println(amountImages + " images");
  }

  private void incrementPackage() {
    amountPackages += 1;
  }

  private void incrementLineOfCode() {
    amountLinesOfCode += 1;
  }

  private void incrementDefinition() {
    amountDefinitions += 1;
  }

  private void incrementClass() {
    amountClasses += 1;
  }

  private void incrementPythonFile() {
    amountPythonFiles += 1;
  }

  private void incrementImage() {
    amountImages += 1;
  }
}

package org.example;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;

public class HangmanGame {
    String word;
    public HangmanGame() throws IOException, InterruptedException {
        setRandomWord();
    }
    public HangmanGame(String toGuess) {
        word = toGuess;
    }

    boolean isLetterInTheWord(String letter){
        return word.contains(letter);
    }

    public void setRandomWord() throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://random-word-api.herokuapp.com/word"))
                .method("GET", HttpRequest.BodyPublishers.noBody())
                .build();
        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        word = response.body().toUpperCase();
        word = word.substring(2, word.length() - 2);

    }

    public void play(){
        int maxTrials = 20; //word.length();
        int currentTrials = 0;
        Scanner scanner = new Scanner(System.in);
        String letter;
        StringBuilder currentSolution = new StringBuilder();
        for(int i=0; i<word.length(); i++){
            currentSolution.append("_");
        }

        word = word.toUpperCase();
        char letterChar;

        while(currentTrials < maxTrials && ! currentSolution.toString().equals(word)) {
            System.out.println("Guess. You have " + (maxTrials - currentTrials) + " left.");

            letter = scanner.next();
            letter = letter.toUpperCase();
            letterChar = letter.charAt(0);


            for(int i=0; i<word.length(); i++){
                if(word.charAt(i) == letterChar){
                    currentSolution.setCharAt(i, letterChar);
                }
            }

            System.out.println("You guessed " + letterChar + ". Your solution: " + currentSolution);
            currentTrials += 1;

        }

        if(currentSolution.equals(word)){
            System.out.println("You won!");
        }else {
            System.out.println("You lost!");
        }
        System.out.println("Your guess: " + currentSolution + " Solution: " + word);


    }
}

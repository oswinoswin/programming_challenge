package org.example;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        System.out.println("Hello world!");
        HangmanGame game = new HangmanGame();
        game.play();


//        game.play();

//        HttpRequest request = HttpRequest.newBuilder()
//                .uri(URI.create("https://random-word-api.herokuapp.com/word"))
//                .method("GET", HttpRequest.BodyPublishers.noBody())
//                .build();
//        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
//        System.out.println(response.body().toUpperCase());
    }
}
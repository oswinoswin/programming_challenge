package com.company;

public class Game {
    Player player1;
    Player player2;
    boolean hasWinner;

    public Game() {
        this.player1 = new Player();
        this.player2 = new Player();
        this.hasWinner = false;
    }

    public void play (){
        while (!hasWinner){
            Action action1 = player1.play();
            System.out.println("First player: " + action1);
            Action action2 = player2.play();
            System.out.println("Second player: " + action2);
            if(action1.equals(Action.PAPER) && action2.equals(Action.ROCK) ||
                    action1.equals(Action.ROCK) && action2.equals(Action.SCISSORS) ||
                    action1.equals(Action.SCISSORS) && action2.equals(Action.PAPER)){
                System.out.println("First player wins!");
                hasWinner = true;
            }
            else if(action2.equals(Action.PAPER) && action1.equals(Action.ROCK) ||
                    action2.equals(Action.ROCK) && action1.equals(Action.SCISSORS) ||
                    action2.equals(Action.SCISSORS) && action1.equals(Action.PAPER)) {
                System.out.println("Second player wins!");
                hasWinner = true;
            }

        }
    }

}

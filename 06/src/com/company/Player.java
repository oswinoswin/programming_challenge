package com.company;


import java.util.Random;

public class Player {
    Random random;
    public Player() {
        this.random = new Random();
    }

    public Action play(){
        int rand = random.nextInt(3);
        return Action.values()[rand];
    }

}

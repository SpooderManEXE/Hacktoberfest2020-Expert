import java.util.Scanner;

class Board {
    // draw blank board or re-draw board with a new value method
    public void drawBoard(int myValue) {
        if (myValue == 0) {
            TicTacToe.gameCounter++;
        }
        TicTacToe.Counter = 0;
        int row, col;
        System.out.println(" -------------");
        for (row = 0; row < 3; row++) {
            for (col = 0; col < 3; col++) {
                TicTacToe.Counter++;
                if (myValue == 0) {
                    TicTacToe.Board[row][col] = Integer.toString(
                            TicTacToe.Counter).charAt(0);
                }
                System.out.print(" | " + TicTacToe.Board[row][col]);
            }
            System.out.println(" | ");
            System.out.println(" -------------");
        }
        System.out.println("Current Score: ");
        System.out.println("Player1: " + TicTacToe.score1 + " Player 2: "
                + TicTacToe.score2);
    }

    // want to play again? method
    public boolean wantToPlayAgain() {
        int row, col;
        char playAgain = '-';
        while (playAgain != 'y' || playAgain != 'n') {
            System.out.println("Do you want to play again? (y/n)");
            playAgain = TicTacToe.input.next().charAt(0);
            if (playAgain == 'y') {
                TicTacToe.moveCounter = 0;
                TicTacToe.Counter = 0;
                for (row = 0; row < 3; row++) {
                    for (col = 0; col < 3; col++) {
                        TicTacToe.Counter++;
                        TicTacToe.Board[row][col] = (char) TicTacToe.Counter;
                    }
                }
                // figure out who starts next game
                if (TicTacToe.gameCounter/2 == (float)TicTacToe.gameCounter/2) {
                    TicTacToe.Player =1;
                    TicTacToe.playSymbol = 'X';
                }
                else {
                    TicTacToe.Player =2;
                    TicTacToe.playSymbol = 'O';
                }
                return true;
            } else if (playAgain == 'n') {
                System.out.println("*** Game Over !!! ***");
                System.runFinalization();
                TicTacToe.input.close();
                return false;
            }
        }
        return false;
    }
}

// my TicTacToe class
public class TicTacToe {
    // set global variables
    public static int Counter = 0, moveCounter = 0, score1 = 0, score2 = 0, gameCounter = 0, Player = 1;
    public static char playSymbol = 'X';
    public static char[][] Board = new char[3][3];
    public static Scanner input = new Scanner(System.in);

    // main func. / program starts here
    public static void main(String[] args) {

        // set local variables
        int row, col, positionNum;

        // make new board object and draw new board
        Board yn = new Board();
        Board myTicTacToeBoard = new Board();
        myTicTacToeBoard.drawBoard(0);

        // check for winner/ continue play
        outerloop: for (;;) {
            if (Board[0][0] == Board[0][1] && Board[0][0] == Board[0][2]
                    || Board[1][0] == Board[1][1] && Board[1][0] == Board[1][2]
                    || Board[2][0] == Board[2][1] && Board[2][0] == Board[2][2]
                    || Board[0][0] == Board[1][0] && Board[0][0] == Board[2][0]
                    || Board[0][1] == Board[1][1] && Board[0][1] == Board[2][1]
                    || Board[0][2] == Board[1][2] && Board[0][2] == Board[2][2]
                    || Board[0][0] == Board[1][1] && Board[0][0] == Board[2][2]
                    || Board[0][2] == Board[1][1] && Board[0][2] == Board[2][0]) {
                if (Player == 1) {
                    Player = 2;
                    score2++;
                } else {
                    Player = 1;
                    score1++;
                }
                System.out.println();
                System.out
                        .println("*********************************************");
                System.out.println("*********** Player " + Player
                        + " wins!!! ****************");
                System.out
                        .println("*********************************************");
                myTicTacToeBoard.drawBoard(1);

                if (yn.wantToPlayAgain()) {
                    myTicTacToeBoard.drawBoard(0);
                } else {
                    break outerloop;
                }
            }

            // check for draw
            else if (moveCounter == 9) {
                System.out.println();
                System.out
                        .println("*********************************************");
                System.out
                        .println("************ It's a DRAW !!! ****************");
                System.out
                        .println("*********************************************");
                if (yn.wantToPlayAgain()) {
                    myTicTacToeBoard.drawBoard(0);
                } else {
                    break outerloop;
                }
            } else {
                // user input
                System.out.println();
                System.out.println("Player " + Player + " enter number 1-9: ");
                positionNum = (int) input.nextInt();

                // assign symbol
                Counter = 0;
                for (row = 0; row < 3; row++) {
                    for (col = 0; col < 3; col++) {
                        Counter++;
                        if (positionNum == Counter) {
                            if (Board[row][col] != 'X'
                                    && Board[row][col] != 'O') {
                                Board[row][col] = playSymbol;
                                moveCounter++;
                                // redraw board
                                myTicTacToeBoard.drawBoard(1);

                                // change player
                                if (playSymbol == 'X') {
                                    playSymbol = 'O';
                                    Player = 2;
                                } else {
                                    playSymbol = 'X';
                                    Player = 1;
                                }
                            } else {
                                System.out
                                        .println("Position already taken, choose different one!");
                            }
                        }
                    }
                }
            }
        }
    }
}
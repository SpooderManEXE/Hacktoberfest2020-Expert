public class ReverseString {

    public static void main(String[] args) {

        String text = "Ashish Yadav";
        String[] textArr = text.split(" ");

        for(int i = 0; i < textArr.length; i++) { 
            char[] ch = textArr[i].toCharArray(); 

            for (int j = ch.length - 1; j >= 0; j--) {
                System.out.print(ch[j]);
            }

            System.out.print(" ");
        }
    }
}

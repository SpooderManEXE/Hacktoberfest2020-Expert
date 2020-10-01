import java.util.*;

public class tempConverter {

	public static void main(String[] args) {
		System.out.println("Enter temperature in Celsius");
		Scanner sc = new Scanner(System.in);
		float temp=sc.nextFloat();
		temp=(temp*9/5)+32;
		System.out.println("Converted temp in Fahrenheat : "+temp);
		sc.close();
	}

}

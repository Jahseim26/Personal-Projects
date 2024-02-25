/*Jahseim Merritt   
* 12/06/23
* COMP167002.202410
* This class recreates the standard Math library.
*/
package pgm; 

public class MyMath {
	
	private static double pie = 3.141592653589793;
	private static double g = 1;
	
	public static double toDegrees(double rad) { 
		return rad * 180 / pie;
	}
	
	public static double toRadians(double deg) {   
		return deg * pie / 180;
		
	}
	
	public static double absoluteValue(double abs) {
		if (abs < 0) {
			return abs * -1;
		}
		else {
			
		return abs;
		}
	}
	
	public static double minimum(double num1, double num2) {   // Method to calculate minimum.
		if (num1 < num2) {
			return num1;
		}
		else {
			return num2;
		}
	}
	
	public static double maximum(double num1, double num2) {  // Method to calculate maximum.
		if (num1 > num2) {
			return num1;
		}
		else {
			return num2;
		}
	}
	
	public static double power (double basenum, int exponent) {
		double powNum = basenum;
		for (int i = 1; i < exponent; ++i) {
			powNum = powNum * basenum;
		}
		return powNum;
	}
		
	
	public static double root(double num, int sqrt) {      // Method to calculate the root 
		double gp = g -((power(g, sqrt)- num) / (sqrt * power(g, sqrt - 1)));
		if (absoluteValue(gp - g) < 10e-10) {
			return gp;
		}
		else {
			g = gp;
			return root(num, sqrt);
		}
	}
	public static int gcd(int num1, int num2) {  // Method to calculate greatest common denominator.
		if (num1 == 0) {
			return num2;
		}
		else if (num2 == 0) {
			return num1;
		}
		else {
			return gcd(num2, num1 % num2);
		}
	}
	
	public static int lcm(int num1, int num2) {      // Method to calculate Least common multiple.
		return((num1 * num2) / (gcd(num1, num2)));
	}
	
	public static double piefunction(double number) {
		if (number < -3.141592653589793) {
			while ((number >= - 3.141592653589793) && (number <= 3.141592653589793)) {
				number = number - (2 * 3.141592653589793);
			}
		}
		return number;
	}
	
	public static double sine(double num) { // Method to calculate Sine.
		num = piefunction(num);
		double result = 0;
		double term = num;
		int i = 0;
		while (absoluteValue(term)> 10e-10){
			result += term;
			term = term * (-(power(num, 2)) / ((2 * i + 3) * (2 * i + 2)));
			i += 1;
		}
		return result;
		
	}
	public static double cosine(double num) { // Method to calculate Cosine.
		num = piefunction(num);
		double result = 0;
		double term = 1;
		int i = 0;
		while (absoluteValue(term)> 10e-10) {
			result += term;
			term = term * (-(power(num, 2)) / ((2 * i + 2) * (2 * i + 1)));
			i += 1;
		}
		return result;
		
	}
	public static double tangent (double num) { // Method to calculate tangent. 
		return sine(num)/ cosine(num);
	}
			
}
